"""Learning about lambda function"""

price = [200, 500, 400, 100]
product = ['shirt', 'tennis', 'jacket', 'cap']

list_final = list(map(lambda x, y: f"{x}: {y}", product, price))  # Add two lists using maps and lambda

print(list_final)
