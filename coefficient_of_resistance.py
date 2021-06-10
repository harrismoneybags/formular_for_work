#this will work out coefficient of resistance.

Rt = float(input("thermal resistance?: "))
R0 = float(input("resistance?: "))
temp_co = float(input("temp coefficient of resistance at same temp as R0?: "))
t = float(input("temperature change?: "))

def work_out_thermal_resistance():
    return R0*(1 + temp_co*t)

def work_out_resistance():
    return (1 + temp_co*t) / Rt

def work_out_temp_change():
    return (Rt / Ro) - 1 / temp_co

def work_out_temp_coefficient():
    return (Rt / Ro) - 1 / t


if Rt == 0: #works out thermal resistance
    print("the thermal resistance is:")
    print(work_out_thermal_resistance())
elif R0 == 0: #works out resistance
    print("the resistance is:")
    print(work_out_resistance())
elif temp_co == 0: #works out temp coefficient
    print("the temp coefficient is:")
    print(work_out_temp_coefficient())
elif t == 0: #works out the temp diffrence
    print("the temperature change is:")
    print(work_out_temp_change())
