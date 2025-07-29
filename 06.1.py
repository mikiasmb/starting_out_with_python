def main():
    print("Enter the number of fat grams and carbohydrate grams you consumed in a day below.")
    fat_grams = float(input("Fat grams: "))
    carb_grams = float(input("Carb grams: "))
    print(f"Calories from fat - {calories_from_fat(fat_grams)}g")
    print(f"Calories from carb - {calories_from_carb(carb_grams)}g")


def calories_from_fat(fat_grams):
    calorie = fat_grams * 9
    return f"{calorie:,.2f}"


def calories_from_carb(carb_grams):
    calories = carb_grams * 4
    return f"{calories:,.2f}"


if __name__ == '__main__':
    main()
