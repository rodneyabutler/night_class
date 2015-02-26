__author__ = 'Rodney'


# Here is our initial list of items for our store. This will eventually live in another file once we
# have set up a few more of the basic items.
# <<<<<<< HEAD
# =======


class InventoryItem(object):
    def __init__(self, name, on_hand, price):
        self.name = name
        self.on_hand = on_hand
        self.price = price


class Catalog(object):
    def __init__(self):
        self.catalog = {}

    def add_items(self):
        item_add = raw_input('What item would you like to buy?: ')
        item_quantity = raw_input("How many would you like to buy?: ")
        print item_add.name()
        try:#***********What is being evaluated?**********
            if item_quantity < item_add.on_hand:
                for self.name in self.catalog:#*******where is the comparison of the string input and the item?********
                    if self.catalog.items == item_add:
                        return item_add.inventory.append()
        except:
            print "We can't fulfill that request"


#  This will create a basic profile for users. Later in the program buyers/sellers will be distinguished

class Profile(object):
    def __init__(self, first_name, last_name, money, password):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money
        self.password = password
        self.inventory = {}

    # def create_user(self):
    #     user_first = raw_input("What is your first name? ")
    #     user_last = raw_input("What is your last name? ")
    #     money_amount = raw_input("How much money do you have?")
    #     user_password = raw_input("Choose a password.")
    #     self.first_name = user_first
    #     self.last_name = user_last
    #     self.money = money_amount
    #     self.password = user_password

# <<<<<<< Formats users information
    def __str__(self):
        return 'Customer: {0} {1}, Money: ${2}, Password: {3}'.format(self.first_name, self.last_name, self.money,
                                                                      self.password)

# class Buyer(Profile):
#     pass
# # this will take items selected by buyer from the store items dictionary.
#
#     def cart(self):
#       self.inventory = {}
#
#
# # class to separate the user interface (what is displayed to the user) and the logic of the program.
# class UserInterface(Store):
#     pass
#
#
#
#     def options(self):
#       self.display = raw_input("what would you like to do?")
#       self.options = raw_input("""
#       1. search
#       2. view cart
#       3. review and payment """)
#
# # >>>>>>> FETCH_HEAD
#




walmart = Catalog()

walmart.catalog = {
            101: InventoryItem('apples', 5, 1.00),
            102: InventoryItem('kashi', 15, 2.15),
            103: InventoryItem('mop', 8, 9.85),
        }
Catalog.add_item()
#print walmart.add_items()
#print walmart.catalog[101].name

# for index, items in walmart.catalog.items():
#     print index, str(items['qty']), str(items['price'])