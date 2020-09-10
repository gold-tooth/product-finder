class MsgParser:
    def __init__(self, user_message):
        self.message_parts = user_message.split(",")
        self.find_params = []

    def extracted_params(self):
        for part in self.message_parts:
            column, compare, value = part.strip().split(" ")
            self.find_params.append({
                "column": column.strip(),
                "compare": compare.strip(),
                "value": float(value.strip())
            })
        return self.find_params    


#ms = MsgParser("proteins > 10 , water < 10 , Fats >= 21")
#print(ms.extracted_params())
