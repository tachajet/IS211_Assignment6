def convertCelsiusToKelvin(cels):
	kelv=(cels+273.15)
	return kelv
def convertCelsiusToFahrenheit(cels):
	fahr=((cels*(9/5))+32)
	return fahr
def convertFahrenheitToCelsius(fahr):
	cels=((fahr-32)*(5/9))
	return cels
def convertFahrenheitToKelvin(fahr):
	kelv=((fahr+459.67)*(5/9))
	return kelv
def convertKelvinToCelsius(kelv):
	cels=(kelv-273.15)
	return cels
def convertKelvinToFahrenheit(kelv):
	fahr=((kelv*(9/5))-459.67)
	return fahr
print(convertCelsiusToFahrenheit(100))
print(convertCelsiusToKelvin(0))
print(convertFahrenheitToCelsius(212))
