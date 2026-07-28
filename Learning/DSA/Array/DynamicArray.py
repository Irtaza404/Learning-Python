import ctypes

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def __str__(self):
        return f"{self.name}({self.roll_no})"

class DynamicArray:
    def __init__(self,capacity=1):
        self.capacity=capacity
        self.n=0
        self.arr=(capacity* ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,value):
        if self.n==self.capacity:
            self.resize(2*self.capacity)
        self.arr[self.n]=value
        self.n+=1
    
    def resize(self,new_cap):
        newarr=(new_cap*ctypes.py_object)()
        for i in range(self.n):
            newarr[i]=self.arr[i]
        self.arr=newarr
        self.capacity=new_cap
    
    def __setitem__(self, index, value):
            if index<0 or index>=self.n:
                raise IndexError()
            self.arr[index]=value
    
        
    def __getitem__(self, index):
        if index<0 or index>=self.n:
            raise IndexError()
        return self.arr[index]
    
    def pop(self):
        if self.n==0:
            return None 
        self.n-=1
        return self.arr[self.n]
    
    def __str__(self):
        value=""
        for i in range(self.n):
            value+=f"{str(self.arr[i])}, "
        return f"[{value}]"
