from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from .config import meta, engine


users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('first_name', String(50), ),
              Column('last_name', String(50)),
              Column('email', String(50), unique=True),
              Column('hashed_password', String(200)),
              Column('is_active', Boolean, nullable=True, default=False),
              )

meta.create_all(engine)