fh = open('output.txt','w')
year = int(input("Enter the Year : "))
fh.write("year is "+str(year)+'\n')

if (year % 4 == 0 and year % 100 != 0 or year % 400 != 0):
    fh.write("It's a leap year "+'\n')
else:
    fh.write("It's NOt a Leap year"+'\n')
