import unittest
from random import randint
from main import bubble_sorting


class TestBubbleSortBinary(unittest.TestCase):

    def test_sorted_array(self):
        arr = ['0b100', '0b101', '0b110']
        result = bubble_sorting(arr)
        self.assertEqual(result, ['0b100', '0b101', '0b110'])

    def test_reverse_sorted_array(self):
        arr = ['0b110', '0b101', '0b100']
        result = bubble_sorting(arr)
        self.assertEqual(result, ['0b100', '0b101', '0b110'])

    def test_equal_elements(self):
        arr = ['0b101', '0b101', '0b101']
        result = bubble_sorting(arr)
        self.assertEqual(result, ['0b101', '0b101', '0b101'])

    def test_single_element(self):
        arr = ['0b100']
        result = bubble_sorting(arr)
        self.assertEqual(result, ['0b100'])

    def test_random_numbers(self):
        arr: list[str] = [bin(randint(0,1000)) for i in range(20)]
        result = bubble_sorting(arr)
        self.assertEqual(result, sorted(arr, key=lambda x: int(x, 2)))


if __name__ == '__main__':
    unittest.main()
