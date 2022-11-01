import time
def countdown(n):
    if (n==0):
        print("Boom!")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

a=int(input("Enter a Limit:"))
countdown(a)