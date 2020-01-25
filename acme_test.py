import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


def test_product_weight(self):
        """Test new product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)


def test_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


def test_product_stealability(self):
        """Test product stealability"""
        prod = Product('Test Product', price=10, weight=20)
        self.assertEqual(prod.stealability(), "Kinda stealable.")


def test_product_explode(self):
        """Test product explodity"""
        prod = Product('Test Product', weight=20, flammability=500)
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    # Generate 30 products
    def test_default_num_products(self):
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

# Valid names?
    def test_legal_names(self):
        self.products = generate_products()
        for prod in self.products:
            name = prod.name.split()
            self.assertIn(name[0], adjectives)
            self.assertIn(name[1], nouns)

if __name__ == '__main__':
    unittest.main()
