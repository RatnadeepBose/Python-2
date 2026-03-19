# ============================================
# Class Methods
# ============================================

class Human:
    def __init__(self, name, age, nationality, hobby, profession, watch_brand, car_brand, net_worth):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.hobby = hobby
        self.profession = profession
        self.watch_brand = watch_brand
        self.car_brand = car_brand
        self.net_worth = net_worth
    
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old from {self.nationality}.")
    
    def show_interests(self):
        print(f"I enjoy {self.hobby} and work as a {self.profession}.")
    
    def show_luxury(self):
        print(f"I wear a {self.watch_brand} watch and drive a {self.car_brand}.")
        print(f"My net worth is approximately ${self.net_worth} million.")
    
    def full_profile(self):
        print("-" * 50)
        print(f"NAME: {self.name}")
        print(f"AGE: {self.age}")
        print(f"NATIONALITY: {self.nationality}")
        print(f"HOBBY: {self.hobby}")
        print(f"PROFESSION: {self.profession}")
        print(f"WATCH: {self.watch_brand}")
        print(f"CAR: {self.car_brand}")
        print(f"NET WORTH: ${self.net_worth} million")
        print("-" * 50)

# Creating people with luxury details
person1 = Human("Rahul Sharma", 32, "Indian", "Yacht Racing", "Tech Entrepreneur", "Patek Philippe", "Lamborghini", 45)
person2 = Human("Emma Watson", 28, "British", "Classic Cars", "Actress", "Rolex", "Aston Martin", 30)
person3 = Human("Carlos Rodriguez", 45, "Spanish", "Golf", "Real Estate Developer", "Audemars Piguet", "Ferrari", 78)
person4 = Human("Priya Kapoor", 35, "Indian", "Art Collection", "Fashion Designer", "Cartier", "Mercedes Maybach", 25)
person5 = Human("James Wellington", 52, "American", "Wine Tasting", "Hedge Fund Manager", "Richard Mille", "Bugatti", 120)
person6 = Human("Sophie Laurent", 29, "French", "Skiing", "Luxury Hotelier", "Hublot", "Porsche", 18)
person7 = Human("Marco Ricci", 41, "Italian", "Opera", "Fashion Executive", "Panerai", "Maserati", 55)
person8 = Human("Naomi Tanaka", 38, "Japanese", "Zen Gardens", "Architect", "Grand Seiko", "Lexus", 22)
person9 = Human("Ahmed Al-Fayed", 48, "Emirati", "Falconry", "Oil Magnate", "Jacob & Co", "Rolls Royce", 200)
person10 = Human("Isabella Rossi", 33, "Italian", "Cooking", "Celebrity Chef", "Bulgari", "Alfa Romeo", 12)

# Show profiles
print("\n=== LUXURY COLLECTION ===\n")

person1.full_profile()
person2.full_profile()
person3.full_profile()
person4.full_profile()
person5.full_profile()
person6.full_profile()
person7.full_profile()
person8.full_profile()
person9.full_profile()
person10.full_profile()

print("\n=== INTRODUCTIONS ===\n")

people = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]

for person in people:
    person.introduce()
    person.show_interests()
    person.show_luxury()
    print()