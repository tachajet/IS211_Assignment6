import unittest
import conversions
import conversions_refactored
#as I noted in my discussion board post, I needed to round() values, but the testing still works
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
				(200,-99.67),
				(255,-.67),
				(312,101.93),
				(765, 917.33))
	confirmed_KC_Conversions=((200,-73.15),
				(400,126.85),
				(347.15,74),
				(765, 491.85),
				(42,-231.15))
	def test_CF_conversion(self):
		for val1,val2 in self.confirmed_CF_Conversions:
			cf_result=conversions.convertCelsiusToFahrenheit(val1)
			self.assertEqual(round(val2),round(cf_result))
	def test_CK_conversion(self):
                for val3,val4 in self.confirmed_CK_Conversions:
                        ck_result=conversions.convertCelsiusToKelvin(val3)
                        self.assertEqual(round(val4),round(ck_result))
	def test_FC_conversions(self):
                for val5,val6 in self.confirmed_FC_Conversions:
                        fc_result=conversions.convertFahrenheitToCelsius(val5)
                        self.assertEqual(round(val6),round(fc_result))
	def test_FK_conversions(self):
                for val7,val8 in self.confirmed_FK_Conversions:
                        fk_result=conversions.convertFahrenheitToKelvin(val7)
                        self.assertEqual(round(val8),round(fk_result))
	def test_KF_conversions(self):
                for val9,val10 in self.confirmed_KF_Conversions:
                        kf_result=conversions.convertKelvinToFahrenheit(val9)
                        self.assertEqual(round(val10),round(kf_result))
	def test_KC_conversions(self):
                for val11,val12 in self.confirmed_KC_Conversions:
                        kc_result=conversions.convertKelvinToCelsius(val11)
                        self.assertEqual(round(val12),round(kc_result))
class RefactorTest(unittest.TestCase):
	cases=(("celsius","Kelvin",74,347.15),
		("fahrenheit","kelVIN",90,305.372),
		("Kelvin","Kelvin",175,175),
		("Kelvin","celsius",347.15,74),
		("Kelvin","Fahrenheit",305.372,90),
		("Celsius","Fahrenheit",1000,1832),
		("Celsius","Celsius",5,5),
		("Fahrenheit","Celsius",212,100),
		("Fahrenheit","Fahrenheit",5,5),
		("mile","yard",1,1760),
		("yard","mile",1760,1),
		("meter","yard",5,5.46807),
		("yard","meter",5.46807,5),
		("mile","meter",1,1609.34),
		("Kelvin","Mile",6,30)		
	)
	def test_RC(self):
		for fromU,toU,value,convert in self.cases:
			RC_result=conversions_refactored.convert(fromU,toU,value)
			self.assertEqual(round(convert), round(RC_result))
	#Refactor test fails because it catches the exception hidden in the cases tuple
		

if __name__ == '__main__':
	unittest.main()

