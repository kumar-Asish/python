light=input("Enter the light color:: ")
light=light.lower()
if(light=="red"):
    print("Stop the car")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("Look")
else:
    print("Unknown light color")
