radius_input=None
area=None

while True:
   radius_input=float(input("enter radius circle:"))
   if radius_input==0:
       break
   elif radius_input>0:
        area=radius_input*radius_input*3.141592
   elif radius_input<0:
        print("radius cannot be nagative")
   print("circle area:",area)
