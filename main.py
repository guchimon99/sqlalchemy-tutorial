import sqlalchemy

from engine_instance import engine
from tables import Base, User

def main():
  print('sqlalchemy version is {0}'.format(sqlalchemy.__version__))
  Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
