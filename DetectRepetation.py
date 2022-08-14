import csv
with open('kbcQuestion.csv', 'r') as file:
    reader1 = csv.reader(file, delimiter=";")
    questions=[]
    i=0
    j=0
    k=0
    for row in reader1:
        questions.append(row[0])
    for row in questions:
        count=-1
        i+=1
        for x in questions:
            j+=1
            if row == x:
                count+=1
                k+=1
        if count>0:
            print("At Line ",i," ",row)
    print("i:",i,"j:",j,"k:",k)