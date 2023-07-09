#file_handaling_seek.py

file = open("/home/abhijit/Python_mca/demo.txt","r")

#move the pointer till specific position
file.seek(50)

#tell() tells the current position of cursor
print(file.tell())
print(file.read())
print(file.tell())