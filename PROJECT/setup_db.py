from driver import *
from app.models import Menu,Admin_User,Waiter_calling
from app.extensions import db
from app.login import hash

ResetDatabase()

# Database context
#------------------------------------------------------------------------------

with app.app_context():
    item = Menu(name = "6oz Beef Burger", type = "food", price = 10.65, cals = "774", diet = "", soldout="false", image="beef_burger.jpeg", ingredients = "beef patty, bun, lettuce, tomato, pickles, cheese")
    item1 = Menu(name = "Vegan Burger", type = "food", price = 9.05, cals = "678", diet = "Ve",soldout="false", image="vegan_burger.jpeg", ingredients = "bun, vegan patty, lettuce, tomato, onions")
    item2 = Menu(name = "Chicken Club Sandwitch", type = "food", price = 7.65, cals = "728", diet = "",soldout="false", image="chicken_club_sandwitch.jpeg", ingredients = "chicken, bacon, lettuce, tomatoe, mayonnaise")
    item3 = Menu(name = "Peroni Beer", type = "drink", price = 5.25, cals = "112", diet = "Ve, 18+",soldout="false", image="peroni_beer.jpeg", ingredients = 'ice')
    waiterCall = Waiter_calling(table_id =0, status = "Called")

    db.session.add(item)
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(waiterCall) ##added to show that waiter calling table works
    
    wpassword = "password"
    wpassword = hash(wpassword)
    User1 = Admin_User(type = "waiter", username= "Tommy", password = wpassword)
    
    wpassword = "password2"
    wpassword = hash(wpassword)
    User2 = Admin_User(type = "kitchen", username= "Vanessa", password = wpassword)
    
    db.session.add(User1)
    db.session.add(User2)
    db.session.commit()
    
#------------------------------------------------------------------------------