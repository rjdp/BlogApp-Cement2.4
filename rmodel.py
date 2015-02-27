#!/usr/bin/env python3
from peewee import *

db = SqliteDatabase('rtblogs.db')


class Category(Model):
    category = CharField()

    class Meta:
        database = db  # this model uses the blog database


class Blog_post(Model):
    title = CharField()
    content = CharField()
    category = CharField(null=True)

    class Meta:
        database = db  # This model uses the "blog.db" database.


db.connect()
try:
    db.create_tables([Blog_post, Category])
except OperationalError as e:
    # print(e)
    pass
