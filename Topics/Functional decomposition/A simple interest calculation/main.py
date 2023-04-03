def calculate(amount, interest_rate, time):
    return (amount * interest_rate * time) / 100, amount + (amount * interest_rate * time) / 100


def print_result(interest, total_amount):
    print('The interest is:', interest)
    print('The total amount is:', total_amount)
