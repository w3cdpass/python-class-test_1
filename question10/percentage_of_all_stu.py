marks = [[23,45,77,45,89,'Dupinder'],[28,75,77,45,89,'Mannu'],
        [23, 80, 77, 89,'Suman'], [63,91,37,65,99,'Rohit'],
        [43,65,77,75,89,'Sunny'],[56,23,45,77,87,'Ravi'],
        ]


for data_givn in marks:
    total_marks_each_student = 0
    for extracted_data in range(len(data_givn) -1):
        total_marks_each_student = total_marks_each_student + data_givn[extracted_data]
        
        division_each_total_marks = (total_marks_each_student / 500) * 100
        
    
    # print(total_marks_each_student, end=' ')
    print(f"{int(division_each_total_marks)}:{data_givn[-1]}")
        # print(extract_data, end =" ")
    # print()
    # print() 
    
    
# '''one only'''
# final_result = []
# total_res = 0
# for percentage in range(len(marks) -1):
#     total_res = total_res + marks[percentage]
#     division_by = (total_res / 500) *100
#     # final_result.append(total_res)
# print(total_res)
# print(final_result)
# print(f"{int(division_by)}: {marks[::-6]}")



# lst = [1,2,3,4,5,6,7,8,9,10, 'game']
# sum = 0
# for new_i in range(len(lst) -1):
#     sum = sum + lst[new_i]
# print(sum)
    # print(new_i)
