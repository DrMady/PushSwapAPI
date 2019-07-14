#!/usr/bin/python

import Operations as Op
import random
import sys

listA = []
listB = []
operation_array = []


def start_argv():
    sys.argv.remove('Start_argv.py')
    for x in sys.argv:
        if represents_int(x):
            listA.append(x)
        else:
            print('Your values are not correct\n')
            exit()
    # print(listA)
    sort(listA, listB)
    # print(listA)
    print(" ".join(operation_array))
    # print(len(operation_array))


def start_theo(list_ref):
    sort(list_ref, listB)


def start_rand(array_len):
    listA.clear()
    for i in range(array_len):
        listA.append(random.randrange(-100, 101, 1))
        print(listA)
    sort(listA, listB)
    print(listA)
    print(operation_array)


def sort(list_ref, list_recipient):
    operation_array.clear()
    while list_ref:
        index_min = min(range(len(list_ref)), key=list_ref.__getitem__)

        if list_ref[index_min] == list_ref[0]:
            Op.pb(list_ref, listB, operation_array)
        else:
            if index_min > len(list_ref) / 2:
                Op.rra(list_ref, operation_array)
            elif index_min <= len(list_ref) / 2:
                Op.ra(list_ref, operation_array)

    if not list_ref:
        while list_recipient:
            Op.pa(listB, list_ref, operation_array)


def represents_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# start_rand(100)
