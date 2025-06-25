# Project: Receipt Generator

# Calculates the price of one product (with tax) Formats a receipt Prints total + label

def printed_receipt(product_name, price, tax_rate):
    def calculate_total(price, tax_rate):
        total = round(price * (tax_rate + 1),2)
        return total
    total = calculate_total(price, tax_rate)
    print(f" Product Name: {product_name}\n Price before Tax: {price}\n Tax Rate: {tax_rate * 100} %\n Total: {total}")

printed_receipt("Book", 100, 0.19)