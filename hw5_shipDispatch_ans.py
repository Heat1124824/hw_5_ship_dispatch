class Stack: #建立堆疊 (不要改!!!)
    def __init__(self, size):
        self.size = size
        self.data = [0]*self.size
        self.top = -1

    def isFull(self):
        return self.top == self.size-1

    def isEmpty(self):
        return self.top == -1

    def push(self, x):
        if self.isFull():
            print("堆疊已滿")
        else:
            self.top = self.top + 1
            self.data[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("堆疊是空的")
        else:
            item = self.data[self.top]
            self.top = self.top - 1
            return item

    def printStack(self):
        for i in range(0, self.top + 1):
            print(self.data[i], end="")
        print()

def dispatch(ship_in, ship_out):
    step = [] #貨船進出程序
    harbor = Stack(len(ship_in)) #港口在這裡視為堆疊
    while ship_out != []: #輸出貨船出港順序
        #處理進出皆為同一艘船的狀況
        if (ship_in != []) and (ship_in[0] == ship_out[0]): 
            ship_in.pop(0)
            ship_out.pop(0)
            step.extend(["push","pop"])
        #港口不為空且港口堆疊頂端與出港串列的第一項號碼一樣，則step加入pop
        elif (not harbor.isEmpty()) and (harbor.data[harbor.top] == ship_out[0]):
            harbor.pop()
            ship_out.pop(0)
            step.append("pop")
        #入港串列不為空時，則step加入push
        elif ship_in != []:
            harbor.push(ship_in.pop(0))
            step.append("push")
        #前面三個條件皆不成立則跳出迴圈
        else:
            break
    #當跳出迴圈時，出港串列不為空，則step直接回傳一個空的串列
    if ship_out != []:
        step = []
    return step

def main():
    ship_in = [1, 5, 8, 6, 9]
    ship_out = [8, 5, 6, 1, 9]
    step = dispatch(ship_in, ship_out)
    print(step)

if __name__ == "__main__":
    main()