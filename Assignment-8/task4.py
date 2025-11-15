import unittest

class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Price must be a numeric value.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._items.append((name.strip(), float(price)))

    def remove_item(self, name):
        for index, (item_name, _) in enumerate(self._items):
            if item_name == name:
                del self._items[index]
                return
        raise ValueError(f"Item '{name}' not found in the cart.")

    def total_cost(self):
        return sum(price for _, price in self._items)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("Apple", 1.5)
        self.assertEqual(self.cart.total_cost(), 1.5)

    def test_add_multiple_items(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Milk", 2.25)
        self.assertEqual(self.cart.total_cost(), 4.5)

    def test_remove_existing_item(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Banana", 0.75)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 0.75)

    def test_remove_nonexistent_item_raises(self):
        self.cart.add_item("Apple", 1.5)
        with self.assertRaises(ValueError):
            self.cart.remove_item("Banana")

    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_add_invalid_name(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("", 1.0)

    def test_add_invalid_price_type(self):
        with self.assertRaises(TypeError):
            self.cart.add_item("Apple", "1.0")

    def test_add_negative_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Apple", -1.0)

    def test_remove_one_of_duplicates(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Apple", 2.0)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 2.0)
if __name__ == "__main__":
    unittest.main()

