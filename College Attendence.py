# Teacher Registration:===============================================================================================

def Teacher():
    global store
    
    print("Welcome In  Teacher Registration Form")
    a=input("Enter Your Name: ")
    b=input("Enter Your Last Name: ")
    c=input("Enter Your E-Mail: ")
    #d=input("Enter Your PhoneNumber: ")
    e=input("Enter Your UserName: ")
    f=input("Enter Your Password: ")
    store={"Name":a,"Last Name":b,"E-Mail":c,"UserName":e,"Password":f}
    
# Admin:==============================================================================================================

 
def admin():

    a=input("Enter UserName: ")
    b=input("Enter Password: ")
    if a=='admin' and b=='admin12345':
        print("\nWelcome Admin:")
        infor()
        
    else:
        print("Try Again: ")
        admin()

        
# Infor:===============================================================================================================        

def infor():
    print("\n1. Teacher Registration    2. Attendence   3.Logout")
    cho=input("Choose The Option: ")
    if cho=="1":
        #print("Welcome in Teacher Registration:")
        Teacher()
        infor()
    elif cho=="2":
        #print("Welcome in Attendence:")
        bhanu()
        #attendence()
        #diploma()
        infor()
    elif cho=="3":
        Logout()
    else:
        print("Try Again:")
        infor()
            
# Login Information:========================================================================================================        

def Login():
    

    
    print("Welcome To Teacher's Login:")


    global user,passs

    user=input("Enter Your UserName: ")
    passs=input("Enter Your Password: ")
    if user==store["UserName"] and passs==store["Password"]:
        print("Welcome in Attendence " + store["Name"])
    else:
        print("Something is wrong Try again:")
        Login()

# Logout:========================================================================================================================       

def Logout():
    option()

# Attendence:====================================================================================================================

def attendence():
    global attendence
    
    print("\nWelcome To VIVEKANANDA COLLEGE OF TECHNOLOGY OF MANAGEMENT: ")

    print("Choose Your Branch & Course For Attendence: ")
    a=("[1]. Diploma  [2]. B.tech  [3]. M.tech  [4]. MBA  [5]. B.ed   [6]. Logout")
    print(a)
    cho=input("Choose The Course: ")
    for x in cho:
        if x=='1':
            print("Welcome In Diploma Course ")
            diploma()
        elif x=='2':
            print("Welcome In B.tech Course ")
            btech()
        elif x=='3':
            print("Welcome In M.tech Course ")
            mtech()
        elif x=='4':
            print("Welcome To MBA Course ")
            mba()
        elif x=='5':
            print("Welcome To B.ed Course ")
            bed()
        elif x=='6':
            Logout()
         
        else:
            print("Try Again:")
            infor()
            
# Diploma Class:====================================================================================================================

def diploma():
    global diploma
    
    print("[1].Computer Science  [2].Electrical ")
    a=input("Choose the Branch: ")
    if a=='1':
        print("Welcome To Computer Science Branch To Take Attendence:")
                
        print("1. Ist year   2. IInd year  3. IIIrd year")
        b=input("Choose The Year:")
        if b=='1':
            print("Welcome To Attendence in Ist Year:")
            Ist()
            
        elif b=='2':
            print("Welcome To Attendence in IInd Year:")
            IInd()
        elif b=='3':
            print("\nWelcome To Attendence in IIIrd Year:")
            
            IIIrd()
        else:
            print("Try Again:")
            diploma()
    elif a=='2':
        print("Welcome To Electrical Branch To Take Attendence:")

        print("1. Ist year   2. IInd year   3. IIIrd year")
        b=input("Choose The Year:")
        if b=='1':
            print("Welcome To Attendence In Ist Year:")
            ElectI()
        elif b=='2':
            print("Welcome To Attendence In IInd Year:")
            electII()
        elif b=='3':
            print("Welcome To Attendence In IIIrd Year:")
            pass
        else:
            print("Try Again:")
            diploma()
        

        
    else:
        print("Something is wrong Try Again:==)")
        attendence()

        
# Elect Ist Year:=====================================================================================================
def ElectI():
    print('''1. Rakesh Kumar   2. Ram Pratap Singh   3. Ashish Sharma   4. Vini Varshney   5. Harish Singh
6. Pooja Sharma   7. Vipul Chaudhary   8. Sonal Verma   9. Kaju Singh   10. Vinaaa Gupta ''')

    print("\n1. Rakesh Kumar")
    a=input("Select no.:")
    if a=="1":
        ans1="yes"
    else:
        ans1="no"

    print("2. Ram Pratap Singh")
    b= input("Select no.:")
    if b=="2":
        ans2="yes"
    else:
        ans2="no"

    print("3. Ashish Sharma")
    c=input("Select no.:")
    if c=="3":
        ans3="yes"
    else:
        ans3="no"

    print("4. Vini Varshney")
    d=input("Select no.:")
    if d=="4":
        ans4="yes"
    else:
        ans4="no"

    print("5. Harish Singh")
    e=input("Select no.:")
    if e=="5":
        ans5="yes"
    else:
        ans5="no"

    print("6. Pooja Sharma")
    f=input("Select no:")
    if f=="6":
        ans6="yes"
    else:
        ans6="no"

    print("7. Vipul Chaudhary")
    g=input("Select no.:")
    if g=="7":
        ans7="yes"
    else:
        ans7="no"
    print("8. Sonal Verma")
    h=input("Select no.:")
    if h=="8":
        ans8="yes"
    else:
        ans8="no"
    print("9. Kaju Singh")
    i=input("Select no.:")
    if i=="9":
        ans9="yes"
    else:
        ans9="no"
    print("10. Vinaaa Gupta")
    j=input("Select no.:")
    if j=="10":
        ans10="yes"
    else:
        ans10="no"


    
    mylist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
    aaa=[]
    ccc=[]
    for x in mylist:
        if x=="yes":
            aaa.append(x)
        elif x=="no":
            ccc.append(x)
            
    global ae,be
    ae=len(aaa)
    be=len(ccc)

    
    print("Total No. of Present Student is : " , len(aaa))
    print("Total No. of Absent Student is : " , len(ccc))
    attendence()
    

def electII():
    global electII

    print('''1. Rakesh Kumar   2. Ram Pratap Singh   3. Ashish Sharma   4. Vini Varshney   5. Harish Singh
6. Pooja Sharma   7. Vipul Chaudhary   8. Sonal Verma   9. Kaju Singh   10. Vinaaa Gupta ''')

    print("\n1. Rakesh Kumar")
    a=input("Select no.:")
    if a=="1":
        ans1="yes"
    else:
        ans1="no"

    print("2. Ram Pratap Singh")
    b= input("Select no.:")
    if b=="2":
        ans2="yes"
    else:
        ans2="no"

    print("3. Ashish Sharma")
    c=input("Select no.:")
    if c=="3":
        ans3="yes"
    else:
        ans3="no"

    print("4. Vini Varshney")
    d=input("Select no.:")
    if d=="4":
        ans4="yes"
    else:
        ans4="no"

    print("5. Harish Singh")
    e=input("Select no.:")
    if e=="5":
        ans5="yes"
    else:
        ans5="no"

    print("6. Pooja Sharma")
    f=input("Select no:")
    if f=="6":
        ans6="yes"
    else:
        ans6="no"

    print("7. Vipul Chaudhary")
    g=input("Select no.:")
    if g=="7":
        ans7="yes"
    else:
        ans7="no"
    print("8. Sonal Verma")
    h=input("Select no.:")
    if h=="8":
        ans8="yes"
    else:
        ans8="no"
    print("9. Kaju Singh")
    i=input("Select no.:")
    if i=="9":
        ans9="yes"
    else:
        ans9="no"
    print("10. Vinaaa Gupta")
    j=input("Select no.:")
    if j=="10":
        ans10="yes"
    else:
        ans10="no"


    
    mylist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
    aap=[]
    ccp=[]
    for x in mylist:
        if x=="yes":
            aap.append(x)
        elif x=="no":
            ccp.append(x)
            
    global aae,bbe
    aae=len(aap)
    bbe=len(ccp)

    
    print("Total No. of Present Student is : " , len(aap))
    print("Total No. of Absent Student is : " , len(ccp))
    attendence()
    
# 1st Year:============================================================================================================
def Ist():
    global Ist

    print('''1. Ramesh Kumar   2. Lakhan Pratap Singh   3. Ashish Sharma   4. Vanshika Varshney   5. Harish Singh
6. Pooja Sharma   7. Vipul Chaudhary   8. Sonal Verma   9. Kaju Singh   10. Vinaaa Gupta ''')

    print("\n1. Ramesh Kumar")
    a=input("Select no.:")
    if a=="1":
        ans1="yes"
    else:
        ans1="no"

    print("2. Lakhan Pratap Singh")
    b= input("Select no.:")
    if b=="2":
        ans2="yes"
    else:
        ans2="no"

    print("3. Ashish Sharma")
    c=input("Select no.:")
    if c=="3":
        ans3="yes"
    else:
        ans3="no"

    print("4. Vanshika Varshney")
    d=input("Select no.:")
    if d=="4":
        ans4="yes"
    else:
        ans4="no"

    print("5. Harish Singh")
    e=input("Select no.:")
    if e=="5":
        ans5="yes"
    else:
        ans5="no"

    print("6. Pooja Sharma")
    f=input("Select no:")
    if f=="6":
        ans6="yes"
    else:
        ans6="no"

    print("7. Vipul Chaudhary")
    g=input("Select no.:")
    if g=="7":
        ans7="yes"
    else:
        ans7="no"
    print("8. Sonal Verma")
    h=input("Select no.:")
    if h=="8":
        ans8="yes"
    else:
        ans8="no"
    print("9. Kaju Singh")
    i=input("Select no.:")
    if i=="9":
        ans9="yes"
    else:
        ans9="no"
    print("10. Vinaaa Gupta")
    j=input("Select no.:")
    if j=="10":
        ans10="yes"
    else:
        ans10="no"

    mylist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
    apss=[]
    awss=[]
    for x in mylist:
        if x=="yes":
            apss.append(x)
        elif x=="no":
            awss.append(x)

    global aa,bb
    aa=len(apss)
    bb=len(awss)

    print("Total No. of Present Student is : " , len(apss))
    print("Total No. of Absent Student is : " , len(awss))
    attendence()



    
    
    

    

    

# 2nd Year:=============================================================================================================
        
def IInd():
    global IInd

    print('''1. Bhanu Pratap Singh   2. Lakhan Singh   3. Ashish Bhardwaj   4. Anmol Varshney   5. Honey Singh
6. Pooja Sharma   7. Vipul Chaudhary   8. Sonal Verma   9. Kaju Singh   10. Vinaaa Gupta ''')

    print("\n1. Bhanu Pratap Singh")
    a=input("Select no.:")
    if a=="1":
        ans1="yes"
    else:
        ans1="no"
    print("2. Lakhan Singh")
    b= input("Select no.:")
    if b=="2":
        ans2="yes"
    else:
        ans2="no"
    print("3. Ashish Bhardwaj")
    c=input("Select no.:")
    if c=="3":
        ans3="yes"
    else:
        ans3="no"
    print("4. Anmol Varshney")
    d=input("Select no.:")
    if d=="4":
        ans4="yes"
    else:
        ans4="no"
    print("5. Honey Singh")
    e=input("Select no.:")
    if e=="5":
        ans5="yes"
    else:
        ans5="no"
    print("6. Pooja Sharma")
    f=input("Select no:")
    if f=="6":
        ans6="yes"
    else:
        ans6="no"
    print("7. Vipul Chaudhary")
    g=input("Select no.:")
    if g=="7":
        ans7="yes"
    else:
        ans7="no"
    print("8. Sonal Verma")
    h=input("Select no.:")
    if h=="8":
        ans8="yes"
    else:
        ans8="no"
    print("9. Kaju Singh")
    i=input("Select no.:")
    if i=="9":
        ans9="yes"
    else:
        ans9="no"
    print("10. Vinaaa Gupta")
    j=input("Select no.:")
    if j=="10":
        ans10="yes"
    else:
        ans10="no"

    mylist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
    aps=[]
    aws=[]
    for x in mylist:
        if x=="yes":
            aps.append(x)
        elif x=="no":
            aws.append(x)

    global za,ax
    za=len(aps)
    ax=len(aws)

            
    print("Total No. of Present Student is : " , len(aps))
    print("Total No. of Absent Student is : " , len(aws))
    attendence()


# 3rd Year:======================================================================================================================
    
def IIIrd():
    global IIIrd
    print('''1. Bhanu Pratap Singh   2. Lakhan Singh   3. Ashish Bhardwaj   4. Anmol Varshney   5. Honey Singh
6. Pooja Sharma   7. Kanishka Singh   8. Trived Bhardwaj   9. Aman Saxena   10. Sahil Bhardwaj''')
    
    print("\n1. Bhanu Pratap Singh")
    a=input("Select no.:")
    if a=="1":
        ans1="yes"
    else:
        ans1="no"
    print("2. Lakhan Singh")
    b= input("Select no.:")
    if b=="2":
        ans2="yes"
    else:
        ans2="no"
    print("3. Ashish Bhardwaj")
    c=input("Select no.:")
    if c=="3":
        ans3="yes"
    else:
        ans3="no"
    print("4. Anmol Varshney")
    d=input("Select no.:")
    if d=="4":
        ans4="yes"
    else:
        ans4="no"
    print("5. Honey Singh")
    e=input("Select no.:")
    if e=="5":
        ans5="yes"
    else:
        ans5="no"
    print("6. Pooja Sharma")
    f=input("Select no:")
    if f=="6":
        ans6="yes"
    else:
        ans6="no"
    print("7. Kanishka Singh")
    g=input("Select no.:")
    if g=="7":
        ans7="yes"
    else:
        ans7="no"
    print("8. Trived Bhardwaj")
    h=input("Select no.:")
    if h=="8":
        ans8="yes"
    else:
        ans8="no"
        
    print("9. Aman Saxena")
    i=input("Select no.:")
    if i=="9":
        ans9="yes"
    else:
        ans9="no"
        
    print("10. Sahil Bhardwaj")
    j=input("Select no.:")
    if j=="10":
        ans10="yes"
    else:
        ans10="no"

    mylist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
    aps=[]
    aws=[]
    for x in mylist:
        if x=="yes":
            aps.append(x)
        elif x=="no":
            aws.append(x)
            
    global zx,ab
    zx=len(aps)
    ab=len(aws)

    
    print("Total No. of Present Student is : " , len(aps))
    print("Total No. of Absent Student is : " , len(aws))
    attendence()

#B.tech Class:=============================================================================================================================

def btech():
    global btech
    
    print("\n[1].Computer Science [2].Electrical [3].Mechenical [4].Civil")
    a=input("Choose The Course: ")
    if a=="1":
        print("Welcome In Computer Science Course To Take Attendence:")
        print("1. Ist year   2. IInd year   3. IIIrd year   4. IVth year")
        b=input("Choose The Year: ")
        if b=="1":
            print("Welcome To Ist Year:")
            pass
        elif b=="2":
            print("Welcome To IInd Year:")
            pass
        elif b=="3":
            print("Welcome To IIIrd Year:")
            pass
        elif b=="4":
            print("Welcome To IVth Year:")
            pass
        
    elif a=="2":
        print("\nWelcome In Electrical Course To Take Attendence:")
        print("1. Ist year   2. IInd year   3. IIIrd year   4. IVth year")
        d=input("Choose The Year: ")
        if d=="1":
            print("Welcome To Ist Year:")
            pass
        elif d=="2":
            print("Welcome To IInd Year:")
            pass
        elif d=="3":
            print("Welcome To IIIrd Year:")
            pass
        elif d=="4":
            print("Welcome To IVth Year:")
            pass
    elif a=="3":
        print("\nWelcome In Meshenical Course To Take Attendence:")
        print("1. Ist year   2. IInd year   3. IIIrd year   4. IVth year")
        a=input("Choose The Year: ")
        if a=="1":
            print("Welcome To Ist Year:")
            pass
        elif a=="2":
            print("Welcome To IInd Year:")
            pass
        elif a=="3":
            print("Welcome To IIIrd Year:")
            pass
        elif a=="4":
            print("Welcome To IVth Year:")
            pass
    elif a=="4":
        print("\nWelcome In Civil Course To Take Attendence:")
        print("1. Ist year   2. IInd year   3. IIIrd year   4. IVth year")
        a=input("Choose The Year:")
        if a=="1":
            print("Welcome To Ist Year:")
            pass
        elif a=="2":
            print("Welcome To IInd Year:")
            pass
        elif a=="3":
            print("Welcome To IIIrd Year:")
            pass
        elif a=="4":
            print("Welcome To IVth Year:")
            pass
    else:
        print("Someting Went's wrong Try Again:")
        btech()
        
        


#def bfirst():
    
    
# M.tech Class:=======================================================================================================================================
        
def mtech():
    global mtech
    
    print("[1].Computer Science [2].Electrical [3].Mechenical [4].Civil")
    a=input("Choose The Course: ")
    if a=="1":
        print("Welcome In Computer Science Course To Take Attendence:")
        print("1. Ist year   2. IInd year ")
        b=input("Choose The Year: ")
        if b=="1":
            print("Welcome To Ist Year:")
            attendence()
        elif b=="2":
            print("Welcome To IInd Year:")
            attendence()
        
    elif a=="2":
        print("\nWelcome In Electrical Course To Take Attendence:")
        print("1. Ist year   2. IInd year ")
        d=input("Choose The Year: ")
        if d=="1":
            print("Welcome To Ist Year:")
            pass
        elif d=="2":
            print("Welcome To IInd Year:")
            pass
        
    elif a=="3":
        print("\nWelcome In Mechenical Course To Take Attendence:")
        print("1. Ist year   2. IInd year ")
        d=input("Choose The Year: ")
        if d=="1": 
            print("Welcome To Ist Year:")
            pass
        elif d=="2":
            print("Welcome To IInd Year:")
            pass
        
    elif a=="4":
        print("\nWelcome In Civil Course To Take Attendence:")
        print("1. Ist year   2. IInd year ")
        d=input("Choose The Year: ")
        if d=="1":
            print("Welcome To Ist Year:")
            pass
        elif d=="2":
            print("Welcome To IInd Year:")
            pass
    else:
        print("Try Again:")
        mtech()
        
# MBA Class:=============================================================================================================================

    
def mba():
    global mba
    pass

# B.ED Class:=============================================================================================================================

def bed():
    global bed
    
    #print("[1].Hindi [2].History [3].Science [4].Math")
    pass

# Select The Option:======================================================================================================================

def option():
    print("\t\t|===============|")
    print("\t\t|Software V 1.0 |")
    print("\t\t|               |")
    print("\t\t|               |")
    print("\t\t|               |")
    print("\t\t|===============|\n")
    print("[1]. Admin:      [2]. Teacher Login Form: ")
    a=input("Select the option: ")
    for x in a:
        if x=='1':
            admin()
            #Teacher()
            #attendence()    
            #Logout()

        elif x=='2':
            #print("Welcome in Teacher Login Form: ")
            Login()
            attendence()
        else:
            print("Try Again:")
            option()
# Total Number Of Student:==================================================================================================================

def diploma1():
    global diploma
    
    print("[1].Computer Science  [2].Electrical ")
    a=input("Choose the Branch: ")
    if a=='1':
        print("Welcome To Computer Science Branch To Take Attendence:")
                
        print("1. Ist year   2. IInd year  3. IIIrd year")
        b=input("Choose The Year:")
        if b=='1':
            print("\nWelcome To Present & Absent Student's in Ist Year:")
            showww()
        elif b=='2':
            print("\nWelcome To Present & Absent Student's in IInd Year:")
            showw()
        elif b=='3':
            print("\nWelcome To Present & Absent Student's in IIIrd Year:")
            
            show()
        else:
            print("Try Again:")
            diploma1()
    elif a=='2':
        print("Welcome To Electrical Branch To Take Attendence:")

        print("1. Ist year   2. IInd year   3. IIIrd year")
        b=input("Choose The Year:")
        if b=='1':
            print("Welcome To Attendence In Ist Year:")
            Istelect()
        elif b=='2':
            print("Welcome To Attendence In IInd Year:")
            IIndelect()
        elif b=='3':
            print("Welcome To Attendence In IIIrd Year:")
            pass
        else:
            print("Try Again:")
            diploma1()
        

        
    else:
        print("Something is wrong Try Again:==)")
        diploma1()
# Present Student's:=========================================================================================================
def Istelect():
    aa=ae
    print("Total Present Student is :",aa)
    bb=be
    print("Total Absent Student is :",bb)

def IIndelect():
    awq=aae
    print("Total Present Student is :",awq)
    aqw=bbe
    print("Total Absent Student is:",aqw)
    
def showww():
    a=aa
    print("Total Present student is :",a)
    b=bb
    print("Total Absent Student is :",b)



def showw():
    a=za
    print("Total Present Student is :",a)
    b=ax
    print("Total Absent Student is :",b) 

    

def show():
    xq=zx
    print("Total Present Student is :",xq)
    xa=ab
    print("Total Absent Student is :",xa)

# Admin:======================================================================================================================


def bhanu():
      print("\nWelcome To VIVEKANANDA COLLEGE OF TECHNOLOGY OF MANAGEMENT: ")
      print("Choose Your Branch & Course For Attendence: ")
      a=("[1]. Diploma  [2]. B.tech  [3]. M.tech  [4]. MBA  [5]. B.ed   [6]. Logout")
      print(a)
      cho=input("Choose The Course: ")
      for x in cho:
          if x=='1':
              print("Welcome In Diploma Course ")
              diploma1()
              
          elif x=='2':
              print("Welcome In B.tech Course ")
              btech()
          elif x=='3':
              print("Welcome In M.tech Course ")
              mtech()
          elif x=='4':
              print("Welcome To MBA Course ")
              mba()
          elif x=='5':
              print("Welcome To B.ed Course ")
              bed()
          elif x=='6':
              Logout()
         
          else:
              print("Try Again:")
              infor()
    
option()






























    

