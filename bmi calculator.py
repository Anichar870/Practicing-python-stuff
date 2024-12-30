def calculate_bmi(weight, height):
    """
    Calculate the BMI using the formula: BMI = weight (kg) / height (m)^2
    :param weight: Weight in kilograms.
    :param height: Height in meters.
    :return: BMI value.
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def bmi_category(bmi):
    """
    Determine the BMI category.
    :param bmi: BMI value.
    :return: BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        if bmi is not None:
            category = bmi_category(bmi)
            print(f"\nYour BMI is: {bmi}")
            print(f"Category: {category}")
        else:
            print("Error: Could not calculate BMI.")
    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
