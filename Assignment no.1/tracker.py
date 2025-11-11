#Kashvi Bihani
#1/11/2025
#Daily calorie tracker
#TASK 1 Describing the work of tracker

print("Welcome to my daily calorie tracker")
print("This will help you to track your daily calorie intake ")
print("It will help you to calculate your average calorie consumption making it easy to manage your health goals.")
#TASK 2 Asking input from user
Meal_name=[]
Calorie_value=[]
track=input("Do you want to add meals?(yes/no):")
if track=="yes":
    meal_value=int(input("How many meals you want to add?"))
    for i in range(meal_value):
        print(f"Meal no.{i+1}")
        meal=input("Enter meal name:")
        calories=float(input("Enter your calories:"))
        Meal_name.append(meal)
        Calorie_value.append(calories)
    print("Meals and calories are saved.")
else:
    print("Okay")
#TASK 3 Printing sum & average of calories

total_calories=sum(Calorie_value)
average_calories=total_calories/len(Meal_name)
daily_limit=float(input("Enter your daily limit:"))
print(" Calorie overview")
print(f"Your average calories is,{average_calories}")
print(f"Your total calories is,{total_calories}")
#TASK 4 & 5 Making report of calorie & daily limit status

if total_calories>daily_limit:
    print("You have exceeded your daily limit")
else:
    print("You are within your daily limit")
data=[]
for i in range(len(Meal_name)):
    data.append(["Meal", Meal_name[i],Calorie_value[i]])
data.append(["Total", total_calories])
data.append(["Average", (average_calories, )])
print("\n Calorie Report ")
print(f"\n{'Meal':<15}{'Calories':>10}")
print("-" * 25)

for i in range(len(Meal_name)):
    print(f"{Meal_name[i]:<15}{Calorie_value[i]:>10}")
print("-" * 25)
print(f"{'Total':<15}{total_calories:>10}")
print(f"{'Average':<15}{average_calories:>10}")

from datetime import datetime

# BONUS TASK Saving the report
save_file = input("Do you want to save your report?(yes/no): ")
if save_file.lower() == "yes":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorie_report.txt", "w") as f:
        f.write("=== Calorie Report ===\n\n")
        f.write(f"Date & Time: {timestamp}\n\n")
        f.write("Meals:\n")
        for i in range(len(Meal_name)):
           f.write(f"{Meal_name[i]:<15}{Calorie_value[i]:>10}\n")
        f.write(f"\nTotal Calories: {total_calories}")
        f.write(f"\nAverage Calories: {average_calories}")
        f.write(f"\nDaily Limit: {daily_limit}")
        if total_calories > daily_limit:
          f.write("\nStatus: You have Exceeded daily Limit")
        else:
          f.write("\nStatus: You are within daily Limit")
        print(f"Session saved successfully to '{"calorie_report.txt"}'")
else:
        print("Okay, session not saved.")

print("Thank you for using daily calorie tracker")


























