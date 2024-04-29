import random
def randInt(min= None  , max=  None ):
    num = random.random()
    if min==None and max ==None:
        num=num*100
    elif min==None and max !=None:
        num=num*max
    elif min !=None and max ==None:
        num=num*(100-min)+min

    elif min !=None and max!=None:
        num=num*(max-min)+min
    return round (num)

#print(randInt(1,None)) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
