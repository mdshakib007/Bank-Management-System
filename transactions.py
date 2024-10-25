from datetime import datetime

class Transaction:
    def __init__(self, name, trax_type, traxid, amount):
        self.name = name
        self.trax_type = trax_type
        self.traxid = traxid
        self.amount = amount
        self.time = datetime.now()
