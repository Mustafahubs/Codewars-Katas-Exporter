def bmi(weight, height):
    Check = weight / height ** 2
    if Check <= 18.5:
        return "Underweight"
    elif Check <= 25.0:
        return "Normal"
    elif Check <= 30.0:
        return "Overweight"
    else:
        return "Obese"
