from datetime import datetime

class Pdf():
    def __init__(self, name, phone, email, bank, account_num, business) -> None:
        self.name = name
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.phone = phone
        self.email = email
        self.bank = bank
        self.account_num = account_num
        self.business = business


class Invoice(Pdf):
    def __init__(self, name, invoice_number, total, phone, email, bank, account_num, buisness) -> None:
        super().__init__(name, phone, email, bank, account_num, buisness)
        self.invoice_number = invoice_number
        self.items = []
        self.sub_totals = {}
        self.total = total

    def items(self):
        return self.items

    def add_line_item(self, item, hours, rate) -> None:
        self.items.append({"item":item, "hours": hours, "rate": rate})

    def remove_line_item(self, item, hours) -> None:
        self.items = list(filter(lambda x: x["item"] != item and x["hours"] != hours, self.items))

    def get_subtotal(self, item) -> float:
        return self.sub_totals[item]

    def get_total(self) -> float:
        return self.total

    def subtotals(self, line_item):
        items = filter(lambda x: x["item"] == line_item, self.items)
        self.sub_totals.update({line_item: sum([item["hours"] * item["rate"] for item in items])})

    def total(self):
        self.total += sum(self.sub_totals.values())

    def compute(self):
        for x in self.items if x not in self.sub_totals.keys():
            self.subtotals(x["item"])
        self.total()

    def __str__(self) -> str:
        return f"Name: {self.name}, Date: {self.date}, Invoice Number: {self.invoice_number}, Total: {self.total}"
