t = (1, 2, 3, 4)

print(t)
print(*t) # print(t[0], t[1], t[2], t[3])

print()
print(1)

def my_print(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i)

my_print()
my_print(1)
my_print(1, 2)