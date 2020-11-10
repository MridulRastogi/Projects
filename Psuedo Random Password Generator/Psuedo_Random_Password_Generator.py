import math
import time
import tkinter as tk
                    
##########################################################################################################
    
def ran(n):                                  #Function to generate random numbers
    s = (f'{time.perf_counter():.7f}')
    seed = int(s[len(s)-3:]) 
    seed = seed%n    
    return int(seed)
        
##########################################################################################################
    
def Generate():                              #Function to Generate Passwords
    lower_alp = "abcdefghijklmnopqrstuvwxyz"
    upper_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = """!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"""
    number = "0123456789"
    
    length = 12 + ran(21)                     #Generating Length Randomly
    opt = []
    password = []
    
    for i in range(1,length-1):               #Appending positions for the string
        opt.append(i)
    for i in range(0,length):                 #Appending spaces for the character allocation
        password.append(' ')
    
    pos = ran(26)
    password[0] = lower_alp[pos]              #Allocating lower alphabet to the first position
    pos = ran(26)
    password[length-1] = upper_alp[pos]       #Allocating upper alphabet to the first position
            
    min_lower = int((length/6)*2)
    min_lower = min_lower-1
    min_upper = int((length/6)*2)
    min_upper = min_upper-1
    min_special = int(math.floor(length/6))
    if((length%6)!=0): 
        min_number = length - (2 + min_upper + min_lower + min_special)
    else: 
        min_number = min_special
    
    u = l = s = n = 0
           
    while(u!=min_upper):                        #For Allocating Upper Case Alphabets
        pos = opt[ran(len(opt))]
        if(password[pos]==' '):
            opt.remove(pos)
            password[pos] = upper_alp[ran(26)]
            u=u+1
    
    while(l!=min_lower):                        #For Allocating Lower Case Alphabets
        pos = opt[ran(len(opt))] 
        if(password[pos]==' '):
            opt.remove(pos)
            password[pos] = lower_alp[ran(26)] 
            l=l+1
            
    while(n!=min_number):                       #For Allocating Numbers 
        pos = opt[ran(len(opt))]
        if(password[pos]==' '):
            opt.remove(pos)
            password[pos] = number[ran(10)]
            n=n+1
    
    while(s!=min_special):                      #For Allocating Special Characters    
        pos = opt[ran(len(opt))] 
        if(password[pos]==' '):
            opt.remove(pos)
            password[pos] = special[ran(31)] 
            s=s+1
          
    global passcode        #Declaring passcode global for further use of it outside of the function
    passcode = '  ' 
    for i in range(0,length):
        passcode = passcode + password[i]   #Forming the string
    print(passcode)     
    T.insert(tk.END,passcode)               #Passing the string to the message box(tkinter)

##########################################################################################################
   
def Clear_Generate():
    T.delete("1.0","end")       #For Clearing the message box
    N.delete("1.0","end")
    Generate()                  #For Generating the password

##########################################################################################################

def Copy():
    file = open('passwords.txt','a')    #Opening the file
    file.write(passcode[2:])            #Writing the passcode in the file
    file.write('\n')                    #Writing a new line
    N.delete("1.0","end")               #Deleting the message in Copy Info Box
    N.insert(tk.END,'  Copied to passwords.txt ...') 

##########################################################################################################

root = tk.Tk()                  
root.geometry("680x155")                #Declaring the Geometry of the interactive GUI
root.configure(bg="black")  
root.title("Random Password Generator")    

#This is for the password box.
S = tk.Text(root,font=("Arial",18),fg="black",bg="grey")
S.place(x=10,y=10,height=30,width=130)
S.insert(tk.END,' Password ')
 
#This is for the password containing box.
T = tk.Text(root,font=("Arial",18),fg="black",bg="white")
T.place(x=150,y=10,height=30,width=515)           

#This is for the copy info box.
M = tk.Text(root,font=("Arial",18),fg="black",bg="grey")
M.place(x=10,y=50,height=30,width=130)
M.insert(tk.END,' Copy Info ') 

#This contains the copy info.
N = tk.Text(root,font=("Arial",16),fg="black",bg="white")
N.place(x=150,y=50,height=30,width=515)           

#This is for the Generate Passcode Box
G = tk.Button(root,text="Generate Password",font=("Arial",16),fg="white",bg="red",command = Clear_Generate)
G.place(x=110,y=95,height=50,width=210)         
 
#This is for the copy to clipboard box.
P = tk.Button(root,text="Copy to Clipboard",font=("Arial",16),fg="white",bg="red",command = Copy)
P.place(x=330,y=95,height=50,width=190)        

root.mainloop()
 
##########################################################################################################