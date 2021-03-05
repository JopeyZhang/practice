# -*- coding:utf-8 -*-
# coding:unicode_escape

for i in range(1, 20):
    for x in range(i, i+1):
        if x % 2 == 0:
            break
    else:
        print("odd number:", x)
