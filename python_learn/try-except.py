# -*- coding:utf-8 -*-


try:
    x = 1/0

except Exception as err:
    print(f'got an error:{err}')
