import psycopg2
from config import params
import csv


def to_sql(list):
    slist = "{"
    for l in range(len(list)):
        slist += "{"
        slist += f'"{list[l][0]}", "{list[l][1]}"'
        slist += '}'
        if l != len(list)-1:
            slist += ','
    return slist+"}"


def add_multiple(list, size):
    config = None
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        command = f"CALL insert_many('{to_sql(list)}', {size})"
        current.execute(command)
        config.commit()
        current.close()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def pagination(limit, offset):
    config = None
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        command = f"select * from pagination('{limit}', '{offset}');"
        current.execute(command)
        print(*current.fetchall(), '\n')
        config.commit()
        current.close()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def act(commands):
    config = None
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(commands)
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def add_num(name, num):
    config = None
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        command = f"CALL insert_one('{name}', '{num}')"
        current.execute(command)
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def del_num(name):
    config = None
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        command = f"CALL deleting('{name}')"
        current.execute(command)
        config.commit()
        current.close()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def upd_num(name, num):
    commands = (
        f"""
        UPDATE accounts SET tell = '{num}' WHERE username = '{name}';
        """
        )
    act(commands)


def upd_name(name, num):
    commands = (
        f"""
        UPDATE accounts SET username = '{name}' WHERE tell = '{num}';
        """
        )
    act(commands)


def show(f):
    commands = [
        """
        SELECT * FROM accounts;
        """,
        """
        SELECT * FROM accounts
        ORDER BY username;
        """,
        """
        SELECT * FROM accounts
        ORDER BY tell;
        """
        ]
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(commands[f])
        print(*current.fetchall(), '\n')
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()

def name_pattern(pattern):
    command = (
        f'''
        SELECT
        *
        FROM
        pattern_names ('{pattern}%');
        '''
    )
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        print(*current.fetchall(), '\n')
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


def tell_pattern(pattern):
    command = (
        f'''
        SELECT
        *
        FROM
        pattern_tell ('{pattern}%');
        '''
    )
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        print(*current.fetchall(), '\n')
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    finally:
        if config is not None:
            config.close()


while True:
    c = int(input(f"{'-'*78}\n0 - Add, 1 - Delete, 2 - Update, 3 - Quite, 4 - Show, 5 - Find name by pattern,\n"
                  '6 - Find tell by pattern, 7 - Add multiple contacts, 8 - Pagination, 9 - CSV\nEnter the number:\n'))
    if c == 0:
        name = str(input('Name:\n'))
        num = str(input('Number:\n'))
        try:
            add_num(name, num)
            print("Success\n")
        except:
            print("Error")
            break
    elif c == 1:
        name = str((input('Name:\n')))
        try:
            del_num(name)
            print("Success\n")
        except:
            print("Error")
            break
    elif c == 2:
        flag = int(input('1 - Change name, 2 - Change number\n'))
        try:
            if flag == 1:
                num = str(input('Number:\n'))
                name = str(input('Name:\n'))
                upd_name(name, num)
            else:
                name = str(input('Name:\n'))
                num = str(input('Number:\n'))
                upd_num(name, num)
            print("Success\n")
        except:
            print("Error")
            break
    elif c == 3:
        break
    elif c == 4:
        f = int(input('Filter mode: 0 - date, 1 - name, 2 - number\n'))
        show(f)
    elif c == 5:
        pattern = input('Enter a pattern:\n')
        name_pattern(pattern)
    elif c == 6:
        pattern = input('Enter a pattern:\n')
        tell_pattern(pattern)
    elif c == 7:
        size = int(input('Enter the size:\n'))
        arr = []
        for i in range(size):
            name = input(f'Enter the {i + 1} name:\n')
            tell = input(f'Enter the {i + 1} number:\n')
            arr.append([name, tell])
        print(arr)
    elif c == 8:
        limit = input("Enter the limit:\n")
        offset = input("Enter the offset:\n")
        pagination(limit, offset)
    elif c == 9:
        with open('data.csv') as f:
            r = csv.reader(f)
            for i in r:
                add_num(i[0], i[1])
        print('Success')
