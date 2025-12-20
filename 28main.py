letter = "Hey my name is{} and i am from  {}"
name = "Harry"
country = "India"
print(letter.format(name, country))
price = 49.09999
print( f"Hey my name is {{name}} and i am from {{country}}")
txt = f"for only {price:.2f} dollars!"
print(txt)
print(type(f"{1+3}"))