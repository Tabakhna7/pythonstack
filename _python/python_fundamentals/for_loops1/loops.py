def Biggie_Size(number):
    newList=[]
    for i in range(0,len(number),1):
        if number[i]>0:
            number[i]="big"
        newList.append(number[i])
    return newList    

print(Biggie_Size([-5,-2,3,4,5,6]))


def Count_Positives(elements):
    count=0

    for g in range(0,len(elements),1):
        if elements[g]>0:
            
            count+=1

        elements[len(elements)-1]=count

    return elements

print(Count_Positives([-1,1,2,2]))

def Sum_Total(para):

    sum =0 

    for o in range (0,len(para),1):
        sum+=para[o]

    return sum
    
print(Sum_Total([1,2,3,4]))


def Average(param):
    length=len(param)
    sum=0
   
    for u in range(0,len(param),1):

        sum+=param[u]

    result=sum/length

    return result

print(Average([1,3,3]))


def length(list):
    return len(list)
    
print(length([1,2]))




def Minimum(para):


    if len(para)==0:
       return False

    else:
    
      return min(para)
    
print(Minimum([1,2,4,5]))

def Maximum(para):


    if len(para)==0:
       return False

    else:
    
      return max(para)
    
print(Maximum([1,2,4,5]))

def ultimate_analysis(numbers):
  
    if len(numbers)==0:
        return False

    
   
    sumTotal = sum(numbers)
    length = len(numbers)
    average = sumTotal / length
    minimum = min(numbers)
    maximum = max(numbers)
    
   
    analysis = {
        'sumTotal': sumTotal,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': length
    }
    
    return analysis


print(ultimate_analysis([37, 2, 1, -9]))


def Reverse_List(num):
    for i in range (len(num)-1,-1,-1):

        print(num[i])


Reverse_List([1,2,3,4,5])