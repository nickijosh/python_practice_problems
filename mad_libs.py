# mad_libs.py

weather_adj = input("Enter a weather adjective: ")
monkey_adj = input("Enter a monkey adjective: ")
lion_adj = input("Enter a lion adjective: ")
experience_adj = input("Enter an experience adjective: ")
mood = input("How did you feel (happy/sad/excited)? ")

print(f"\nOn a beautiful {weather_adj} day, I went to the zoo.")
print(f"I saw a funny {monkey_adj} monkey swinging from the trees.")
print(f"Then, I spotted a majestic {lion_adj} lion lounging in the sun.")
print(f"What a wild and {experience_adj} experience!")

if mood.lower() == "sad":
    print("But I felt a bit down as I walked past the cages.")
else:
    print("I couldn’t stop smiling throughout the visit!")