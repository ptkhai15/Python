A = 10
type(A) \\int
B = 99.9
type(B) \\float
C = 45.j
type(C) \\complex
Number_1 = 15
Number_2 = 47
Number_1 + Number_2 \\ 62
Number_3 = 19.5
Number_4 = 33
Number_3 + Number_4 \\52.5
Number_2 - Number_1 \\32
Number_4 - Number_3 \\13.5
Number_1 * Number_2 \\705
Number_3 * Number_4 \\643.5
Number_1 / Number_2 \\0.3191489
Number_3 / Number_4
Number_1 % Number_2 \\2
Number_3 % Number_4 \\13.5
4 ** 3 \\64
10 ** 5 \\100000
81 ** 0.5\\9
Number_2 // Number_1 \\3
Number_4 // Number_3 \\1.0
8 + 4 * 3 / 2 - 18 \\-4.0
8 + ((4*3)/2) -18 \\-4.0
A = int(input("Please enter a value: "))
B = int(input("Please enter a value: "))
C = (A ** 2 + B ** 2) ** 0.5
print("Hypotenuse: ", C)
Height = float(input("Please enter your height in meters"))
Weight = int(input("Please enter your weight: "))
BMI = Weight / (Height ** 2)
print("BMI: ", BMI)

