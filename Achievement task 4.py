#Function temp defined for calculation and printing of the output
def temp():
  print(" Please Enter the temprature")
  temprature=float(input())
  print(" Please Select the Unit of the temprature \n \t1.Celsius \n \t2.Farenhite")
  unit=int(input())
  if unit==1:
    temprature=(temprature*9/5) + 32
    print("Temprature in Farenhite is : ")
    print(int(temprature)) 
  elif unit==2:
    temprature=(temprature-32)*5/9
    print("Temprature in Celsius is :")
    print(int(temprature))
  else :
    print("Incorrect selection")
#Speed function defined for the speed Convertor and printing the output
def speed():
  print(" Please Enter the speed to be converted")
  speedy=float(input())
  print(" Please Enter the unit of speed \n \t1.KMPH \n \t2.MPH")
  unit=float(input())
  if unit==1:
    speedy=0.6214*speedy
    print("Speed in mph is:")
    print(speedy)
  elif unit==2:
    speedy=speedy/0.6214
    print("Speed in kph is:")
    print(int(speedy))
#Asking the user what they want to calculate
print("Please enter what you want to convert 1.Temprature 2.Speed")
Choice=int(input())
if Choice==1:
  print("Hello, Welcome to the Temprature Converter")
  temp()
elif Choice==2:
  print("Hello, Welcome to the Speed Converter")
  speed()
else :
  print("Incorrect Choice")