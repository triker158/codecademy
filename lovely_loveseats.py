# variables
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep.  Red or white."
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = 0.088
customer_one_total = 0
customer_one_itemization = ""
customer_one_tax = 0

# customer one
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = "Item1: " + lovely_loveseat_description + "\nItem2: " + luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# customer one receipt
print("Customer One Items:")
print()
print(customer_one_itemization)
print()
print("Customer One Total:")
# print("$ " + str(customer_one_total))
print("$ {:0.2f}".format(customer_one_total))

# Using str.format()'s syntax to display answer with two 
# decimal places (without altering the underlying value of answer):
# Where:

# : introduces the format spec
# 0 enables sign-aware zero-padding for numeric types
# .2 sets the precision to 2
# f displays the number as a fixed-point number