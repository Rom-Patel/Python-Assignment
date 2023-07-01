#Create a function with a default parameter "file" storing the file path
def data_opr(roll_no, name, class_name, file="assign_7.txt"):
    try:
#Open the "file" in append mode
        with open(file, "a") as f:
#Use writelines() method to add your roll number, name, and class
            f.writelines([f"\nRoll Number: {roll_no}", f"\nName: {name}", f"\nClass: {class_name}"])
    except IOError as e:
        print("An error occurred while opening or writing to the file:", str(e))
    else:
        try:
            with open(file, "r") as f:
#Use readines() method to print your data in the prompt
                print(f.readlines())
        except IOError as e:
            print("An error occurred while reading the file:", str(e))

data_opr("14", "Rom Patel", "CO-A")
