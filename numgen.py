import sys
import os
import time
import json
from datetime import datetime, timedelta, date

def main_menu():
    while True:
        clear_screen()
        print("\nWelcome to the Numerology Calculator!")
        print()
        display_current_date_numbers()
        print("Please select an option:")
        print()
        print("1. New Calculation")
        print("2. View Previously Saved Calculation")
        print("3. Delete Entry")
        print("4. Numerology Categories")
        print("5. Chinese Zodiac")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                new_calculation()
            elif choice == 2:
                view_saved_calculation()
            elif choice == 3:
                entry_number = int(input("Enter the entry number you want to delete: "))
                delete_saved_calculation(entry_number)
            elif choice == 4:
                show_numerology_categories()
            elif choice == 5:
                show_chinese_zodiac()
            elif choice == 6:
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            time.sleep(1)

def show_numerology_categories():
    while True:
        print("\nNumerology Categories:")
        print("1. Life Path Number")
        print("2. Expression Number")
        print("3. Soul Urge Number")
        print("4. Personality Number")
        print("5. Birthday Number")
        print("6. Personal Year Number")
        print("7. Personal Month Number")
        print("8. Personal Day Number")
        print("9. Life Cycle Number")
        print("10. Pinnacle Cycle Number")
        print("11. Major Life Cycle Number")
        print("0. Return to Main Menu")

        user_choice = int(input("\nEnter the number of the category you want to learn about, or '0' to return to the main menu: "))

        if user_choice == 0:
            break
        elif user_choice == 1:
            print("\nLife Path Number: The date of birth components (month, day, and year) are reduced to single digits and summed up. The resulting number is then reduced to a single digit or a master number (11, 22, or 33).")
        elif user_choice == 2:
            print("\nExpression Number: Each letter of the full name is assigned a numerical value based on its position in the alphabet. The numbers are then added together and reduced to a single digit or master number.")
        elif user_choice == 3:
            print("\nSoul Urge Number: The numerical values of the vowels in the full name are added together and reduced to a single digit or master number.")
        elif user_choice == 4:
            print("\nPersonality Number: The numerical values of the consonants in the full name are added together and reduced to a single digit or master number.")
        elif user_choice == 5:
            print("\nBirthday Number: The day of birth is reduced to a single digit or master number.")
        elif user_choice == 6:
            print("\nPersonal Year Number: The current year's digits are added to the Life Path Number, and the sum is reduced to a single digit.")
        elif user_choice == 7:
            print("\nPersonal Month Number: The current month's digits are added to the Personal Year Number, and the sum is reduced to a single digit.")
        elif user_choice == 8:
            print("\nPersonal Day Number: The current day's digits are added to the Personal Month Number, and the sum is reduced to a single digit.")
        elif user_choice == 9:
            print("\nLife Cycle Number: Derived from the Life Path Number, this calculation reveals three major periods in one's life, each with its own unique challenges and opportunities.")
        elif user_choice == 10:
            print("\nPinnacle Cycle Number: Also derived from the Life Path Number, this calculation shows four specific time periods in one's life, representing the challenges and opportunities they will face.")
        elif user_choice == 11:
            print("\nMajor Life Cycle Number: Similar to the Life Cycle and Pinnacle Cycle Numbers, this calculation identifies three major phases in one's life, each with its own set of experiences and challenges.")
        else:
            print("\nInvalid selection. Please try again.")

        input("\nPress Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_personality_traits(life_path_number):
    if life_path_number == 8:
        return [
            "Ambitious: 8 Life Path individuals are highly ambitious and driven to succeed in their chosen endeavors. They set high goals for themselves and work tirelessly to achieve them.",
            "Strong leadership: They possess natural leadership qualities and can take charge in any situation. Their confidence and authority often inspire others to follow their lead.",
            "Organized and efficient: 8 Life Path individuals are known for their ability to create structure and bring order to any environment. They are skilled at managing their resources effectively and efficiently.",
            "Financially focused: They have a natural talent for understanding financial matters and often excel in careers related to finance, business, or investments. Money and material success are important to them, and they are always looking for ways to increase their wealth.",
            "Resilient: 8 Life Path individuals are extremely resilient and can overcome obstacles that might discourage others. They are determined to succeed and never give up, even in the face of adversity.",
            "Authoritative: They can be authoritative and assertive, which can sometimes come across as domineering or controlling. This trait can be both a strength and a challenge, as it helps them lead but may also create friction in relationships.",
            "Practical: They are practical and realistic, focusing on tangible results rather than abstract ideas. They are more likely to base their decisions on facts and logic than on emotions or intuition.",
            "Balancing power and compassion: 8 Life Path individuals may need to work on balancing their powerful, assertive nature with compassion and empathy. This balance can help them be more effective leaders and partners in their personal and professional lives.",
        ]
    # You can add more cases for other Life Path numbers later

def display_current_date_numbers():
    numerology_explanations = {
        1: "A day to take action or start something new. It's a day of leadership, independence, and ambition.",
        2: "A day for cooperation, diplomacy, and relationships. It's also a good day for patience and detail-oriented tasks.",
        3: "A day for creativity, communication, and social interaction. Three is also associated with joy and optimism.",
        4: "A day for hard work, organization, and practical matters. Four brings a stable and grounding energy.",
        5: "A day for adventure, freedom, and change. Five is associated with flexibility and unpredictability.",
        6: "A day for responsibility, love, and home-related matters. Six is linked to balance and harmony.",
        7: "A day for introspection, spirituality, and rest. Seven is a deeply introspective and philosophical number.",
        8: "A day for financial and business matters. Eight is associated with power, abundance, and success.",
        9: "A day for completion, compassion, and service to others. Nine symbolizes endings and spiritual growth.",
    }

    today = date.today()

    current_day_number = reduce_number(today.day)
    current_month_number = reduce_number(today.month)
    current_year_number = reduce_number(today.year)

    current_date_number = reduce_number(current_day_number + current_month_number + current_year_number)

    print(f"Current Day Number: {current_day_number}")
    print(f"Current Month Number: {current_month_number}")
    print(f"Current Year Number: {current_year_number}")
    print(f"Numerological Value of the Current Date: {current_date_number}")
##    print(numerology_explanations[current_date_number] + "\n")

def show_chinese_zodiac():
    zodiac = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']

    descriptions = {
        'Rat': 'Rats are quick-witted, resourceful, and versatile.',
        'Ox': 'Oxen are diligent, dependable, strong and determined.',
        'Tiger': 'Tigers are brave, competitive, unpredictable, and confident.',
        'Rabbit': 'Rabbits are gentle, quiet, elegant and alert; quick, skillful, kind and patient.',
        'Dragon': 'Dragons are confident, intelligent, enthusiastic and hardworking.',
        'Snake': 'Snakes are intelligent, hardworking, reliable and meticulous.',
        'Horse': 'Horses are warm-hearted, enthusiastic, and positive.',
        'Sheep': 'Sheep are gentle, calm, mothering, and kind. They love peace and quiet and are sympathetic to others\' needs.',
        'Monkey': 'Monkeys are witty, intelligent, and have a magnetic personality.',
        'Rooster': 'Roosters are honest, bright, communicative, and ambitious.',
        'Dog': 'Dogs are loyal, honest, and trustworthy and have a strong sense of duty.',
        'Pig': 'Pigs are diligent, compassionate, and generous. They have great concentration: once they set a goal, they will devote all their energy to achieving it.'
    }

    while True:
        print("Enter '1' to input your birth year")
        print("Enter '2' to see all Chinese Zodiac signs and their years")
        print("Enter '3' to return to the main menu")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            while True:
                try:
                    birth_year = int(input("Please enter your birth year: "))
                    if birth_year >= 1900 and birth_year <= 2100:
                        break
                    else:
                        print("Invalid year. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid year.")

            sign = zodiac[(birth_year - 1900) % 12]
            print(f"Your Chinese Zodiac sign is: {sign}")
            print(descriptions[sign])  # Prints the description of the sign
        elif user_choice == '2':
            for index, sign in enumerate(zodiac):
                print(f"{sign}: {', '.join(str(year) for year in range(1900 + index, 2101, 12))}")
        elif user_choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")

def get_full_name():
    return input("Please enter your full name at birth: ")

def get_date_of_birth():
    while True:
        dob = input("Please enter your date of birth (mm dd yyyy): ")
        try:
            month, day, year = map(int, dob.split())
            if 1 <= month <= 12 and 1 <= day <= 31 and 1900 <= year <= 2100:
                return dob
            else:
                raise ValueError
        except ValueError:
            print("Invalid date format. Please try again.")

def reduce_number(num):
    while num >= 10 and num not in [11, 22, 33]:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_life_path_number(birthdate: str) -> int:
    # Split the birthdate string into separate parts (month, day, year)
    numbers = birthdate.split()

    # Convert each part into a list of digits
    digits = [list(map(int, str(number))) for number in numbers]

    # Flatten the list of lists into a single list of digits
    flattened_digits = [digit for sublist in digits for digit in sublist]

    # Add up all the digits
    total = sum(flattened_digits)

    # If the total is a two-digit number, split the digits and add them together until a single digit is obtained
    while total > 9:
        total = sum(map(int, str(total)))

    return total

def calculate_expression_number(full_name):
    letter_values = {char: idx for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
    full_name = full_name.upper().replace(" ", "")

    name_value = sum(letter_values[char] for char in full_name)
    return reduce_number(name_value)

def calculate_soul_urge_number(full_name):
    letter_values = {char: idx for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
    full_name = full_name.upper().replace(" ", "")

    vowel_value = sum(letter_values[char] for char in full_name if char in "AEIOU")
    return reduce_number(vowel_value)

def calculate_birth_day_number(dob):
    _, day, _ = map(int, dob.split())
    return reduce_number(day)

def calculate_personality_number(full_name):
    letter_values = {char: idx for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
    full_name = full_name.upper().replace(" ", "")

    consonant_value = sum(letter_values[char] for char in full_name if char not in "AEIOU")
    return reduce_number(consonant_value)

def calculate_maturity_number(life_path_number, expression_number):
    return reduce_number(life_path_number + expression_number)

def calculate_karmic_debt_number(dob):
    month, day, year = map(int, dob.split())
    birth_numbers = [month, day, year]
    return (
        reduce_number(sum(repeating_numbers))
        if (
            repeating_numbers := [
                num for num in birth_numbers if birth_numbers.count(num) > 1
            ]
        )
        else None
    )

def calculate_hidden_passion_number(full_name):
    letter_values = {char: idx for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
    full_name = full_name.upper().replace(" ", "")

    letter_count = {char: full_name.count(char) for char in set(full_name)}
    max_count = max(letter_count.values())

    return reduce_number(
        sum(
            letter_values[char]
            for char in letter_count
            if letter_count[char] == max_count
        )
    )

def calculate_subconscious_self_number(dob):
    date_numbers = [int(char) for char in dob if char.isdigit()]
    digit_count = {digit: date_numbers.count(digit) for digit in range(1, 10)}
    return sum(1 for count in digit_count.values() if count > 0)

def save_calculation(full_name, dob, life_path_number, expression_number, soul_urge_number, birth_day_number, personality_number, maturity_number, karmic_debt_number, hidden_passion_number, personal_year_number, personal_month_number, personal_day_number, subconscious_self_number, major_life_cycle_number):
    calculation = {
        "full_name": full_name,
        "dob": dob,
        "life_path_number": life_path_number,
        "expression_number": expression_number,
        "soul_urge_number": soul_urge_number,
        "birth_day_number": birth_day_number,
        "personality_number": personality_number,
        "maturity_number": maturity_number,
        "karmic_debt_number": karmic_debt_number,
        "hidden_passion_number": hidden_passion_number,
        "personal_year_number": personal_year_number,
        "personal_month_number": personal_month_number,
        "personal_day_number": personal_day_number,
        "subconscious_self_number": subconscious_self_number,
        "major_life_cycle_number": major_life_cycle_number,
    }

    try:
        with open("saved_calculations.json", "r") as file:
            saved_calculations = json.load(file)
    except FileNotFoundError:
        saved_calculations = []

    # Check if the calculation is already saved
    if any(saved_calc["full_name"] == full_name and saved_calc["dob"] == dob for saved_calc in saved_calculations):
        print("This calculation has already been saved.")
    else:
        saved_calculations.append(calculation)

        with open("saved_calculations.json", "w") as file:
            json.dump(saved_calculations, file, indent=4)

def view_saved_calculation():
    try:
        with open("saved_calculations.json", "r") as file:
            if file.read(1):
                file.seek(0)
                saved_calculations = json.load(file)
            else:
                saved_calculations = []

        if not saved_calculations:
            print("No saved calculations found.")
        else:
            for idx, calculation in enumerate(saved_calculations, start=1):
                print("\nEntry Number:", idx)
                display_calculation(calculation)
    except FileNotFoundError:
        print("No saved calculations found.")
    time.sleep(5)  # Add a 5-second delay before returning to the main menu
    main_menu()

def display_traits_or_exit(calculation):
    while True:
        choice = input("\n1. View Personality Traits\n2. Exit\nEnter your choice (1-2): ")

        if choice == '1':
            if calculation["life_path_number"] == 8:
                print("\nPersonality Traits for Life Path Number 8:")
                for trait in get_personality_traits(8):
                    print("-", trait)
            else:
                print("Personality traits are only available for Life Path Number 8.")
        elif choice == '2':
            break
        else:
            print("Invalid input. Please enter a valid choice (1-2).")


def display_calculation(calculation):
    print("Full Name:", calculation["full_name"])
    print("Date of Birth:", calculation["dob"])
    print("Life Path Number:", calculation["life_path_number"])
    print("Expression Number:", calculation["expression_number"])
    print("Soul Urge Number:", calculation["soul_urge_number"])
    print("Birth Day Number:", calculation["birth_day_number"])
    print("Personality Number:", calculation["personality_number"])
    print("Maturity Number:", calculation["maturity_number"])
    if "karmic_debt_number" in calculation and calculation["karmic_debt_number"]:
        print("Karmic Debt Number:", calculation["karmic_debt_number"])
    else:
        print("Karmic Debt Number: None")
    if "hidden_passion_number" in calculation:
        print("Hidden Passion Number:", calculation["hidden_passion_number"])
    else:
        print("Hidden Passion Number: Not available")
    print("Personal Year Number:", calculation["personal_year_number"])
    print("Personal Month Number:", calculation["personal_month_number"])
    print("Personal Day Number:", calculation["personal_day_number"])
    print("Subconscious Self Number:", calculation["subconscious_self_number"])
    print("Major Life Cycle Number:", calculation["major_life_cycle_number"])

    display_traits_or_exit(calculation)

def delete_saved_calculation(entry_number):
    try:
        with open("saved_calculations.json", "r") as file:
            saved_calculations = json.load(file)

        if not saved_calculations:
            print("No saved calculations found.")
        elif entry_number == 0:
            print("Deletion canceled. Returning to the main menu.")
        elif entry_number > len(saved_calculations) or entry_number < 1:
            print("Invalid entry number.")
        else:
            del saved_calculations[entry_number - 1]
            with open("saved_calculations.json", "w") as file:
                json.dump(saved_calculations, file)
            print(f"Entry number {entry_number} has been deleted.")
    except FileNotFoundError:
        print("No saved calculations found.")

    time.sleep(2)
    main_menu()

def new_calculation():
    while True:
        full_name = input("Please enter your full name at birth (0 to return to the main menu): ")
        if full_name == "0":
            break
        dob = input("Please enter your date of birth (mm dd yyyy): ")
        life_path_number = calculate_life_path_number(dob)
        expression_number = calculate_expression_number(full_name)
        soul_urge_number = calculate_soul_urge_number(full_name)
        birth_day_number = calculate_birth_day_number(dob)
        personality_number = calculate_personality_number(full_name)
        maturity_number = calculate_maturity_number(life_path_number, expression_number)
        karmic_debt_number = calculate_karmic_debt_number(dob)
        hidden_passion_number = calculate_hidden_passion_number(full_name)
        personal_year_number = calculate_personal_year_number(dob)
        personal_month_number = calculate_personal_month_number(dob)
        personal_day_number = calculate_personal_day_number(dob)
        subconscious_self_number = calculate_subconscious_self_number(dob)
        major_life_cycle_number = calculate_major_life_cycle_number(dob)

        display_calculation({
            "full_name": full_name,
            "dob": dob,
            "life_path_number": life_path_number,
            "expression_number": expression_number,
            "soul_urge_number": soul_urge_number,
            "birth_day_number": birth_day_number,
            "personality_number": personality_number,
            "maturity_number": maturity_number,
            "karmic_debt_number": karmic_debt_number,
            "hidden_passion_number": hidden_passion_number,
            "personal_year_number": personal_year_number,
            "personal_month_number": personal_month_number,
            "personal_day_number": personal_day_number,
            "subconscious_self_number": subconscious_self_number,
            "major_life_cycle_number": major_life_cycle_number
        })
        save_calculation(full_name, dob, life_path_number, expression_number, soul_urge_number, birth_day_number,
                         personality_number, maturity_number, karmic_debt_number, hidden_passion_number,
                         personal_year_number, personal_month_number, personal_day_number, subconscious_self_number,
                         major_life_cycle_number)

    main_menu()

def get_current_date():
    current_date = datetime.now()
    return current_date.month, current_date.day, current_date.year

def calculate_personal_year_number(dob):
    month, day, _ = map(int, dob.split())
    reduced_month = reduce_number(month)
    reduced_day = reduce_number(day)

    _, _, current_year = get_current_date()
    reduced_year = reduce_number(current_year)

    return reduce_number(reduced_month + reduced_day + reduced_year)

def calculate_personal_month_number(dob):
    personal_year_number = calculate_personal_year_number(dob)

    current_month, _, _ = get_current_date()
    reduced_month = reduce_number(current_month)

    return reduce_number(personal_year_number + reduced_month)

def calculate_personal_day_number(dob):
    personal_month_number = calculate_personal_month_number(dob)

    _, current_day, _ = get_current_date()
    reduced_day = reduce_number(current_day)

    return reduce_number(personal_month_number + reduced_day)

def calculate_major_life_cycle_number(dob):
    month, day, year = map(int, dob.split())
    birth_date = datetime(year, month, day)
    current_date = datetime.now().date()
    age_in_days = (current_date - birth_date.date()).days

    return reduce_number(age_in_days)

if __name__ == "__main__":
    main_menu()
