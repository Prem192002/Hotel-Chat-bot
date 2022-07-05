#Hotel management system 
#using python and MySQL(DBMS)

    
from tkinter.messagebox import YES


print("WELCOME TO STAR HOTEL")
print("Hii... I AM ALEXA, YOUR HOTEL ASSISTANT :)")
y=input("DO YOU WANT ANY ASSISTANCE (yes/no) ? \n")
if y=="no":
    print("THANK YOU")
if y=="yes":
    n=input("WHAT IS YOUR NAME ? \n")
    print("HOW CAN I HELP YOU", n,":)")
    print("""--> BOOKING
--> CHECKIN
--> CHECKOUT
--> PRICE CHART""")
a="booking"
b="checkin"
c="checkout"
e="price chart"
d=input("YOUR RESPONCE: \n")

if d==a:                          #booking
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="DBMS PASSWORD"
    )
      
    y=db.cursor()
    y.execute("use star_hotel") 
    y.execute("select bed_type from hotel_data")
    z=y.fetchall()
    from scipy import stats  #max repitationyes
    md=stats.mode(z)
        
    num_person=int(input("enter the number of person\n"))
    name=input("enter the person name\n")
    check_in=int(input("Enter the check_in date xx.03.2022\n"))    #input variables
    check_out=int(input("Enter the check_out datexx.03.2022\n"))
    type=input("Enter the type of room AC/NONAC\n")
    print("would like to inform you that many guest choosed",md)
    bt=input("eneter the bed type {single_bed/double_bed/royal_bed/four_bedded}\n" )
    bed_amount=int(input("Enter the amount per day:\n"))
    sql = "insert into hotel_data (person_count,name,check_in,check_out,room_type,bed_type) values(%s,%s,%s,%s,%s,%s)"
    t=(num_person,name,check_in,check_out,type,bt)
    y.execute(sql,t)
    db.commit()
    no_of_days=abs(check_in-check_out)
    print ("ypu are staying for ",no_of_days, "days")
    print("Your respoce has been recorded")
    print("Thank you for booking with us")


if d==b:                           #check_in
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="DBMS PASSWORD"
    )
    cur=db.cursor()
    cur.execute("use star_hotel")
    n=input("enter your name: \n")
    c=float(input("enter the checkin date: \n"))
    
    sql="select name,check_in from hotel_data where name=%s and check_in=%s"
    t=(n,c)
    
    cur.execute(sql,t)
    z=cur.fetchall()

    for x in z:
        if n in z:
            print (x,"Data Found")
        import random
        room=[101,102,103,104,105,106,107,108,109,110]
        roomnumber=random.choice(room)                      #random allotment
        cmd="update hotel_data set room_num=%s where name=%s"
        val=(roomnumber,n)
        cur.execute(cmd,val)
        db.commit()
        print("Thank you for checkin, Your room number is", roomnumber)
        

if d==c:                        #checkout
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="DBMS PASSWORD"
    )
    cur=db.cursor()
    cur.execute("use star_hotel")
    x=input("enter the name: \n")
    y=float(input("Enter the check_out date \n"))
    sql="delete from hotel_data where name=%s and check_out=%s"
    t=(x,y)
    cur.execute(sql,t)
    db.commit()
    for x in cur:
        print(x)
    
    print("you have successfully checkedout from the hotel")
    
    print("thank you and visit again:)")
    print("press fn+f5 to return to the main menu")

if d==e:                            #prices
    import mysql.connector                  
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="DBMS PASSWORD"
    )
    cur=db.cursor()
    cur.execute("use star_hotel")
    cur.execute("select * from prices")
    z=cur.fetchall()
    for x in z:
        print(x)
    print("press fn+f5 to return to the main menu")
