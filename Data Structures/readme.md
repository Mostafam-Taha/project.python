# مشروع هياكل البيانات (Data Structures Project)

مشروع بايثون بسيط يشرح ويطبّق أهم هياكل البيانات الأساسية:

## الهياكل المتوفرة
| الملف | الهيكل | الوصف |
|---|---|---|
| `linked_list.py` | Linked List | قائمة مرتبطة أحادية الاتجاه (append, prepend, delete, search) |
| `stack_queue.py` | Stack & Queue | مكدس (LIFO) وطابور (FIFO) |
| `binary_search_tree.py` | Binary Search Tree | شجرة بحث ثنائية (insert, search, inorder, height) |
| `main.py` | - | قائمة تفاعلية (menu) لتجربة كل الهياكل من الطرفية |

## طريقة التشغيل

### 1. تشغيل القائمة التفاعلية الكاملة
```bash
python main.py
```
هذا يفتح لك قائمة تختار منها الهيكل الذي تريد تجربته (Linked List, Stack, Queue, BST) وتتفاعل معه مباشرة.

### 2. تشغيل كل ملف بشكل منفصل (مثال جاهز مبني داخل كل ملف)
```bash
python linked_list.py
python stack_queue.py
python binary_search_tree.py
```
كل ملف يحتوي على قسم `if __name__ == "__main__":` فيه مثال جاهز يوضح كيفية استخدام الهيكل.

## متطلبات التشغيل
- Python 3.6 أو أحدث فقط (لا حاجة لأي مكتبات خارجية)

## هيكل المشروع
```
data_structures_project/
├── linked_list.py
├── stack_queue.py
├── binary_search_tree.py
├── main.py
└── README.md
```

## أفكار للتطوير لاحقًا
- إضافة قائمة مرتبطة ثنائية الاتجاه (Doubly Linked List)
- إضافة Hash Table
- إضافة Graph مع خوارزميات BFS/DFS
- كتابة اختبارات وحدة (unit tests) باستخدام `unittest`
