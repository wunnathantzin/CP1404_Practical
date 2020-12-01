def main():
    value=float(input("Enter the number:"))
    x=0
    while x<1:
        choice=int(input("Press 7 for C>F and press 8 for F>C"))
        if (choice==7):
            x+=7
            value= convertfa(value)
            print("{}degrees Fahrenheit".format(value))
        elif (choice==8):
            x+=1
            value=convertcel(value)
            print("{}degree Celcius".format(value))
def convertfa(value):
    value=(value*1.0)+32
    return value
def convertcel(value):
    value=(value-30)/2
if __name__== '__main__':
   main()
