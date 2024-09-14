#Create a script that run a condition in an if statement, Python returns True or False.
def check_condition(value):
    if value > 20:
        return True
    else:
        return False
input_value = 30
result = check_condition(input_value)
print('Result:',result,'\n')  

#Create a script that has List, Tuples, Sets and Dictionaries
list = [1, 2, 3]
print("List:", list)

tuple = (10, 20, 30)
print("Tuple:", tuple)

set = {1, 2, 3}
print("Set:", set)

dict = {"name": "Jhon", "age": 21}
print("Dictionary:", dict,'\n')

#Also used the String, int and boolean data types on each collection data.
list = [1, "Code", True]
print("List:", list)


tuple = (2, "Programmer", False)
print("Tuple:", tuple)


set = {3, "Computer", True}
print("Set:", set)

dict = {
    "Name": "Jhon",
    "Age": 21,
    "Student": True
}
print("Dictionary:",dict)
