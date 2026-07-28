import ctypes

class MyArray:
    def __init__(self,capacity):
        self.capacity=capacity
        self.arr=(capacity* ctypes.py_object)()
        for i in range(capacity):
            self.arr[i]=None
        
    
    def __len__(self):
        return self.capacity
    
    def __setitem__(self, index, value):
        if index<0 or index>=self.capacity:
            raise IndexError()
        
        self.arr[index]=value
    
    def __getitem__(self, index):
        if index<0 or index>=self.capacity:
            raise IndexError()
        return self.arr[index]
    
    def __str__(self):
        return f"[{' ,'.join(map(str,self.arr))}]"

if __name__=="__main__":
    myArray=MyArray(int(input("Size:")))
    while True:
        print("1. Set value ")
        print("2. Get value at index")
        print("3. print Array")
        print("4. exit")
        match int(input("choice:")):
            case 1:
                myArray[int(input("index:"))]=input("value") 
            case 2:
                print(myArray[int(input("index:"))])
            case 3:
                print(myArray)
            case 4:
                break
            case _:
                print("Invalid input")