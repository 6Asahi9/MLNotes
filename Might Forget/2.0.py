person = {"name": "Asahi", "age":21}
def identity(age, **kwargs):
    if str(age) == "Asahi":
        return True
    return False
        
print(identity(**person))

# ** is using to open up the dict like 
{"name": "Asahi", "age":21}
# becomes 
name = "Asahi", "age" = 21
# and if you have exrta arguments **kwargs helps by absorbing them
