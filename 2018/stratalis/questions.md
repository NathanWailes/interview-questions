## Question 1 of 8

Implement the *CargoShip* class so that:

- *load* adds all items from *new_cargo* to the *cargo*.  *new_cargo* and *cargo* are lists of tuples where the first 
element in the tuple is a port name and the second element is the item weight.
- *unload* removes items from *cargo* that are in the same port and returns them as a list of tuples.  if there are no 
items for that port, then an empty list should be returned.
- *can_depart* returns *True* if the sum of all weights in cargo is less than or equal to the *capacity*, and *False* 
if not.

For example, if a new *CargoShip* is created with capacity 10 and *load* is called with `[("New York", 1), ("London", 
20)]`, then calling `unload("New York")` should return `[("New York", 1)]`, `cargo` should have the value of 
`[("London"), 20)]` and calling `can_depart()` should return *False*. 


### Starter code:

    class CargoShip:
        
        def __init__(self, capacity):
            self.cargo = []
            self.capacity = capacity
            
        def unload(self, port):
            """
            :param port: (String)
            :returns: [(String, Int)]
            """
            return None
        
        def can_depart(self):
            """
            :returns: (Bool)
            """
            return None
        
        def load(self, new_cargo):
            """
            :param new_cargo: [(String, Int)]
            """
            pass
        
    
    ship = CargoShip(10)
    ship.load([("New York", 1), ("London", 20)])
    print(ship.unload("New York")) #should print [("New York", 1)]
    print(ship.cargo) #should print [("London", 20)]
    print(ship.can_depart()) #should print False


## Question 2 of 8

It took 2040 digits to assign every employee a number (from 1 to N).

How many employees are there?  For example, it takes 15 digits (1 2 3 4 5 6 7 8 9 10 11 12) to assign numbers to 12 
employees.


## Question 3 of 8

Design a data structure that can **EFFICIENTLY** store and check if the total of any three successively added elements
is equal to a given total.

For example, `MovingTotal()` creates an empty container with no existing totals.  `append([1, 2, 3])` appends elements
`[1, 2, 3]`, which means that there is only one existing total (1 + 2 + 3 = 6).  `append([4])` appends element 4 and 
creates an additional total from `[2, 3, 4]`.  There would now be two totals (1 + 2 + 3 = 6 and 2 + 3 + 4 = 9).  At this
point `contains(6)` and `contains(9)` should return `True`, while `contains(7)` should return `False`.

### Starter code

    class MovingTotal:
    
        def append(self, numbers):
            """
            :param numbers: (list) The list of numbers.
            """
            pass
    
        def contains(self, total):
            """
            :param total: (int) The total to check for.
            :returns: (bool) If MovingTotal contains the total.
            """
            return None
    
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))



## Question 4 of 8

A character in a platformer game is standing on a single row of floor tiles numbered 0 to N, at position X.

When the character moves, the tile at the previous position disappears.  The character can only move left and right, and
always jumps over one tile, and any holes.  The character will not move if there are no tiles left to move to (you do 
not need to implement this in the code).

Implement a class that models this behavior and can report the character's position.

For example, `Platformer(6, 3)` creates a row of 6 tiles (numbered 0 to 5) and a character positioned on tile 3 [0 1 2
(3) 4 5].  A call to `jump_left()` moves the character two tiles to the left and the tile at position 3 disappears [0 
(1) 2 4 5].  A subsequent call to `jump_right()` moves the character two tiles to the right and the tile at position 1
disappears, skipping tiles that have disappeared [0 2 (4) 5].

### Starter code

    class Platformer:
    
        def __init__(self, n, x):
            """
            :param n: (int) The initial number of tiles.
            :param x: (int) The initial position of the character.
            """
            pass
            
        def jump_left(self):
            pass
    
        def jump_right(self):
            pass
    
        def position(self):
            """
            :returns: (int) The position of the character.
            """
            return None
    
    platformer = Platformer(6, 3)
    print(platformer.position())
    platformer.jump_left()
    print(platformer.position())
    platformer.jump_right()
    print(platformer.position())


## Question 5 of 8

A hospital patient tracking system is restructuring its patient records.  The current format is fragmented, each patient
is represented as a list of *namedtuple*.  Each element contains a different piece of information about the patent.

Your task is to write a function that merges all of the information into one *namedtuple*, named Patient, in the order
that it's provided to the function.

For example:

    PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
    personal_details = PersonalDetails(date_of_birth = '06-04-1972')
    
    Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
    complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
    
    print(MedicalRecord.merge(personal_details, complexion))

Should display:

    Patient(date_of_birth='06-04-1972', eye_color='Blue', hair_color='Black')

### Starter code

    from collections import namedtuple
    
    class MedicalRecord:
        
        @staticmethod
        def merge(*records):
            """
            :param records: (varargs list of namedtuple) The patient details.
            :returns: (namedtuple) named Patient, containing details from all records, in entry order.
            """
            return None
        
    PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
    personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                       
    Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
    complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
      
    print(MedicalRecord.merge(personal_details, complexion))



## Question 6 of 8

Given the following data definition, write a query that selects all customer names together with the number of 
transactions that they made. Customers with no transactions should be included as customers with 0 transactions.

    TABLE customers
      id INTEGER NOT NULL PRIMARY KEY
      name VARCHAR(30) NOT NULL
    
    TABLE transactions
      id INTEGER NOT NULL PRIMARY KEY
      customerId INTEGER REFERENCES customers(id)
      amount DECIMAL(15, 2) NOT NULL

See the example case for more details

### Example case


Suggested testing environment: http://sqlite.online/

Example case create statement:

    CREATE TABLE customers ( id INTEGER NOT NULL PRIMARY KEY, name VARCHAR(30) NOT NULL );
    
    CREATE TABLE transactions ( id INTEGER NOT NULL PRIMARY KEY, customerId INTEGER REFERENCES customers(id), amount DECIMAL(15,2) NOT NULL );
    
    INSERT INTO customers(id, name) VALUES(1, 'Steve'); INSERT INTO customers(id, name) VALUES(2, 'Jeff'); INSERT INTO transactions(id, customerId, amount) VALUES(1, 1, 100);

Expected output (in any order):

    name transactions
    Steve 1
    Jeff 0

Explanation:

In this example. There are two customers, Steve and Jeff. Steve has made one transaction. Jeff has made zero transactions.


## Question 7 of 8

Users of an online bulletin board are kept in table `users`:

    TABLE users
      id INTEGER PRIMARY KEY NOT NULL,
      email VARCHAR(50) NOT NULL,
      passwordHash VARCHAR(60) NOT NULL

Site admins need to be able to ban users.  Write a statement that will alter the table and add a column named `banned` 
with the following properties:

- The type must be integer.
- The default value is 0.
- The only allowed values are 0 and 1.

See the example case for more details.

### Example case

(Note from Nathan: I forgot to copy this.)


## Question 8 of 8

Information about people and their parents are stored in the following table:

    TABLE people
      id INTEGER NOT NULL PRIMARY KEY
      motherId INTEGER REFERENCES people(id)
      fatherId INTEGER REFERENCES people(id)
      name VARCHAR(30) NOT NULL
      age INTEGER NOT NULL

Write a query that selects the names of all parents together with the age of their youngest child.

See the example case for more details.

### Example case

Suggested testing environment: http://sqlite.online/

Example case create statement:

    CREATE TABLE people ( id INTEGER NOT NULL PRIMARY KEY, motherId INTEGER REFERENCES people(id), fatherId INTEGER REFERENCES people(id), name VARCHAR(30) NOT NULL, age INTEGER NOT NULL );
    
    INSERT INTO people(id, motherId, fatherId, name, age) VALUES(1, NULL, NULL, 'Adam', 50); INSERT INTO people(id, motherId, fatherId, name, age) VALUES(2, NULL, NULL, 'Eve', 50); INSERT INTO people(id, motherId, fatherId, name, age) VALUES(3, 2, 1, 'Cain', 30); INSERT INTO people(id, motherId, fatherId, name, age) VALUES(4, 2, 1, 'Seth', 20);

Expected output (in any order):

    name age
    Adam 20
    Eve 20

Explanation:

In this example. Adam and Eve are parents and have two children: Cain and Seth. Seth is younger and is 20 years old.
