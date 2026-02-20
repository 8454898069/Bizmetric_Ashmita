hotel_name = "Welcome Hotel"

# menu dictionary (item : price)
menu_dict = {
    1: ("Idli", 30),
    2: ("Dosa", 50),
    3: ("Vada", 25),
    4: ("Puri", 40)
}

# ----- show menu -----
print("\nMENU")
print("-" * 30)
for key, value in menu_dict.items():
    print(f"{key}. {value[0]} - ₹{value[1]}")
print("-" * 30)

# ----- take user input -----
choice = int(input("Enter item number: "))
quant = int(input("Enter quantity: "))

item_name, price = menu_dict[choice]
total = price * quant

# ----- create bill text -----
bill = (
    "-" * 40 + "\n" +
    f"{hotel_name:^40}\n" +
    "-" * 40 + "\n" +
    f"{'sr':<5}{'menu':<15}{'quant':>13}{'price':>7}\n" +
    f"{1:<5}{item_name:<15}{quant:>13}{price:>7}\n" +
    "-" * 40 + "\n" +
    f"{'Total':<30}{total}\n" +
    "-" * 40
)

# print bill
print("\n" + bill)

# save to file (overwrite)
with open("bill.txt", "w") as f:
    f.write(bill)

print("\nBill saved to bill.txt")
