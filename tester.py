import unittest
import conversions

class ConversionTester(unittest.TestCase):
	confirmed_CF_Conversions=((300,572),
				(0,32),
				(100,212),
				(50,122),
				(1000,1832))
	confirmed_CK_Conversions=((0,273.15),
				(100,373.15),
				(74,347.15),
				(5,278.15),
				(37,310.15))
	def test_CF_conversion(self):
		for val1,val2 in self.confirmed_CF_Conversions:
			cf_result=conversions.convertCelsiusToFahrenheit(val1)
			self.assertEqual(val2,cf_result)
	def test_CK_conversion(self):
                for val3,val4 in self.confirmed_CK_Conversions:
                        ck_result=conversions.convertCelsiusToKelvin(val3)
                        self.assertEqual(val4,ck_result)
if __name__ == '__main__':
	unittest.main()

