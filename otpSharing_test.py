from otpSharing import isEmail
from otpSharing import generateOTP
from otpSharing import verifyOTP
import unittest

class TestOtpSharing(unittest.TestCase):
    def test_isEmail1(self):
        testcase1 = "sample.123@email.xyz"
        expected1 = True
        testcase2 = "sample-email@email.xyz"
        expected2 = False
        self.assertEqual(isEmail(testcase1),expected1)
        self.assertEqual(isEmail(testcase2),expected2)

    def test_generateotp(self):
        expected = 6
        testcase = len(generateOTP())
        self.assertEqual(testcase,expected)


    def test_verifyOTP(self):
        expected = 123465
        testcase = 123465
        self.assertTrue(verifyOTP(testcase,expected))


if __name__=="__main__":
    unittest.main()