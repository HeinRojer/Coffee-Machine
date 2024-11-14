"☕"
# water , coffee , milk , cost of the item
menu={"espresso":[50,18,0,1.50],"latte":[200,24,150,2.50 ],"cappuccino":[250,24,100, 3.00]}
coins ={"penny":0.01, "dime": 0.10 , "nickel": 0.05, "quarter": 0.25}
print(" Penny = 0.01$       Dime = 0.10$        Nickel = 0.05$      Quarter = 0.25$")
water = 300
milk = 200
coffee = 100
money = 0
change = 0
this_code_bellow_me_runs_only_if_i_stay_true = True
while this_code_bellow_me_runs_only_if_i_stay_true == True:
    coffee_input = input ( "What would you like ? (espresso/latte/cappuccino)  :" ).lower ( )
    if coffee_input == "report":
        print(f"Water = {water}ml \nMilk = {milk}ml \nCoffee = {coffee}g \nMoney = {money}$")
    elif coffee_input =="espresso":
        if water > menu[coffee_input][0] :
            print("Please insert coins ")
            quarters = 0.01* int(input("How many quarters : "))
            dimes = 0.10 * int(input("How many dimes : "))
            nickels = 0.05 * int(input("How many nickels : "))
            pennies = 0.25 * int(input("How many pennies : "))
            added_money = quarters + dimes + pennies +nickels
            if added_money > menu[coffee_input][3]:
                change = added_money - menu[coffee_input][3]
                print(f"Here is {change}$ in change.")
                print("Here is your Espresso ☕ Enjoy !")
                water = water - menu[coffee_input][0]
                milk =milk - menu[coffee_input][1]
                coffee = coffee - menu[coffee_input][2]
            elif added_money < menu[coffee_input][3]:
                change = menu [ coffee_input ][ 3 ]- added_money
                print ( f" Sorry that's not enough money , You are {change}$ short" )
                print ( "Money refunded " )
            else:
                print ( "Here is your Espresso ☕ Enjoy !" )
                water = water - menu [ coffee_input ] [ 0 ]
                milk = milk - menu [ coffee_input ] [ 1 ]
                coffee = coffee - menu [ coffee_input ] [ 2 ]
        else:
            print("Sorry there is not enough water")
            print("Water-Refil Needed")
            this_code_bellow_me_runs_only_if_i_stay_true = False

    elif coffee_input =="latte":
        if water > menu [ coffee_input ] [ 0 ] :
            print("Please insert coins ")
            quarters = 0.01* int(input("How many quarters : "))
            dimes = 0.10 * int(input("How many dimes : "))
            nickels = 0.05 * int(input("How many nickels : "))
            pennies = 0.25 * int(input("How many pennies : "))
            added_money = quarters + dimes + pennies +nickels
            if added_money > menu[coffee_input][3]:
                change = added_money - menu[coffee_input][3]
                print(f"Here is {change}$ in change.")
                print("Here is your Latte ☕ Enjoy !")
                water = water - menu[coffee_input][0]
                milk =milk - menu[coffee_input][1]
                coffee = coffee - menu[coffee_input][2]
            elif added_money < menu[coffee_input][3]:
                change = menu [ coffee_input ][ 3 ]- added_money
                print ( f" Sorry that's not enough money , You are {change}$ short" )
                print ( "Money refunded " )
            else:
                print ( "Here is your Latte ☕ Enjoy !" )
                water = water - menu [ coffee_input ] [ 0 ]
                milk = milk - menu [ coffee_input ] [ 1 ]
                coffee = coffee - menu [ coffee_input ] [ 2 ]
        else :
            print ( "Sorry there is not enough water" )
            print ( "Water-Refil Needed" )
            this_code_bellow_me_runs_only_if_i_stay_true = False

    elif coffee_input =="cappuccino":
        if water > menu [ coffee_input ] [ 0 ] :
            print("Please insert coins ")
            quarters = 0.01 * int(input("How many quarters : "))
            dimes = 0.10 * int(input("How many dimes : "))
            nickels = 0.05 * int(input("How many nickels : "))
            pennies = 0.25 * int(input("How many pennies : "))
            added_money = quarters + dimes + pennies + nickels
            if added_money > menu[coffee_input][3]:
                change = added_money - menu[coffee_input][3]
                print(f"Here is {change}$ in change.")
                print("Here is your Cappuccino ☕ Enjoy !")
                water = water - menu[coffee_input][0]
                milk = milk - menu[coffee_input][1]
                coffee = coffee - menu[coffee_input][2]
            elif added_money < menu[coffee_input][3]:
                change = menu [ coffee_input ][ 3 ]- added_money
                print( f" Sorry that's not enough money , You are {change}$ short" )
                print( "Money refunded " )
            else:
                print ( "Here is your Cappuccino ☕ Enjoy !" )
                water = water - menu [ coffee_input ] [ 0 ]
                milk = milk - menu [ coffee_input ] [ 1 ]
                coffee = coffee - menu [ coffee_input ] [ 2 ]
        else :
            print ( "Sorry there is not enough water" )
            print ( "Water-Refil Needed" )
            this_code_bellow_me_runs_only_if_i_stay_true = False
    else:
        print("Sorry that's not on our menu")
        again = input("Would you like to order again \n  1.yes  2.no")
        if again == "no":
            print("Thank You")
            this_code_bellow_me_runs_only_if_i_stay_true = False


