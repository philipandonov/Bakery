from bakery.bakery import Bakery

bakery = Bakery("Random Name")
print(bakery.add_drink('Tea', 'Carrot cake', 3.5,'ew'))
print(bakery.add_drink('Water', 'Banana Bread', 2.5,'das'))
print(bakery.add_drink('Tea', 'Chocolate cake', 4,'eads'))
print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.reserve_table(10))
print(bakery.order_drink(55, 'Carrot cake', 'Banana Bread', 'Chocolate cake', 'Banana Puding', 'Pankecas' ))
print(bakery.leave_table(55))