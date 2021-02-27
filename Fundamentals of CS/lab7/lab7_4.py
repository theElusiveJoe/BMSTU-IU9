#!/bin/python3

def fact(x):
    if x <= 1:
        return 1
    else:
        return x*fact(x-1)


def makemem(foo):
    mem = {}
    def memed(*args):
        key = str(args)
        if key in mem:
            print("i remember it!")
        else:
            print("calculating:")
            val = foo(*args)
            mem[key] = val
        return mem[key]
    return memed


memedfact = makemem(fact)

print(memedfact(5))
print(memedfact(5))
