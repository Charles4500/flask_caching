from app import app
from faker import Faker
from models.items import db, Item

# Seeding the database

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()
    print('Seeding the database')
    for i in range(0, 50):
        item_one = Item(name=fake.name(), price=13,
                        description=fake.text())

        db.session.add(item_one)
        db.session.commit()
    print('Finished seeding the database')
