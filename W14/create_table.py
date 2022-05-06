import psycopg2
from config import params


def create_table():
    command = (
        '''
        CREATE TABLE accounts(
            username VARCHAR (255) UNIQUE NOT NULL,
            tell VARCHAR (13) UNIQUE NOT NULL
        );
        '''
    )
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        current.close()
        config.commit()

    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()


create_table()
