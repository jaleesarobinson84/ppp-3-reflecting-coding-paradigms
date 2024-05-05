#functional Prompts
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm

def main():
    print("This program will sort and flatten an array of integers in ascending order")
    print("Please enter a list of integers, seperated by a space")
    user_input = input("Enter a list of integers: ")
    user_input = user_input.split(" ")
    user_input = list(map(int, user_input))
    print(user_input)
    print(sort_and_flatten(user_input))

def sort_and_flatten(array):
    array = [array]
    for item in array:
        for i in range(len(item)):
            array.append(item[i])
            return sorted(array)
        
 # this code does not ensure data immutability, it modifies the original array passing by reference
# this solution is a not a pure function, it modifies the original array passed by reference. This is a side effect and and violates the principle of modifying the original array
#  the function "sort_and_flatten" is not a higher order function because it does not return a value, it modifies the original array passed by
# Yes, using a different programing style would be more appropriate to solve this problem
# Functional programming is helpful with solveing problems like flattening and sorting nested lists because of the emphasis on immutability on immutablity, ans higher order functions.


    # OOP - Object Oriented Prompts
    # Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria

    class Podracer:
        def __init__(self, max_speed, condition, price):
            self.max_speed = max_speed
            self.condition = condition
            self.price = price
            
    def repair(self):
        self.condition = "repaired"

    def AnakinsPod(Proracer):
        def boost(self):
            self.max_speed = self.max_speed + 10

    class SebulasPod(Proracer):
        def flame_jet(self, other_podracer):
            other_podracer.condition = "damaged"
            other_podracer.price = other_podracer.price + 1000
            other_podracer.max_speed = other_podracer.max_speed - 10
    
    # Example Usage
    # Creating instance of podracer
    podracer1 = Podracer(max_speed=100, condition="damaged", price=1000)
    podracer2 = Podracer(max_speed=400, condition="repaired", price=800)

    #calling repair method
    prodracer1.repair()

    # creating instance of AnakinsPod and SebulasPod
    anakins_pod = AnakinsPod(max_speed=100, condition="perfect", price=1000)
    sebulas_pod = SebulasPod(max_speed=400, condition="repaired", price=800)
   
   #calling boost method & flame_jet method
    anakins_pod.boost()
    sebulas_pod.flame_jet(sebulas_pod)

    #printing attributes to see changes
    print("anakins_pod.max_speed:", anakins_pod.max_speed)
    print("sebulas_pod.condition:", sebulas_pod.condition)
    print("sebulas_pod.price:", sebulas_pod.price)

# this code demonstrates Encapsulation "Podracers" class encapsulates the attributes and methods of the Podracers class
# this code demonstrates Inheritance "AnakinsPod" and "SebulasPod" classes
# this code demonstrates Polymorphism "AnakinsPod" and "SebulasPod"
# this code demonstrates Abstraction "AnakinsPod" and "SebulasPod"
# OOP - Object Oriented Prompts assisted by the "AnakinsPod" and "SebulasPod"