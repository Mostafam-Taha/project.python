# -*- coding: utf-8 -*-
"""
سكريبت لتوليد بيانات تجريبية كثيرة (موظفين) وحفظها في ملف employees.json
يشتغل مرة واحدة بس عشان نجهز قاعدة بيانات أولية للمشروع
"""

import json
import random

first_names = [
    "أحمد", "محمد", "سارة", "منى", "خالد", "علي", "فاطمة", "مريم", "يوسف",
    "إبراهيم", "نور", "هبة", "عمر", "زياد", "ليلى", "رنا", "طارق", "دينا",
    "كريم", "شريف", "ياسمين", "هدى", "وليد", "أمير", "سلمى", "ندى", "حسن",
    "منير", "رشا", "عادل"
]

last_names = [
    "المصري", "السيد", "عبد الله", "حسين", "إبراهيم", "الشريف", "فتحي",
    "رضوان", "الجندي", "زكي", "صلاح", "عثمان", "جابر", "توفيق", "نصار"
]

departments = ["المبيعات", "التسويق", "الموارد البشرية", "تقنية المعلومات",
               "المالية", "خدمة العملاء", "الإنتاج"]

cities = ["القاهرة", "الإسكندرية", "الجيزة", "المنصورة", "أسوان", "الأقصر",
          "طنطا", "الزقازيق"]


def generate_employees(count=50):
    employees = []
    for i in range(1, count + 1):
        emp = {
            "id": i,
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "department": random.choice(departments),
            "city": random.choice(cities),
            "age": random.randint(22, 58),
            "salary": random.randint(4000, 25000),
            "is_active": random.choice([True, True, True, False])  # أغلبهم نشطين
        }
        employees.append(emp)
    return employees


if __name__ == "__main__":
    data = generate_employees(50)
    with open("employees.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"تم إنشاء {len(data)} سجل موظف في employees.json")