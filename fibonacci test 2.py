#test fibonacci sequence


import time

print("Behold...")
time.sleep(2)
print("Pumbas fantastic fibonacci sequence!")
time.sleep(2)

x = 0
x_inc = 1
counter = 1
while counter < 30:
    print (x)
    counter = counter + 1
    x_hold = x
    x = x_inc
    x_inc = x_inc + x_hold
    time.sleep(0.5)



    #prints 0
    # sets x to 1
    # sets x inc to 2

    #prints 1
    #sets x eual to 2
    #sets x inc to 3

    #prints 2
    #sets x equal to 3
    #sets x inc equal to 5

    #prints 3
    #sets x equal to 5
    #sets x inc equal to 8
