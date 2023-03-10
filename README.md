<h1 align="center">AirBnB clone - The console</h1>

---
![AIRBNB-1](https://scontent.ftun9-1.fna.fbcdn.net/v/t1.15752-9/332943001_1148770339848776_1838865706291267138_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=79i4d4CnptoAX9aNJcs&tn=fu1T55lF8FGUQoRe&_nc_ht=scontent.ftun9-1.fna&oh=03_AdTwcypcHtPJ3cyPPMCOZeibmEqIYDbrtDYVvrcH04CCJQ&oe=641F0242)
---


## Description:

- This is the first step of getting to clone the AirBnB. this repo contains an implementation of the console

- The project currently only implements the back-end console.


### Files contents :card_index_dividers:

| File                                               | Description                   |
| -------------------------------------------------- | ----------------------------- |
| [models](./models/)                                | Our Package                   |
| [tests](./tests/)                                  | Contains test files           |
| [models/engine](./models/engine/)                  | will contain our file storage |
| [console.py](./console.py)                         | Our console                   |
| [__init__.py](./models/__init__.py)                | the __init__ file             |
| [base_model.py](./models/base_model.py)            | BaseModel the parent Class    |
| [file_storage.py](./models/engine/file_storage.py) | Our file storage              |
| [user.py](./models/user.py)                        | User Class                    |
| [state.py](./models/state.py)                      | State Class                   |
| [city.py](./models/city.py)                        | City Class                    |
| [amenity.py](./models/amenity.py)                  | Amenity Class                 |
| [place.py](./models/place.py)                      | Place Class                   |
| [review.py](./models/review.py)                    | Review Class                  |

---

## Requirements:

```
You need to install python3
```

## Installation

First things first cloning

```bash
git clone https://github.com/weedii/holbertonschool-AirBnB_clone.git
```
Second navigate (cd) to the newly created directory
```bash
cd holbertonschool-AirBnB_clone 
``` 
Congrats u can now start the console
```bash
./console.py 
```

---

### Using the Console

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) Exiting ...
```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py

```
(hbnb) quit
Exiting ...
```

$ ./console.py

```
(hbnb) EOF
Exiting ...
```

---

## How to use the commands

| Commands | Description                                 |
| -------- | ------------------------------------------- |
| Help     | displays all commands available             |
| Create   | Create object and print id                  |
| Update   | updates attribute of an object              |
| Destroy  | destroys specified object                   |
| show     | retrieve an object from a file, a database. |
| all      | display all objects in class                |
| quit     | Exits concol                                |


## Exemples:

$ ./console.py

```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

---

## Authors :black_nib:
* Amine Khammassi <[Amine Khammassi](https://github.com/aminekham)> Email:<5785@holbertonstudents.com>
* Wael Abidi <[Wael Abidi](https://github.com/weedii)> Email: <5684@holbertonstudents.com>
