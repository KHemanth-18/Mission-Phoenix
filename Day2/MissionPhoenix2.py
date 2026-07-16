#Type casting
#explicit type casting

city = "chennai"
pincode = 600116
temperature_in_celsius = 37.16
living_in_flat = True

print(type(city))
print(type(pincode))
print(type(temperature_in_celsius))
print(type(living_in_flat))

pincode = float(pincode)
print(type(pincode))

temperature_in_celsius = int(temperature_in_celsius)
print(temperature_in_celsius)
print(type(temperature_in_celsius))

living_in_flat = str(living_in_flat)
print(living_in_flat)
print(type(living_in_flat))

pincode = bool(pincode)
print(pincode)
print(type(pincode))

#Implicit type casting

a = 9
b = 3.5

a = a + b
print(a)
b = b / a
print(b)