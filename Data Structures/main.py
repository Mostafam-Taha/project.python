# -*- coding: utf-8 -*-
"""
====================================================
مشروع: نظام إدارة الموظفين باستخدام JSON
====================================================
المشروع ده مثال متقدم على التعامل مع ملفات JSON في بايثون
هنستخدم فيه:
  - القراءة   : json.load
  - الكتابة   : json.dump
  - إضافة عنصر جديد (اقرأ -> عدّل في بايثون -> اكتب تاني)
  - تعديل عنصر موجود
  - حذف عنصر
  - بحث وفلترة
  - إحصائيات (average, count, max, min) باستخدام الداتا
====================================================
"""

import json
import os

DATA_FILE = "employees.json"


# ---------------------------------------------------
# دوال أساسية للتعامل مع الملف (قراءة / كتابة)
# ---------------------------------------------------

def load_data():
    """تقرأ كل الموظفين من ملف JSON وترجعهم كـ list of dict"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """تكتب الـ list of dict كامل في ملف JSON (بتستبدل القديم بالكامل)"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ---------------------------------------------------
# العمليات (CRUD): إضافة - عرض - تعديل - حذف
# ---------------------------------------------------

def add_employee():
    data = load_data()
    new_id = max([emp["id"] for emp in data], default=0) + 1

    name = input("اسم الموظف: ").strip()
    department = input("القسم: ").strip()
    city = input("المدينة: ").strip()
    age = int(input("العمر: "))
    salary = int(input("المرتب: "))

    new_employee = {
        "id": new_id,
        "name": name,
        "department": department,
        "city": city,
        "age": age,
        "salary": salary,
        "is_active": True
    }

    data.append(new_employee)   # نضيف في الذاكرة
    save_data(data)             # نعيد كتابة الملف بالكامل
    print(f"\n✅ تم إضافة الموظف بنجاح برقم ID = {new_id}\n")


def view_all(data=None):
    data = data if data is not None else load_data()
    if not data:
        print("\nلا يوجد بيانات لعرضها.\n")
        return

    print("\n" + "-" * 70)
    print(f"{'ID':<5}{'الاسم':<20}{'القسم':<18}{'المدينة':<12}{'العمر':<6}{'المرتب':<8}{'نشط؟'}")
    print("-" * 70)
    for emp in data:
        status = "نعم" if emp["is_active"] else "لا"
        print(f"{emp['id']:<5}{emp['name']:<20}{emp['department']:<18}"
              f"{emp['city']:<12}{emp['age']:<6}{emp['salary']:<8}{status}")
    print("-" * 70)
    print(f"إجمالي عدد السجلات: {len(data)}\n")


def search_employee():
    data = load_data()
    keyword = input("اكتب اسم أو قسم أو مدينة للبحث عنه: ").strip()

    results = [
        emp for emp in data
        if keyword in emp["name"] or keyword in emp["department"] or keyword in emp["city"]
    ]

    if results:
        print(f"\n🔍 تم العثور على {len(results)} نتيجة:")
        view_all(results)
    else:
        print("\n❌ لا يوجد نتائج مطابقة.\n")


def update_employee():
    data = load_data()
    emp_id = int(input("اكتب رقم الـ ID للموظف اللي عايز تعدله: "))

    for emp in data:
        if emp["id"] == emp_id:
            print(f"البيانات الحالية: {emp}")
            print("اضغط Enter لو مش عايز تغيّر القيمة")

            name = input(f"الاسم الجديد ({emp['name']}): ").strip()
            department = input(f"القسم الجديد ({emp['department']}): ").strip()
            salary = input(f"المرتب الجديد ({emp['salary']}): ").strip()

            if name:
                emp["name"] = name
            if department:
                emp["department"] = department
            if salary:
                emp["salary"] = int(salary)

            save_data(data)
            print("\n✅ تم تعديل بيانات الموظف بنجاح.\n")
            return

    print("\n❌ لم يتم العثور على موظف بهذا الـ ID.\n")


def delete_employee():
    data = load_data()
    emp_id = int(input("اكتب رقم الـ ID للموظف اللي عايز تحذفه: "))

    new_data = [emp for emp in data if emp["id"] != emp_id]

    if len(new_data) == len(data):
        print("\n❌ لم يتم العثور على موظف بهذا الـ ID.\n")
    else:
        save_data(new_data)
        print(f"\n🗑️ تم حذف الموظف رقم {emp_id} بنجاح.\n")


# ---------------------------------------------------
# إحصائيات عامة على البيانات
# ---------------------------------------------------

def show_statistics():
    data = load_data()
    if not data:
        print("\nلا يوجد بيانات لعمل إحصائية.\n")
        return

    salaries = [emp["salary"] for emp in data]
    active_count = sum(1 for emp in data if emp["is_active"])

    departments_count = {}
    for emp in data:
        dept = emp["department"]
        departments_count[dept] = departments_count.get(dept, 0) + 1

    print("\n📊 إحصائيات عامة:")
    print(f"عدد الموظفين الكلي: {len(data)}")
    print(f"عدد الموظفين النشطين: {active_count}")
    print(f"متوسط المرتب: {sum(salaries) / len(salaries):.2f}")
    print(f"أعلى مرتب: {max(salaries)}")
    print(f"أقل مرتب: {min(salaries)}")

    print("\nعدد الموظفين لكل قسم:")
    for dept, count in sorted(departments_count.items(), key=lambda x: -x[1]):
        print(f"  - {dept}: {count}")
    print()


# ---------------------------------------------------
# القائمة الرئيسية
# ---------------------------------------------------

def main_menu():
    while True:
        print("=" * 40)
        print("     نظام إدارة الموظفين (JSON)")
        print("=" * 40)
        print("1. عرض كل الموظفين")
        print("2. إضافة موظف جديد")
        print("3. تعديل بيانات موظف")
        print("4. حذف موظف")
        print("5. بحث")
        print("6. إحصائيات")
        print("0. خروج")

        choice = input("اختر رقم العملية: ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            search_employee()
        elif choice == "6":
            show_statistics()
        elif choice == "0":
            print("مع السلامة 👋")
            break
        else:
            print("\n⚠️ اختيار غير صحيح، حاول تاني.\n")


if __name__ == "__main__":
    main_menu()