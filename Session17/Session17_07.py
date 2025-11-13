#file=None
#try:
    #print("Opened...")
    #file=open("student.txt","wt")
    #file.write("salam")
    #1/0
#except:
    #print("Error...")
#finally:
 #   if file:
  #      file.close()
   #     print("Closed...")

with open("student.txt","wt") as file:
    print("Opened...")
    file.write("Salam")
    #file.close() دیگه نیاز نیس بنویسیم و خودش اتوماتیک بسته میشود
print("Continue...")