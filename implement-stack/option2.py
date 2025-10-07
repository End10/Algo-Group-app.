# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class IntStack:


    # the plan for this plate is to have a long integer.
    # i'll have the integer plate be a float, since it will have a larger stack capacity
    # this stack can only hold integers from 0-9, which is a large limitation

    plate = 1.12
    digitHolder = 0

    def init(self):# initialize step for class
        pass

    def push(self, plate, newTop):#add a plate to the stack by pushing the line down through decimal point
        #global plate
        plate /= 10
        plate += float(newTop)

        return plate

    def pop(self, plate):#figure out how large the ones place is and remove it and move down the decimal point
        #global plate
        plateOnesPlace = int(plate)

        plate-=plateOnesPlace
        plate*=10

        return plate
    
    def peek(self, plate):#turn plate to int to ignore other "plates"
        if plate is None:
            print("Plate is empty")
        print(int(plate))

    def size(self, plate): 

        length = len(str(plate))#calculations to get correct size without decimal point included
        plate *= 10**(length-2)
        length = len(str(int(plate)))

        print(str(length)+" digit(s)")

    def showPlate(self, plate):
        print(plate)

s1 = IntStack()

s1.showPlate(s1.plate)

s1.plate = s1.push(s1.plate, 5)#seems to not change the variable... need to bring result out to bigger scope???
s1.plate = s1.push(s1.plate, 3)

s1.showPlate(s1.plate)
s1.size(s1.plate)
s1.peek(s1.plate)

s1.plate = s1.pop(s1.plate)#very irritating that pop doesnt seem to change the variable

s1.showPlate(s1.plate)#woah there seems to be some sort of bit error when calculating. final showPlate function returns 5.112000000000001 (weird)
