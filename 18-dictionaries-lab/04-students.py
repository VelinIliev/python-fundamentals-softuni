students = {}
while True:
    entry = input()
    if len(entry.split(":")) == 1:
        entry = entry.replace("_", " ", 1)
        for i in students:
            if students[i]['course'] == entry:
                print(f"{students[i]['name']} - {i}")
        break
    else:
        entry = entry.split(":")
        student_name = entry[0]
        student_id = int(entry[1])
        student_course = entry[2]
        students[student_id]= { 'name': student_name, 'course': student_course}
