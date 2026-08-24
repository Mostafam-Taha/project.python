"""
تنفيذ بسيط لقائمة مرتبطة (Linked List) أحادية الاتجاه
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """إضافة عنصر في نهاية القائمة"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        """إضافة عنصر في بداية القائمة"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data):
        """حذف أول عنصر يطابق القيمة المعطاة"""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def search(self, data):
        """البحث عن عنصر في القائمة"""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def to_list(self):
        """تحويل القائمة المرتبطة إلى list عادية للعرض"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __str__(self):
        return " -> ".join(str(item) for item in self.to_list()) or "قائمة فارغة"


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    print("القائمة:", ll)
    print("طول القائمة:", len(ll))
    print("موقع القيمة 20:", ll.search(20))
    ll.delete(20)
    print("بعد حذف 20:", ll)
