from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_cities_1(self):
        actual = fit_transform(
            ['Moscow', 'New York', 'Moscow', 'London', 'Paris']
            )
        expected = [('Moscow', [0, 0, 0, 1]),
                    ('New York', [0, 0, 1, 0]),
                    ('Moscow', [0, 0, 0, 1]),
                    ('London', [0, 1, 0, 0]),
                    ('Paris', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_cities_2(self):
        actual = fit_transform(
            ['Moscow', 'New York', 'Moscow']
            )
        expected = [('Moscow', [0, 1]),
                    ('New York', [1, 0]),
                    ('Moscow', [0, 1])]
        self.assertEqual(actual, expected)

    def test_animals_1(self):
        actual = fit_transform(
            ['cat', 'dog', 'mouse', 'turtle', 'dog', 'mouse']
            )
        self.assertIn(('turtle', [1, 0, 0, 0]), actual)

    def test_animals_2(self):
        actual = fit_transform(
            ['cat', 'dog', 'mouse', 'turtle', 'dog', 'mouse']
            )
        with self.assertRaises(AttributeError):
            actual.fit_transform(1337)

    if __name__ == '__main__':
        unittest.main()
        """python -m unittest -v"""
