from .find_rules import FindRule

class ProductsFinder:
    def __init__(self, product_list):
        self.products = product_list 

    def find_all(self, conds):
        products = self.products
        for cond in conds:
            rule = FindRule.create(products, cond)
            products = rule.filter()
            if len(products) == 0:
                break
        return products


    