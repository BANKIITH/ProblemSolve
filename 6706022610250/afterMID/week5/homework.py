
n = int(input("กรอกจำนวนนักศึกษา: "))


students = {}


for i in range(n):
    name = input(f"ป้อนชื่อนักศึกษาคนที่ {i+1}: ")
    score = int(input(f"ป้อนคะแนนของ {name}: "))
    students[name] = score


sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
print("คะแนนทั้งหมดเรียงจากมากไปน้อย:")
for name, score in sorted_students:
    print(f"{name}: {score}")


print("Top 3 นักศึกษาที่ได้คะแนนสูงสุด:")
for name, score in sorted_students[:3]:
    print(f"{name}: {score}")


print("Top 3 นักศึกษาที่ได้คะแนนต่ำสุด:")
for name, score in sorted_students[-3:]:
    print(f"{name}: {score}")


search_score = int(input("กรุณากรอกคะแนนที่ต้องการค้นหา: "))
matching_students = [name for name, score in students.items() if score == search_score]

if matching_students:
    print(f"มีนักศึกษาทั้งหมด {len(matching_students)} คน ที่ได้คะแนน {search_score}:")
    print(", ".join(matching_students))
else:
    print("ไม่พบนักศึกษาที่ได้คะแนนนี้")
