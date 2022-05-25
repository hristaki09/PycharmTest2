from gender_converter import convert_gender
from unittest import TestCase

class Test(TestCase):
    def test_convert_gender_m(self):
        actual = convert_gender("M")
        expected = "MALE"
        self.assertEqual(actual, expected)

    def test_convert_gender_f(self):
        actual = convert_gender("F")
        expected = "FEMALE"
        self.assertEqual(actual, expected)

    def test_convert_gender_u(self):
        actual = convert_gender("HELLO")
        expected = "UNKNOWN_GENDER"
        self.assertEqual(actual, expected)

#
# class Test:
#     def test_convert_gender_m(self):
#         actual = convert_gender("M")
#         expected = "MALE"
#         if actual == expected:
#             assert True
#         else:
#             assert False
#
#     def test_convert_gender_f(self):
#         actual = convert_gender("F")
#         expected = "FEMALE"
#         if actual == expected:
#             assert True
#         else:
#             assert False
#
#     def test_convert_gender_u(self):
#         actual = convert_gender("")
#         expected = "UNKNOWN_GENDER"
#         if actual == expected:
#             assert True
#         else:
#             assert False