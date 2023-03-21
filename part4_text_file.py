# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1870096
# Date: 10/04/2022

p=0 #pass_credit
d=0 #defer_credit
f=0 #fail_credit

def Staff_ver_txt():
    global p
    global d
    global f

    progress=[]
    trailer=[]
    retriever=[]
    exclude=[]
    
    credit= [0, 20, 40, 60, 80, 100, 120]
    level=[progress,trailer,retriever,exclude]
    run=0
    v=0
    u=0
    
    marks=[]
    output=[]
    
    x=True
    while x:
        while True:                  #input data for p,d,f and check
            try:
                p=int(input("\nEnter your total PASS creadits : "))
            except ValueError:
                print("Integer required")
            else:
                if p not in credit:
                    print("Out of range")
                elif p in credit:
                    break
        while True:
            try:
                d=int(input("Enter your total DEFER creadits : "))
            except ValueError:
                print("Integer required")
            else:
                if d not in credit:
                    print("Out of range")
                elif d in credit:
                    break

        while True:
            try:
                f=int(input("Enter your total FAIL creadits : "))
            except ValueError:
                print("Integer required")
            else:
                if f not in credit:
                    print("Out of range")
                elif f in credit:
                    break
        
        while True:
            if p+d+f !=120: #check total
                print("Total Incorrect\n")
                break
            elif p+d+f==120:
                if p==120:
                    print("Progress\n")#Progress
                    progress.append(0)
                    output.append("Progress")
                    break
                elif p==100:
                    print("Progress (module trailer)\n") #Progress(module trailer)
                    trailer.append(0)
                    output.append("Progress (module trailer)")
                    break
            
                elif f==80 or f==100 or f==120:
                    print("Exclude\n") #Exclude
                    exclude.append(0)
                    output.append("Exclude")
                    break
                
                else:
                    print("Module retriever\n") #Module retriever
                    retriever.append(0)
                    output.append("Module retriever")
                    break
        marks.append([p,d,f])
        
        while True:
            run=input("Would you like to enter anothr set of data ?\nEnter 'y' for yes or 'q' to quit and view results : ")
            if run=="y":
                x=True
                break
            elif run=="q":
                x=False
                print("\n-----------------------------------------------------")
                print("\nHorizontal Histogram") #Horizontal Histogram
                print("Progress ",len(progress),  ":", "*"*len(progress))
                print("Trailer  ",len(trailer),    ":", "*"*len(trailer))
                print("Retriever",len(retriever),":", "*"*len(retriever))
                print("Exclude  ",len(exclude),    ":", "*"*len(exclude))

                total=len(progress)+len(trailer)+len(retriever)+len(exclude)
                print("\n")
                print(total, "outcomes in total.\n") #Total outcomes
                print("------------------------------------------------------")

                print("\nVertical Histogram\n") #Vertical Histogram
        
                print("Progress",len(progress),"|",
                      "Trailer",len(trailer),"|",
                      "Retriever", len(retriever),"|",
                      "Exclude",len(exclude))

                for a in range(total):
                        for b in level:
                            if len(b) > 0:
                                print("    ", "*", "    ", end="  ")
                                b.pop()
                            else:
                                print("    ", " ", "    ", end="  ")
                        print()
                print("------------------------------------------------------")
                
                f=open("Data_File.txt","w") #writing a Text file
                for item in output:
                    f.write((item) + " - " + (str(marks[v])[1:-1]) + "\n")
                    v=v+1 
                f.close()

                f=open("Data_File.txt","r") #reading a Text file
                print(f.read())

                print("------------------------------------------------------\n")

                break
            else:
                print("Please Enter 'y' or 'q'\n")
#Staff_ver_txt()

def program_part4():
    while True:
        print("Enter '1' for Staff Version (Text File)")
        print("Enter 'q' for Quit")
        option=input("\nPlease Enter the option [1/q] : ")

        if option=="1":
                print("\n--- Staff Version (Text File) ---")
                Staff_ver_txt() #calling function
            
        elif option=="q":
            quit()
        
        elif option!="1" or "q":
            print("Invalide Optin. Please enter again.\n")

program_part4()

    
    
 
