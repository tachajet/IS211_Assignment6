def convert(fromUnit,toUnit,value):
	convertedVal=0
	if (fromUnit.upper()=="METER"):
		if (toUnit.upper()=="MILE"):
			convertedVal=(value/1609)
		elif (toUnit.upper()=="YARD"):
			convertedVal=(value*1.094)
		elif (toUnit.upper()=="METER"):
			convertedVal=value
		elif (toUnit.upper()=="KELVIN") or (toUnit.upper()=="CELSIUS") or (toUnit.upper()=="FAHRENHEIT"):
			raise ConversionNotPossible
	elif (fromUnit.upper()=="YARD"):
		if (toUnit.upper()=="MILE"):
			convertedVal=(value/1760)
		elif (toUnit.upper()=="YARD"):
			convertedVal=value
		elif (toUnit.upper()=="METER"):
			convertedVal=(value/1.094)
		elif (toUnit.upper()=="KELVIN") or (toUnit.upper()=="CELSIUS") or (toUnit.upper()=="FAHRENHEIT"):
			raise ConversionNotPossible
	elif (fromUnit.upper()=="MILE"):		
		if (toUnit.upper()=="MILE"):
			convertedVal=value
		elif (toUnit.upper()=="METER"):
			convertedVal=(value*1609)
		elif (toUnit.upper()=="YARD"):
			convertedVal=(value*1760)
		elif (toUnit.upper()=="KELVIN") or (toUnit.upper()=="CELSIUS") or (toUnit.upper()=="FAHRENHEIT"):
			raise ConversionNotPossible
			convertedVal="Conversion not possible"
	elif (fromUnit.upper()=="KELVIN"):
		if (toUnit.upper()=="CELSIUS"):
			convertedVal=(value-273.15)
		elif (toUnit.upper()=="FAHRENHEIT"):
			convertedVal=((value*(9/5))-459.67)
		elif (toUnit.upper()=="KELVIN"):
			convertedVal=value
		elif (toUnit.upper()=="METER") or (toUnit.upper()=="MILE") or (toUnit.upper()=="YARD"):
			raise ConversionNotPossible
	elif (fromUnit.upper()=="CELSIUS"):
		if (toUnit.upper()=="KELVIN"):
			convertedVal=(value+273.15)
		elif (toUnit.upper()=="FAHRENHEIT"):
			convertedVal=((value*(9/5))+32)
		elif (toUnit.upper()=="CELSIUS"):
			convertedVal=value
		elif (toUnit.upper()=="METER") or (toUnit.upper()=="MILE") or (toUnit.upper()=="YARD"):
			raise ConversionNotPossible
	elif (fromUnit.upper()=="FAHRENHEIT"):
		if (toUnit.upper()=="FAHRENHEIT"):
			convertedVal=value
		elif (toUnit.upper()=="KELVIN"):
			convertedVal=((value+459.67)*(5/9))
		elif (toUnit.upper()=="CELSIUS"):
			convertedVal=((value-32)*(5/9))
		elif (toUnit.upper()=="METER") or (toUnit.upper()=="MILE") or (toUnit.upper()=="YARD"):
			raise ConversionNotPossible
	
		
	else:
		convertedVal="Not a valid input"
		print(ConversionNotPossible.message())
	return convertedVal
class ConversionNotPossible(Exception):
	def __init__(self,message="Conversion is not possible"):
		self.message=message
		super().__init__(self.message)

