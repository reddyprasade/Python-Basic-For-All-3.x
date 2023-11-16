import json

# some JSON:
x = '{ "name":"reddy", "age":29, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



data = { "name":"reddy", "age":29, "city":"New York"}


# Converting Dict into Json object
Json_Convert_Data = json.dumps(data)
print(Json_Convert_Data)


### List,tuple,set,dict,int,float,complex,bool,string

"""
When you convert from Python to JSON,
Python objects are converted into the JSON (JavaScript) equivalent:


Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""


x = {
  "name": "Reddy",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


print(json.dumps(x, indent=4, sort_keys=True))
