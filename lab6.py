
n = int(input("Enter a number: "))
f = lambda x: (x-3)/(x**2)
a = [f(x) for x in range(1,n)]
print(a)



result = 1
def function2(n):
    global result

    result *= ((float(n) / (float(n) + 2)) - 10)

    if n > 1:
        function2(n-1)



num = int(input("Enter a number: "))
function2(num)