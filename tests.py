import unittest
from sort_weights import sort

class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        """Test a package that meets neither bulky nor heavy criteria."""
        self.assertEqual(sort(50, 40, 30, 10), "STANDARD")

    def test_special_bulky_package(self):
        """Test a package that is bulky but not heavy."""
        self.assertEqual(sort(200, 40, 30, 10), "SPECIAL")

    def test_special_heavy_package(self):
        """Test a package that is heavy but not bulky."""
        self.assertEqual(sort(50, 40, 30, 25), "SPECIAL")

    def test_rejected_package_bulky_and_heavy(self):
        """Test a package that is both bulky and heavy."""
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_bulky_volume_edge(self):
        """Test a package that is bulky due to its volume."""
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")  # Volume = 1,000,000 cm³
        self.assertEqual(sort(101, 100, 100, 10), "SPECIAL")  # Volume > 1,000,000 cm³

    def test_edge_case_bulky(self):
        """Test a package at the edge of bulky dimensions."""
        self.assertEqual(sort(150, 100, 100, 10), "SPECIAL")  # Width hits bulky threshold
        self.assertEqual(sort(100, 150, 100, 10), "SPECIAL")  # Height hits bulky threshold
        self.assertEqual(sort(100, 100, 150, 10), "SPECIAL")  # Length hits bulky threshold

    def test_edge_case_heavy(self):
        """Test a package at the edge of heavy mass."""
        self.assertEqual(sort(50, 40, 30, 20), "SPECIAL")  # Mass hits heavy threshold

    def test_invalid_input(self):
        """Test invalid inputs to the function."""
        with self.assertRaises(ValueError):
            sort("a", "b", "c", "d")  # Non-numeric strings

        with self.assertRaises(ValueError):
            sort(50, -40, 30, 10)  # Negative dimension

        with self.assertRaises(ValueError):
            sort(50, 40, 30, -10)  # Negative mass

        with self.assertRaises(ValueError):
            sort(50, 40, 30)  # Missing mass argument

        with self.assertRaises(ValueError):
            sort()  # Missing all arguments

    def test_zero_dimensions(self):
        """Test zero dimensions or mass."""
        with self.assertRaises(ValueError):
            sort(0, 40, 30, 10)  # Zero width

        with self.assertRaises(ValueError):
            sort(50, 0, 30, 10)  # Zero height

        with self.assertRaises(ValueError):
            sort(50, 40, 0, 10)  # Zero length

        with self.assertRaises(ValueError):
            sort(50, 40, 30, 0)  # Zero mass

if __name__ == "__main__":
    unittest.main()
