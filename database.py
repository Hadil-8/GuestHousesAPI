import sqlite3
import pandas as pd



# Create a SQLite database connection
conn = sqlite3.connect('GHsys.db')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database URL
DATABASE_URL = "sqlite:///./GHsys.db"  # Example: SQLite database

# Create an engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite-specific argument
)

Base = declarative_base()

# Create a cursor object
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS GuestHouses(
    GuestHouse_id TEXT PRIMARY KEY,
    Name TEXT,
    Region TEXT,
    City TEXT,
    Address TEXT,
    Description TEXT,
    Phone TEXT,
    EcoCertification BOOLEAN,
    PricePerNight INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Activities(
    Activity_id TEXT PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    Type TEXT,
    Region TEXT,
    City TEXT,
    Price INTEGER
)
''')




# Commit the changes
conn.commit()


conn = sqlite3.connect('database.db')


# Load activities data
activities_df = pd.read_csv('Activities.csv')

# Create SQLAlchemy engine

# Load activities data into the database
activities_df.to_sql('Activities', conn, if_exists='append', index=False)

# Load guesthouses data
guesthouses_df = pd.read_csv('GuestHouses.csv')

# Load guesthouses data into the database
guesthouses_df.to_sql('GuestHouses', conn, if_exists='append', index=False)

# Commit the changes
conn.commit()

# Query to extract data from activities
activities_query = cursor.execute('SELECT * FROM Activities')
activities_data = activities_query.fetchall()

# Query to extract data from guesthouses
guesthouses_query = cursor.execute('SELECT * FROM GuestHouses')
guesthouses_data = guesthouses_query.fetchall()

print("\nActivities Data:")
for row in activities_data:
    print(row)

    
# Print the extracted data
print("GuestHouses Data:")
for row in guesthouses_data:
    print(row)



engine = create_engine('sqlite:///GHsys.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Close the connection
conn.close()