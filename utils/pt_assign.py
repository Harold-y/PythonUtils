import random

if __name__ == '__main__':
    params = ['剑', '金', '木', '水', '火', '土', '炼器', '阵法', '道韵', '神识', '魔气', '悟性']
    length = len(params)
    params_dict = {}
    for i in params:
        params_dict[i] = 0

    total_pt = 50
    for i in range(0, total_pt):
        choose = random.randint(0, length - 1)
        params_dict[params[choose]] += 1

    health = random.randint(50, 70)
    attack = random.randint(5, 10)
    defend = random.randint(5, 15)
    lingshi = random.randint(100, 500)

    print(params_dict)
    print(health, attack, defend, lingshi)
