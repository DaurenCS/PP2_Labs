import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="postgres",
  password="DaU178007")

cursor = conn.cursor()

cursor.execute(
  """ CREATE TABLE rank(
    name varchar(255),
    score int,
    level int
  );
  """
)
conn.commit()
cursor.close()
conn.close()
