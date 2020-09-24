def c_to_f (celsius):
  fah = (celsius * 9/5) + 32
  return fah

celsius = int(input('Give me a degree in celsius: '))  

f_conversion = c_to_f(celsius)
print(f'The conversion from {celsius} degree celsius to Fahrenheit is {f_conversion}.')