##데이터
column_names = ['name','salary','job']
db_rows =[('Alice',18000,'data scientist'),
          ('Bob',99000,'mid_level manager'),
          ('Frank',87000,'CEO')]

db = [dict(zip(column_names,row)) for row in db_rows]

print(db)
