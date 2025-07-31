area = input("whose area you want to calculate  : ")

if area.lower()  == "rectangle" :
    lenth = int(input("Enter lenth : "))
    breadth = int(input("Enter breadth : "))
    print("Area is : ",lenth*breadth)

elif area.lower() == "square":
    side = int(input("Enter side : "))
    
    print("Area is : ",side*side)

elif area.lower()  == "triangle" : 
    height = int(input("Enter height : "))
    base = int(input("Enter base : "))
    print("Area is : ", 0.5*height*base)

elif area.lower() == "circle":
    radius = int(input("Enter radius : "))
    print("Area is : ",2*3.17*radius*radius)






else:
    print("sorry!!! we have no idea about this")