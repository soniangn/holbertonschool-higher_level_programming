#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    n = len(dir(hidden_4))
    for i in range(0, n):
        if i[0:2] != "__":
            print("{}".format(i))
