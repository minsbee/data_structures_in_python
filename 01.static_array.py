class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity

        # 여기서 정의된 self.data는 Python의 리스트 객체임. 배열과 유사하지만 크기 조정이 동적으로 조절되며 다양한 메서드를 지원하는 자료구조
        # 이 때, 리스트에 * 연산을 적용하면 리스트 자체가 반복되어 [None], [None], [None],  << 이런 형태의 값을 가지게 되는 것이 아니라 리스트 내에서 값을 횟수(여기서는 capacity)만큼 반복하게 됨
        self.data = [None] * capacity

        # 앞서 빈 값으로 데이터를 capacity만큼 채워 유효한 데이터의 갯수가 0인 것은 알고 있지만 해당 배열에 데이터를 추가 / 삭제할 때마다 수동으로 유효 데이터의 갯수를 추적하기 위해 초기값 0으로 유효데이터 숫자를 초기화 해줌
        self.length = 0


    # 정적 배열의 조회 메서드
    def __getitem__(self, index):
        if 0 <= index < self.capacity:
            return self.data[index]
        else:
            raise IndexError("Index out of range!")


    # 정적 배열의 값 입력 메서드
    # length의 의미를 앞서서는 유효한 데이터의 갯수로 정의했으나 그런 경우 length를 줄여야 하는 문제가 있음 (value is None 인 경우)
    # 그러나 그런 경우 조회 시에 Hole을 허용하지 않게 되므로 배열의 빈 값이 중간에 있는 경우 매 번 shift를 통해 앞으로 땡겨줘야 하며,
    # 연산이 고반복인 경우 O(n)의 연산이 지속적으로 발생해 조회 효율이 지나치게 떨어지게 됨.
    # 따라서 length의 정의를 유효한 데이터가 있는 인덱스의 끝을 나타내도록 하여 중간 Hole을 허용함으로써 length를 줄이는 문제를 방지하고,
    # 코드 작성 및 연산 효율을 최적화 하는 방식으로 "암묵적 합의"를 한 결과가 아래 코드임..
    def __setitem__(self, index, value):
        if 0 <= index < self.capacity:
            self.data[index] = value
            # 여기서 주의해야 할 게 self.length보다 인덱스가 많이 커지는 경우에는 중간의 Hole이 급격하게 커져버리는 문제가 있을 수 있음.
            # 그래서 아래와 같이 연속성을 유지하도록 코드를 강제로 짤 수도 있으나. 자유도가 떨어지는 단점이 있음

            # def __setitem__(self, index, value):
            #     if not (0 <= index < self.capacity):
            #         raise IndexError("Index out of range")
            #     if index > self.length:  # 연속성 강제
            #         raise IndexError("Cannot set value beyond length; use append instead")
            #     self.data[index] = value
            #     if index == self.length:  # 정확히 끝에 추가 시 length 증가
            #         self.length += 1

            if index >= self.length:
                self.length = index + 1
        else:
            raise IndexError("Index out of range!")


    # 배열에 값 추가, 다만 기존에 setItem으로 중간에 Hole이 생긴 경우 중간 빈 인덱스를 채우는 게 아닌 가장 끝 length 다음으로 들어가는 것에 유의
    def append(self, value):
        if self.length >= self.capacity:
            raise OverflowError("Array is full!")
        else:
            self.data[self.length] = value
            self.length += 1


    # 배열 사이에 값 삽입 특별히 주의할 것은 따로 없고 인덱스를 추가했을 때 넘치는 지, 그리고 인덱스가 배열 범위 내에 있는지만 확인
    # 그리고 나머지는 반복문으로 뒤로 값을 하나씩 밀어주면 됨
    def insert(self, index, value):
        if self.length >= self.capacity:
            raise OverflowError("Array is full!")
        if index < 0 or index > self.length:
            raise IndexError("Index out of range!")
        else:
            for i in range(self.length, index, -1):
                self.data[i] = self.data[i-1]

            self.data[index] = value
            self.length += 1


    # delete는 간단하게 인덱스로 제거할 부분이 결정되면 그 인덱스를 기준으로 반복문을 통해 앞으로 값을 전부 수정해주면 됨
    def delete(self, index):
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of range!")

        deleted_value = self.data[index]

        for i in range(index, self.length-1, 1):
            self.data[i] = self.data[i+1]

        self.data[self.length - 1] = None
        self.length -= 1

        return deleted_value


    def __str__(self):
        return f"Data: {self.data[:self.length]}, Length: {self.length}, Initial Capacity: {self.capacity}"

    def __len__(self):
        return self.length



arr = StaticArray(10)
print(arr[0]) # None
print(arr.length) # 0 (초기 할당된 값 출력)
print(arr.data) # [None, None, None, None, None, None, None, None, None, None]
print(arr.capacity) # 10 (초기 집어넣은 인자)


arr[2] = "item set!"
print("=====================setitem applied==========================")
print(arr.length)
print(arr.data)


arr.append("added by append")
print("=====================append applied===========================")
print(arr.length)
print(arr.data)
print(arr)
print(len(arr))



class StaticArray2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0


    def __getitem__(self, index):
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of range again!")

        else:
            return self.data[index]


    def __setitem__(self, index, value):
        # setitem은 배열의 크기 자체에 변화를 주지는 않으니까 굳이 length 체크를 할 필요는 없음
        # if self.length > self.capacity:
        #     raise OverflowError("Array is full again!")
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of range again!")

        self.data[index] = value

        if index >= self.length:
            self.length = index + 1


    def append(self, value):
        if self.length >= self.capacity:
            raise OverflowError("Array is full again!")

        self.data[self.length] = value
        self.length += 1


    def insert(self, index, value):
        if self.length >= self.capacity:
            raise OverflowError("Array is full again!")

        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of range again!")

        else:
            for i in range(self.length, index, -1):
                self.data[i] = self.data[i - 1]

            self.data[index] = value
            self.length += 1


    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range again!")

        deleted_value = self.data[index]

        for i in range(index, self.length):
            self.data[i] = self.data[i + 1]

        self.data[self.length - 1] = None
        self.length -= 1

        return f"{deleted_value} is deleted in array!"


    def __str__(self):
        return f"Data: {self.data[:self.length]}, Length: {self.length}, Total capacity: {self.capacity}"

    def __len__(self):
        return self.length


arr2 = StaticArray2(15)

print(arr[0])
print(arr2.data)
print(arr2.length)
print(arr2.capacity)
print(arr2)

arr2[10] = "new value set in here!!"
print("=====================setitem applied==========================")
print(len(arr2))
print(arr2.data)


arr2.append("value appended in here!!!")
print("=====================append applied===========================")
print(arr2)
print(len(arr2))


arr2.delete(11)
print("=====================delete applied===========================")
print(arr2)
print(len(arr2))