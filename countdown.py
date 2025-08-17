def countdown(n):
    if n == 0:
        return
    print("entering " + str(n))
    countdown(n - 1)
    print("returning from " + str(n))


countdown(5)
