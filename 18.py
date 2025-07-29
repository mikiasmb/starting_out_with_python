vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party a gluten-free? ")
vege = vegetarian.lower()
veg = vegan.lower()
gluten = gluten_free.lower()

if vege and veg and gluten == "yes":
    print("Here are your restaurant choices:"
          "\nCorner Cafe"
          "\nThe Chef's Kitchen")
elif vege and veg and gluten == 'no':
    print("Here are your restaurant choices:"
          "\nJoe's Gourmet Burgers")
elif vege and gluten == 'yes' and veg == 'no':
    print("Here are your restaurant choices:"
          "Main Street Pizza Company")
elif vege == 'yes' and veg and gluten == 'no':
    print("Here are your restaurant choices:"
          "Main Street Pizza Company"
          "Mama's Fine Italian")
elif vege and gluten == 'yes' and veg == 'no':
    print("Here are your restaurant choices:"
          "Main Street Pizza Company")
elif vege and gluten == 'yes' and veg == 'no':
    print("Here are your restaurant choices:"
          "\n Main Street Pizza Company"
          "\nCorner Cafe"
          "\nThe Chef's Kitchen")
else:
    print("invalid input")
