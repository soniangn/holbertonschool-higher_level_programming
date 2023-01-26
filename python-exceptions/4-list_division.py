#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for number in range(list_length):
        try:
            quotient = my_list_1[number] / my_list_2[number]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            new_list.append(quotient)
    return new_list
    