'''
# try except else finally raise

#exception handaling 
num = int(input("enter number:"))
try:
    if(num < 0):
        raise ValueError
except ValueError:
    print("number must be positive integer")
else:
    for i in range(1,11):
        print(i*num)

'''
#code 2

try:
    num = 10/0
except ZeroDivisionError:
    print("can't devide by zero")
except Exception as e:
    print("an exception occured: ",str(e))
else:
    print("operation done")
finally:
    print("final block executed!!")
