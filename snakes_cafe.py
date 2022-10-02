intro_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

appetizers_intro = """
Appetizers
----------
"""

entrees_intro = """
Entrees
-------
"""

desserts_intro = """
Desserts
--------
"""

drinks_intro = """
Drinks
------
"""

orders_prompt_question = """
***********************************
** What would you like to order? **
***********************************
"""

appetizers = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0
}

entrees = {
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0
}

desserts = {
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0
}

drinks = {
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}

appetizer_names = appetizers.keys()
entree_names = entrees.keys()
dessert_names = desserts.keys()
drink_names = drinks.keys()


if __name__ == '__main__':
    print(intro_message)
    print(appetizers_intro, end="")
    for appetizer_name in appetizer_names:
        print(appetizer_name)
    print(entrees_intro, end="")
    for entree_name in entree_names:
        print(entree_name)
    print(desserts_intro, end="")
    for dessert_name in dessert_names:
        print(dessert_name)
    print(drinks_intro, end="")
    for drink_name in drink_names:
        print(drink_name)
    print(orders_prompt_question, end="")
    order = input("> ")
    while order != "quit":
        if order in appetizer_names:
            appetizers[order] += 1
            print(f"\n** {appetizers[order]} order of {order} have been added to your meal **\n")
            order = input("> ")
        elif order in entree_names:
            entrees[order] += 1
            print(f"\n** {entrees[order]} order of {order} have been added to your meal **\n")
            order = input("> ")
        elif order in dessert_names:
            desserts[order] += 1
            print(f"\n** {desserts[order]} order of {order} have been added to your meal **\n")
            order = input("> ")
        elif order in drink_names:
            drinks[order] += 1
            print(f"\n** {drinks[order]} order of {order} have been added to your meal **\n")
            order = input("> ")
        elif order == "quit":
            quit()
        else:
            print("\nYour input is invalid. Please try again or type \"quit\"\n")
            order = input("> ")
