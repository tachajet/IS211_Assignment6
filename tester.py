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
	confirmed_FC_Conversions=((572,300),
				(32,0),
				(212,100),
				(122,50),
				(1832,1000))
	confirmed_FK_Conversions=((0,255.372),
				(100,310.928),
				(212,373.15),
				(90,305.372),
				(350,449.817))
	confirmed_KF_Conversions=((100,-279.67),
				(200,-99.67))
	confirmed_KC_Conversions=((200,-73.15),
				(400,126.85),
				(347.15,74))
	def test_CF_conversion(self):
		for val1,val2 in self.confirmed_CF_Conversions:
			cf_result=conversions.convertCelsiusToFahrenheit(val1)
			self.assertEqual(val2,cf_result)
	def test_CK_conversion(self):
                for val3,val4 in self.confirmed_CK_Conversions:
                        ck_result=conversions.convertCelsiusToKelvin(val3)
                        self.assertEqual(val4,ck_result)
	def test_FC_conversions(self):
                for val5,val6 in self.confirmed_FC_Conversions:
                        fc_result=conversions.convertFahrenheitToCelsius(val5)
                        self.assertEqual(val6,round(fc_result))
	def test_FK_conversions(self):
                for val7,val8 in self.confirmed_FK_Conversions:
                        fk_result=conversions.convertFahrenheitToKelvin(val7)
                        self.assertEqual(val8,round(fk_result))
	def test_KF_conversions(self):
                for val9,val10 in self.confirmed_KF_Conversions:
                        kf_result=conversions.convertKelvinToFahrenheit(val9)
                        self.assertEqual(val10,round(kf_result))
	def test_KC_conversions(self):
                for val11,val12 in self.confirmed_KC_Conversions:
                        kc_result=conversions.convertKelvinToCelsius(val11)
                        self.assertEqual(val12,kc_result)
if __name__ == '__main__':
	unittest.main()

