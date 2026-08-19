
def calculate_tip(bill,tip_percent):
    tip_amount=bill*(tip_percent/100)
    return tip_amount




while True:
    bill_amount=float(input("What is your bill amount?\n>"))
    tip_percentage=float(input("What is the tip percentage?\n>"))
    final_tip=calculate_tip(bill_amount,tip_percentage)
    print(f"Tip amount: ${final_tip}")
    again=input("Do you want to calculate another tip? (yes/no): ")
    if again=="yes":
        continue
    else:
        break 