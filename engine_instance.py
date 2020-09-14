import os
from sqlalchemy import create_engine

path = os.getcwd()
engine = create_engine("sqlite:///{0}/tutorial.sqlite".format(path), echo=True)
