#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import argparse,pdb
parser = argparse.ArgumentParser(description='BrainFuck')
parser.add_argument("-p","--programm",help="programm")
parser.add_argument("-d","--debug",help="Отладка")
args = parser.parse_args()

a = [0]
len_a = 1
p = 0
head = 0
cycle = []
ticks = 0

if args.programm == None:
    prg = input("Введите программу:")
else:
    r = [x.rstrip() for x in open(args.programm,"rt").readlines() if not ((x[0] == "#") or (x == ''))]
    prg = "".join([x for x in r])

if args.debug == None:
    debug = False
else:
    debug = True

prg = prg.rstrip()

def getsq(head):
    global squares
    for x in squares:
        if head < x:
            return x
    return -1


def bf_exec(c):
    global p,a,cycle,head,ticks,len_a,inp
    if c == "+":
        a[p] += 1
        if a[p] > 255:
            a[p] = 0
    elif c == "-":
        a[p] -= 1
        if a[p] < 0:
            a[p] = 255
    elif c == ">":
        p += 1
        if p >= len_a:
            a.append(0)
            len_a += 1
    elif c == "<":
        p -= 1
        if p < 0:
            return [3,"Индекс не может быть отрицательным"]
    elif c == ".":
        print(chr(a[p]),end='')
    elif c == ",":
        a[p] = ord(inp[0])
        inp = inp[1:]
    elif c == "[":
        r = getsq(head)
        if r == -1:
            return [2,"Не найдена ]"]
        if a[p] == 0:
            head = r + 1
        else:
            cycle.append(head)
    elif c == "]":
        # pdb.set_trace()
        if a[p] != 0:
            head = cycle[-1]
        else:
            cycle.pop(-1)
    else:
        return [1,"Незвестная команда"]
    head += 1
    ticks += 1
    return [0, ""]

def bf_translator():
    global prg,head
    # pdb.set_trace()
    if prg[head].isnumeric():
        _head = head
        n = 0
        while prg[head].isnumeric():
            n *= 10
            n += int(prg[head]) 
            head +=1
            if head >= len(prg): 
                break
        prg = prg[:_head-1] + prg[_head-1] * n + prg[head:]
        head = _head + n
    head += 1

#Транслятор
while head < len(prg):
    bf_translator()

# Ищем скобки
squares = [x-1 for x,y in enumerate(prg) if y == "]"]

print(prg)

len_prg = len(prg)
head = 0

print("===================")
inp = input("Введите строку:")
print("===================")
while head != len_prg:
    err = bf_exec(prg[head])
    if debug:
        print("::::::::::%d:::::::::" %ticks)
        print("Память: ["+ ";".join([str(x) for x in a[:p]] + [" {"+str(a[p])+"} "] + [str(x) for x in a[p+1:]]) +"]" )
        if head != len_prg:
            print("Программа: " + prg[:head] + " {" + prg[head] + "} " + prg[head+1:])
    if err[0] != 1:
        if err[0]:
            print("Brainfuck error %d: %s on [%d], symbol \"%s\"" %(err[0],err[1],head,prg[head]))
            print("Отладочная иноформация:\n---------------------")
            print("Положение считывателя: %d" %(head))
            print("Положение каретки: %d" %p)
            if p > 0:
                print("Память: ["+ ";".join([str(x) for x in a[:p]] + [" {"+str(a[p])+"} "] + [str(x) for x in a[p+1:]]) +"]" )
            else:
                print("Память: ["+ ";".join([str(x) for x in a]) + "]")
            print("Программа: " + prg[:head] + " {" + prg[head] + "} " + prg[head+1:])
            print("---------------------")
            break
print("\n===================\n Тиков:%d, Ячеек:%d" %(ticks,len(a)))
