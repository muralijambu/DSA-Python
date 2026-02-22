a=5
b=2
try:
    print("resource open")
    print(a/b)
    
    k=int(input("enter input "))
    print(k)
except ZeroDivisionError as e:
    print(e)    
except ValueError as e:
    print(e)   
except Exception as e:
    print(e)     
finally:
    print("resource closed")    