from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    x = random.choice(adjectives)
    y = random.choice(nouns)
    name = f'{x} {y}'
    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    flammability = random.uniform(0, 2.5)
    products[i] = product(name, price, weight, flammability)
    return products


def inventory_report(products):
    prices = []
    weights = []
    flamm = []
    for p in products:
        prices.append(p.price)
        weights.append(p.weight)
        flamm.append(p.flammability)
    avg_p = sum(prices) / len(prices)
    avg_w = sum(weights) / len(weights)
    avg_f = sum(flamm) / len(flamm)

    print(avg_p, avg_w, avg_f)
if __name__ == '__main__':
    inventory_report(generate_products())
