#works out the missing value

P = float(input("What's the power in watts?: "))
I = float(input("What's the current?: "))
V = float(input("What's the voltage?: "))

def work_out_power():
    return V * I

def work_out_current():
    return P / V

def work_out_voltage():
    return P / I

if V == 0: #works out voltage
    print("your voltage is:")
    print(work_out_voltage())
elif I == 0: #works out current
    print("your current is:")
    print(work_out_current())
elif R == 0: #works out power
    print("your power is:")
    print(work_out_power())
