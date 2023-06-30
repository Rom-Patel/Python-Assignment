# Create a function named ds with parameters roll_no and name.
# Add those parameters in the following data structures:
# list, tuple, sets and dictionaries

def ds(roll_no,name):
    global List 
    global Tuple
    global Set
    global Dictionary
    List=[roll_no,name]
    Tuple=(roll_no,name)
    Set={roll_no,name}
    Dictionary={"Roll no.": roll_no , "Name":name}


def printds():
   
    print("\nList       : ",List,"\n")
    print("Tuple      : ",Tuple,"\n")
    print("Set        : ",Set,"\n")
    print("Dictionary : ",Dictionary,"\n")

#After adding values change the values during runtime
def dsUpdate():
   print("Updating Data Structures :-\n")
   rn=int(input("Enter the roll no : "))
   nm=input("Enter the name    : ")
   ds(rn,nm)
   List.append("CO-Batch-1")
   Set.add("SYCO-A")
   Dictionary["Language"]="Python"           
   Dictionary.update({"Class":"SYCO-A"})

# Driver code:-
ds(14,"Rom Patel")
printds()
dsUpdate()
printds()

#Delete these data structures
del List
del Tuple
del Set
del Dictionary