'''#########################################################################
   Program to convert infix expression into 
   postfix expression Ex. A+(B*C-(D/E-F)*G)*H  ---->> ABC*DE/F-G*-H*+
   
   NOTE::-Please take care that here we are not using expression involving 
   mathematical operators like  ^,** etc..
   and use only '()' in expression if neccessary 
   ######################################################################### '''
#Node class definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Stack class definition     
class Stack:
    #constructor 
    def __init__(self):
        self.top=None
    
    def push(self,data):
        a=Node(data);
        if self.top is None:
            self.top=a
        else:
            a.next=self.top
            self.top=a
    
    def pop(self):
        if self.top is None:
            return
        else:
            self.top=self.top.next

    def isempty(self):
        if self.top is None:
            return True
        else:
            return False

def precedence(a,b):
    if ((a is '+' or a is '-') and ( b is '-' or b is '+')) or ((a is '*' or a is '/') and (b is '/' or b is '*')) :
        return True
    if (a is '*' or a is '/') and (b is '-' or b is '+'):
        return True
    else:
        return False
# End of Stack class

#main() 
def main():
    exp=input("Enter a valid infix Expression::")
    s=Stack()
    post_exp=[]
    for i in range(len(exp)):
        if exp[i] is '+' or exp[i] is '-' or exp[i] is '*' or exp[i] is '/'or exp[i] is '('or exp[i] is ')':
            if s.isempty() is True or exp[i] is '(' or s.top.data is '(':
                s.push(exp[i])
            else:
                if exp[i] is ')':
                    while s.top.data is not '(':
                        post_exp.append(s.top.data)
                        s.pop()
                    s.pop()
                elif precedence(s.top.data,exp[i]) is True:
                    #while s.top is not None or s.top.data is not '(':
                    post_exp.append(s.top.data)
                    s.pop()
                    s.push(exp[i])
                else:
                    s.push(exp[i])
        else:
            post_exp.append(exp[i])
        
    if s.top is not None:
        while s.top is not None:
            post_exp.append(s.top.data)
            s.pop()
    print("The Postfix conversion is::",end="")
    for i in range(len(post_exp)):
        print(post_exp[i],end="")
main()
    
