class FindRule:
    @staticmethod
    def create(product_list, cond):
        if cond.get("column") == "name":
            return TextFindRule(product_list, cond)
        else:
            return NumFindRule(product_list, cond)    

    def __init__(self, product_list, cond):
        self.products = product_list
        self.column = cond.get('column') # name, proteints, water, fats, 
        self.compare = cond.get('compare')
        self.value = cond.get('value')

        

    def filter(self):
        raise NotImplementedError()

class TextFindRule(FindRule):

    def filter(self):
        selected_products = []
        for prod in self.products:
            if self.comparer().check(prod.get(self.column), self.value):
                selected_products.append(prod)
        return selected_products
    def comparer(self):
        return {
            "=": CompareEqualText
        }.get(self.compare)    
    

class NumFindRule(FindRule):

    def filter(self):
        selected_products = []
        for prod in self.products:
            if self.comparer().check(prod.get(self.column), self.value):
                selected_products.append(prod)
            
        return selected_products
    def comparer(self):
        return {
            "=": CompareEqualNum,
            "<": CompareLessNum,
            ">": CompareLargerNum,
            "<=": CompareLessOrEqualNum,
            ">=": CompareLargerOrEqualNum
        }.get(self.compare)

class CompareEqualText():
    @staticmethod
    def check(a, b):
        return a.lower() == b.lower()

class CompareEqualNum():
    @staticmethod
    def check(a, b):
        return float(a) == float(b)

class CompareLargerNum():
    @staticmethod
    def check(a, b):
        return float(a) > float(b)

class CompareLessNum():
    @staticmethod
    def check(a, b):
        return float(a) < float(b)

class CompareLargerOrEqualNum():
    @staticmethod
    def check(a, b):
        return  CompareLargerNum.check(a, b) or CompareEqualNum.check(a, b)

class CompareLessOrEqualNum():
    @staticmethod
    def check(a, b):
        return  CompareLessNum.check(a, b) or CompareEqualNum.check(a, b)




