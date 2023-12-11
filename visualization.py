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

print("\nQuery_b Result:")

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

import matplotlib.pyplot as plt

# Query a Result for Visualization
labels_a = [row[0] for row in result_a]
values_a = [row[1] for row in result_a]

# Plotting a bar chart for Query a
plt.figure(figsize = (8, 5))
plt.bar(labels_a, values_a, color = 'blue')
plt.xlabel('Taster')
plt.ylabel('Points')
plt.ylim([70, 100]) 
plt.title('Average points by taster')
plt.savefig('bar_chart_a.png')
plt.show()

# Query b Result for Visualization
labels_2b = [row[1] for row in result_b]
values_2b = [row[0] for row in result_b]

# Plotting a pie chart for Query b
plt.figure(figsize = (8, 8))
plt.pie(labels_2b, labels = values_2b, autopct = '%1.1f%%', startangle = 140)
plt.title('Percentage of Wine Production')
plt.savefig('pie_chart_b.png')
plt.show()

# Query c Result for Visualization
values_c = [int(row[0]) for row in result_c]
label_c = [str(row[1]) for row in result_c]
# Plotting a bar chart for Query c

plt.figure(figsize = (8, 5))
plt.plot(label_c, values_c, color = 'maroon')
plt.bar(label_c, values_c, color = 'cyan')
plt.xlabel('Points')
plt.ylabel('Country')
plt.title('Avarage Points in Countries')
plt.ylim([70, 100]) 
plt.savefig('bar_chart_c.png')
plt.show()