def disp(a,b):
    try:
        print(a/b)
       # print(a/c) --> NameError occurred and handled.
    except ZeroDivisionError:
        print("ZeroDivisionError occurred and handled.")
    except NameError:
        print("NameError occurred and handled.")
    except TypeError:
        print("TypeError occurred and handled")
    except:
        print("Some Error occurred.")
disp(10,'Kodnest') # TypeError occurred and handled
disp(10,0) # ZeroDivisionError occurred and handled.
disp(10,5) # 2.0

