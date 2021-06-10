0#this will work out the missng value

V = float(input("voltage?: "))
I = float(input("current?: "))
R = float(input("resistance?: "))

def work_out_voltage():
    return (I * R)

def work_out_current():
    return (V / R)

def work_out_resistance():
    return (v / I)

if V == 0: #works out voltage
    print("your voltage is:")
    print(work_out_voltage())
elif I == 0: #works out current
    print("your current is:")
    print(work_out_current())
elif R == 0: #works out resistance
    print("your resistance is:")
    print(work_out_resistance())
