"""n=input()
singer=list(map(n))"""

#discussion on classes in the data structure
"""class Cookie:
    def __init__(self,color):
        self.color=color

    def get_color(self):
        return self.color

    def set_color(self,color):
	    self.color=color
		
cookie_one=Cookie('green')
cookie_two=Cookie('blue')

print('cookie one is ', cookie_one.get_color())
print('cookie two is ',cookie_two.get_color())

cookie_one.set_color('yellow')

print('\n cookie one is now ',cookie_one.get_color())
print('cookie two is still',cookie_two.get_color())


class Linkedlist:
    def __init__(self,value):
        
    def append(self,value):

    def pop(self):

    def prepend(self,value):

    def insert(self,index,value):

    def remove(self,index):

        """

#discussion on pointers 
""" num1=11
num2=num1

print("Before num2 values is updated")
print("num1=",num1)
print("num2=",num2)

print('num1 points to:',id(num1))
print('num2 points to',id(num2))

num2=22

print("Before num2 values is updated")
print("num1=",num1)
print("num2=",num2)

print('num1 points to:',id(num1))
print('num2 points to',id(num2))

"""

#understanding pointers using different data types dictionary
#question is do we create an additional dictionary that is identical someplace else in memory
#and have dictionary two point at it
#or do we have dictionary two point at the same dictionary in memory?
#
#so the answer to that is they are both going to point to the same dictionary

"""
dict1 ={
    'value':11
}
dict2=dict1

print("Before num2 values is updated")
print("dict1=",dict1)
print("dict2=",dict2)

print('dict1 points to:',id(dict1))
print('dict2 points to',id(dict2))

#changing to new value
dict3={
    'value':44
}
dict2=dict3

print("After the new value pointing")
print("dict1=",dict1)
print("dict2=",dict2)
print("dict3=",dict3)

print('dict1 points to:',id(dict1))
print('dict2 points to:',id(dict2))
print('dict3 points to:',id(dict3))

"""


############################  Linkedlist #################################
#And our constructor is going to start off like this. so we can create the first node in the linkedlist at the time 
#that we create the linked list.
#we are going to have a variable new node and that's going to be equal to node with a capital N
#it is going to call the node class

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length +=1
        return True
    """def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length ==0:
            self.head=None
            self.tail=None
        return temp
        return temp.value
my_linked_list=Linkedlist(5)
my_linked_list.append(6)

#(2) Items - Returns 2 Node
print(my_linked_list.pop())
#(1) Items - Returns 1 Node
print(my_linked_list.pop())
#(0) Items - Returns None
print(my_linked_list.pop())
#my_linked_list.print_list()


    def prepend(self,value):
        newnode=Node(value)
        if self.length ==0 :
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.length+=1
        return True

    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    
my_linked_list=Linkedlist(5)
my_linked_list.append(6)
#(2) Items - Returns 2 Node
print(my_linked_list.popfirst())
#(1) Items - Returns 1 Node
print(my_linked_list.popfirst())
#(0) Items - Returns None
print(my_linked_list.popfirst())
#my_linked_list.print_list()
my_linked_list.print_list()
"""
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

my_linked_list=Linkedlist(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))