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
    in_list = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23,
               -21, 5]
    print(existRepeat(in_list))
