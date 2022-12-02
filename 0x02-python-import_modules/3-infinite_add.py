#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv1 = sys.argv
    sum = 0
    for i in argv1:
        if i in argv1[0]:
            sum += int(i)
    print(sum)
