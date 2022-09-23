from decimal import Decimal
import pprint
import pickle
import json

products = [
    {'name': 'Soap', 'quantity': 3, 'price': 23.50, 'is_expired': False},
    {'name': 'Tissue', 'quantity': 6, 'price': 20.00, 'is_expired': False},
    {'name': 'Durex', 'quantity': 2, 'price': 123.99, 'is_expired': False},
    {'name': 'Neck choke', 'quantity': 1, 'price': 239.99, 'is_expired': True}
]

with open('json_object.json', mode='w') as file:
    json.dump(products, file, indent=4)

# products = [
#      {'name':'Soap','quantity': 3, 'price':Decimal('23.50'),'is_expired': False},
#      {'name':'Tissue','quantity': 6, 'price':Decimal('20.00'),'is_expired': False},
#      {'name':'Durex','quantity': 2, 'price':Decimal('123.99'),'is_expired': False},
#      {'name':'Neck choke','quantity': 1, 'price':Decimal('239.99'),'is_expired': True},
#
# ]
# x=pickle.dumps(products)
# print(type(x))

# with open('picked_object.text',mode='wb') as file:
#        pickle.dump(products,file)

# with open('picked_object.text', mode='rb') as file:
#          x = pickle.load(file)
#          print(x)
#          pprint.pprint(x, indent=4)

print(0.1 + 0.2)
print(Decimal('0.1') + Decimal('0.2'))
