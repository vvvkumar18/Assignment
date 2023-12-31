from tabulate import tabulate
import mysql.connector

data=mysql.connector.connect(
      host="localhost",
      username = "root",
      password="kumar@1234567",
      database="database6"
    )
#Perform curd operations

# Insert
def insertion(food_id,food_name,food_price,food_type):
    result=data.cursor()
    sql="Insert into food(food_id,food_name,food_price,food_type) values(%s,%s,%s,%s)"
    val=(food_id,food_name,food_price,food_type)
    result.execute(sql,val)
    data.commit()
    print("DATA INSERTED SUCCESSFULLY")

# Update
def update(food_id,food_name,food_price,food_type):
    result = data.cursor()
    sql = "UPDATE food set food_name=%s,food_price=%s,food_type=%s WHERE food_id=%s"
    val = (food_name, food_price, food_type, food_id)
    result.execute(sql,val)
    data.commit()
    print("DATA UPDATED SUCCESSFULLY")

# Search  
def search():
    result=data.cursor()
    sql="SELECT FOOD_ID, FOOD_NAME, FOOD_PRICE, FOOD_TYPE FROM food"
    result.execute(sql)
    output=result.fetchall()
    data.commit()
    print(tabulate(output, headers=["FOOD_ID", "FOOD_NAME", "FOOD_PRICE", "FOOD_TYPE"]))
    #print(output)
# Delete
def delete(food_id):
    result=data.cursor()
    sql="DELETE from food where food_id=%s"
    val=([food_id])
    result.execute(sql,val)
    data.commit()
    print("DATA DELETED SUCCESSFULLY")





while True:
    print("1.Insertion Data")
    print("2.Update Data")
    print("3.Search Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        food_id = input("Enter The Food Id : ")
        food_name = input("Enter the Food Name : ")
        food_price= input("Enter the Food Price : ")
        food_type = input("Enter Food type : ")
        insertion(food_id,food_name,food_price,food_type)

    elif choice == 2:
  

        food_id = int(input("Enter The Food Id: "))
        food_name = input("Enter the Food Name: ")
        food_price = input("Enter the Food Price: ")
        food_type = input("Enter Food Type: ")
        update(food_id, food_name, food_price, food_type)

    elif choice == 3:
        search()
    elif choice == 4:
        food_id = input("Enter The Food Id to Delete : ")
        delete(food_id)

    elif choice == 5:
        quit()

    else:
        print("Invalid Selection . Please Try Again !")
