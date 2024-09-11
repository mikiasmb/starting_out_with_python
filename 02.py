import random


def main():
    countries_and_capitals = {
        "Ethiopia": "Addis Ababa",
        "United States": "Washington, D.C.",
        "France": "Paris",
        "Japan": "Tokyo",
        "Germany": "Berlin",
        "Brazil": "Brasília",
        "Canada": "Ottawa",
        "Australia": "Canberra",
        "India": "New Delhi",
        "China": "Beijing",
        "Russia": "Moscow",
        "United Kingdom": "London",
        "Mexico": "Mexico City",
        "South Africa": "Pretoria",
        "Nigeria": "Abuja",
        "Saudi Arabia": "Riyadh",
        "Italy": "Rome",
        "Spain": "Madrid",
        "South Korea": "Seoul",
        "Turkey": "Ankara",
        "Egypt": "Cairo",
        "Argentina": "Buenos Aires",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Netherlands": "Amsterdam",
        "Switzerland": "Bern",
        "New Zealand": "Wellington",
        "Thailand": "Bangkok",
        "Vietnam": "Hanoi",
        "Kenya": "Nairobi",
    }
    question_count = int(input("How many questions do you want: "))
    while question_count < 1 or question_count > len(countries_and_capitals):
        print(f"Total countries are {len(countries_and_capitals)}")
        question_count = int(input("Enter a valid number: "))
        
    correct_count = 0
    wrong_count = 0
    
    for i in range(question_count):
        question = generate_quiz(countries_and_capitals)
        print(question)
        correct, wrong = check_answer(countries_and_capitals, question)
        correct_count += correct
        wrong_count += wrong
    
    print(f"Correct: {correct_count}")
    print(f"Wrong: {wrong_count}")


def generate_quiz(countries_capitals):
    return random.choice(list(countries_capitals.keys()))


def check_answer(countries_capitals, question):
    answer = input(": ").strip().lower()
    if answer == countries_capitals[question].lower():
        print("Correct!")
        return 1, 0
    else:
        print(f"Wrong! The correct answer was {countries_capitals[question]}.")
        return 0, 1


if __name__ == '__main__':
    main()
    