#! /usr/bin/python

import psycopg2

# Establish connection to PostgreSQL database
postgresqlconn = psycopg2.connect("dbname=zoo")

# Create a cursor object that will be used to perform queries
postgrecursor = postgresqlconn.cursor()

# Insert data into the animals table
postgrecursor.execute("insert into animals values ('Coco', 'gorilla', '2001-10-05')")

# Commit the insert
postgresqlconn.commit()

# Execute a query
postgrecursor.execute("select animals.species, count(diet.food) as meals from animals join diet on animals.species = diet.species group by animals.species")

# Fetch all the results of the query
rows = postgrecursor.fetchall()

# Display the results
for row in rows:
  print row

# Close the database connection
postgresqlconn.close()
