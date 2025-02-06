'''
1. Compile Time Error / Syntax Error
2. Run-time Error

try block - used to keep the logic in which we may get some error.
except block - will be executed when exception occurs in try block logic.
else block - will be executed when there is try block logic executed without any error.
finally block - will be executed irrespective of exception occured or not.

'''
def disp(a,b):
    try:
        print('Task started')
        print(a/b) # ZeroDivisionError: division by zero
    except:
        print("Some Error Handled")
    else:
        print('Task executed without any exception')
    finally:
        print('Task Ended')

disp(10,0)
disp(10,5)
disp(20,2)
