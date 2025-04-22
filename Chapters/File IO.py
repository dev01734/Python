"""Two types of Files: Text Files(.txt), Binary Files(.mp4, .jpg)"""
 
'''Read From a File : Open a file, read what is present in it and then close it'''
# f=open("file.txt")        #Opens that file
# print(f.read())           #reads the text present in that file
# f.close()                 #closes that file after work is done

'''Writes to a file :'''
# string = "Hey Dev you are soo goood"
# f=open("files.txt", "w")
# f.write(string)
# f.close()

'''Readline & Readlines'''
# f=open("file.txt")  
# lines=f.readlines()                   # To print multiple lines at a time 
# print(lines, type(lines))

# f=open("file.txt")  
# line1=f.readline()                      # To print single line at a time
# print(line1, type(line1))
# line2=f.readline()
# print(line2, type(line2))
# line3=f.readline()
# print(line3, type(line3))
# f.close()

'''OR Readline in other format'''
# f=open("file.txt")  
# line=f.readline()
# while(line != ""):
#     print(line)
#     line= f.readline()
# f.close()

'''With Statement'''
# f=open("file.txt")        
# print(f.read())           
# f.close()        
'''Same Can be written using 'With' Statement'''
# with open("file.txt") as f:
#     print(f.read())                 #here you dont have to close the file


