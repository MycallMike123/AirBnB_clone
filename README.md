 Airbnb Console

This project is a command-line interpreter for managing Airbnb-like data. It allows users to interactively create, retrieve, update, and delete objects such as users, places, states, cities, amenities, and reviews.

## Command Interpreter

### Starting the Command Interpreter
To start the command interpreter, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the console.py file using Python 3.

```bash
$ python3 console.py

Using the Command Interpreter
Once the command interpreter is started, you can use the following commands:

create: Creates a new instance of a given class, saves it to the JSON file, and prints its ID.
show: Prints the string representation of an instance based on the class name and ID.
destroy: Deletes an instance based on the class name and ID.
update: Updates an instance based on the class name and ID by adding or updating attributes.
all: Prints all string representations of instances based on the class name.
quit or EOF: Exits the command interpreter.

Examples
Here are some examples of using the command interpreter:

(hbnb) create User
f1b9de96-bc4d-4c12-aa51-63704ad63fa0
(hbnb) show User f1b9de96-bc4d-4c12-aa51-63704ad63fa0
[User] (f1b9de96-bc4d-4c12-aa51-63704ad63fa0) {'email': '', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) update User f1b9de96-bc4d-4c12-aa51-63704ad63fa0 email "test@example.com"
(hbnb) show User f1b9de96-bc4d-4c12-aa51-63704ad63fa0
[User] (f1b9de96-bc4d-4c12-aa51-63704ad63fa0) {'email': 'test@example.com', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) all User
["[User] (f1b9de96-bc4d-4c12-aa51-63704ad63fa0) {'email': 'test@example.com', 'password': '', 'first_name': '', 'last_name': ''}"]
(hbnb) quit
$
