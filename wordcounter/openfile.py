#code to open an input file for reading
#user will be prompted to provide file including path
#fname variable will hold the user input

def openfile():
    fname = input("Enter filename including path: ")
    #uncomment below for debugging
    #filename and path should look like C:\\TestData\<filename>
    #print("Filename and path is: " + fname)

    fin = open(fname)

    return fin
    #print(fin.read())