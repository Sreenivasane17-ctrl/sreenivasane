# project


from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient


MongoURL = MongoClient("mongodb+srv://sreenivasane:sreenivasane172009@cluster0.ojzdxvv.mongodb.net/?appName=Cluster0")
myDB = MongoURL["Project"]

user_Collection = myDB["user"]

Product_collection = myDB["Product"]

order_collection = myDB["Order"]

def add_user():
    while True:
        try:
            Name = input("Enter your name: ")
            Email = input("Enter your email: ")
            Password = input("Enter your password: ")
            created_At = datetime.now()
            Mobile = int(input("Enter your mobile number: "))
            Address = input("Enter your address: ")

            existing_user = user_Collection.find_one({"Email" : Email})
            if existing_user:
                print("The entered Email is alresdy exists!!!")
                continue
            user_data = {
                "Name" : Name,
                "Email" : Email,
                "Password" : Password,
                "created_At" : datetime.now(),
                "Mobile" : Mobile,
                "Address" : Address
            }
    
            result= user_Collection.insert_one(user_data)
            print("User inserted successful!!!")
            print("User Id: ",result.inserted_id)

            choose = input("Do you want to continue Yes/No : ")
            if choose.lower() != "yes":
                break
        except Exception as e:
            print("Error:", e)

def user_product():
    products = [
        {
            "Name": "Smart Watch",
            "Price": 2000,
            "Model": "Boat",
            "Colour": "Black",
            "Stock": 20,
            "Discount": 5
        },
        {
            "Name": "Airpods",
            "Price": 25000,
            "Model": "Apple",
            "Colour": "White",
            "Stock": 25,
            "Discount": 8
        },
        {
            "Name": "Sneakers",
            "Price": 499,
            "Model": "Asian",
            "Colour": "Brown",
            "Stock": 50,
            "Discount": 30
        },
        {
            "Name": "Wrist Watch",
            "Price": 999,
            "Model": "Titan",
            "Colour": "Silver",
            "Stock": 40,
            "Discount": 10
        },
        {
            "Name": "Laptop",
            "Price": 70000,
            "Model": "Asus Vivobook",
            "Colour": "Matte Silver",
            "Stock": 40,
            "Discount": 10
        },
        {
            "Name": "Smart Phone",
            "Price": 25000,
            "Model": "Oppo",
            "Colour": "Sky Blue",
            "Stock": 40,
            "Discount": 10
        },
        {
            "Name": "LED TV",
            "Price": 42000,
            "Model": "Samsung Crystal",
            "Colour": "Black",
            "Stock": 18,
            "Discount": 10
        },
        {
            "Name": "Refrigerator",
            "Price": 32000,
            "Model": "LG Double Door",
            "Colour": "Grey",
            "Stock": 12,
            "Discount": 18
        },
        {
            "Name": "Washing Machine",
            "Price": 28000,
            "Model": "IFB Front Load",
            "Colour": "White",
            "Stock": 20,
            "Discount": 14
        },
        {
            "Name": "Air Conditioner",
            "Price": 39000,
            "Model": "Daikin Split AC",
            "Colour": "White",
            "Stock": 15,
            "Discount": 22
        },
        {
            "Name": "Gaming Mouse",
            "Price": 2500,
            "Model": "Logitech G102",
            "Colour": "Black",
            "Stock": 90,
            "Discount": 5
        },
        {
            "Name": "Mechanical Keyboard",
            "Price": 6500,
            "Model": "Redragon K552",
            "Colour": "Black",
            "Stock": 35,
            "Discount": 16
        }
    ]

    result = Product_collection.insert_many(products)
    print(f"{len(result.inserted_ids)} Products Inserted Successfully.")


def order_insert():
    while True:
        try:
            user_id = input("Enter the User Id")
            product_id = input("Enter your Product Id")
            User_ID = ObjectId(user_id)
            Product_ID = ObjectId(product_id)

            user = user_Collection.find_one({"_id": User_ID})
            product = Product_collection.find_one({"_id": Product_ID})
            if user is None:
                print("User not found")
                continue
            product = Product_collection.find_one({"_id": Product_ID})

            if product is None:
                print("Product not found")
                continue
            Quantity = int(input("Enter Quantity: "))
 
            if Quantity <= 0:
                print("Quantity must be greater than 0")
                continue
 
            if Quantity > product["Stock"]:
                print("Not enough Stock available!")
                continue
 
            discount_price = product["Price"] * product["Discount"] / 100
            Amount = (product["Price"] - discount_price) * Quantity
 
            isPaid = input("Is Paid (yes/no): ")
            Is_Delivered = input("Is Delivered (yes/no): ")
 
            order = {
                "User_Id": User_ID,
                "Product_Id": Product_ID,
                "Amount": Amount,
                "Quantity": Quantity,
                "Is_Paid": isPaid.lower() == "yes",
                "Ordered_Date": datetime.now(),
                "Is_Delivered": Is_Delivered.lower() == "yes"
            }
 
            order_collection.insert_one(order)

            Product_collection.update_one(
            {"_id": Product_ID},
            {"$inc": {"Stock": -Quantity}}
        )
            print("Order inserted successfully!")
            choice = input("Do you want to continue (yes/no): ")
            if choice.lower() != "yes":
                break
 
        except Exception as e:
            print("Error:", e)

           

def view_users():
    users = user_Collection.find()

    for user in users:
        print("-" * 50)
        print("ID :", user["_id"])
        print("Name :", user["Name"])
        print("Email :", user["Email"])
        print("Mobile :", user["Mobile"])
        print("Address :", user["Address"])

def view_products():
    products = Product_collection.find()

    for product in products:
        print("-" * 50)
        print("ID :", product["_id"])
        print("Name :", product["Name"])
        print("Price :", product["Price"])
        print("Model :", product["Model"])
        print("Colour :", product["Colour"])
        print("Stock :", product["Stock"])
        print("Discount :", product["Discount"], "%")

def view_orders():
    orders = order_collection.find()

    for order in orders:
        user = user_Collection.find_one({"_id": order["User_Id"]})
        product = Product_collection.find_one({"_id": order["Product_Id"]})

        print("-" * 60)
        print("Order ID :", order["_id"])
        print("Customer :", user["Name"])
        print("Product :", product["Name"])
        print("Quantity :", order["Quantity"])
        print("Amount :", order["Amount"])
        print("Paid :", order["Is_Paid"])
        print("Delivered :", order["Is_Delivered"])
        print("Ordered Date :", order["Ordered_Date"])
    

def delete_user():
    user_id = input("Enter User ID: ")

    result = user_Collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count:
        print("User Deleted Successfully.")
    else:
        print("User Not Found.")

 
def delete_product():
    product_id = input("Enter Product ID: ")

    result = Product_collection.delete_one({"_id": ObjectId(product_id)})

    if result.deleted_count:
        print("Product Deleted Successfully.")
    else:
        print("Product Not Found.")


def update_user():
    try:
        user_id = input("Enter User ID: ")

        user = user_Collection.find_one({"_id": ObjectId(user_id)})

        if user is None:
            print("User not found.")
            return

        name = input(f"Enter Name ({user['Name']}): ")
        email = input(f"Enter Email ({user['Email']}): ")
        mobile = input(f"Enter Mobile ({user['Mobile']}): ")
        address = input(f"Enter Address ({user['Address']}): ")

        user_Collection.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "Name": name if name else user["Name"],
                    "Email": email if email else user["Email"],
                    "Mobile": int(mobile) if mobile else user["Mobile"],
                    "Address": address if address else user["Address"]
                }
            }
        )

        print("User Updated Successfully.")

    except Exception as e:
        print("Error:", e)


def update_product():
    try:
        product_id = input("Enter Product ID: ")

        product = Product_collection.find_one({"_id": ObjectId(product_id)})

        if product is None:
            print("Product not found.")
            return

        price = input(f"Enter Price ({product['Price']}): ")
        stock = input(f"Enter Stock ({product['Stock']}): ")
        discount = input(f"Enter Discount ({product['Discount']}): ")

        Product_collection.update_one(
            {"_id": ObjectId(product_id)},
            {
                "$set": {
                    "Price": int(price) if price else product["Price"],
                    "Stock": int(stock) if stock else product["Stock"],
                    "Discount": int(discount) if discount else product["Discount"]
                }
            }
        )

        print("Product Updated Successfully.")

    except Exception as e:
        print("Error:", e)


def search_user():
    email = input("Enter User Email: ")

    user = user_Collection.find_one({"Email": email})

    if user:
        print("\nUser Found")
        print("ID:", user["_id"])
        print("Name:", user["Name"])
        print("Email:", user["Email"])
        print("Mobile:", user["Mobile"])
        print("Address:", user["Address"])
    else:
        print("User Not Found.")


def search_product():
    name = input("Enter Product Name: ")

    product = Product_collection.find_one({"Name": {"$regex": name, "$options": "i"}})

    if product:
        print("\nProduct Found")
        print("ID:", product["_id"])
        print("Name:", product["Name"])
        print("Price:", product["Price"])
        print("Model:", product["Model"])
        print("Colour:", product["Colour"])
        print("Stock:", product["Stock"])
        print("Discount:", product["Discount"])
    else:
        print("Product Not Found.")


def cancel_order():
    try:
        order_id = input("Enter Order ID: ")

        order = order_collection.find_one({"_id": ObjectId(order_id)})

        if order is None:
            print("Order Not Found.")
            return

        Product_collection.update_one(
            {"_id": order["Product_Id"]},
            {
                "$inc": {
                    "Stock": order["Quantity"]
                }
            }
        )

        order_collection.delete_one({"_id": ObjectId(order_id)})

        print("Order Cancelled Successfully.")

    except Exception as e:
        print("Error:", e)


def order_history():
    user_id = input("Enter User ID: ")

    orders = order_collection.find({"User_Id": ObjectId(user_id)})

    found = False

    for order in orders:
        found = True

        product = Product_collection.find_one(
            {"_id": order["Product_Id"]}
        )

        print("-" * 50)
        print("Order ID:", order["_id"])
        print("Product:", product["Name"])
        print("Quantity:", order["Quantity"])
        print("Amount:", order["Amount"])
        print("Paid:", order["Is_Paid"])
        print("Delivered:", order["Is_Delivered"])
        print("Date:", order["Ordered_Date"])

    if not found:
        print("No Orders Found.")


def main():
    while True:

        print("\n========= E-COMMERCE MENU =========")
        print("1. Add User")
        print("2. Insert Products")
        print("3. Place Order")
        print("4. View Users")
        print("5. View Products")
        print("6. View Orders")
        print("7. Update User")
        print("8. Update Product")
        print("9. Search User")
        print("10. Search Product")
        print("11. Delete User")
        print("12. Delete Product")
        print("13. Cancel Order")
        print("14. User Order History")
        print("15. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_user()

        elif choice == "2":
            user_product()

        elif choice == "3":
            order_insert()

        elif choice == "4":
            view_users()

        elif choice == "5":
            view_products()

        elif choice == "6":
            view_orders()

        elif choice == "7":
            update_user()

        elif choice == "8":
            update_product()

        elif choice == "9":
            search_user()

        elif choice == "10":
            search_product()

        elif choice == "11":
            delete_user()

        elif choice == "12":
            delete_product()

        elif choice == "13":
            cancel_order()

        elif choice == "14":
            order_history()

        elif choice == "15":
            print("Thank You... Visit Again!")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()