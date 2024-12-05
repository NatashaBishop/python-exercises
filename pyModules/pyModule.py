# inspired by https://www.analyticsvidhya.com/blog/2021/07/working-with-modules-in-python-must-known-fundamentals-for-data-scientists
#VARIABLE we are accling data from in another function by importing this file as module
person1 = {
  "name": "Chirag Goyal",
  "age": 19,
  "country": "India"
  "education”: “IIT Jodhpur"  
}

#function we are accling data from in another function by importing this file as module
def welcome(name):
  print("Hello, " + name +" to Python")
