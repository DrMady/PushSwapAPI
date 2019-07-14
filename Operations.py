listA = []
listB = []


def sa(list_ref, pos1, pos2, operation_array):
    if list_ref:
        get = list_ref[pos1], list_ref[pos2]
        list_ref[pos2], list_ref[pos1] = get

    operation_array.append('sa')
    return list_ref, operation_array


def sb(list_ref, pos1, pos2, operation_array):

    if list_ref:
        get = list_ref[pos1], list_ref[pos2]
        list_ref[pos2], list_ref[pos1] = get

    operation_array.append('sb')
    return list_ref, operation_array


def sc(operation_array):
    sa(listA, 0, 1, operation_array)
    sb(listB, 0, 1, operation_array)
    operation_array.append('sc')
    return operation_array


def pa(list_ref, list_recipient, operation_array):
    if list_ref:
        list_recipient.insert(0, list_ref.pop(0))

    operation_array.append('pa')
    return list_ref, operation_array


def pb(list_ref, list_recipient, operation_array):
    if list_ref:
        list_recipient.insert(0, list_ref.pop(0))

    operation_array.append('pb')
    return list_ref, operation_array


def ra(list_ref, operation_array):
    list_ref.append(list_ref.pop(0))

    operation_array.append('ra')
    return list_ref, operation_array


def rb(list_ref, operation_array):
    list_ref.append(list_ref.pop(0))

    operation_array.append('rb')
    return list_ref, operation_array


def rr(operation_array):
    ra(listA, operation_array)
    rb(listB, operation_array)
    operation_array.append('rr')
    return operation_array


def rra(list_ref, operation_array):
    list_ref.insert(0, list_ref.pop(-1))

    operation_array.append('rra')
    return list_ref, operation_array


def rrb(list_ref, operation_array):
    list_ref.insert(0, list_ref.pop(-1))

    operation_array.append('rrb')
    return list_ref, operation_array


def rrr(operation_array):
    rra(listA, operation_array)
    rrb(listB, operation_array)
    operation_array.append('rrr')
    return operation_array
