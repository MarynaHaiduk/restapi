# README #

The Agify API is a simple RESTful interface for getting the average age of a person with a particular name,
the code contained in this repository is capable of pulling age data from the API.

example:
```python
dashdanw@Dashs-MacBook-Pro python-take-home-agify % poetry shell
Python 3.9.10 (main, Jan 15 2022, 11:40:53) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [2]: from src.agify.client import AgifyAPIClient

In [3]: c=AgifyAPIClient()

In [5]: data = c.fetch("Dash")

In [6]: data.name
Out[6]: 'Dash'

In [7]: data.age
Out[7]: 33

```

For this coding challenge you will use the API in src/agify/client.py to pull data for the 100 most common names from the agify API, store it locally using a database of your choice (sqlite may be the easiest option), and provide that data  through a restful interface. 

It is up to you which parts you want to focus on, the most important things are that you are able to demonstrate your strong suits and provide a minimum viable functionality. We should be able to query the DB for information and recieve it back.

The Data: (data)

```json
[
  'James',
  'Robert',
  'John',
  'Michael',
  'William',
  'David',
  'Richard',
  'Joseph',
  'Thomas',
  'Charles',
  'Christopher',
  'Daniel',
  'Matthew',
  'Anthony',
  'Mark',
  'Donald',
  'Steven',
  'Paul',
  'Andrew',
  'Joshua',
  'Kenneth',
  'Kevin',
  'Brian',
  'George',
  'Edward',
  'Ronald',
  'Timothy',
  'Jason',
  'Jeffrey',
  'Ryan',
  'Jacob',
  'Gary',
  'Nicholas',
  'Eric',
  'Jonathan',
  'Stephen',
  'Larry',
  'Justin',
  'Scott',
  'Brandon',
  'Benjamin',
  'Samuel',
  'Gregory',
  'Frank',
  'Alexander',
  'Raymond',
  'Patrick',
  'Jack',
  'Dennis',
  'Jerry',
  'Tyler',
  'Aaron',
  'Jose',
  'Adam',
  'Henry',
  'Nathan',
  'Douglas',
  'Zachary',
  'Peter',
  'Kyle',
  'Walter',
  'Ethan',
  'Jeremy',
  'Harold',
  'Keith',
  'Christian',
  'Roger',
  'Noah',
  'Gerald',
  'Carl',
  'Terry',
  'Sean',
  'Austin',
  'Arthur',
  'Lawrence',
  'Jesse',
  'Dylan',
  'Bryan',
  'Joe',
  'Jordan',
  'Billy',
  'Bruce',
  'Albert',
  'Willie',
  'Gabriel',
  'Logan',
  'Alan',
  'Juan',
  'Wayne',
  'Roy',
  'Ralph',
  'Randy',
  'Eugene',
  'Vincent',
  'Russell',
  'Elijah',
  'Louis',
  'Bobby',
  'Philip',
  'Johnny'
]
```
