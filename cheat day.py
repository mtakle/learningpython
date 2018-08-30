#cheat day program

cal_prot = 4
cal_carb = 4
cal_fat = 9

tef_prot = float(0.35)
tef_carb = float(0.15)
tef_fat = float(0.15)

prot = input("Input grams of protein: ")
prot = int(prot)
carb = input("Input grams of carbs: ")
carb = int(carb)
fat = input("Input grams of fat: " )
fat = int(fat)

sum_cal = (cal_prot*prot) + (cal_carb*carb) + (cal_fat*fat)
perc_prot = float((cal_prot*prot)/sum_cal)
perc_carb = float((cal_carb*carb)/sum_cal)
perc_fat = float((cal_fat*fat)/sum_cal)
calories = (cal_prot*prot) + (cal_carb*carb) + (cal_fat*fat)
calories_print = str(calories)

print("Total daily calories: " + calories_print)

tdee = input("Input total daily calorie expenditure: ")
tdee = int(tdee)
calories = calories - tdee
calories_print = str(calories)

print("Total daily calories after tdee: " + calories_print)

thermic_effect_prot = (tef_prot * perc_prot)
thermic_effect_carb = (tef_carb * perc_carb)
thermic_effect_fat = (tef_fat * perc_fat)
thermic_effect = thermic_effect_prot + thermic_effect_carb + thermic_effect_fat
thermic_effect = round(thermic_effect, 5)

calories_by_tef = sum_cal * thermic_effect
calories_by_tef = int(calories_by_tef)
calories_by_tef_print = str(calories_by_tef)
calories = calories - calories_by_tef
calories_print = str(calories)
print("Thermic effect of food: " + calories_by_tef_print)
print("Total daily calories after tef: " + calories_print)

#calories on fat, modifer + 10%
#convert to grams








neat_factor = 100
neat_expenditure = calories / 1000 * neat_factor
print_neat_expenditure = str(neat_expenditure)

print("Non exercise activity thermogenesis: " + print_neat_expenditure)

calories = calories - neat_expenditure
calories_print = str(calories)

print("Total daily calories after tdee: " + calories_print)
