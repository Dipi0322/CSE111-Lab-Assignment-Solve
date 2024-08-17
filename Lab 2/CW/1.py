def bmi(height,weight):
  height = height / 100
  BMI = round(weight/(height)**2,1)

  if BMI < 18.5:
    return f"Score is {BMI}, You are Underwight"
  elif 18.5 <= BMI <= 24.9:
    return f"Score is {BMI}, You are Normal"
  elif 25 <= BMI <= 30:
    return f"Score is {BMI}, You are Overweight"
  elif BMI > 30:
    return f"Score is {BMI}, You are Obese"

h = int(input("Height in cm: "))
w = int(input("Weight in kg: "))
print(bmi(h,w))