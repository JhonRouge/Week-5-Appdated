#if demo

sub1grade = (input("Enter grade for subject 1: "))
sub2grade = (input("Enter grade for subject 2: "))
sub3grade = (input("Enter grade for subject 3: "))
sub4grade = (input("Enter grade for subject 4: "))
sub5grade = (input("Enter grade for subject 5: "))

ave = int(sub1grade + sub2grade + sub3grade + sub4grade + sub5grade) / 5

print(f"Your average grade is {ave}")

if ave >= 90:
    print("You passed!")
elif ave >= 70:
    print("You failed")
else:
    print("You failed")