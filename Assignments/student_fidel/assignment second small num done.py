#write a program to find the second smallest number in a list

ben = [12, 45, 2, 41, 31, 10, 8, 6, 4]

def find(list1):
    length = len(list1)
    list1.sort()
    return ("largest element is:", list1[length-1])
    return ("smallest element is:", list1[0])
    return ("second largest element is:", list1[length-2])
    return ("second smallest element is:", list1[1])
    
find(ben)

