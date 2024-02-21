#coffee shop simulator
#introduction
print('Welcome to ferns bakery and coffee shop')
print('how may I get u started today:3')

#prices
pricecoffee = 5
pricemuffin = 4

#asking user for the quanities
coffee = int(input('number of coffees:'))
muffins = int(input('number of muffins'))

#multiplying price and number of items
sub_coffees = coffee*pricecoffee
sub_muffins = muffins*pricemuffin

#before tax:)
sub = sub_coffees + sub_muffins

#with tax:(
tax = .06
sub_tax = tax*sub
total = sub+sub_tax

#total
print('Total is $' + str(total))
print('thank you for shopping with us today. Enjoy :3')
