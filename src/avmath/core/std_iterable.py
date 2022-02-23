from .fraction import _Fraction
from .checks import _check_instances, _check_matrix


class STDIterable(tuple):

    _check_instances = _check_instances

    def __new__(cls, *args):
        iterable_args = STDIterable._check_instances(args,
                                                     list, tuple, STDIterable)
        if not iterable_args[0]:
            raise TypeError(f"Tuple must contain iterable values "
                            f"(not '{iterable_args[1]}')")
        for ele in args:
            numeric_args = STDIterable._check_instances(ele,
                                                        int, float, complex,
                                                        _Fraction)
            if not numeric_args[0]:
                raise TypeError(f"Tuple values must be numeric"
                                f"(not '{numeric_args[1]}')")
        if not _check_matrix(args):
            raise TypeError(f"Iterable has not got consistent dimensions")
        if iterable_args[0]:
            if len(args) > 1:
                args = [STDIterable(e) for e in args]
        return super().__new__(cls, args)

    def __add__(self, other):
        if len(self) != len(other):
            raise ArithmeticError("Iterables must have the same length")
        return STDIterable([self[i]+other[i] for i in range(len(self))])