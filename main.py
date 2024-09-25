# PA00 Code Assignment for CompSci. Created by John Elehwany
# This program requires the user to input prices for groceries from different stores and then calculates the average price
# of groceries from each store.

print("""
Grocery Store Average Price Calculator
for Walmart, Acme, & Wegmans

- WALMART PRICES -""")
# Input for prices from Walmart
bananas_walmart = float(input('Enter the price of bananas from Walmart: '))
oranges_walmart = float(input('Enter the price of oranges from Walmart: '))
cmilk_walmart = float(input('Enter the price of chocolate milk from Walmart: '))
glue_walmart = float(input('Enter the price of glue from Walmart: '))
psugar_walmart = float(input('Enter the price of powdered sugar from Walmart: '))

# Determines average price of Walmart groceries
walmart_avg = (bananas_walmart + oranges_walmart + cmilk_walmart + glue_walmart + psugar_walmart) / 5
# Outputs Walmart average
print(f"""
The average price of groceries at Walmart is: ${walmart_avg:.2f}""")

# Input for prices from Acme
print("""
- ACME PRICES -""")
bananas_acme = float(input('Enter the price of bananas from Acme: '))
oranges_acme = float(input('Enter the price of oranges from Acme: '))
cmilk_acme = float(input('Enter the price of chocolate milk from Acme: '))
glue_acme = float(input('Enter the price of glue from Acme: '))
psugar_acme = float(input('Enter the price of powdered sugar from Acme: '))

# Determines average price of Acme groceries
acme_avg = (bananas_acme + oranges_acme + cmilk_acme + glue_acme + psugar_acme) / 5
# Outputs Acme average
print(f"""
The average price of groceries at Acme is: ${acme_avg:.2f}""")

# Input for prices from Wegmans
print("""
- WEGMANS PRICES -""")
bananas_wegmans = float(input('Enter the price of bananas from Wegmans: '))
oranges_wegmans = float(input('Enter the price of oranges from Wegmans: '))
cmilk_wegmans = float(input('Enter the price of chocolate milk from Wegmans: '))
glue_wegmans = float(input('Enter the price of glue from Wegmans: '))
psugar_wegmans = float(input('Enter the price of powdered sugar from Wegmans: '))

# Determines average price of Wegmans groceries
wegmans_avg = (bananas_wegmans + oranges_wegmans + cmilk_wegmans + glue_wegmans + psugar_wegmans) / 5
# Outputs Acme average
print(f"""
The average price of groceries at Wegmans is: ${wegmans_avg:.2f}""")

# Calculates the total average of all three stores
total_avg = (walmart_avg + acme_avg + wegmans_avg) / 3
# Outputs total average
print(f"""

- TOTAL AVERAGE PRICE OF ALL STORES: -
The total average price for groceries from all three stores is: ${total_avg:.2f}""")
