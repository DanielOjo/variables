#Daniel Ogunlana
#23/09/2014
#Assignment Statement Spot Check

shape_Width= int(input("Please enter the Width of the shape:"))
shape_Length= int(input("Please enter the Length of the shape:"))
shape_Depth= int(input("Please enter the Depth of the shape:"))

mainSectionVolume= shape_Width*shape_Length*shape_Depth

circle_Radius= shape_Width/2
circleArea= 3.14*circle_Radius**2

halfCircleVolume= (circleArea/2)*shape_Depth

poolVolume= mainSectionVolume+halfCircleVolume

print("The Volume of the pool is {0}".format(poolVolume))


