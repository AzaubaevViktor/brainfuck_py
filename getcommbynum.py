#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import pdb

inp = int(input("Введите число, для которого нужно получить код:"))

res = []

for i in range(inp):
    for j in range(inp):
        comm = "+" * i
        if j != 0:
            comm += "[>" + "+" * j + "<-]"
        l = inp-i*j
        # pdb.set_trace()
        if l != 0:
            comm += ">"
            if l > 0:
                comm += "+" * l
            elif l < 0:
                comm += "-" * (-l)

        res.append(comm) 

res.sort(key=len)
print("Самые короткие команды:")
print(res[0])
print(res[1])
print(res[2])
print(res[3])