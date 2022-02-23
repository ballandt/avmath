def _check_instances(arg, *types):
    for ele in arg:
        if not type(ele) in types:
            return False, ele
    return True, True


def _check_matrix(arg):
    for ele in arg:
        if len(ele) != len(arg[0]):
            return False
    return True
