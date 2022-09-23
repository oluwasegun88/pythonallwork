def add(a:float, b:float) -> float | None:
    try:
        #c = a+'b'
        #name = int('great')
        lst =[1,2,3]
        #print(lst[6])
        file=open('file.txt',mode='r',encoding='utf-8')
        print(file.read())
        print("About to close")
        #return a/b
        print(a/b)
    except ZeroDivisionError as e:
        print("Can't divide with zero -->", e)
        raise ValueError("I know all is not well")
        #return None
    except (TypeError, NameError):
        print("Type error")
    else:
        print("Owo epo")
    finally:
        print("About to close")
        file.close()



print(add(1,0))
