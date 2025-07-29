def main():
    print("Enter the number of fat grams and carbohydrate grams you consumed in a day below.")
    fat_grams = float(input("Fat grams: "))
    carb_grams = float(input("Carb grams: "))
    calories_from_fat, calories_from_carb = calories(fat_grams, carb_grams)
    print(f"Calories from fat - {calories_from_fat}g")
    print(f"Calories from carb - {calories_from_carb}g")


def calories(fat_grams, carb_grams):
    calories_from_fat = format(fat_grams * 9, ",.2f")
    calories_from_carb = format(carb_grams * 4, ",.2f")
    return calories_from_fat, calories_from_carb


if __name__ == '__main__':
    main()
