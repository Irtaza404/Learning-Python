class Student:
    count=0
    def __init__(self,name,age):
        Student.count+=1
        self.id=f"STD-{Student.count:03}"
        self.name,self.age=name,age
    
    def __eq__(self, value):
        return self.name==value.name and self.age==value.age

    def __str__(self):
        return f"ID :{self.id} , name :{self.name}, age :{self.age}"
        
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def inputs(self):
        name=input("Name:")
        age=int(input("age"))
        return Student(name,age)
    
    def insert(self,index,n=None):
        if not (0<=index<=self.size) :
            raise ValueError("not possible")
        n=Node(self.inputs()) if n is None else Node(n)
        if self.head==None:
            self.head=n
        elif index==0:
            n.next=self.head
            self.head=n
        else:
            temp=self.head
            no=0
            while no!=index-1:
                temp=temp.next  
                no+=1
            n.next=temp.next
            temp.next=n    
        
        self.size+=1
    
    def delete(self):
        if self.head is None:
            raise ValueError("Empty")
        data=self.inputs()
        if self.head.data==data:
            self.head=self.head.next
            self.size-=1
            return
        temp =self.head
        while temp.next is not None:
            if temp.next.data==data:
                temp.next=temp.next.next
                self.size-=1
                return
            temp=temp.next
        
        print("Not found")
    
    def delete_at(self,index):
        if self.head is None:
            raise ValueError("Empty")
        if not(0 <=index<self.size):
            raise IndexError("invalid index")
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        temp =self.head
        n=0
        while temp is not None:
            if n==index-1:
                temp.next=temp.next.next
                self.size-=1
                return
            temp=temp.next
            n+=1
        
        print("Not found")      
    
    def find(self):
        if self.head is None:
            raise ValueError("Empty")
        data=self.inputs()
        temp= self.head
        n=0
        while temp!=None:
            if temp.data==data:
                return n
            n+=1
            temp=temp.next
        return -1    
    def append(self, data=None):
        self.insert(self.size, data)

    def prepend(self, data=None):
        self.insert(0, data)
    def __len__(self):
        return self.size
    def __str__(self):
        if self.head is None:
            return "Empty list"
        temp=self.head
        result=""
        while temp!=None:
            result+=f"{temp.data} -> "
            temp=temp.next
        return result+"None"

if __name__ == "__main__":
    sll = SinglyLinkedList()
    while True:
        print("\n1. Append")
        print("2. Prepend")
        print("3. Insert at index")
        print("4. Delete by value")
        print("5. Delete at index")
        print("6. Find")
        print("7. Print list")
        print("8. Length")
        print("9. Exit")

        match int(input("choice: ")):
            case 1:
                sll.append()
            case 2:
                sll.prepend()
            case 3:
                index = int(input("index: "))
                sll.insert(index)
            case 4:
                sll.delete()
            case 5:
                index = int(input("index: "))
                sll.delete_at(index)
            case 6:
                result = sll.find()
                print(f"Found at index: {result}" if result != -1 else "Not found")
            case 7:
                print(sll)
            case 8:
                print(f"Length: {len(sll)}")
            case 9:
                break
            case _:
                print("Invalid input")