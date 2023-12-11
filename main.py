import psycopg2 

username = 'postgres'
password = '7256'
database = 'postgres'
host = 'localhost'
port = '5432'

# Connect to PostgreSQL
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
# Create a cursor
cur = conn.cursor()

# Query a
query_a = """
    SELECT taster_name, AVG(e.points) AS average_evaluation
    FROM wine w
    JOIN evaluation e ON w.eva_id = e.eva_id
    JOIN taster ta ON ta.taster_id = e.taster_id
    GROUP BY taster_name;
"""

cur.execute(query_a)
result_a = cur.fetchall()

print("Query_a result:")

for row in result_a:
    print(row)

# Query b
query_b = """
SELECT country, COUNT(*) AS wine_count
FROM wine w
JOIN location_ l ON w.wine_id = l.wine_id
GROUP BY country;
"""
cur.execute(query_b)
result_b = cur.fetchall()

print("\nQuery_b result:")

for row in result_b:
    print(row)

# Query c
query_c = """
SELECT AVG(e.points) AS average_evaluation, l.country 
FROM wine w
JOIN evaluation e ON w.eva_id = e.eva_id
JOIN taster ta ON ta.taster_id = e.taster_id
JOIN location_ l ON l.wine_id = w.wine_id
GROUP BY l.country;
"""
cur.execute(query_c)
result_c = cur.fetchall()

print("\nQuery_c result:")

for row in result_c:
    print(row)

# Close communication with the database
cur.close()
conn.close()