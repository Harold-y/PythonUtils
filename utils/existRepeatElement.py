from typing import List
import typing


def existRepeat(in_list: List[typing.Any]) -> dict:
    elements = {}
    for item in in_list:
        if elements.get(item) is None:
            elements[item] = 1
        else:
            print("Repeat Element Detected: ", item)
            elements[item] += 1
    return elements


if __name__ == '__main__':
    in_list = [62, 50, 63, 55, 30, 57, 48, 58, 45, 65, 57, 60, 61, 53, 62]
    print(existRepeat(in_list))
