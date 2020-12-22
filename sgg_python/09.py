### tail  recursion
def factor(num,result):
    if num ==1:
        return result
    else :
        return factor(num -1 , result * num)
#print(factor(5,1))

def power(num, pow,result):
    if pow == 0:
        return result
    else:
        return power(num,pow-1, result * num)
#print(power(5,3,1))

def par(string):
    if len(string) < 2:
        return True
    else:
        return False if string[0]!= string[-1] else par(string[1:-1])
#print(par("fdcabbacdf"))

def fib(step, num1,num2):
    return num1 if step < 2 else fib(step -1, num2, num1 + num2)
print(fib(10,1,1))