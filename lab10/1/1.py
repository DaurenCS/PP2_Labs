import psycopg2
import random
import datetime

time = datetime.datetime.now()

def add():
  name = input('Eneter your name...\n')

  sql = f'select name  from contacts where name = \'{name}\''
  cursor.execute(sql)
  names = cursor.fetchall()

  if len(names)>0:
    print("sorry you alreadu exist\n")
  else:
    number = input('write your number...\n')
    sql1 = f'''insert into contacts(name,number,data)
    values(\'{name}\',\'{number}\',\'{time.strftime("%X")}\')

    '''

    cursor.execute(sql1)
    conn.commit()

    # cursor.close()
    # conn.close()

def delete():
  dname = input('who do you want to delete...\n')
  sql = f''' delete
  from contacts
  where name = \'{dname}\';
  
  '''
  cursor.execute(sql)
  conn.commit()
  # cursor.close()
  # conn.close()

def show():

  sql = '''select *
 from contacts 
  '''
  cursor.execute(sql)
  s = cursor.fetchall()

  print(s)

def sort():
  n = int(input('1 - sort with name, 2- sort wiht date\n'))
  
  sql = '''select *
  from contacts
  '''
  cursor.execute(sql)
  na = cursor.fetchall()
  if n == 1:
    na.sort(key=lambda x:x[0])
    print(na)
    if int(input('reverse it?   1-yes, 2-no\n')) == 1:
      na.reverse()
      print(na)
    else:
      pass
  elif n == 2:
    na.sort(key=lambda x:x[2])
    print(na)
    if int(input('reverse it?   1-yes, 2-no\n')) == 1:
      na.reverse()
      print(na)
    else:
      pass
  


conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="postgres",
  password="DaU178007")

cursor = conn.cursor()


run = True

while run:
  
  step = int(input('1 - add, 2 - delete, 3 - sort, 4 - show, 5 - exit\n '))

  if step == 1:
    add()

  if step == 2:
    delete()
  
  if step == 4:
    show()

  if step == 3:
    sort()

  if step == 5:
    run = False

cursor.close()
conn.close()
  
  
