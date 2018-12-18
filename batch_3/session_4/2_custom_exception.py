class MyFalanaException(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__("This is my class exception :: " + message)

try:
    # manually raising exception....
    # raise Exception("ye gadbad generic wali hui he......")
    raise MyFalanaException("ye gadbad hui he,,,,,")

    #print("print element at index  3... " + str(l[3]))
# except IndexError as iee:
#     print("Handling MyFalanaException here... " + str(iee))
except MyFalanaException as ie:
    print("Handling MyFalanaException here... " + str(ie))
except Exception as gie:
    print("Handling Exception here... " + str(gie))
