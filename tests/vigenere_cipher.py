
if __name__ == '__main__':
    key = 'd'
    text = 'w'
    expected = 'Z'

    add = ord(key) + ord(text)
    print(add)
    print(chr(add % 27 + ord('A')))

