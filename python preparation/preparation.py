#python function parctise problems

def lesser(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    elif (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0):
        print(max(a,b))
 
