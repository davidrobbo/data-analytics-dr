from DummyTransform import DummyTransform
import unittest

dummy = DummyTransform()
dummy_false = DummyTransform(add_boolean_field=False)


class DummyTransformTest(unittest.TestCase):
    def test(self):
        self.assertEqual(dummy.add_boolean_field, True)
        self.assertEqual(dummy_false.add_boolean_field, False)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
