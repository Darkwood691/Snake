#sorting algorithms


def mergeSort(scores):
    if len(scores)>1:
        mid = len(scores)//2
        leftHalf = scores[:mid]
        rightHalf = scores[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        i=0
        j=0
        k=0
        
        while i<len(leftHalf) and j<len(rightHalf):
            if int(leftHalf[i][1]) > int(rightHalf[j][1]):
                scores[k]=leftHalf[i]
                i+=1
            else:
                scores[k]=rightHalf[j]
                j+=1
            k+=1
        while i < len(leftHalf):
            scores[k]=leftHalf[i]
            i+=1
            k+=1
        while j < len(rightHalf):
            scores[k]=rightHalf[j]
            j+=1
            k+=1

    return scores


def bubbleSort(array): 
    x=1
    while x != 0:
        x=0
        for n in range(len(array)-1):
            if int(array[n][1])<int(array[n+1][1]):
                a=array[n]
                array[n]=array[n+1]
                array[n+1]=a
                x=x+1                
    return array                    

def sortPrep(scores,algorithm):
    scores=scores.split("\n")
    scores=list(scores)
    scores.pop()
    array=[]
    for item in scores:
        item=item.split(" ")
        array.append([item[0],item[1]])
        
    if algorithm == "merge":
        array=(mergeSort(array))
    elif algorithm == "bubble":
        array=(bubbleSort(array))

    return array

    
"""
scoreboard = open("xscoreboard.txt", "r")
oldScores=scoreboard.read()

print(sortPrep(oldScores,"merge"))
print("\n")
print(sortPrep(oldScores,"bubble"))
"""
