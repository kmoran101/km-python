import openfile

fin = openfile.openfile()

#read one line at a time
for line in fin:

    #split the line into words delimited by spaces
    for word in line.split():

        #display the individual words
        print(word.lower().rstrip(",."))