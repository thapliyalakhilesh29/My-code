class Persion:
 
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob


    def calculate_age(self):
        current_year = int(input("Enter current year:" ))
        if (current_year < self.dob[2] ):
            print("please Enter right input")
        else:
           print (current_year - self.dob[2])
        


persion1 = Persion("Rahul", "India",[3,9,1994])
persion1.calculate_age()

    