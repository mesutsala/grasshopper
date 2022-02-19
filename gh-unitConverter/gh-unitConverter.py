"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "Mesut Sala"
__version__ = "2021.08.29"

import rhinoscriptsyntax as rs

unitOutput = []

if sourceUnit == "m" and targetUnit == "mm":
    unitOutput.append(float(Input)*1000)
elif sourceUnit == "m" and targetUnit == "ft":
    unitOutput.append(float(Input)*3.281)
elif sourceUnit == "m" and targetUnit == "in":
    unitOutput.append(float(Input)*39.37)
elif sourceUnit == "m" and targetUnit == "m":
    unitOutput.append(float(Input))

elif sourceUnit == "mm" and targetUnit == "m":
    unitOutput.append(float(Input)/1000)
elif sourceUnit == "mm" and targetUnit == "ft":
    unitOutput.append(float(Input)/305)
elif sourceUnit == "mm" and targetUnit == "in":
    unitOutput.append(float(Input)/25.4)
elif sourceUnit == "mm" and targetUnit == "mm":
    unitOutput.append(float(Input))

elif sourceUnit == "ft" and targetUnit == "in":
    unitOutput.append(float(Input)*12)
elif sourceUnit == "ft" and targetUnit == "m":
    unitOutput.append(float(Input)/3.281)
elif sourceUnit == "ft" and targetUnit == "mm":
    unitOutput.append(float(Input)*304.8)
elif sourceUnit == "ft" and targetUnit == "ft":
    unitOutput.append(float(Input))

elif sourceUnit == "in" and targetUnit == "ft":
    unitOutput.append(float(Input)/12)
elif sourceUnit == "in" and targetUnit == "m":
    unitOutput.append(float(Input)/39.37)
elif sourceUnit == "in" and targetUnit == "mm":
    unitOutput.append(float(Input)*25.4)
elif sourceUnit == "in" and targetUnit == "in":
    unitOutput.append(float(Input))
    
else:
    print("sourceUnit and targetUnit are: m, mm, ft, in")