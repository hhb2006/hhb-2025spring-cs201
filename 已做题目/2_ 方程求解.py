def f(x):
    return x**3 - 5*x**2+ 10*x - 80

def f1(x):
    return 3*x**2 - 10*x + 10

x0 = 6
while True:
    x1 = x0 - f(x0)/f1(x0)
    if abs(x0 - x1) <= 10**(-10):
        break
    x0 = x1

print('%.9f'% x0)

# http://cs101.openjudge.cn/practice/04140/