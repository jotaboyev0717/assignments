
name = input("Pet's name: ")
age = input("age: ")
type = input("pet's type: ")
toy = input("favourite toy: ")
place = input("shelter name: ")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("          -- ADOPT ME! --")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Hi, my name is " + name + "!\n")
print("I am a " + age + " " + type + ".")
print("My favorite toy is a " + toy + ".\n")
print("Come meet me today at the " + place + "!\n")
print("----------------------------------------")
print("Adoption ID: " + name.upper() + "-" + type.upper() + "-" + place.upper())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
