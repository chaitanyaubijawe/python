
w_map = {}
def World_Map():
    w_map = {}

    def populat_country():
        # local to its method
        ''' comment '''
        w_map = {"method-level":"populat_country"}
        print("Inside populat_country")

    def populate_cities():
        nonlocal w_map
        w_map = {"non-local":"accessing parent method level variable...."}
        print("Inside populate_cities")

    def populate_states():
        global w_map
        w_map = {"global":"scope is global...."}
        print("Inside populate_states")

    populat_country()
    print("After populat_country local : ", w_map)
    populate_cities()
    print("After populate_cities:: nonlocal ", w_map)
    populate_states()
    print("After populate_states:: modifying global var... but values are still non local ", w_map)

print("global before modification , " , w_map)
World_Map()

print("Global variable : ", w_map)
