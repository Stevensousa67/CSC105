import pickle


class Person:

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


myperson = Person("Steven", 22)
print(myperson)
outfile1 = open("Steven.txt", 'wb')
pickle.dump(myperson, outfile1)
outfile1.close()

infile1 = open('Steven.txt', 'rb')
person2 = pickle.load(infile1)
infile1.close()
print(person2.getName(), person2.getAge())

# Create dictionary object
classRec = {}
classRec[1234] = ['Fred', 'Smith', 3.2, 'CS', 2021]
classRec[1235] = ['Mary', 'Jones', 3.3, 'CS', 2020]

# Print contents
print(classRec)

# Open an outfile for binary write and dump the object
outfile = open('myFile.txt', 'wb')
pickle.dump(classRec, outfile)
outfile.close()

# open the file for binary read and load the object into a new variable
infile = open('myFile.txt', 'rb')
classRec2 = pickle.load(infile)

# Print contents of loaded dictionary at a key
print(classRec2.get(1235))
