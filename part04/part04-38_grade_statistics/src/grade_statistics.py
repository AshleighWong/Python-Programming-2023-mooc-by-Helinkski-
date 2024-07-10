# Write your solution here

def exam_points(total_points: int):
    zero=0
    one=0
    two=0
    three=0
    four=0
    five = 0
    for x in total_points:
        if x >= 0 and x < 15:
            zero += 1
        elif x < 18:
            one +=1
        elif x < 21:
            two+=1     
        elif x < 24:
            three+=1
        elif x < 28:
            four +=1
        elif x < 31:
            five +=1
    print(" 5:", "*"*five)
    print(" 4:", "*"*four)
    print(" 3:", "*"*three)
    print(" 2:", "*"*two)
    print(" 1:", "*"*one)
    print(" 0:", "*"*zero)


def grade_input():
    grade_list = []
    while True:
        grades = input("Exam points and exercises completed: ")
        if grades == "":
            break
        
        entry = grades.split()
        entry1 = int(entry[0])
        entry2 = int(entry[1]) // 10
        grade_list.append(entry1)
        grade_list.append(entry2)
    return grade_list


def total(grade_list:list):
    total_list = []
    for i in range(0, len(grade_list), 2):
        total = grade_list[i] + grade_list[i+1]
        total_list.append(total)
    return total_list


def average(total_list):
    sums = 0
    for x in total_list:
        sums += x
    
    average = sums / len(total_list)  
    return average

    
def passed(grade_list:list):
    fail1 = 0
    total_list = []
    total_list = total(grade_list)
    for x in total_list:
        if x <=14:
            fail1 +=1
    
    fail2=0
    for i in range(0, len(grade_list), 2):
        if grade_list[i] < 10:
            fail2 +=1

    if fail1 == 0 and fail2 !=0:
        total_failed = fail2
    else:       
        total_failed = (fail1 + fail2) - fail2
    passing = (len(total_list) - total_failed) / len(total_list)
    return round(passing * 100.0, 1)
            

def main():
    x = grade_input()
    y = total(x)
    z = average(y)
    w = passed(x)
    print("Statistics: ")
    print(f"Points average: {z}")
    print(f"Pass percentage: {w}")
    print("Grade distribution:")
    exam_points(y)    
    

main()
# x = grade_input()
# print(x)
# y= total(x)
# print(total(x))
# exam_points(y)
# z = average(y)
# w = passed(x)
# print(w)
# print(z)