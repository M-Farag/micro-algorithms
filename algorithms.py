# Return a new amount after applying a discount on the original amount
def discount_and_return_new_value(amount: int,discount: int):
    return amount * ( 1 - (discount/100))