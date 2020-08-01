from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
import os

# Application and database setup
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.join.path(
    basedir, "quotes.db"
)

db = SQLAlchemy(app)
# Marshmallow library is used for effective object serialisation
ma = Marshmallow(app)


# Database creation flask commands
@app.cli.command("db_create")
def db_create():
    db.create_all()
    print("datbase created!")


@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database dropped!")


@app.cli.command("db_seed")
def db_seed():
    quote1 = Quote(
        quote_desc="It always seem impossible until it is done.",
        quote_type="Motivation",
        author="Nelson Mandela",
    )
    quote2 = Quote(
        quote_desc="With the new day comes new strength and new thoughts.",
        quote_type="Motivation",
        author="Eleanor Roosevelt",
    )

    quote3 = Quote(
        quote_desc="The secret of getting ahead is getting started.",
        quote_type="Motivation",
        author="Mark Twain",
    )

    quote4 = Quote(
        quote_desc="With self-discipline most anything is possible.",
        quote_type="Inspiration",
        author="Theodore Roosevelt",
    )

    quote5 = Quote(
        quote_desc="It is during our darkest moments that we must focus to see the light.",
        quote_type="Inspiration",
        author="Aristotle",
    )

    db.session.add(quote1)
    db.session.add(quote2)
    db.session.add(quote3)
    db.session.add(quote4)
    db.session.add(quote5)
    db.session.commit()
    print('Database seeded!')


# database model
class Quote(db.Model):
    __tablename__ = 'quotes'
    quote_id = Column(Integer, primary_key = True)
    quote_desc = Column(String)
    quote_type = Column(String)
    author = Column(String)


# Quote model added to the Marshmallow library for JSON serialization
class QuoteSchema(ma.Schema):
    class Meta:
        fields = ('quote_id', 'quote_desc', 'quote_type', 'author')


quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)

