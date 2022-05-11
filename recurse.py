i=0
def fuin():
    global i
    i=i+1
    if i<=10:
        print(i)
    fuin()
fuin()