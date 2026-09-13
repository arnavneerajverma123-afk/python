student_data = { 
"id1":{"name": "Sara", "Class" : "V", "subject_intregration":"English,Maths,Science"},
"id2":{"name": "David", "Class" : "V", "subject_intregration":"English,Maths,Science"},
"id3":{"name": "Sara", "Class" : "V", "subject_intregration":"English,Maths,Science"},
"id4":{"name": "Surya", "Class" : "V", "subject_intregration":"English,Maths,Science"}
}
result = {}
seen_keys = []
for student_id , details in student_data.items():
    unique_key = (details["name"],details["Class"]),details["subject_intregration"]
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
    print(k,":",v)