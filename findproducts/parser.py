from class_parser import Parser
from data_manager import DataManager
from class_findproducts import ProductsFinder

parser = Parser()
parser.perform()
data = parser.data()
#print(data)

dm = DataManager()
dm.save(data)
#print(dm.load())

filtered_products = ProductsFinder(dm.load()).find_all([
    {"column": "proteins", "compare": "<", "value": 0.3},
    {"column": "water", "compare": ">=", "value": 87 }
])
print(filtered_products)

