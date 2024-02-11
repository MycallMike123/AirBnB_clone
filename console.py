#!/usr/bin/python3
"""Module for the Airbnb Console"""
import cmd
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""

    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']
    dotcmds = ['.all()', '.count()']

    def do_create(self, arg):
        """Creates a new instance of BaseModel or User, saves it, \
                and prints the id"""

        if arg == '':
            print('** class name missing **')

        elif arg not in HBNBCommand.classes:
            print('** class doesn\'t exist **')

        else:
            if arg == 'BaseModel':
                instance = BaseModel()

            elif arg == 'User':
                instance = User()

            elif arg == 'Place':
                instance = Place()

            elif arg == 'State':
                instance = State()

            elif arg == 'City':
                instance = City()

            elif arg == 'Amenity':
                instance = Amenity()

            elif arg == 'Review':
                instance = Review()

            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        args = arg.split()

        if arg == '':
            print('** class name missing **')

        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')

        else:
            if len(args) < 2:
                print('** instance id missing **')

            else:
                class_name = args[0]
                objid = args[1]
                key = class_name + '.' + objid

                try:
                    print(storage.all()[key])

                except KeyError:
                    print('** no instance found **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = arg.split()

        if arg == '':
            print('** class name missing **')

        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')

        else:
            if len(args) < 2:
                print('** instance id missing **')

            else:
                class_name = args[0]
                objid = args[1]
                key = class_name + '.' + objid

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all instances"""

        args = arg.split()
        res = []
        if len(args) != 0:

            if args[0] not in HBNBCommand.classes:
                print('** class doesn\'t exist **')
                return

            else:

                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        res.append(value.__str__())

        else:
            for key, value in storage.all().items():
                res.append(value.__str__())
        print(res)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        args = arg.split()

        if arg == '':
            print('** class name missing **')

        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')

        elif len(args) < 2:
            print('** instance id missing **')

        elif len(args) < 3:
            print('** attribute name missing **')

        elif len(args) < 4:
            print('** value missing **')

        else:
            class_name = args[0]
            objid = args[1]
            attr = args[2]
            value = args[3]
            oob = ['id', 'created_at', 'updated_at']

            if attr in oob:
                print('** attribute can\'t be updated **')
                return

            """Begins string validity test"""
            if value[0] == '"' and value[-1] == '"' or value[0] == "'":
                if value[0] != '"':
                    print("** A string argument must be between \
                            double quotes **")
                    return

                value = value[1:-1]
            else:
                try:
                    for c in value:
                        if c == '.':
                            value = float(value)
                            break

                    else:
                        value = int(value)

                except ValueError:
                    print("** A string argument must \
                            be between double quote **")

            if (attr[0] == '"' and attr[-1] == '"')\
               or attr[0] == "'" or attr[-1] == "'":
                if attr[0] != '"' or attr[-1] == "'":
                    print("** A string argument must be between \
                            double quotes **")
                    return

                attr = attr[1:-1]

            """string validity test ends"""
            key = class_name + '.' + objid

            try:
                inst = storage.all()[key]
                inst.__dict__[attr] = value
                inst.save()

            except KeyError:
                print('** no instance found **')

    def do_BaseModel(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, value in storage.all().items():

            if type(value).__name__ == 'BaseModel':
                obj.append(value)

        if argument in HBNBCommand.dotcmds:
            res = [value.__str__() for value in obj]
            if argument == HBNBCommand.dotcmds[0]:
                print(res)

            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':

                return cmd.Cmd.default(self, arg)
            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':

            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[9:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'BaseModel.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'BaseModel.' + args_list[0]

                        try:
                            instance = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dict_args:
                            keyval = s.split(':')
                            key = keyval[0]
                            value = keyval[1]

                            while(value[0] == " "):
                                value = value[1:]
                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (value[0] == '"' and value[-1] == '"')\
                               or (value[0] == "'" and value[-1] == "'"):
                                value = value[1:-1]

                            else:
                                for c in value:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in value:
                                        if c == '.':
                                            value = float(value)
                                            break

                                    else:
                                        value = int(value)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = value
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                value = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """Begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if value[0] == '"' and value[-1] == '"':
                    value = value[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for j in value:
                            if j == '.':
                                value = float(value)
                                break

                        else:
                            value = int(value)

                    except ValueError:
                        pass

                """ string validity test ends """

                key = 'BaseModel.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = value
                    inst.save()

                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_User(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'User':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]
            if argument == HBNBCommand.dotcmds[0]:
                print(res)

            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[9:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'User.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if arg[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'User.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dict_args:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]

                            while(val[0] == " "):
                                val = val[1:]
                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:

                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:
                                        if c == '.':
                                            value = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """begin string validity test"""

                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:
                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """string validity test ends"""

                key = 'User.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = value
                    inst.save()
                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_Place(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'Place':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]
            if argument == HBNBCommand.dotcmds[0]:
                print(res)
            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)
            else:
                model_id = argument[9:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'Place.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'Place.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dictargs:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]
                            while(val[0] == " "):
                                val = val[1:]
                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:
                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:

                                        if c == '.':
                                            val = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """Begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:

                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """string validity test ends"""

                key = 'Place.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = val
                    inst.save()

                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_State(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'State':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]
            if argument == HBNBCommand.dotcmds[0]:
                print(res)

            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, argument)

            else:
                model_id = argument[9:-1]
                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'State.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'State.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dictargs:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]
                            while(val[0] == " "):
                                val = val[1:]

                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:
                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:
                                        if c == '.':
                                            val = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """Begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:
                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """ string validity test ends """

                key = 'State.' + model_id
                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = val
                    inst.save()
                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_City(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'City':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]

            if argument == HBNBCommand.dotcmds[0]:
                print(res)

            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[9:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'City.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)
            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'City.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dict_args:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]

                            while(val[0] == " "):
                                val = val[1:]

                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return
                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:
                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:
                                        if c == '.':
                                            val = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """Begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:
                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """string validity test ends"""

                key = 'City.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = val
                    inst.save()

                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_Amenity(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'Amenity':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]

            if argument == HBNBCommand.dotcmds[0]:
                print(res)

            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[6:-1]

                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in obj:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                model_id = argument[9:-1]
                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'Amenity.' + model_id
                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'Amenity.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dict_args:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]

                            while(val[0] == " "):
                                val = val[1:]

                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:
                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:
                                        if c == '.':
                                            val = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:

                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """string validity test ends"""

                key = 'Amenity.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = val
                    inst.save()

                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_Review(self, arg):
        obj = []
        parse_line = cmd.Cmd.parseline(self, arg)
        argument = parse_line[2]

        for key, val in storage.all().items():
            if type(val).__name__ == 'Review':
                obj.append(val)

        if argument in HBNBCommand.dotcmds:
            res = [val.__str__() for val in obj]
            if argument == HBNBCommand.dotcmds[0]:
                print(res)
            elif argument == HBNBCommand.dotcmds[1]:
                print(len(res))

        elif argument[0:6] == '.show(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)
            else:
                model_id = argument[6:-1]
                if model_id == '':
                    print("** instance id missing **")
                    return

                for instance in objects:
                    if instance.id == model_id:
                        print(instance)
                        break

                else:
                    print('** no instance found **')

        elif argument[0:9] == '.destroy(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)
            else:
                model_id = argument[9:-1]
                if model_id == '':
                    print("** instance id missing **")
                    return

                key = 'Review.' + model_id

                try:
                    del storage.all()[key]
                    storage.save()

                except KeyError:
                    print('** no instance found **')

        elif argument[0:8] == '.update(':
            if argument[-1] != ')':
                return cmd.Cmd.default(self, arg)

            else:
                args = argument[8:-1]
                args_list = args.split(',')
                oob = ['id', 'created_at', 'updated_at']

                if len(args_list) < 2 and args_list[0] == '':
                    print('** instance id missing **')
                    return

                elif len(args_list) < 2:
                    print('** attribute name missing **')
                    return

                else:
                    i = 0
                    while (i < len(args_list)):
                        while(args_list[i][0] == " "):
                            args_list[i] = args_list[i][1:]
                        i += 1

                    if args_list[1][0] == '{' and args_list[-1][-1] == '}':
                        dict_args = args_list[1:]
                        dict_args[0] = dict_args[0][1:]
                        dict_args[-1] = dict_args[-1][:-1]
                        key = 'Review.' + args_list[0]

                        try:
                            inst = storage.all()[key]

                        except KeyError:
                            print('** no instance found **')
                            return

                        for s in dict_args:
                            keyval = s.split(':')
                            key = keyval[0]
                            val = keyval[1]
                            while(val[0] == " "):
                                val = val[1:]

                            if key in oob:
                                print('** attribute can\'t be updated **')
                                return

                            if (key[0] == '"' and key[-1] == '"')\
                               or (key[0] == "'" and key[-1] == "'"):
                                key = key[1:-1]

                            else:
                                print("** Dictionary object keys must be \
strings **")
                                return

                            if (val[0] == '"' and val[-1] == '"')\
                               or (val[0] == "'" and val[-1] == "'"):
                                val = val[1:-1]

                            else:
                                for c in val:
                                    if c == " ":
                                        print("** A string argument with a \
space must be between double quotes **")
                                        return

                                try:
                                    for c in val:
                                        if c == '.':
                                            val = float(val)
                                            break

                                    else:
                                        val = int(val)

                                except ValueError:
                                    pass

                            inst.__dict__[key] = val
                            inst.save()
                        return

                    elif len(args_list) < 3:
                        print('** value missing **')
                        return

                model_id = args_list[0]
                attr = args_list[1]
                val = args_list[2]

                if attr in oob:
                    print('** attribute can\'t be updated **')
                    return

                """begin string validity test"""
                if (attr[0] == '"' and attr[-1] == '"'):
                    attr = attr[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]

                else:
                    for i in attr:
                        if i == " ":
                            print("** A string argument with a space \
must be between double quotes **")
                            return

                    try:
                        for c in val:
                            if c == '.':
                                val = float(val)
                                break

                        else:
                            val = int(val)

                    except ValueError:
                        pass

                """string validity test ends"""

                key = 'Review.' + model_id

                try:
                    inst = storage.all()[key]
                    inst.__dict__[attr] = val
                    inst.save()

                except KeyError:
                    print('** no instance found **')

        else:
            return cmd.Cmd.default(self, arg)

    def do_quit(self, arg):
        """Quit command to exit from cmd"""

        return True

    def do_EOF(self, arg):
        """Exiting the program"""

        print()
        return True

    def emptyline(self):
        """Empty line + Enter shouldn't execute anything"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
