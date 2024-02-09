from market.models import Item, User
from market import app, db
from sqlalchemy.exc import IntegrityError

with app.app_context():
    db.create_all()

    # Attempt to add items
    try:
        item1 = Item(id=1, name='Iphone 10', price=500, description='desc', barcode='012345678911')
        db.session.add(item1)
        db.session.commit()

        item2 = Item(id=2, name='Laptop', price=600, description='description', barcode='345884849220')
        db.session.add(item2)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Roll back the session in case of error for items
        print('An item with this ID already exists.')

    # Attempt to add users
    try:
        user1 = User(id=1, username='user', email_address='user@email.com',
                     password='123456')
        db.session.add(user1)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Roll back the session in case of error for users
        print('A user with this ID already exists.')

    print(Item.query.filter(Item.id < 3).all())
    print(User.query.filter(User.id < 3).all())
