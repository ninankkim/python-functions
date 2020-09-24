def f_to_c (fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

fahrenheit = int(input('Give me a degree in Fahrenheit: '))  

f_conversion = f_to_c(fahrenheit)
print(f'The converision from {fahrenheit} degree fahrenheit to Celsius is {f_conversion}.')
