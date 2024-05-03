def collinear():
    x1 = int(input("Enter x1 coordinate : "))
    y1 = int(input("Enter y1 coordinate : "))
    x2 = int(input("Enter x2 coordinate : "))
    y2 = int(input("Enter y2 coordinate : "))
    x3 = int(input("Enter x3 coordinate : "))
    y3 = int(input("Enter y3 coordinate : "))
    a = (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))==0
    print(a)
collinear()