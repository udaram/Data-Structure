#Bracket maching Program using Python


#Class to create a node
class Node:
    #constructer for field of node
    def __init__(self,data):
        self.data=data
        self.next=None

#declaration of a user defined class named stack
class stack:
    #constructer
    def __init__(self):
        self.top=None
    
    #Push into the stack
    def push(self,data):
        a=Node(data) #creating a node
        if self.top is None: #check whether stack is empty
            self.top=a
        else:
            a.next=self.top
            self.top=a
    #Function to pop
    def pop(self):
        if self.top is None:
            return
        else:
            self.top=self.top.next
    #check the emptyness of stack
    def isempty(self):
        if self.top is None:
            return True
        else:
            return False

# Declaration of main()         
def main():
    s=stack()
    #taking input of barcket strng from user
    string=input("Enter the string of Brackets::")
    
    for i in range(len(string)):
        if string[i] is '(' or string[i] is '{' or string[i] is '[' :
            s.push(string[i])
        elif string[i] is '}' or string[i] is ']' or  string[i] is ')':
            if s.top is None:
                print("Wrong bracket statement!!!")
                quit()
            elif string[i] is ')':
                if s.top.data is '(':
                    s.pop()
                else:
                    print("Wrong bracket statement!!!")
                    quit()
            elif string[i] is '}':
                if s.top.data is '{':
                    s.pop()
                else:
                    print("Wrong bracket statement!!!")
                    quit()
            elif string[i] is ']':
                if s.top.data is '[':
                    s.pop()
                else:
                    print("Wrong bracket statement!!!")
                    quit()
        else:
            print("Wrong bracket statement!!!")
            quit()
    if s.isempty() is True:
        print("Right bracket statement!!!")
        quit()
    else:
        print("Wrong bracket statement!!!")
        quit()
main()
    

        
