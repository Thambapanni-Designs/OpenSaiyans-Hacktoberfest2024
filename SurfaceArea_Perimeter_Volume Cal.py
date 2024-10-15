#Initializing varibales
length = 0
width = 0
height = 0

#input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

#Calculation
surface_area = 2*((length * width )+ (width * height)+ (length * height) )
perimeter = 2*(width*length)
volume = width*length*height

#output
print("Surface area is: ",surface_area)
print("Perimeter is: ",perimeter)
print("Volume is: ",volume)
