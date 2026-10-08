# PART 1: define a function with no arguements to greet the customer
def greet_customer():
    print("Welcome to My Lemonade Stand!")
    print("Fresh lemonade- made just for you.")

    # PART 2: call the greet_customer function
    greet_customer()

    # PART 3: ask for the price per cup, and the number of cups sold
    price_per_cup = float(input("Enter the price per cup in rupees: "))
    cups_sold = int(input("Enter the number of cups sold: "))

    # PART 4: define a function that takes an aruguement and returns the total cost
    def calculate_total(price, cups):
        total = price * cups
        return total

    # PART 5: call calculate_total function and store the value it returns
    total_cost = calculate_total(price_per_cup, cups_sold)

    # PART 6: use a built-in function to round the total, then print it
    rounded_total = round(total_cost,)
    print("Total cost:", rounded_total)

    # PART 7: ask how much money the customer paid
    amount_paid = float(input("Enter the amount paid by the customer: "))

    # PART 8: define a function that takes arguements and returns a thank you message based on cups sold
    def thank_you_message(cups): 
        if cups <= 5:
            # PART 9: call calculate_change and store the value it returns
            change_due = calculate_change(amount_paid, rounded_total)
            rounded_change = round(change_due, 2)

     # PART 10: define a function that returns a thank you message based on cups sold
            def thank_you_message(cups):
                if cups >= 5:
                    return "Wow!, big order! Thanks so much for your support!"
                else:
                    return "Thanks for Stopping by the Stand!" 

    # PART 11: call thank_you_message and store the value it returns
            closing_message = thank_you_message(cups_sold)

     # PART 12: print the final lemonade stand receipt
        print("")
        print("====== LEMONADE STAND RECEIPT ======")
        print("Price per cup: ", price_per_cup)
        print("Cups sold: ", cups_sold)
        print("Total cost: ", total_cost)
        print("Amount paid: ", amount_paid)
        print("Change due: ", change_due)
        print(closing_message)
        print("==================================================")