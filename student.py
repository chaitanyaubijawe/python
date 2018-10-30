from address import Address


class Student:
    std = 1

    def __init__(self, f_name, l_name, roll_num):
        self.f_name = f_name
        self.l_name = l_name
        self.r_num = roll_num
        self.contact_details(9065,9087)
        self.stud_address()

    def contact_details(self,home_contact,school_contact):
        self.home = home_contact
        self.school = school_contact

    def address_details(self,address_line_1,area,zip_code,city):
        # self.address_line_1 = address_line_1
        # self.area = area
        # self.zip = zip_code
        # self.city = city
        #return (address_line_1 + " " + area + " " + str(zip_code) + " " + city)
        self.addr = Address(address_line_1 , area , str(zip_code) , city)
        #return self.addr

    def stud_address(self):

        self.address_details("Cosmos", "Magarpatta", 444111, "Pune")

        # print(type(self.home_address), self.home_address.address_line_1, self.address_line_1)
        print(type(self.addr), self.addr.address_line_1)
        self.school_address = self.address_details("Eon IT Park","Khardi",411614,"Pune")


# # school_add = ["Eon IT park","Kharadi",411614,"Pune"]
   #  myfile = open("names.csv")
   #  #print(myfile)
   #  row_content = myfile.read()
   #  #print((row_content))
   #  rows = row_content.splitlines()
   #  #print(rows)
   #  for r in rows:
   #      data = r.split(",")
   #  stud_1 = Student('Nimesh','Shroti',1)
   #  print(stud_1.f_name + " " + stud_1.l_name,stud_1.r_num,stud_1.home,stud_1.school,stud_1.home_address,stud_1.school_address)







