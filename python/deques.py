class Deque():
    def __init__(self):
        self.front = []
        self.back = []

    def push(self, val):
        self.front.append(val)

        if not self.back:
            self.split_front()

    def pop(self):
        if self.front:
            ret = self.front.pop()
            if not self.front and self.back:
                self.split_back()
            return ret
        elif self.back:
            assert(len(self.back) == 1)
            return self.back.pop()

    def enque(self, val):
        self.back.append(val)
        if not self.front:
            self.split_back()

    def deque(self):
        if self.back:
            ret = self.back.pop()
            if not self.back and self.front:
                self.split_front()
            return ret
        elif self.front:
            assert(len(self.front) == 1)
            return self.front.pop()

    def split_back(self):
        length = len(self.back)
        self.front = self.back[:length / 2]
        self.front.reverse()
        self.back = self.back[length/2:]

    def split_front(self):
        length = len(self.front)
        self.back = self.front[:length / 2]
        self.back.reverse()
        self.front = self.front[length/2:]
