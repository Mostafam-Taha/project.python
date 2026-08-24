"""
البرنامج الرئيسي: قائمة تفاعلية لتجربة كل هياكل البيانات
"""

from linked_list import LinkedList
from stack_queue import Stack, Queue
from binary_search_tree import BinarySearchTree


def linked_list_demo():
    ll = LinkedList()
    while True:
        print("\n--- Linked List ---")
        print("الحالة الحالية:", ll)
        print("1) إضافة عنصر (نهاية) | 2) إضافة عنصر (بداية) | 3) حذف عنصر | 4) بحث | 0) رجوع")
        choice = input("اختر: ").strip()
        if choice == "1":
            ll.append(input("القيمة: "))
        elif choice == "2":
            ll.prepend(input("القيمة: "))
        elif choice == "3":
            ok = ll.delete(input("القيمة المراد حذفها: "))
            print("تم الحذف" if ok else "القيمة غير موجودة")
        elif choice == "4":
            idx = ll.search(input("القيمة المراد البحث عنها: "))
            print(f"موجودة في الموقع {idx}" if idx != -1 else "غير موجودة")
        elif choice == "0":
            break
        else:
            print("اختيار غير صحيح")


def stack_demo():
    s = Stack()
    while True:
        print("\n--- Stack ---")
        print("الحالة الحالية:", s)
        print("1) push | 2) pop | 3) peek | 0) رجوع")
        choice = input("اختر: ").strip()
        if choice == "1":
            s.push(input("القيمة: "))
        elif choice == "2":
            try:
                print("تم إزالة:", s.pop())
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                print("العنصر العلوي:", s.peek())
            except IndexError as e:
                print(e)
        elif choice == "0":
            break
        else:
            print("اختيار غير صحيح")


def queue_demo():
    q = Queue()
    while True:
        print("\n--- Queue ---")
        print("الحالة الحالية:", q)
        print("1) enqueue | 2) dequeue | 3) peek | 0) رجوع")
        choice = input("اختر: ").strip()
        if choice == "1":
            q.enqueue(input("القيمة: "))
        elif choice == "2":
            try:
                print("تم إزالة:", q.dequeue())
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                print("العنصر الأول:", q.peek())
            except IndexError as e:
                print(e)
        elif choice == "0":
            break
        else:
            print("اختيار غير صحيح")


def bst_demo():
    bst = BinarySearchTree()
    while True:
        print("\n--- Binary Search Tree ---")
        print("Inorder:", bst.inorder())
        print("1) إدراج قيمة | 2) بحث عن قيمة | 3) عرض الارتفاع | 0) رجوع")
        choice = input("اختر: ").strip()
        if choice == "1":
            try:
                bst.insert(int(input("القيمة (رقم): ")))
            except ValueError:
                print("الرجاء إدخال رقم صحيح")
        elif choice == "2":
            try:
                val = int(input("القيمة (رقم): "))
                print("موجودة" if bst.search(val) else "غير موجودة")
            except ValueError:
                print("الرجاء إدخال رقم صحيح")
        elif choice == "3":
            print("الارتفاع:", bst.height())
        elif choice == "0":
            break
        else:
            print("اختيار غير صحيح")


def main():
    while True:
        print("\n=== مشروع هياكل البيانات ===")
        print("1) Linked List")
        print("2) Stack")
        print("3) Queue")
        print("4) Binary Search Tree")
        print("0) خروج")
        choice = input("اختر هيكل البيانات: ").strip()

        if choice == "1":
            linked_list_demo()
        elif choice == "2":
            stack_demo()
        elif choice == "3":
            queue_demo()
        elif choice == "4":
            bst_demo()
        elif choice == "0":
            print("مع السلامة!")
            break
        else:
            print("اختيار غير صحيح، حاول مرة أخرى")


if __name__ == "__main__":
    main()
