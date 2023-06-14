import qrcode
PRODUCTS=[]

def read_from_database():
    f=open("database.txt","r")

    for line in f:
   
        result=line.split(",")
        my_dict={"code": result[0], "name": result[1], "price": result[2], "count": result[3]}

        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    f=open("database.txt", "w")
    
    for product in PRODUCTS:
        f.write(str(product["code"])+ ","+ str(product["name"])+ "," + str(product["price"])+ "," +str(product["count"]))
    
    print(" data successully saved ")

    f.close()

def show_menu():
    print("0-QRcode")
    print("1-add")
    print("2-Edit")
    print("3-Remove")
    print("4-search")
    print("5-show list")
    print("6-buy")
    print("7-Exit")

def add():
    code=input("enter code: ")
    name=input("enter name: ")
    price=input("enter price: ")
    count=input("enter count: ")
    new_product={"code": code, "name":name, "price":price, "count":count}
    PRODUCTS.append(new_product)

def edit():
    product_code=input("enter product code: ")
    for product in PRODUCTS:
        if product_code==product['code']:
            print("code=",product["code"],", name=",product["name"],", price=",product["price"],", count=",product["count"])
            name=input("enter new name to be edited: ")
            if name!='':
                product['name']=name

            price=input("enter new price to be edited: ")
            if price!='':
                product['price']=int(price)

            count=input("enter new count to be edited: ")
            if count!='':
                product['count']=int(count)
            
            print("The product edited successfully")
            break

    else:
        print("your product code wasn't found!")
    
def remove():
    product_code=input("enter product code:")

    for product in PRODUCTS:
        if product["code"]==product_code:
            PRODUCTS.remove(product)
            break
        print("your chosen product had been successfully deleted!")
    else:
     print("your product code was not found!")


def search():
    user_input=("type your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            print(product["code"], "\t", product["name"], "\t", product["price"])
            break  
    else:
        print("your product code was not found")


def show_list():
    print("code\t\tname\tprice\tcount")
    for product in PRODUCTS:
        print(product["code"], "\t", product["name"], "\t", product["price"])

def buy():
    factor=[]
    total_cost=0
    while True:
        product_code=input("enter your desired product code or enter exit to quit:")
        if product_code=="exit":
            break

        for product in PRODUCTS:
            if product["code"]==product_code:
                product_number=int(input("enter the number of product you want: "))
                if int(product["count"])<product_number:
                       print("insufficient inventory!")
                else:
                    product["count"]==int(product["count"])-product_number
                    cost=int(product["price"])*product_number
                    buy_dict={"code": product["code"], "name": product["name"], "number": product_number, "price": cost}
                    factor.append(buy_dict)
                break
        else:
            print("your desired product wasn't found!")

    print("===================================================")
    print("code \t\t name \t\t number \t\t price")
    for product in factor:
        print(product["code"], "\t\t", product["name"],"\t\t", product["number"] , "\t\t" ,product["price"])
        total_cost+=product["price"]
    print("===================================================")
    print("Total cost:" , total_cost , "\n")
    print(" Thank you for your shopping!  \n")

def make_qrcode():
    product_code=input("enter your product code to generate QRcode: ")
    for product in PRODUCTS:
        if product["code"]==product_code:
            q=qrcode.make(product["code"]+ "-" +product["name"]+ "-" +product["price"])
            q.save("product data to qrcode.png")
            print("QRcode was successully made!")
            break
    else:
        print("your product code was not found!")

print("welcome to my store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice=int(input("enter your choice: "))

    if choice==0:
        make_qrcode()
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:  
        buy()
    elif choice==7:
        write_to_database()
        exit(0)

    else:
        print("Incorrect input(mesle adam vared kon!)")

