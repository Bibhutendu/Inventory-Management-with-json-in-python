import json
import pandas as pd
import os.path
import numpy as np

if os.path.isfile("grocery_stock") is False:
    available_products = {1001: {"name":"freedom oil", "price":77.0, "weight":"500ml", "quantity":27, "exp_date":"12/12/24"},
                        1002: {"name":"soya bean packets", "price":10.0, "weight":"50gm", "quantity":30, "exp_date":"1/3/25"},
                        1003: {"name":"horlicks", "price":278.0, "weight":"500gm", "quantity":15, "exp_date":"12/12/25"},
                        1004: {"name":"bhitania", "price":40.0, "weight":"200gm", "quantity":38, "exp_date":"24/5/25"},
                        1005: {"name":"lotte choco pie", "price":10.0, "weight":"20gm", "quantity":47, "exp_date":"8/7/25"},
                        1006: {"name":"uncle chips", "price":10.0, "weight":"18gm", "quantity":67, "exp_date":"2/2/25"},
                        }

    js = json.dumps(available_products)

    fd = open("grocery_stock",'w')
    fd.write(js)
    fd.close()



# diplay product details page
def display_products():
    
    txt = open("grocery_stock",'r')
    data = json.load(txt)
    txt.close()

    table = pd.DataFrame(columns = ["ID", "name", "price", "weight", "quantity", "exp_date"])
    for i in data.keys():
        temp = pd.DataFrame(["ID"])
        temp["ID"] = [i]
        for j in data[i].keys():
            temp[j] = [data[i][j]]
        table = table._append(temp)
    table = table.reset_index(drop=True)
    print(table)



def display_specific_product():
    txt = open("grocery_stock",'r')
    data = json.load(txt)
    txt.close()
    

    count = 0
    op1 = input("Enter the product name: ")
    op2 = input("Enter the id of product: ")
    data2 = []

    for i in data:
            if data[i]["name"] == op1 or i == op2:
                row = {
                    'Product Id':op2,
                    'Product Name':data[op2]["name"],
                    'Price':data[op2]["price"],
                    'Weight':data[op2]["weight"],
                    'Quantity':data[op2]["quantity"],
                    'Exp Date':data[op2]["exp_date"]
                }
                data2.append(row)                
                df = pd.DataFrame(data2)                
                print(df)            
                break
            else:
                count = count + 1
    if count == len(data):
        print("Product not found")


#insert new product
def insert_new_product():
     txt = open("grocery_stock","r")
     data = json.load(txt)
     txt.close()
     product_id = input("Enter the product id: ")
     if product_id not in data.keys():
         product_name = input("Enter the product name: ")
         product_price = float(input("Enter the product price: "))
         product_weight = input("Enter the product weight: ")
         product_quantity = int(input("Enter the product quantity: "))
         product_exp_date = input("Enter the exp date: ")
         data[product_id] = {"name":product_name,
                                "price":product_price,
                                "weight":product_weight,
                                "quantity":product_quantity,
                                "exp_date":product_exp_date}

         js = json.dumps(data)
         fd = open("grocery_stock",'w')
         fd.write(js)
         fd.close() 
     else:
         print("Id is already existing")    
        
     
     d = int(input("Press '1' to enter new data or '0' to exit\nEnter your choice: "))
     if d == 1:
        insert_new_product()
        

#update product details
def update_product_details():
    txt = open('grocery_stock','r')
    data = json.load(txt)

    up_id = input("Enter the product id to be updated: ")
    if up_id in data.keys():
        choice = input("1 - Update the whole product data \n0 - update specific attribute of product\nEnter your choice: ")
        if choice == '1':
            product_name = input("Enter the product name: ")
            product_price = float(input("Enter the product price: "))
            product_weight = input("Enter the product weight: ")
            product_quantity = int(input("Enter the product quantity: "))
            product_exp_date = input("Enter the exp date: ")
            data[up_id] = {"name":product_name, "price":product_price, "weight":product_weight, "quantity":product_quantity, "exp_date":product_exp_date}
            print("Product Id"+ str(up_id)+ " is updated successfully")
        
        elif choice == '0':
            spe_at = input("Enter the specific attribute: ")
            if spe_at in data[up_id].keys():
                new_up_at = input("Enter the "+ spe_at + " details: ")
                data[up_id][spe_at] = new_up_at
                print("Product ID "+str(up_id)+" attribute " + str(spe_at)+ " is Updated Successfully...!!!")
            else:
                print("Invalid Product Attribute...!!!")
        else:
            print("Invalid Product Attribute...!!!")
    else:
        print("Invalid Product Attribute...!!!")
    
    js = json.dumps(data)
    fd = open("grocery_stock", 'w')
    fd.write(js)
    fd.close()


# delete product details
def delete_product_details():
    txt = open('grocery_stock','r')
    data = json.load(txt)
    txt.close()

    choice = input("Enter the product id to delete: ")
    if choice in data.keys():
        data.pop(choice)
        print("Product ID "+str(choice)+" Deleted Successfully...!!!")
    else:
        print("invalid product id")
    
    js = json.dumps(data)
    fd = open('grocery_stock','w')
    fd.write(js)
    fd.close()



#User purchase details
def User_purchase_details():
    if(os.path.isfile("user_data.json")is False):
        print("No user and purchase details are available")
        return
    txt = open("user_data.json",'r')
    user_data = json.load(txt)
    txt.close()
    count = 0
    data = []
    choice = int(input("0 - Display all the purchase bills\n1 - Display spcific user purchase biils: "))
    if choice == 1:
        op = input("Enter the User ID: ")
        for i in user_data.keys():
            if op == user_data[i]["user_id"]:
                print(user_data[i])
                count = count+1
            print("Total number of purchase: ",count)
        else:
            print("Invalid User ID")
    
    elif choice == 0:
        for purchaseno in user_data.keys():                                   
            for id in range((len(user_data[purchaseno]['item_id']))):
                id = int(id)
                if id < len(user_data[purchaseno]['item_price']):
                    row = {
                        'purchase no.': purchaseno,
                        'user id':user_data[purchaseno]['user_id'],
                        'user name':user_data[purchaseno]['name'],
                        'item id':user_data[purchaseno]['item_id'][id],
                        'item price':user_data[purchaseno]['item_price'][id],
                        'item quantity':user_data[purchaseno]['item_quntity'][id],
                        'total price':user_data[purchaseno]["total_price"]
                    }                              
                data.append(row)

        df = pd.DataFrame(data)
        # df.set_index('purchase no.',inplace =True)
        print(df)
    
    else:
        print("Invalid choice")

#generate bill
def generate_bill(purchase_no,user_id,user_name,item_ids,item_name,item_quantity,
                      item_price,total_price):
    print("############## RELIANCE FRESH ##############")
    print("##############  PURCHASE BILL ##############")
    print("Purchase No.: ",purchase_no)
    print("User ID       User Name")
    print(user_id,"     ",user_name)
    print("############################################")
    d = []
    for i in range(len(item_ids)):
        row = {"S.No.":i,
               "Item Id":item_ids[i],
               "Item Name":item_name[i],
               "Item Quantity":item_quantity[i],
               "Item_Price":item_price[i]
        }
        d.append(row)
    df = pd.DataFrame(d)
    df.set_index('S.No.',inplace = True)
    print(df)
    print("Total Price: ",total_price)


#buy product
def buy_product():
    if(os.path.isfile("user_data.json") is False):
        user_data = {}
        user_ids = {}
    else:
        txt = open("user_data.json",'r')
        user_data = json.load(txt)
        txt.close()
        ff = open("user_ids",'r')
        user_ids = json.load(ff)
        ff.close()
    
    
    fd = open("grocery_stock",'r')
    data = json.load(fd)
    fd.close()
    
    
    item_ids = []
    item_name = []
    item_quantity = []
    item_price = []
    total_price = []
    
    print("\n")
    p = int(input("Enter Your User ID if You are Old Customer else press '0' To New User ID :- "))

    if p == 0:
        if(len(user_data)==0):
            user_id = 101
            user_name = input("Enter Your Name :- ")
            
            user_ids[user_id] = user_name
            
        else:
            user_id  = int(list(user_ids.keys())[-1])+1           
            user_name = input("Enter Your Name :- ")
            user_ids[user_id] = user_name

            
    else:
        user_id = str(p)
        user_name = user_ids[user_id]
        
    
    while(1):       
        for i in user_ids:
            if i == user_id:           
                pid = input("Enter the product id: ")
                if pid in data:
                    item_ids.append(pid)
                    pn = data[pid]['name']
                    item_name.append(pn)
                    n = 1
                    while(1):
                        pq = int(input("Enter the quantity of product: "))
                        if pq > data[pid]["quantity"]:
                            print("Sorry! we don't have the required quantity")
                            print("Available quantity = ",data[pid]["quantity"])
                            n = int(input("1 - modify quantity \n0 - skip product\nEnter your choice: "))
                            print("\n")
                            if n == 1:
                                continue
                            else:
                                break
                        else:
                            data[pid]["quantity"] = data[pid]["quantity"] - pq                            
                            item_quantity.append(pq)
                            pp = data[pid]['price']
                            tpp = pp * pq
                            item_price.append(tpp)
                            break
                    
        o = int(input("0 - to generate bill\n1 - to add products\nEnter your choice: "))
        print("\n")
        if n == 1 and o == 0:
            break
        elif n == 0 and o == 0:
            break
        elif n == 0 and o == 1:
            continue
        else:
            continue         
                
    purchase_no = len(user_data)+1
    total_price = str(np.sum(item_price))        
    
    user_data[purchase_no] = {"user_id":user_id,
                                "name":user_name,
                                "item_id":item_ids,
                                "item_name":item_name,
                                "item_quntity":item_quantity,
                                "item_price":item_price,
                                "total_price":total_price
                                }
    
    if n == 1 and o == 0:
        generate_bill(purchase_no,user_id,user_name,item_ids,item_name,item_quantity,
                      item_price,total_price)
    elif item_price != 0:
        item_ids.pop()
        item_name.pop()
        generate_bill(purchase_no,user_id,user_name,item_ids,item_name,item_quantity,
                      item_price,total_price)
    else:
        print("Thank you for shopping with us!")

    with open('user_ids','w') as fd:
        json.dump(user_ids,fd)
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    with open('grocery_stock','w') as f:
        json.dump(data,f)

# admin page
def admin():
    
    while(1):
        print("\n")
        print("............Adminstrator...........")
        print("1. Display all products")
        print("2. Display specific product")
        print("3. Insert new product details")
        print("4. Update product details")
        print("5. Delete product details")
        print("6. User purchase details")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        print("\n")

        match choice:
            case 1:
                display_products()
                continue
            case 2:
                display_specific_product()
                continue
            case 3:
                insert_new_product()
                continue
            case 4:
                update_product_details()
                continue
            case 5:
                delete_product_details()
                continue
            case 6:
                User_purchase_details()
                continue
            case 7:
                break
            case _:
                print("invaild choice")
        



#customber page
def customber():
    while(1):
        print("\n")
        print(".............. CUSTOMBER ..............")
        print("1 - Display all products")
        print("2 - Display specific product")
        print("3 - Buy product")        
        print("4 - Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                display_products()
                
            case 2:
                display_specific_product()
                
            case 3:
                buy_product()
                           
            case 4:
                break

            case _:
                print("invalid choice")
    

    
    
# main interface
while(1):
    print("\n............choose any one option.............")
    print("1. Admin")
    print("2. Customber")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        admin()
    elif(choice == 2):
        customber()
    elif(choice == 3):
        break
    else:
        print("Invalid choice.....")