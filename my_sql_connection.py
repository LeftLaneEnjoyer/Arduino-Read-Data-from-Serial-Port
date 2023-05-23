import mysql.connector

class mymysqlconnector:
  def __init__(self, data_insert):
    self.data_insert = data_insert
    
    
    self.connection = mysql.connector.connect(
                  host='localhost',
                  database='temperatur',
                  user='root',
                  password=''
              )
    self.cursor = self.connection.cursor()
      
  def inserttemp(self):

      test = [self.data_insert]
              # prepare the SQL query to insert data into the table with a timestamp column
      sql_query = """INSERT INTO data (temperatur, uhrzeit) 
                      VALUES (%s, NOW())"""

        # define the values for the query
      values = test
        # execute the query
      self.cursor.execute(sql_query, values)

        # commit the changes to the database
      self.connection.commit()
      
  def insertluft(self):
    test = [self.data_insert]
              # prepare the SQL query to insert data into the table with a timestamp column
    sql_query = """INSERT INTO luft (feuchtigkeit, uhrzeit) 
                      VALUES (%s, NOW())"""

        # define the values for the query
    values = test
        # execute the query
    self.cursor.execute(sql_query, values)

        # commit the changes to the database
    self.connection.commit()
      
          
        

  def closeconnection(self):     # close the cursor and connection
    if (self.connection.is_connected()):
      self.cursor.close()
      self.connection.close()
  #print("MySQL connection is closed")
          

        
