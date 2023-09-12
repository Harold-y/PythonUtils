import subprocess
from time import sleep
import re
import numpy as np
from time import gmtime, strftime
import datetime
import pandas as pd


def ping_avg_latency(hostname: str = "www.google.com"):
    all_latency = []
    group_latency = []
    group_avg = []
    group_variance = []
    group_time = []
    for i in range(0, 10):
        p = subprocess.Popen(["ping.exe", hostname], stdout=subprocess.PIPE)
        res = str(p.communicate()[0], "utf-8")
        latency_list = re.findall(r"((time=)(\d+))", res)

        current = []
        for item in latency_list:
            current.append(int(item[2]))
        all_latency.extend(current)
        group_latency.append(current)

        group_avg.append(np.average(current))
        group_variance.append(np.var(current))
        group_time.append(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

        sleep(5)

    total_avg = np.average(all_latency)
    total_variance = np.var(all_latency)
    print("*-*-*" * 5)
    print(f"Summary: \nAverage: {total_avg} | Variance: {total_variance}\nTotal Tried: 10\n"
          f"Groups Latency Stats: {group_latency}\nGroups Latency Means: {group_avg}\nGroups Latency Variances: "
          f"{group_variance}\nGroup Latency Tested on: {group_time}")
    print("*-*" * 5)

    return total_avg, total_variance, group_latency, group_avg, group_variance, group_time


def save_ping_data(hostname: str = "www.google.com", duration_min=5):
    start = datetime.datetime.now()
    measure_times = []
    measure_latency = []

    while (datetime.datetime.now() - start).total_seconds() / 60 < duration_min:
        total_avg, total_variance, group_latency, group_avg, group_variance, group_time = ping_avg_latency()
        measure_times.extend(group_time)
        measure_latency.extend(group_latency)

    measure_site = [hostname] * len(measure_times)
    df = pd.DataFrame({'timestamp': measure_times, 'site': measure_site, 'latency': measure_latency})
    df.to_csv('out.csv')


save_ping_data()
