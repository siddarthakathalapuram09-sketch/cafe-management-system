from datetime import datetime

name=input("Enter your name:")
#LISTS of items 
lists='''
Rice Rs 20/kg
Sugar Rs 30/kg
Salt Rs 20/kg
Oil Rs 120/kg
Maggi Rs 50/kg
boost Rs 90/each
Past Rs 20/each
penut butter Rs 120/box
paneer Rs 120/kg
'''
#decleration
print(lists)
print = 0
priselist = []
totalprise = 0
Finalfinalprise = []
ilist = []
qlist = []
plist = []

# rates of items
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 120,
    'maggi': 50,
    'boost': 90,
    'past': 20,
    'peanut butter': 120,
    'paneer': 120
}

option = int(input("For list of items press 1: "))

if option ==1:
    print(lists)
