class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def inputs(self):
        name = input("Name:")
        age = int(input("age"))
        return Student(name, age)

    def insert(self, index, n=None):
        if not (0 <= index <= self.size):
            raise ValueError("not possible")
        n = Node(self.inputs()) if n is None else Node(n)

        if self.head is None:
            n.next = n
            self.head = n
        elif index == 0:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            n.next = self.head
            temp.next = n
            self.head = n
        else:
            temp = self.head
            no = 0
            while no != index - 1:
                temp = temp.next
                no += 1
            n.next = temp.next
            temp.next = n

        self.size += 1

    def delete(self):
        if self.head is None:
            return
        data = self.inputs()
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                self.size -= 1
                return
        elif self.head.data == data:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = temp.next.next
            self.head = temp.next
            self.size -= 1
            return
        else:
            temp = self.head
            while temp.next != self.head:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    self.size -= 1
                    return
                temp = temp.next
        return "Not found"

    def delete_at(self, index):
        if self.head is None:
            return
        if not (0 <= index < self.size):
            raise IndexError("invalid index")
        # SAME TRAP as delete(): index 0 (head) must be handled separately
        # from the general case, because the LAST node needs repointing.
        if self.size == 1:
            self.head = None
            self.size -= 1
            return
        if index == 0:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
            self.size -= 1
            return
        temp = self.head
        n = 0
        while n != index - 1:
            temp = temp.next
            n += 1
        temp.next = temp.next.next
        self.size -= 1

    def find(self):
        if self.head is None:
            return -1
        data = self.inputs()
        temp = self.head
        n = 0
        # SAME TRAP as before: must check head BEFORE the loop condition
        # would exit, since "temp.next == head" fires right after the
        # last node — a plain while-loop here would skip checking head.
        while True:
            if temp.data == data:
                return n
            temp = temp.next
            n += 1
            if temp == self.head:
                break
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
        temp = self.head
        result = ""
        while True:
            result += f"{temp.data} -> "
            temp = temp.next
            if temp == self.head:
                break
        return result + "(back to head)"


if __name__ == "__main__":
    cll = CircularLinkedList()
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
                cll.append()
            case 2:
                cll.prepend()
            case 3:
                index = int(input("index: "))
                cll.insert(index)
            case 4:
                print(cll.delete())
            case 5:
                index = int(input("index: "))
                cll.delete_at(index)
            case 6:
                result = cll.find()
                print(f"Found at index: {result}" if result != -1 else "Not found")
            case 7:
                print(cll)
            case 8:
                print(f"Length: {len(cll)}")
            case 9:
                break
            case _:
                print("Invalid input")