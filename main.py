#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

import json

expenses_file = 'expenses.json' 
expenses_file = open('expenses.json') # opening JSON file
expenses = json.load(expenses_file) # returns JSON object as a dictionary
expenses_file.close()

expenses = []

n = -1

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    print("1. Add edition.")
    print("2. Top 10 biggest expenses")
    print("3. Top 10 smallest expenses")
    print("4. Medium expenses")
    print("5. Exit")

    command = input("\nChoose command:")


    if command == "1":
        expenses1 = []
        print("You want to add edition! Let's start!")
        a = input("Write name of the edition!")
        expenses1.append(a)
        b = input("Write sum of the edition!")
        expenses1.append(b)
        c = input("Write category of the edition!")
        expenses1.append(c)
        print(expenses1)
#       with open('expenses.json') as json_file:
#           json.dumps(expenses1)
        expenses_file = open('expenses.json')
        expenses1 = json.load(expenses_file)
        expenses_file.close()
        print("Edition added!")
        pass


    elif command == "2":
        print("You want to see 10 biggest expenses! Let's start!")
        while True (n < 101):
          n = n + 1
          expensesB = expenses[n][1]
          expensesB.sort(function(0, 100000){return 0 - 100000})
          print(expenses_file[-10:])
          print("Here you go!")


    elif command == "3":
        print("You want to see 10 smallest expenses! Let's start!")
        while True (n < 101):
          n = n + 1
          expensesS = expenses[n][1]
          expensesS.sort(function(0, 100000){return 0 - 100000})
          print(expenses_file[-10:])
          print("Here you go!")
        pass


    elif command == "4":
        print("You want to see your medium expenses! Let's start!")
        pass


    elif command == "5":
        print("Exiting...")
        break

    else:
        print("Error")
        break


# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

