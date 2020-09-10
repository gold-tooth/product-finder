class ProductMesage():
    def __init__(self, product):
        self.product = product

    def transform_to_str(self):
        nice_str = ("{name}  колличество белков {proteins}" 
            ", колличество жиров {fats}"
            ", колличество калорий {kcal}"
            ", колличество углеводов {carbohydrates}"
            ", колличество воды {water}"
        ).format(
            name = self.product.get('name'),
            proteins = self.product.get('proteins'),
            fats = self.product.get('fats'),
            kcal = self.product.get('kcal'),
            carbohydrates = self.product.get('carbohydrates'),
            water = self.product.get('water')
        )
        return nice_str
#pm = ProductMesage({'proteins': ' 12.7', 'kcal': ' 510', 'carbohydrates': ' 50.6', 'fats': ' 29.9', 'water': ' 3.9', 'name': 'Халва тахинная'})
#print(pm.transform_to_str())
