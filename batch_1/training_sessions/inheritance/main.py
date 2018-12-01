if __name__ == '__main__':
    from A import A
    from B import B
    from C import C
    from D import D
    a = A()
    a.m1()

    b = B()
    #b.m1()
    b.m2()

    # a.m2()
    print("diamond problems....")
    d = D()
    d.m1()

    d.shuffle(A,C)

    d.m1()
    d.__class__