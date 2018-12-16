from b import B
# import b

# class C(b.B):
class C(B):
    def __init__(self):
        super().__init__()
        print("inside c constructor...")



if __name__ == "__main__":

    c = C()
