# Check the wiki for more information and the use cases of any algorithm

# Calculate and return a new amount after applying a discount on the original amount
def discount_and_return_new_value(amount: float,discount: float):
    return amount * ( 1 - (discount/100))

# Calculate and return the remaining units for a goal
def remaining_units_towards_a_goal(aimed_amount: float,accomplished_amount: float,progress_rate_per_unit: float):
    return (aimed_amount - accomplished_amount) / progress_rate_per_unit