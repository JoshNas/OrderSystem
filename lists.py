import functions as f

order = []
total = 0
order_number = 1
server = ''
table = ''
current_guest = ''

"""Checks if server has been set"""
server_set = False
"""Checks if table has been set"""
table_set = False
"""Checks if guest has been set"""
guest_set = False

appetizers = []
appetizers_prices = []
entrees = []
entrees_prices = []
drinks = []
drinks_prices = []
per_row = {'AppsPerRow': 3, 'EntreesPerRow': 5, 'DrinksPerRow': 4}

f.get_appetizers()
f.get_entrees()
f.get_bar_menu()
f.get_row_nums()

print(per_row)

# apps_per_row = 3
# entrees_per_row = 5
# drinks_per_row = 4
# with open('perRow.csv', 'r') as f:
#     l = f.readlines()
#     print(l)
#     print(l[0][1])



# use loop to strip spaces from other list to create database menu list
menu = []

for a in appetizers:
    menu.append(a.replace(' ', '').replace("'", "").replace(".", "").replace("/", ""))
for e in entrees:
    menu.append(e.replace(' ', '').replace("'", "").replace(".", "").replace("/", ""))
for d in drinks:
    menu.append(d.replace(' ', '').replace("'", "").replace(".", "").replace("/", ""))









