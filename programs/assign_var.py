def args(*args):
    sum = 0
    args = list(args)
    args[0] = 1
    for i in args:
        sum += i 
    print(sum)

def kwargs(**kwargs):
    print("Hello " + kwargs['first'] + kwargs['last'])

args(2,2,3,4,5,6,7,8,9)
kwargs(first = "Promise", last = "Mutum")