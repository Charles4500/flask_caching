from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

# Define naming convention for database schema
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)


class Item(db.Model,SerializerMixin):
    __tablename__ = 'items'
    
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(60),nullable=False)
    price=db.Column(db.Float,nullable=False)
    description= db.Column(db.String(256),nullable=False)