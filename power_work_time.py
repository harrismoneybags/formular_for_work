#this works out the power, elapsed time or work

P = (float(input("what's the power?: ")))
W = (float(input("what's the work?: ")))
T = (float(input("what's the time elapsed?: ")))

def work_out_power():
    return W / T

def work_out_elapsed_time():
    return W / P

def work_out_work_done():
    return P * T

if P == 0: #works out voltage
    print("your voltage is:")
    print(work_out_power())
elif W == 0: #works out current
    print("your current is:")
    print(work_out_elapsed_time())
elif W == 0: #works out power
    print("your power is:")
    print(work_out_work_done())
