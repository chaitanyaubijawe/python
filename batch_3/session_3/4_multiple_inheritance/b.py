from a import A
class B(A):
    def __init__(self):
        super().__init__()
        print("constructor of B")

    def m_a(self):
        super().m_a()
        print("method of B")

    def m2_a(self, arg):
        # super().m2_a(arg)
        super().m2_a()
        print("method of B : " + str(arg))
