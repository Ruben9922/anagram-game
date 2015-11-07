def InputInt(message):
    inputvalid = False
    while inputvalid == False:
        try:
            number = int(input(message))
            inputvalid = True
            return number
        except ValueError as e:
            print("Integers only! ({0})".format(e))
            
def InputFloat(message):
    inputvalid = False
    while inputvalid == False:
        try:
            number = float(input(message))
            inputvalid = True
            return number
        except ValueError as e:
            print("Numbers only! Decimals are allowed. ({0})".format(e))
            
def InputOptionChar(validoptions,message = "Enter option: "):
    option = ""
    inputvalid = False
    while inputvalid == False:
        option = input(message).lower()
        for validoption in validoptions:
            if option == validoption:
                inputvalid = True
                break
        if inputvalid == False:
            print("Invalid option!")
    return option
    
def InputOptionInt(titlelist,optioncount):
    for i in range(0,len(titlelist)):
        print("  {0}: {1}".format(i,titlelist[i]))
    while True:
        option = InputInt("Enter option: ")
        if option >= 0 and option < optioncount:
            break
        else:
            print("Invalid option!")
    return option
    
def SearchArray(item,array):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1
