#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import sys

def main():

    answer = 10
    num = range(0, 10)
    four_operator = ["*", "/", "+", "-"]
    str_operator = ["%s%s%s%s%s%s%s", "((%s%s%s)%s%s)%s%s", "(%s%s(%s%s%s))%s%s", "(%s%s%s)%s(%s%s%s)", "%s%s((%s%s%s)%s%s)", "%s%s(%s%s(%s%s%s))"]

    for formula in [zz % (str(a), x, str(b), y, str(c), z, str(d)) for a in num for x in four_operator for b in num for y in four_operator for c in num for z in four_operator for d in num for zz in str_operator]:
        try:
            if eval(formula) == answer:
                print formula + "=" + str(answer)
        except ZeroDivisionError:
            pass

    return 0

if __name__ == "__main__":
    sys.exit(main())
