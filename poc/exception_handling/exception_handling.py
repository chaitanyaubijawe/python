
class A(Exception):
    pass

class B(A):
    pass

try:
    try:
        #a = 1/0
        # open("asd.txt")
        print("simple... try n except")
        raise B("meko nai karneka kuch")

    except ZeroDivisionError as e:
        print("Error :: ", e, e.args, type(e))

    except B as e:
        print("Error :: ", e, e.args, type(e))
        try:
            raise Exception("wrapping into my own...." )
        except A as e:
            print("sdfsdf")

    except A as e:
        print("Error :: ", e, e.args, type(e))

    except Exception as e:
        print("Error :: ", e, e.args, type(e))
    else:
        print("Else :: ")
    finally:
        print("finally")
except Exception as e:
    print("hahahah..... ", e)



#

print("here")

def m1(*args, **kwargs):

    print(type(args))
    for item in args:
        print("Tuple item :: ", item)
    print(type(kwargs))




m1(1,2,3, abc=1,efg=2)

