import psycopg2
import random
import datetime

time = datetime.datetime.now()




# TASK 1
def show():

  sql = '''create or replace function show()
  returns table(
      name varchar(255),
    number varchar(255),
    data varchar(255)
  )

  as
  $$
  begin 
  return query
  select  s.name, s.number, s.data from contacts as s;
end
$$ 
language plpgsql;

select *
 from show();

  '''
  cursor.execute(sql)
  s = cursor.fetchall()

  print(s)
#TASK 2
def add():

    name = input('Eneter your name...\n')
    
    cursor.execute(f'select name  from contacts where name = \'{name}\'')
    x = cursor.fetchall()

    if len(x)>0:
        string = f'''update contacts
                    set number  = $2
                    where contacts.name = iname ;
                    update contacts
                    set data = \'{time.strftime("%X")}\'
                    where contacts.name = iname ;
                    '''
                    
    else:
        string = f'''insert into contacts(name,number,data)
    values(iname,inumber,\'{time.strftime("%X")}\');'''

    number = input('write your number...\n')
    
    if (len(number) == 12 and number[0] == '+' and number[1] == '7' and number[2] == '7')or(len(number) == 11 and number[0] == '8' and number[1] == '7'):
        sql1 = f'''
        create or replace procedure add(iname varchar, inumber varchar)
        as
        $$
        begin
        {string}
       
        end;
        $$
        language plpgsql;

        call add('{name}','{number}')

        '''

        cursor.execute(sql1)
        conn.commit()
    else: 
        print("Invalid number")
#TASK 3
def ladd():
  m = input('Number of objects:\n')
  l = []
  for i in range(int(m)):
    name = input(f'{i}: Eneter your name...\n')
    cursor.execute(f'select name  from contacts where name = \'{name}\'')
    x = cursor.fetchall()

    if len(x)>0:
        string = f'''update contacts
                    set number  = $2
                    where contacts.name = iname ;
                    update contacts
                    set data = \'{time.strftime("%X")}\'
                    where contacts.name = iname ;
                    '''
                    
    else:
        string = f'''insert into contacts(name,number,data)
    values(iname,inumber,\'{time.strftime("%X")}\');'''

    number = input(f'{i}: write your number...\n')
    
    if (len(number) == 12 and number[0] == '+' and number[1] == '7' and number[2] == '7')or(len(number) == 11 and number[0] == '8' and number[1] == '7'):
        sql1 = f'''
        create or replace procedure add(iname varchar, inumber varchar)
        as
        $$
        begin
        {string}
       
        end;
        $$
        language plpgsql;

        call add('{name}','{number}')

        '''

        cursor.execute(sql1)
        conn.commit()
    else: 
      l.append((name, number))
  if len(l) > 0:
    print('Incorrect data:')
    for i in l:
      print(i, '\n')
#TASK 4
def quering():
    lim = int(input("Enter the lim\n"))
    x = int(input("Enter the setoff\n"))
    sql = f'''create or replace function task4(lim integer, x integer)
returns setof contacts
as
$$
begin
return query
select * from contacts
order by name
limit lim offset x;

end;
$$
language plpgsql;

select *
from task4({lim},{x});'''

    cursor.execute(sql)
    s = cursor.fetchall()
    print(s)

#TASK 5
def delete():
    n = int(input("1 - by Name?,  2 - by number?"))
    if n == 1:
        dname = input('who do you want to delete...\n')
        sql = f''' create or replace procedure delete1(iname varchar)
        as
        $$
        begin
            delete
            from  contacts 
            where contacts.name = iname;
        end;
        $$
        language plpgsql;
            call delete('{dname}');
        
        '''
        cursor.execute(sql)
        conn.commit()
    elif n == 2:
        dnum = input('Enter the Number...\n')
        sql = f''' create or replace procedure delete(iname varchar)
        as
        $$
        begin
            delete
            from  contacts 
            where contacts.number = iname;
        end;
        $$
        language plpgsql;
            call delete('{dnum}');
        
        '''
        cursor.execute(sql)
        conn.commit()




  


conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="postgres",
  password="DaU178007")

cursor = conn.cursor()


run = True

while run:
  
  step = int(input('1 - add, 2 - delete, 3 - quering, 4 - show, 5 - exit, 6 - add list\n '))

  if step == 1:
    add()

  if step == 2:
    delete()
  
  if step == 4:
    show()

  if step == 3:
    quering()

  if step == 5:
    run = False

  if step == 6:
    ladd()

cursor.close()
conn.close()