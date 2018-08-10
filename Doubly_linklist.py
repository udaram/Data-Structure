#Doubly Linklist implementation

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

# Doubly Link list class 
class Doubly_linklist:
    #constructor
    def __init__(self):
        self.head=None
        self.tail=None
    #funcion to insert in Doubly link list at end 
    def insert(self,data):
        a=Node(data)
        if self.head is None:
            self.head=self.tail=a
        else:
            self.tail.next=a
            a.prev=self.tail
            self.tail=a
    #to insert node at begining of list
    def insert_At_Beg(self,data):
        a=Node(data)
        if self.head is None:
            self.head=self.tail=a
        else :
            a.next=self.head
            self.head.prev=a
            self.head=a
    #Insertion at perticular Position 
    def insert_At_Pos(self,pos,data):
        a=Node(data)
        p=self.head
        i=0
        if pos==0:
            self.insert_At_Beg(data)
        else:
            while p!=None and pos-1!=i:
                i+=1
                p=p.next
            if p is None and pos>i :
                print("INVALID POSITION")
            else:
                a.prev=p
                a.next=p.next
                p.next.prev=a
                p.next=a
    #to display list
    def display(self):
        p=self.head
        print("\nDoubly Link list is:::",end ="")
        if p is None:
            print("Empty!!!!")
        while p is not None:
            print("<=> ",p.data,end =" ")
            p=p.next
    #Display list in reverse order
    def reverse(self):
        p=self.tail
        if p is None:
            print("List is Empty")
        else:
            while p is not None:
                print("<=>",p.data,end="")
                p=p.prev
    #delete the  starting node from List
    def delete(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head=self.head.next
            self.head.prev=None
    #deletion from End
    def delete_form_End(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    #Deletion from a perticular position
    def delete_From_Pos(self,pos):
        if self.head==None:
            print("List is Empty")
        elif pos==0:
            self.delete()
        else:
            p=self.head
            i=0
            while p!=None and pos-1 is not i:
                i+=1
                p=p.next
            if p is None and pos>=i:
                print("Invalid Position")
            elif p.next.next is None and i is pos-1:
                p.next=None
                self.tail=p;
            else:
                p.next.next.prev=p
                p.next=p.next.next
                
def main():
    l=Doubly_linklist()
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
            l.insert_At_Beg(a)
        elif option is 3:
            a=int(input("Enter data::"))
            l.insert(a)
        elif option is 4:
            pos=int(input("Enter Position(0 ......n)::"))
            a=int(input("Enter data::"))
            l.insert_At_Pos(pos,a)
        elif option is 5:
            l.display()
        elif option is 6:
            print("List in Reverse Order is :::",end="")
            l.reverse()
        elif option is 7:
            l.delete()
        elif option is 8:
            l.delete_form_End()
        elif option is 9:
            pos=int(input("Enter Position(0 ......n)::"))
            l.delete_From_Pos(pos)
        else:
            quit()
        ch=input("\nEnter y to continue program:::")
main()
