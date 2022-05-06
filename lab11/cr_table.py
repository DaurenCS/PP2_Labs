import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="postgres",
  password="DaU178007")

cursor = conn.cursor()

cursor.execute(
  """ CREATE TABLE contacts1(
    name varchar(255),
    number varchar(255),
    data varchar(255)
  );
  """
)