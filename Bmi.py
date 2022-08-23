ref_bmi = float(18.5)
maxref_bmi = float(24.9)
height = float(input("what's your height in meters: "))
weight = float(input("what's your weight in kg: "))
BMI=weight/(height*height)
print("your BMI is ",BMI)

if(ref_bmi>=BMI):
    print("you're underweight")
elif(ref_bmi<=BMI<=maxref_bmi):
    print("you're perfect")
else:
    print("you're overweight")        
