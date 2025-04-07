def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

print("Script started...")  # Debug print

price = float(input("Enter the original price of the item: "))
print(f"Original price: {price}")  # Debug print

discount_percent = float(input("Enter the discount percentage: "))
print(f"Discount percentage: {discount_percent}")  # Debug print

final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying the discount is: {final_price}")
