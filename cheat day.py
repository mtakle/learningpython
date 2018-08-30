#cheat day program

cal_prot = 4
cal_carb = 4
cal_fat = 9

tef_prot = 0.35
tef_carb = 0.15
tef_fat = 0.15

prot = input("Input grams of protein :")
prot = int(prot)
carb = input("Input grams of carbs :")
carb = int(carb)
fat = input("Input grams of fat :")
fat = int(fat)

calories = (cal_prot*prot) + (cal_carb*carb) + (cal_fat*fat)
calories_print = str(calories)

print("Total daily calories: " + calories_print)
