# Return a new amount after applying a discount on the original amount
# Check the wiki for more information about this algorithm
def discount_and_return_new_value(amount: float,discount: float):
    return amount * ( 1 - (discount/100))