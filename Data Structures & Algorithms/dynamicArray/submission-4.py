class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        if self.capacity > 0:
            self.arr = [0 for _ in range(self.capacity)]
        self.pointer = 0 #keep track of next empty spot, 
                        #also happens to be the length of the arr.



    def get(self, i: int) -> int:
        if i < len(self.arr):
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < len(self.arr):
            self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.pointer == self.capacity:
            self.resize()
        self.arr[self.pointer] = n
        self.pointer += 1
        
    def popback(self) -> int:
        if len(self.arr) > 0:
            self.pointer -= 1
        return self.arr[self.pointer]

    def resize(self) -> None:
        self.capacity = 2* self.capacity
        new_arr = [0] * self.capacity 

        for i in range(self.pointer):
            new_arr[i] = self.arr[i]
        self.arr= new_arr


    def getSize(self) -> int:
        return self.pointer
        
    
    def getCapacity(self) -> int:
        return self.capacity
