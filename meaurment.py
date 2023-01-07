
def measurment():
    
        
    print("choose which measurement you need to calculate")
    print("1.Centimeter to Inces")
    print("2.Inces to Centimeter")
    print("3.Feet to Inches")
    print("4.Inches to Foot")
    print("5.Meter to Inches")
    print("6.Inches to Meter")
    to_convert = int(input("To choose Enter a number"))
    if to_convert==1:
        value = int(input("Enter value to convert : "))
        cm_to_inch =value*0.393701
        print(cm_to_inch)
      
    elif to_convert==2:
        value=int(input("Enter value to convert : "))
        inch_to_cm = value*2.54
        print(inch_to_cm)
      
    elif to_convert==3:
        value=int(input("Enter value to convert : "))
        feet_to_inches=value*12
        print(feet_to_inches)

    elif to_convert==4:
        value=int(input("Enter value to convert : "))
        inches_to_feet = value*0.0833333
        print(inches_to_feet)
      
    elif to_convert==5:
        value=int(input("Enter value to convert : "))
        meter_to_inches = value*39.3701
        print(meter_to_inches)
      
    elif to_convert==6:
        value=int(input("Enter value to convert : "))
        inches_to_meter = value*0.0254
        print(inches_to_meter)
      
    elif to_convert==6:
        value=int(input("Enter value to convert : "))
      
    else:
        print("Invalid number")
measurment()

while True:        
    status = (input("do you want to continue? Yes/No:"))    
    if status.lower=="yes":
        measurment()
        continue
    else:
        break

    

