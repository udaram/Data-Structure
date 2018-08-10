#Linklist implementation

class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

#Link list class 
class linklist:
    #constructor
    def __init__(self):
        self.head=None
        self.tail=None
    #funcion to insert in link list at end 
    def insert(self,data):
        a=Node(data)
        if self.head==None:
            self.head=self.tail=a
        else:
            self.tail.link=a
            self.tail=a
    #to insert node at begining of list
    def insertAtBeg(self,data):
        a=Node(data)
        if self.head is None:
            self.head=self.tail=a
        else :
            a.link=self.head
            self.head=a
    #Insertion at perticular Position 
    def insertAtPos(self,pos,data):
        a=Node(data)
        p=self.head
        i=0
        if pos==0:
            self.insertAtBeg(data)
        else:
            while p!=None and pos-1!=i:
                i+=1
                p=p.link
            if p is None and pos>i :
                print("INVALID POSITION")
            else:
                a.link=p.link.link
                p.link=a
    #to display list
    def display(self):
        p=self.head
        print("\nLink list is:::",end ="")
        if p is None:
            print("Empty!!!!")
        while p is not None:
            print("-> ",p.data,end =" ")
            p=p.link
    #Display list in reverse order
    def reverse(self,p):
        if p is None:
            return
        else:
            self.reverse(p.link)
            print(" -> ",p.data,end="")
    #delete the  starting node from List
    def delete(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head=self.head.link
    #deletion from End
    def deleteAtEnd(self):
        if self.head is None:
            print("List is Empty")
        else:
            q=p=self.head
            while p.link is not None:
                q=p
                p=p.link
            if q.link is None:
                self.delete()
            else:
                q.link=None
                self.tail=q
    def deleteFromPos(self,pos):
        if self.head==None:
            print("List is Empty")
        elif pos==0:
            self.delete();
        else:
            p=self.head
            i=0
            while p!=None and pos-1 is not i:
                i+=1
                p=p.link
            if p is None and pos>=i:
                print("Invalid Position")
            else:
                p.link=p.link.link

def main():
    l=linklist()
    ch='y'
    while ch is 'y':
        print('''1.Insertion
2.Insert at begining
3.Insert at End 
4.Insert at Position
5.Display list
6.Display in reverse order
7.Delete from begining
8.Delete from end
9.Delete from position
10.EXIT''')
        
        option=int(input("Enter option:::"))
        
        if option is 1:
            a=int(input("Enter data::"))
            l.insert(a)
        elif option is 2:
            a=int(input("Enter data::"))
            l.insertAtBeg(a)
        elif option is 3:
            a=int(input("Enter data::"))
            l.insert(a)
        elif option is 4:
            pos=int(input("Enter Position(0 ......n)::"))
            a=int(input("Enter data::"))
            l.insertAtPos(pos,a)
        elif option is 5:
            l.display()
        elif option is 6:
            print("List in Reverse Order is :::",end="")
            l.reverse(l.head)
        elif option is 7:
            l.delete()
        elif option is 8:
            l.deleteAtEnd()
        elif option is 9:
            pos=int(input("Enter Position(0 ......n)::"))
            l.deleteFromPos(pos)
        else:
            quit()
        ch=input("\nEnter y to continue program:::")
main()
