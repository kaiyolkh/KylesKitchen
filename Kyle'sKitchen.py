# Name: Kyle Lam
# This was one of the summative projects in the Grade 10 ICS2O1 course
# Created some time in late May or June of 2019
# Text formatting is a bit messed up on PyCharm console. Please use Python IDLE for the best experience
# Not the best code but it is my work, enjoy.
# =============================================================================================================================

# this program is an ordering machine which takes order from the menu and allows the user to checkout.
import time  # import time function for the short pauses to work.

# short pauses are everywhere in this program because it makes the user easier to understand the processes of the order.
# it is relatively more pleasing to look at, instead of giving a bunch of information to the user at once.
print("Welcome to Kyle's Kitchen!")  # print welcome phrase
# major while loop
repeat = 0
# minor while loops
cart_rep = 0
rep_conf = 0
payment_rep = 0
quan_rep = 0
remove_rep = 0
tax_rep = 0
# variables & inputs
payment = 0
sub = 0
cash = 0
card = 0
edit = 0
remove = 0
# costs
cs_cost = 0
gs_cost = 0
hotdog_cost = 0
hamburg_cost = 0
fries_cost = 0
cp_cost = 0
pp_cost = 0
hp_cost = 0
water_cost = 0
coke_cost = 0
fanta_cost = 0
sprite_cost = 0
# quantities
cs = 0
gs = 0
hotdog = 0
hamburger = 0
fries = 0
cp = 0
pp = 0
hp = 0
water = 0
coke = 0
fanta = 0
sprite = 0

while repeat != 1:  # main while loop for the entire order and cart process to function
    print("=====================================================================\nPlease choose any items below:")
    print(
        "\n---------------------Salads---------------------\n1. Caesar Salad\t\t\t\t$4.99\n2. Garden Salad\t\t\t\t$4.99")
    print(
        "\n-------------------Fast Food--------------------\n3. Hotdog\t\t\t\t$3.49\n4. Hamburger\t\t\t\t$3.99\n5. French Fries\t\t\t\t$1.99")
    print(
        "\n--------------Pizzas(1 Slice Each)--------------\n6. Cheese Pizza\t\t\t\t$2.49\n7. Pepperoni Pizza\t\t\t$2.99\n8. Hawaiian Pizza\t\t\t$3.49")
    print(
        "\n---------------Drinks & Beverages---------------\n9. Water\t\t\t\t$0.99\n10.Coke\t\t\t\t\t$1.49\n11.Fanta\t\t\t\t$1.49\n12.Sprite\t\t\t\t$1.49")
    # menu(above)
    item = input(
        "\nPlease enter the item number: ")  # displays after menu, asks user to input the item number from the menu

    try:  # try and except function for value errors
        if item == "1":  # if the user input is item number 1
            quan = int(input(
                "Please enter the quantity of the item: "))  # asks user to input the quantity of the requested item
            if quan <= 0:  # if the quantity of the item is 0 or below, then it tells the user that the input is too small.
                print("\nInput amount too small. Please try again.")
                time.sleep(1)  # short pause.
                repeat += 0  # loops back to the order memu
            if quan > 0:  # if the quantity of the item is above 0, then it adds the cost of the item to the subtotal
                sub = sub + (quan * 4.99)
                cs_cost = cs_cost + (quan * 4.99)
                cs += quan  # stores the quantity of the requested item for future use, especially the receipt
                print("Please wait while we are preparing your order......")
                time.sleep(1)  # short pause
                cart_rep += 1  # leads to the cart
        # same process goes from option 1 to 12. the only difference is the cost of the items.
        elif item == "2":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 4.99)
                gs_cost = gs_cost + (quan * 4.99)
                gs += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "3":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 3.49)
                hotdog_cost = hotdog_cost + (quan * 3.49)
                hotdog += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "4":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 3.99)
                hamburg_cost = hamburg_cost + (quan * 3.99)
                hamburger += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "5":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 1.99)
                fries_cost = fries_cost + (quan * 1.99)
                fries += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "6":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 2.49)
                cp_cost = cp_cost + (quan * 2.49)
                cp += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "7":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 2.99)
                pp_cost = pp_cost + (quan * 2.99)
                pp += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "8":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 3.49)
                hp_cost = hp_cost + (quan * 3.49)
                hp += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "9":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 0.99)
                water_cost = water_cost + (quan * 0.99)
                water += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "10":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 1.49)
                coke_cost = coke_cost + (quan * 1.49)
                coke += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "11":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 1.49)
                fanta_cost = fanta_cost + (quan * 1.49)
                fanta += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        elif item == "12":
            quan = int(input("Please enter the quantity of the item: "))
            if quan <= 0:
                print("\nInput amount too small. Please try again.")
                time.sleep(1)
                repeat += 0
            if quan > 0:
                sub = sub + (quan * 1.49)
                sprite_cost = sprite_cost + (quan * 1.49)
                sprite += quan
                print("Please wait while we are preparing your order......")
                time.sleep(1)
                cart_rep += 1

        else:  # if the input number is not 1-12, then error message will be prompted
            print("\nInvalid input, Please try again\n")

            repeat += 0  # loops back to the order menu

    except(ValueError):  # if the input number is not a number(value error), then error message will be prompted
        print("\nInvalid input, Please try again\n")

        repeat += 0  # loops back to the order menu

    if cart_rep == 1:  # if the cart and order confirmation activates
        print(
            "------------------------------------------\nYou have ordered:\n")  # tell the user what they have ordered.
        if cs > 0:
            print("1. Caesar Salad\t\t\tx" + str(cs))
        if gs > 0:
            print("2. Garden Salad\t\t\tx" + str(gs))
        if hotdog > 0:
            print("3. Hotdog\t\t\tx" + str(hotdog))
        if hamburger > 0:
            print("4. Hamburger\t\t\tx" + str(hamburger))
        if fries > 0:
            print("5. French Fries\t\t\tx" + str(fries))
        if cp > 0:
            print("6. Cheese Pizza\t\t\tx" + str(cp))
        if pp > 0:
            print("7. Pepperoni Pizza\t\tx" + str(pp))
        if hp > 0:
            print("8. Hawaiian Pizza\t\tx" + str(hp))
        if water > 0:
            print("9. Water\t\t\tx" + str(water))
        if coke > 0:
            print("10.Coke\t\t\t\tx" + str(coke))
        if fanta > 0:
            print("11.Fanta\t\t\tx" + str(fanta))
        if sprite > 0:
            print("12.Sprite\t\t\tx" + str(sprite))
        # only the items that have been placed in the cart would appear in the list
        print("\nThe current subtotal price is: $" + str(round(sub, 2)))  # displays current subtotal price.
        time.sleep(1)  # short pause
        while rep_conf != 1:  # while loop for the reorder process
            rep = input(
                "------------------------------------------\n\nDo you want to order more? (\"y\" for yes, \"n\" for no)\nYou can edit your ordered items by entering \"e\"\n\nEnter Option Here: ")
            if rep == "y":  # ask for user input to reorder (above), if the input is yes then it loops back to the order menu
                print("\nPlease wait.....\n")
                cart_rep -= 1  # leave the cart and order confirmation loop
                repeat += 0  # loops back to the order menu
                time.sleep(1)  # short pause
                break  # break/end this part of the program
            elif rep == "n":  # if the input is no
                if sub > 0:  # checks if the subtotal amount is 0 or not, if the subtotal is above 0 (if user did order something)
                    print("\nThank you for ordering, please wait while we process your receipt......\n")
                    time.sleep(1)  # short pause
                    repeat += 1  # goes to receipt
                    break  # break/end this part of the program
                if sub == 0:  # if the subtotal is at 0 (if use did not order/emptied their cart)
                    print("\nThere are no items to checkout")
                    time.sleep(1)  # short pause
                    repeat += 0  # loops back to the order menu
            elif rep == "e":  # if the user input is e (if user wants to edit the cart)
                if sub > 0:  # if the subtotoal is above 0
                    print(
                        "------------------------------------------\nYou have ordered:\n")  # shows the user what they have ordered and the subtotal
                    if cs > 0:
                        print("1. Caesar Salad\t\t\tx" + str(cs))
                    if gs > 0:
                        print("2. Garden Salad\t\t\tx" + str(gs))
                    if hotdog > 0:
                        print("3. Hotdog\t\t\tx" + str(hotdog))
                    if hamburger > 0:
                        print("4. Hamburger\t\t\tx" + str(hamburger))
                    if fries > 0:
                        print("5. French Fries\t\t\tx" + str(fries))
                    if cp > 0:
                        print("6. Cheese Pizza\t\t\tx" + str(cp))
                    if pp > 0:
                        print("7. Pepperoni Pizza\t\tx" + str(pp))
                    if hp > 0:
                        print("8. Hawaiian Pizza\t\tx" + str(hp))
                    if water > 0:
                        print("9. Water\t\t\tx" + str(water))
                    if coke > 0:
                        print("10.Coke\t\t\t\tx" + str(coke))
                    if fanta > 0:
                        print("11.Fanta\t\t\tx" + str(fanta))
                    if sprite > 0:
                        print("12.Sprite\t\t\tx" + str(sprite))

                    print("\nThe current subtotal price is: $" + str(
                        round(sub, 2)) + "\n------------------------------------------")
                    time.sleep(1)
                    print("\nWhich item do you want to remove?")  # asks the user which item to remove

                    edit = input("Enter the item number: ").lower()  # asks the user to enter the item number
                    while remove_rep != 1:  # while loop for the cart edit process
                        try:  # try and except for value errors
                            if edit == "1":  # if the item number entered is 1
                                if cs > 0:  # if the item is above 0, then it asks how many to remove
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= cs:  # if the user input is 1 and above, and the limit is under the number of items ordered
                                        cs = cs - remove  # updates the stored value of the item after removal
                                        sub = sub - (remove * 4.99)  # updates the subtotal price after removal of item
                                        cs_cost = cs_cost - (remove * 4.99)  # updates the item cost after removal
                                        print("\nItem amount subtracted to:", cs)  # prints out the statements
                                        if sub > 0:  # if the subtotal is above 0, then it tells the user the subtotal price
                                            print("Subtotal price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)  # short pause
                                            remove_rep += 0  # loops back to the reorder process
                                            break  # break/end this part of the program
                                        if sub == 0:  # if the subtotal is at 0, it tells the user that there is nothing left in the cart
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0  # loops back to order menu
                                            break  # break/end this part of the program
                                    elif remove < 1:  # if the number of items to remove is below 1, then error message will be prompted
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0  # loops back to the reorder message
                                        break  # break/end this part of the program
                                    elif remove > cs:  # if the user input is greater than the number of items ordered, then error message will be prompted
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0  # loops back to the reorder message
                                        break  # break/end this part of the program
                                elif cs <= 0:  # if the number of the requested item is 0, then it tells the user there is no items to edit.
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0  # loops back to the reorder process
                                    break  # break/end this part of the program
                            # same process goes from option 1 to 12. the only difference is the cost and the variables of the items.
                            if edit == "2":
                                if gs > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= gs:
                                        gs = gs - remove
                                        sub = sub - (remove * 4.99)
                                        gs_cost = gs_cost - (remove * 4.99)
                                        print("\nItem amount subtracted to:", gs)
                                        if sub > 0:
                                            print("Subtotal price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > gs:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif gs <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "3":
                                if hotdog > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= hotdog:
                                        hotdog = hotdog - remove
                                        sub = sub - (remove * 3.49)
                                        hotdog_cost = hotdog_cost - (remove * 3.49)
                                        print("\nItem amount subtracted to:", hotdog)
                                        if sub > 0:
                                            print("Subtotal price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > hotdog:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif hotdog <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "4":
                                if hamburger > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= hamburger:
                                        hamburger = hamburger - remove
                                        sub = sub - (remove * 3.99)
                                        hamburg_cost = hamburg_cost - (remove * 3.99)
                                        print("\nItem amount subtracted to:", hamburger)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > hamburger:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif hamburger <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "5":
                                if fries > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= fries:
                                        fries = fries - remove
                                        sub = sub - (remove * 1.99)
                                        fries_cost = fries_cost - (remove * 1.99)
                                        print("\nItem amount subtracted to:", fries)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > fries:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif fries <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "6":
                                if cp > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= cp:
                                        cp = cp - remove
                                        sub = sub - (remove * 2.49)
                                        cp_cost = cp_cost - (remove * 2.49)
                                        print("\nItem amount subtracted to:", cp)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > cp:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif cp <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "7":
                                if pp > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= pp:
                                        pp = pp - remove
                                        sub = sub - (remove * 2.99)
                                        pp_cost = pp_cost - (remove * 2.99)
                                        print("\nItem amount subtracted to:", pp)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > pp:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif pp <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "8":
                                if hp > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= hp:
                                        hp = hp - remove
                                        sub = sub - (remove * 3.49)
                                        hp_cost = hp_cost - (remove * 3.49)
                                        print("\nItem amount subtracted to:", hp)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > hp:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif hp <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "9":
                                if water > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= water:
                                        water = water - remove
                                        sub = sub - (remove * 0.99)
                                        water_cost = water_cost - (remove * 0.99)
                                        print("\nItem amount subtracted to:", water)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > water:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif water <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "10":
                                if coke > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= coke:
                                        coke = coke - remove
                                        sub = sub - (remove * 1.49)
                                        coke_cost = coke_cost - (remove * 1.49)
                                        print("\nItem amount subtracted to:", coke)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > coke:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif coke <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "11":
                                if fanta > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= fanta:
                                        fanta = fanta - remove
                                        sub = sub - (remove * 1.49)
                                        fanta_cost = fanta_cost - (remove * 1.49)
                                        print("\nItem amount subtracted to:", fanta)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > fanta:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif fanta <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            if edit == "12":
                                if sprite > 0:
                                    remove = int(input("How many do you want to remove?: "))
                                    if remove >= 1 and remove <= sprite:
                                        sprite = sprite - remove
                                        sub = sub - (remove * 1.49)
                                        sprite_cost = sprite_cost - (remove * 1.49)
                                        print("\nItem amount subtracted to:", sprite)
                                        if sub > 0:
                                            print("Total price is now at: $" + str(round(sub, 2)))
                                            time.sleep(1)
                                            remove_rep += 0
                                            break
                                        if sub == 0:
                                            time.sleep(1)
                                            print("There is nothing left in your cart.")
                                            time.sleep(1)
                                            repeat += 0
                                            break
                                    elif remove < 1:
                                        print("\nInvalid Input, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                    elif remove > sprite:
                                        print("\nInput amount too big, Please try again.")
                                        time.sleep(1)
                                        remove_rep += 0
                                        break
                                elif sprite <= 0:
                                    print("\nThere are no items available to edit.")
                                    time.sleep(1)
                                    remove_rep += 0
                                    break

                            else:  # if the item number entered is not between 1-12 then error message will be prompted
                                print("\nInvalid input, Please try again.")

                                remove_rep += 0  # loops back the reorder process
                                break
                        except(ValueError):  # if the input is not a number, then error message will be prompted
                            print("\nInvalid Input, Please try again.\n")

                            remove_rep += 0  # loops back to the reorder process

                else:  # if there is nothing left in the cart, then error message will be prompted
                    print("\nThere are no items in your cart to edit")

                    rep_conf += 0  # loops back to the reorder process
            else:  # if the user input is not y, n, or e, then error message will be prompted
                print("\nInvalid input, Please try again.")

                remove_rep += 0  # loops back to the reorder process

if repeat == 1:  # if receipt is activated
    print(
        "Here is your receipt:\n=====================================================================\nKyle's Kitchen\n\nYour Order:\n")
    print(
        "Item\t\t\tQuantity\t\tPrice\n==========================================================")  # print receipt, the cost and quantity
    if cs > 0:
        print("1. Caesar Salad\t\t" + str(cs) + "\t\t\t$" + str(round(cs_cost, 2)))
    if gs > 0:
        print("2. Garden Salad\t\t" + str(gs) + "\t\t\t$" + str(round(gs_cost, 2)))
    if hotdog > 0:
        print("3. Hotdog\t\t" + str(hotdog) + "\t\t\t$" + str(round(hotdog_cost, 2)))
    if hamburger > 0:
        print("4. Hamburger\t\t" + str(hamburger) + "\t\t\t$" + str(round(hamburg_cost, 2)))
    if fries > 0:
        print("5. French Fries\t\t" + str(fries) + "\t\t\t$" + str(round(fries_cost, 2)))
    if cp > 0:
        print("6. Cheese Pizza\t\t" + str(cp) + "\t\t\t$" + str(round(cp_cost, 2)))
    if pp > 0:
        print("7. Pepperoni Pizza\t" + str(pp) + "\t\t\t$" + str(round(pp_cost, 2)))
    if hp > 0:
        print("8. Hawaiian Pizza\t" + str(hp) + "\t\t\t$" + str(round(hp_cost, 2)))
    if water > 0:
        print("9. Water\t\t" + str(water) + "\t\t\t$" + str(round(water_cost, 2)))
    if coke > 0:
        print("10.Coke\t\t\t" + str(coke) + "\t\t\t$" + str(round(coke_cost, 2)))
    if fanta > 0:
        print("11.Fanta\t\t" + str(fanta) + "\t\t\t$" + str(round(fanta_cost, 2)))
    if sprite > 0:
        print("12.Sprite\t\t" + str(sprite) + "\t\t\t$" + str(round(sprite_cost, 2)))

    print("\nSubtotal:\t\t\t\t\t$" + str(round(sub, 2)))  # subtotal
    print("Tax (HST 13%):\t\t\t\t\t$" + str(round((sub * 1.13) - sub, 2)))  # tax
    print("Your Total after tax is:\t\t\t$" + str(round(sub * 1.13, 2)))  # total after tax
    print("\t\t\t\t\t    ==============")
    print("\nThank you for coming to Kyle's Kitchen!")
    time.sleep(1)
    while tax_rep != 1:  # while loop for tips input (messed up tax and tips)
        print(
            "\n=====================================================================\nPlease enter the amount of tips you would like to pay:")
        print("1. 10%\n2. 15%\n3. 20%\n4. Other\n5. No Tips")  # 5 options
        tax = input("Enter Here: ")
        try:  # try and except function in case of value errors
            if tax == "1":  # if the input is 1, it multiplies the total after tax by 10% then displays the final total.
                total = round((sub * 1.13) * 1.1, 2)  # stores the total value for later
                print("\nYour final total is: $" + str(round((sub * 1.13) * 1.1,
                                                             2)))  # displays final total (did not use the total variable because value error
                time.sleep(1)  # short pause
                break  # break and it goes down to the next process
            # Same process goes for input 2 - 4 just different variables and tips amount
            elif tax == "2":
                total = round((sub * 1.13) * 1.15, 2)
                print("\nYour final total is: $" + str(round((sub * 1.13) * 1.15, 2)))
                time.sleep(1)
                break
            elif tax == "3":
                total = round((sub * 1.13) * 1.2, 2)
                print("\nYour final total is: $" + str(round((sub * 1.13) * 1.2, 2)))
                time.sleep(1)
                break
            elif tax == "4":  # if the input is 4, it asks user for the tip percentage
                percent = int(input("Please enter the % amount for tips: "))
                if percent > 0:  # if the input is above 0 then executes the process below (pretty much the same as the options above but the user can input any percentage)
                    decimal = percent / 100  # simplifies the equation below
                    total = round((sub * 1.13) + (sub * 1.13 * decimal), 2)
                    print("\nYour final total is: $" + str(round((sub * 1.13) + (sub * 1.13 * decimal), 2)))
                    time.sleep(1)
                    break
                elif percent <= 0:  # if the input is 0 and below, then error message will prompt
                    print("\nPercentage is not valid. Please try again.")
                    time.sleep(1)
                    tax_rep += 0
            elif tax == "5":  # if the input is 5, which is no tips, then the final total does not change
                total = round(sub * 1.13, 2)
                print("\nYour final total is: $" + str(round((sub * 1.13), 2)))
                time.sleep(1)
                break
            else:  # if the input is not 1-5, then error message will prompt
                print("\nInvalid input. Please try again.")

                tax_rep += 0  # loops back to ask the user for tips amount

        except(ValueError):  # if the input is not a number (value error), then the error message will prompt
            print("\nInvalid Input. Please try again.")

            tax_rep += 0  # loops back to ask the user for tips amount

    while payment_rep != 1:  # while loop for the next process, which is the payment option
        print(
            "\n=====================================================================\nPlease Select the type of payment:\n1. Cash\n2. Credit Card")
        payment = input("Enter Here: ")  # ask the user for cash or credit card
        try:  # try and except for value errors
            if payment == "1":  # if the user wants to pay cash
                cash = float(input(
                    "Please enter the amount of cash you are paying: $"))  # asks the user how much they are paying in cash
                print("\nPlease wait while we are processing the payment.....")
                time.sleep(1)  # short pause
                if cash >= round(total,
                                 2):  # checks if the cash input is more than the total price, if cash input is higher than total price
                    print("==========================================================\n\t\t      Kyle's Kitchen")
                    print("      123 Big House Drive, Markham, Ontario, L3R 4J9")
                    print(
                        "\nItem\t\t\tQuantity\t\tPrice\n==========================================================")  # print receipt, the cost and quantity
                    if cs > 0:
                        print("1. Caesar Salad\t\t" + str(cs) + "\t\t\t$" + str(round(cs_cost, 2)))
                    if gs > 0:
                        print("2. Garden Salad\t\t" + str(gs) + "\t\t\t$" + str(round(gs_cost, 2)))
                    if hotdog > 0:
                        print("3. Hotdog\t\t" + str(hotdog) + "\t\t\t$" + str(round(hotdog_cost, 2)))
                    if hamburger > 0:
                        print("4. Hamburger\t\t" + str(hamburger) + "\t\t\t$" + str(round(hamburg_cost, 2)))
                    if fries > 0:
                        print("5. French Fries\t\t" + str(fries) + "\t\t\t$" + str(round(fries_cost, 2)))
                    if cp > 0:
                        print("6. Cheese Pizza\t\t" + str(cp) + "\t\t\t$" + str(round(cp_cost, 2)))
                    if pp > 0:
                        print("7. Pepperoni Pizza\t" + str(pp) + "\t\t\t$" + str(round(pp_cost, 2)))
                    if hp > 0:
                        print("8. Hawaiian Pizza\t" + str(hp) + "\t\t\t$" + str(round(hp_cost, 2)))
                    if water > 0:
                        print("9. Water\t\t" + str(water) + "\t\t\t$" + str(round(water_cost, 2)))
                    if coke > 0:
                        print("10.Coke\t\t\t" + str(coke) + "\t\t\t$" + str(round(coke_cost, 2)))
                    if fanta > 0:
                        print("11.Fanta\t\t" + str(fanta) + "\t\t\t$" + str(round(fanta_cost, 2)))
                    if sprite > 0:
                        print("12.Sprite\t\t" + str(sprite) + "\t\t\t$" + str(round(sprite_cost, 2)))

                    print("\nSubtotal:\t\t\t\t\t$" + str(round(sub, 2)))  # subtotal
                    print("Tax (HST 13%):\t\t\t\t\t$" + str(round((sub * 1.13) - sub, 2)))  # tax
                    print("Tips:\t\t\t\t\t\t$" + str(round(total - (sub * 1.13), 2)))  # tips
                    print("Your final total is:\t\t\t\t$" + str(round(total, 2)))  # total after tax
                    print("\t\t\t\t\t    ==============")
                    print("Payment Method: \t\t\t    Cash($" + str(round(cash, 2)) + ")")
                    print("The change is:\t\t\t\t\t$" + str(round((cash - total), 2)))  # change
                    time.sleep(1)  # short pause
                    print(
                        "\n==========================================================\n\t Thank you for coming to Kyle's Kitchen!\n==========================================================")
                    break  # end of program
                elif cash < round(total,
                                  2):  # if cash is below the total price, tells the user that they don't have enough
                    print("\nYou do not have enough money! Please try again.")
                    time.sleep(1.5)
                    payment_rep += 0  # loops back to ask for payment option
            elif payment == "2":  # if the user wants to pay with credit card, it asks the user which card to pay with
                card = input(
                    "\nWhich Card are you using?\n1. Visa Card\n2. Mastercard\n3. American Express\nEnter Here: ")
                if card == "1":  # if the user wants to play with visa, it tells the user to input card number
                    cardnum = input("Please input your card number: ")
                    cardlist = [int(x) for x in cardnum]  # splits the input into a list
                    if cardlist[0] == 4:  # if the first number of the input is a 4
                        pin = int(input("Please enter your security pin: "))  # asks for security pin
                        print("\nVerifying Purchase, Please wait.....")
                        time.sleep(1.25)
                        print("\nPayment Successful!")  # tells the user that the payment is successful
                        time.sleep(1.5)
                        print("==========================================================\n\t\t      Kyle's Kitchen")
                        print("      123 Big House Drive, Markham, Ontario, L3R 4J9")
                        print(
                            "\nItem\t\t\tQuantity\t\tPrice\n==========================================================")  # print receipt, the cost and quantity
                        if cs > 0:
                            print("1. Caesar Salad\t\t" + str(cs) + "\t\t\t$" + str(round(cs_cost, 2)))
                        if gs > 0:
                            print("2. Garden Salad\t\t" + str(gs) + "\t\t\t$" + str(round(gs_cost, 2)))
                        if hotdog > 0:
                            print("3. Hotdog\t\t" + str(hotdog) + "\t\t\t$" + str(round(hotdog_cost, 2)))
                        if hamburger > 0:
                            print("4. Hamburger\t\t" + str(hamburger) + "\t\t\t$" + str(round(hamburg_cost, 2)))
                        if fries > 0:
                            print("5. French Fries\t\t" + str(fries) + "\t\t\t$" + str(round(fries_cost, 2)))
                        if cp > 0:
                            print("6. Cheese Pizza\t\t" + str(cp) + "\t\t\t$" + str(round(cp_cost, 2)))
                        if pp > 0:
                            print("7. Pepperoni Pizza\t" + str(pp) + "\t\t\t$" + str(round(pp_cost, 2)))
                        if hp > 0:
                            print("8. Hawaiian Pizza\t" + str(hp) + "\t\t\t$" + str(round(hp_cost, 2)))
                        if water > 0:
                            print("9. Water\t\t" + str(water) + "\t\t\t$" + str(round(water_cost, 2)))
                        if coke > 0:
                            print("10.Coke\t\t\t" + str(coke) + "\t\t\t$" + str(round(coke_cost, 2)))
                        if fanta > 0:
                            print("11.Fanta\t\t" + str(fanta) + "\t\t\t$" + str(round(fanta_cost, 2)))
                        if sprite > 0:
                            print("12.Sprite\t\t" + str(sprite) + "\t\t\t$" + str(round(sprite_cost, 2)))
                        print("\nSubtotal:\t\t\t\t\t$" + str(round(sub, 2)))  # subtotal
                        print("Tax (HST 13%):\t\t\t\t\t$" + str(round((sub * 1.13) - sub, 2)))  # tax
                        print("Tips:\t\t\t\t\t\t$" + str(round(total - (sub * 1.13), 2)))  # tips
                        print("Your final total is:\t\t\t\t$" + str(round(total, 2)))  # total after tax
                        print("\t\t\t\t\t    ==============")
                        print("Payment Method:\t\t\t\t     Credit(Visa)")
                        time.sleep(1)  # short pause
                        print(
                            "\n==========================================================\n\t Thank you for coming to Kyle's Kitchen!\n==========================================================")
                        break  # end of program
                # same process if the user wants to give mastercard or american express, only the beginning of card number is different
                if card == "2":  # mastercard
                    cardnum = input("Please input your card number: ")
                    cardlist = [int(x) for x in cardnum]
                    if cardlist[0] == 5 and cardlist[1] >= 1 and cardlist[
                        1] <= 5:  # if the card number input begins with 51-55
                        pin = int(input("Please enter your security pin: "))
                        print("\nVerifying Purchase, Please wait.....")
                        time.sleep(1.25)
                        print("\nPayment Successful!")
                        time.sleep(1.5)
                        print("==========================================================\n\t\t      Kyle's Kitchen")
                        print("      123 Big House Drive, Markham, Ontario, L3R 4J9")
                        print(
                            "\nItem\t\t\tQuantity\t\tPrice\n==========================================================")  # print receipt, the cost and quantity
                        if cs > 0:
                            print("1. Caesar Salad\t\t" + str(cs) + "\t\t\t$" + str(round(cs_cost, 2)))
                        if gs > 0:
                            print("2. Garden Salad\t\t" + str(gs) + "\t\t\t$" + str(round(gs_cost, 2)))
                        if hotdog > 0:
                            print("3. Hotdog\t\t" + str(hotdog) + "\t\t\t$" + str(round(hotdog_cost, 2)))
                        if hamburger > 0:
                            print("4. Hamburger\t\t" + str(hamburger) + "\t\t\t$" + str(round(hamburg_cost, 2)))
                        if fries > 0:
                            print("5. French Fries\t\t" + str(fries) + "\t\t\t$" + str(round(fries_cost, 2)))
                        if cp > 0:
                            print("6. Cheese Pizza\t\t" + str(cp) + "\t\t\t$" + str(round(cp_cost, 2)))
                        if pp > 0:
                            print("7. Pepperoni Pizza\t" + str(pp) + "\t\t\t$" + str(round(pp_cost, 2)))
                        if hp > 0:
                            print("8. Hawaiian Pizza\t" + str(hp) + "\t\t\t$" + str(round(hp_cost, 2)))
                        if water > 0:
                            print("9. Water\t\t" + str(water) + "\t\t\t$" + str(round(water_cost, 2)))
                        if coke > 0:
                            print("10.Coke\t\t\t" + str(coke) + "\t\t\t$" + str(round(coke_cost, 2)))
                        if fanta > 0:
                            print("11.Fanta\t\t" + str(fanta) + "\t\t\t$" + str(round(fanta_cost, 2)))
                        if sprite > 0:
                            print("12.Sprite\t\t" + str(sprite) + "\t\t\t$" + str(round(sprite_cost, 2)))
                        print("\nSubtotal:\t\t\t\t\t$" + str(round(sub, 2)))  # subtotal
                        print("Tax (HST 13%):\t\t\t\t\t$" + str(round((sub * 1.13) - sub, 2)))  # tax
                        print("Tips:\t\t\t\t\t\t$" + str(round(total - (sub * 1.13), 2)))  # tips
                        print("Your final total is:\t\t\t\t$" + str(round(total, 2)))  # total after tax
                        print("\t\t\t\t\t    ==============")
                        print("Payment Method:\t\t\t\tCredit(Mastercard)")
                        time.sleep(1)  # short pause
                        print(
                            "\n==========================================================\n\t Thank you for coming to Kyle's Kitchen!\n==========================================================")
                        break  # end of program

                if card == "3":  # american express
                    cardnum = input("Please input your card number: ")
                    cardlist = [int(x) for x in cardnum]
                    if cardlist[0] == 3 and cardlist[1] == 4 or cardlist[0] == 3 and cardlist[
                        1] == 7:  # if the card number input begins with 34 or 37
                        pin = int(input("Please enter your security pin: "))
                        print("\nVerifying Purchase, Please wait.....")
                        time.sleep(1.25)
                        print("\nPayment Successful!")
                        time.sleep(1.5)
                        print("==========================================================\n\t\t      Kyle's Kitchen")
                        print("      123 Big House Drive, Markham, Ontario, L3R 4J9")
                        print(
                            "\nItem\t\t\tQuantity\t\tPrice\n==========================================================")  # print receipt, the cost and quantity
                        if cs > 0:
                            print("1. Caesar Salad\t\t" + str(cs) + "\t\t\t$" + str(round(cs_cost, 2)))
                        if gs > 0:
                            print("2. Garden Salad\t\t" + str(gs) + "\t\t\t$" + str(round(gs_cost, 2)))
                        if hotdog > 0:
                            print("3. Hotdog\t\t" + str(hotdog) + "\t\t\t$" + str(round(hotdog_cost, 2)))
                        if hamburger > 0:
                            print("4. Hamburger\t\t" + str(hamburger) + "\t\t\t$" + str(round(hamburg_cost, 2)))
                        if fries > 0:
                            print("5. French Fries\t\t" + str(fries) + "\t\t\t$" + str(round(fries_cost, 2)))
                        if cp > 0:
                            print("6. Cheese Pizza\t\t" + str(cp) + "\t\t\t$" + str(round(cp_cost, 2)))
                        if pp > 0:
                            print("7. Pepperoni Pizza\t" + str(pp) + "\t\t\t$" + str(round(pp_cost, 2)))
                        if hp > 0:
                            print("8. Hawaiian Pizza\t" + str(hp) + "\t\t\t$" + str(round(hp_cost, 2)))
                        if water > 0:
                            print("9. Water\t\t" + str(water) + "\t\t\t$" + str(round(water_cost, 2)))
                        if coke > 0:
                            print("10.Coke\t\t\t" + str(coke) + "\t\t\t$" + str(round(coke_cost, 2)))
                        if fanta > 0:
                            print("11.Fanta\t\t" + str(fanta) + "\t\t\t$" + str(round(fanta_cost, 2)))
                        if sprite > 0:
                            print("12.Sprite\t\t" + str(sprite) + "\t\t\t$" + str(round(sprite_cost, 2)))
                        print("\nSubtotal:\t\t\t\t\t$" + str(round(sub, 2)))  # subtotal
                        print("Tax (HST 13%):\t\t\t\t\t$" + str(round((sub * 1.13) - sub, 2)))  # tax
                        print("Tips:\t\t\t\t\t\t$" + str(round(total - (sub * 1.13), 2)))
                        print("Your final total is:\t\t\t\t$" + str(round(total, 2)))  # total after tax
                        print("\t\t\t\t\t    ==============")
                        print("Payment Method:\t\t\t  Credit(American Express)")
                        time.sleep(1)  # short pause
                        print(
                            "\n==========================================================\n\t Thank you for coming to Kyle's Kitchen!\n==========================================================")
                        break  # end of program
                    else:
                        print("\nInvalid Input. Please try again.")  # error message will be prompted

                        payment_rep += 0
                else:  # if the input for card option is not 1-3, or if the card number entered does not satisfy the conditions
                    print("\nInvalid Input. Please try again.")  # error message will be prompted

                    payment_rep += 0  # loops back to ask for payment option
            else:  # if the user input for payment option is not 1 or 2, then the following error message will be prompted
                print("\nInvalid Input, Please enter 1 or 2 for the payment option.")
                # the while loop of payment option will automatically occur
        except(
        ValueError):  # handles all value errors in this process, if any of the specified int input is not a number, then error message will be prompted
            print("\nInvalid Input. Please try again.")

            payment_rep += 0  # loops back to ask for payment option
