#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import sys

def main():

    num = range(1, 10)
    four_operator = ["*", "/", "+", "-"]

    for i in [(str(a), x, str(b), y, str(c), z, str(d)) for a in num for x in four_operator for b in num for y in four_operator for c in num for z in four_operator for d in num]:
        formula = "".join(i)
        if eval(formula) == 10:
            print formula + "=10"

    return 0

if __name__ == "__main__":
    sys.exit(main())
