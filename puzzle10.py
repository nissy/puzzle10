#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import sys
import itertools

def main():

    answer = 10
    num = range(0, 10)
    four_operator = ["*", "/", "+", "-"]
    str_operator = ["((%s%s%s)%s%s)%s%s", "(%s%s(%s%s%s))%s%s", "(%s%s%s)%s(%s%s%s)", "%s%s((%s%s%s)%s%s)", "%s%s(%s%s(%s%s%s))"]

    for abcd in itertools.combinations_with_replacement(num, 4):
        for formula in [zz % (str(perm[0]), xyz[0], str(perm[1]), xyz[1], str(perm[2]), xyz[2], str(perm[3])) for perm in itertools.permutations(abcd) for xyz in itertools.product(four_operator, repeat=3) for zz in str_operator]:
            try:
                if eval(formula) == answer:
                    print formula + "=" + str(answer)
                    break
            except ZeroDivisionError:
                pass

    return 0

if __name__ == "__main__":
    sys.exit(main())
