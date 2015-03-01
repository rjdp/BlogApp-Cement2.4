# BlogApp-Cement2.4
A basic Blog control CLI app.

Third-party Libraries used - `Peewee ORM` , `Cement 2.4` 
Python Interpreter = `Python 3.4.2`  
Database = `Sqlite3`  

Models for the Blog
=====================
1. Blog_post model with fileds `title`,`content`,`category` and an `id` field that is automatically generated by Sqlite as primary key field. 
2. Category models(lists available categories under which a blog post can be categorized) with a field `category` and `id` field automatically generated by Sqlite as a primary key field. 

Setting up for use
=====================
1. Run `rmodel.py` to create models for the minimal Blog . 
2. `BlogApp.py` is the main command-line app to control the Blog , usage is as given below. 

Using BlogApp
===============

**Usage** | **Description** 
----------|-----------------
`BlogApp.py` | Name of application itself. 
`BlogApp.py --help` | Lists help and commands available. 
`BlogApp.py post add "title" "content" `  | Adds a new blog a new blog post with title and content. 
`BlogApp.py post list`  | Lists all blog posts. 
`BlogApp.py post search "keyword"`  | Lists all blog posts where “keyword” is found in title and/or content. 
`BlogApp.py category add "category-name" ` | Creates a new category. 
`BlogApp.py category list` |  Lists all categories
`BlogApp.py category assign <post-id> <cat-id>` | Assigns category to post
`BlogApp.py post add "title" "content" --category="cat-name"` |  Adds a new blog a new blog post with title, content and assign a category to it. It category doesn’t exist, it is be created first.


Improvements for next version 
==============================
1. Needs Code refactoring .
2. More Error handling to make the usage graeful.
3. In-depth Study of the Cement Latest version Documentaion to make the utility near robust by using necessary framework features .
4. This app was made more to be result oriented inorder to meet a self imposed deadline ,so the code efficiency and best practices were not the top concern .

