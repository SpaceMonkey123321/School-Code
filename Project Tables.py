import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='welcome')

mycursor = mycon.cursor()

mycursor.execute("USE restaurant")



mycursor.execute("Create Table if not exists soups (itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists salads(itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists appetizers (itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists pasta (itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists pizza(itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists smoothies(itemno int(3), itemname varchar(100), price int(4))")

mycursor.execute("Create Table if not exists deserts(itemno int(3), itemname varchar(100), price int(4))")



mycursor.execute("insert into soups values(1, 'Minestrone',225), (2,'Smoked Mushroom Soup',200), (3,'Smoked Chicken Soup',250)")
mycon.commit()

mycursor.execute("insert into salads values(3,'Caeser Salad',265), (4,'Citrus Chicken Salad',335), (5,'Smoked Salmon Salad',400), (6,'Tuna Salad',355)")
mycon.commit()

mycursor.execute("insert into appetizers values(7,'Grilled Tomato Bruschetta',225),(8,'Chicken Crostini',300),(9,'Crispy Zucchini Fries',200),(10,'Cheesy Jalapeno Poppers',250),(11,'Fried Prawn and Calamari',400)")
mycon.commit()

mycursor.execute("insert into pasta values(11,'Penne Picante',350),(12,'Lamb Lasagna',450),(13,'Spaghetti Carbonara',400),(14,'Rosemary Fettuccini',375),(15,'Baked Penne',350)")
mycon.commit()

mycursor.execute("insert into pizza values(16,'Margherita',300),(17,'Four Cheese Special',350),(18,'Pesto Pepper',325),(19,'Classic Pepperoni',375),(20,'Chicken and Jalapeno',400),(21,'Chicken Loaded Pizza',350)")
mycon.commit()

mycursor.execute("insert into smoothies values(22,'Vanilla',200),(23,'Strawberry',200),(24,'Peach',200),(25,'Banana',200),(26,'Blueberry',200)")

mycursor.execute("insert into deserts values(27,'Cheese Cake',250),(28,'Chocolate Walnut Brownie',225),(29,'Red Velvet Cake',200),(30,'Chocolate Fudge Cake',175)")
mycon.commit()


mycursor.execute("Create table if not exists reservations (restaurant varchar(20), name varchar(30), number int(2), time varchar(10), date varchar(10))") 
mycursor.execute("Create table if not exists orders (restaurant varchar(20), name varchar(30), item varchar(100), price int(4), date varchar(10))") 

mycursor.execute("Create table if not exists menu(itemno int(2), itemname varchar(30), price int(4))")
mycursor.execute("insert into menu values(1, 'Minestrone',225), (2,'Smoked Mushroom Soup',200), (3,'Smoked Chicken Soup',250),(3,'Caeser Salad',265), (4,'Citrus Chicken Salad',335), (5,'Smoked Salmon Salad',400), (6,'Tuna Salad',355),(7,'Grilled Tomato Bruschetta',225),(8,'Chicken Crostini',300),(9,'Crispy Zucchini Fries',200),(10,'Cheesy Jalapeno Poppers',250),(11,'Fried Prawn and Calamari',400),(16,'Margherita',300),(17,'Four Cheese Special',350),(18,'Pesto Pepper',325),(19,'Classic Pepperoni',375),(20,'Chicken and Jalapeno',400),(21,'Chicken Loaded Pizza',350),(22,'Vanilla',200),(23,'Strawberry',200),(24,'Peach',200),(25,'Banana',200),(26,'Blueberry',200),(27,'Cheese Cake',250),(28,'Chocolate Walnut Brownie',225),(29,'Red Velvet Cake',200),(30,'Chocolate Fudge Cake',175)")
mycon.commit()