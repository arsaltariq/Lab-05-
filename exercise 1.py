name=input("Enter Name:")
fname=input("Enter Father Name:")
math=int(input("Enter Mathematics Marks:"))
sci=int(input("Enter Science Marks:"))
eng=int(input("Enter English Marks:"))
gk=int(input("Enter General Knowledge Marks:"))
total=400
sub=math+sci+eng+gk
age=(sub*100)/total

def percentage():
    age=(sub*100)/total
    return age
def grade():
    if age>80:
        print("Grade A+")
    elif age>70:
        print("Grade A")
    elif age>60:
        print("Grade B")
    else:
        print("Failes")
def marksheet():
    print("Your Name:",name)
    print("Your Father Name:",fname)
    print("Your Mathematics Marks:",math)
    print("Your Science Marks:",sci)
    print("Your English Marks",eng)
    print("Your General Knowledge Marks:",gk)
    print("Total Score:",sub)
    print("Your Percentage:",percentage())
    print("Your Grade:",grade())
