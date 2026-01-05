sub1=int(input("Enter mark of First subject:"))
sub2=int(input("Enter mark of Second subject:"))
sub3=int(input("Enter mark of Third subject:"))
sub4=int(input("Enter mark of Fourth subject:"))
sub5=int(input("Enter mark of Fifth subject:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("Grade A")
elif(avg>=80):
    print("Grade B")
elif(avg>=70):
    print("Grade C")
elif(avg>=60):
    print("Grade D")
else:
    print("Grade F")