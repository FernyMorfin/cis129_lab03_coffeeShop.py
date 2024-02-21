#coffee shop simulator
#introduction
print(' ...')
print('✿  Welcome to ferns bakery and coffee shop  ✿')
print(' ')
print('|*******MENU********|')
print('|coffe   $5         |')
print('|muffins $4         |')
print('|tea     $2         |')
print('|block of cheese  $7|')
print('|___________________|')
print(' ')
print('how may I get u started today  (─‿ ‿ ─)')
print(' ')

#prices
pricecoffee = 5
pricemuffin = 4
pricetea = 2
pricecheese = 7

#asking user for the quanities
coffee = int(input('number of coffees:'))
muffins = int(input('number of muffins'))
tea = int(input('number of tea:'))
cheese = int(input('number of cheese blocks:'))

#multiplying price and number of items
sub_coffees = coffee*pricecoffee
sub_muffins = muffins*pricemuffin
sub_tea = tea * pricecheese
sub_blockofcheese = cheese*pricecheese

#before tax:)
sub = sub_coffees + sub_muffins + sub_tea + sub_blockofcheese

#with tax:(
tax = .06
sub_tax = tax*sub
total = sub+sub_tax

#total
print("...")
print('your Total is $' + str(total))
print('✿')
print('✿  Thank you for shopping with us  ✿')
print('✿  Enjoy ʕ•́ᴥ•̀ʔっ ✿')
