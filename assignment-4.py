
#Break statement
a="hello"
print("\nBreak statement")
for i in a:
    if i=="o":
        break
    else:
        print(i)


#Continue statement
a="world"
print("\nContinue statement")
for i in a:
    if i=="l":
        continue
    else:

        print(i)


#Pass statement
a="Python"
print("\nPass statement")
for i in a:
    if i=="y":
        pass
    else:
        print(i)


#FOR LOOP - Pass statement with else
a="coder"
print("\nFOR LOOP - Pass statement with else")
for i in a:
    if i=="c":
        pass
    else:
        print(i)
else:
    print("This has pass")


#FOR LOOP - Break statement with else
a="hello"
print("\nFOR LOOP - Break statement with else")
for i in a:
    if i=="l":
        break
    else:
        print(i)
else:
    print("This has break")


#FOR LOOP - Continue statement with else
a="world"
print("\nFOR LOOP - Continue statement with else")
for i in a:
    if i=="r":
        continue
    else:
        print(i)
else:
    print("This has continue")


#WHILE LOOP - Break statement with else
i=0
print("\nWHILE LOOP - Break statement with else")
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1
else:
    print("This has break")


