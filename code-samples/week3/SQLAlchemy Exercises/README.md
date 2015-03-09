#SQLALchemy Exercises

####What is SQLAlchemy?
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

####What is the different between SQLAlchemy and psycopg2?
SQLAlchemy is a ORM, psycopg2 is a database driver. These are completely different things: SQLAlchemy generates SQL statements and psycopg2 sends SQL statements to the database. SQLAlchemy depends on psycopg2 or other database drivers to communicate with the database.

As a rather complex software layer SQLAlchemy does add some overhead but it also is a huge boost to development speed, at least once you learned the library. SQLAlchemy is a excellent library and will teach you the whole ORM concept, but if you don't want to generate SQL statements to begin with then you don't want SQLAlchemy.

[link to StackOverflow](http://stackoverflow.com/questions/8588126/sqlalchemy-or-psycopg2)

<br/>
*link:*
* [A simple SQLAlchemy Tutorial](http://www.blog.pythonlibrary.org/2012/07/01/a-simple-sqlalchemy-0-7-0-8-tutorial/)
