hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if(h < 40):
    pay = h*r #ชั่วโมงน้อยกว่า 40 ชั่วโมง
    print("Your Pay:",pay)

elif(h>40):
    pay = ((40*r)+(1.5*r*(h-40)))
    print("Your Pay:",pay)

else:
    print("error! Please enter number")
