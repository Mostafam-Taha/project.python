"""
تنفيذ بسيط لهياكل بيانات Stack (المكدس) و Queue (الطابور)
"""


class Stack:
    """مكدس: آخر عنصر يدخل هو أول عنصر يخرج (LIFO)"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """إضافة عنصر فوق المكدس"""
        self.items.append(item)

    def pop(self):
        """إزالة وإرجاع العنصر العلوي"""
        if self.is_empty():
            raise IndexError("المكدس فارغ")
        return self.items.pop()

    def peek(self):
        """معاينة العنصر العلوي دون إزالته"""
        if self.is_empty():
            raise IndexError("المكدس فارغ")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Queue:
    """طابور: أول عنصر يدخل هو أول عنصر يخرج (FIFO)"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """إضافة عنصر إلى نهاية الطابور"""
        self.items.append(item)

    def dequeue(self):
        """إزالة وإرجاع العنصر الأول"""
        if self.is_empty():
            raise IndexError("الطابور فارغ")
        return self.items.pop(0)

    def peek(self):
        """معاينة أول عنصر دون إزالته"""
        if self.is_empty():
            raise IndexError("الطابور فارغ")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    print("== Stack ==")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("المكدس:", s)
    print("pop:", s.pop())
    print("المكدس بعد pop:", s)

    print("\n== Queue ==")
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print("الطابور:", q)
    print("dequeue:", q.dequeue())
    print("الطابور بعد dequeue:", q)
