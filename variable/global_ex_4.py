x = "awesome"


def myFunc():
    global x
    print("Pyrhon is " + x)
    x = "fantastic"


myFunc()
print("Pyrhon is " + x)