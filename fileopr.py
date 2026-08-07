file=open("fileopr.txt","r")
content=file.read()
print(content)
file.close()


#file=open("fileopr.txt","r")
#content=file.readlines()
#print(content)
#file.close()

with open("fileopr.txt","r") as file:
    print(file.read())
  