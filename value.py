def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

#     ✍️exercise
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?


print(double("22"))

#    I predicted that it would return "44" but it actually returned "2222". This is because the * operator, when used with strings, concatenates the string to itself the specified number of times. So "22" * 2 results in "22" + "22", which gives "2222".
