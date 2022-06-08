import mysql.connector

path = open("C:\\Users\\Mert\\Documents\\Marvel.txt")



try:

    connection = mysql.connector.connect(host = "localhost",
                                         database = "se226-marvel",
                                         user = "root",
                                         password = "5140")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS NewTable")
    mySQL_CreateTable = """ CREATE TABLE NewTable (
                         ID INT ,
                         MOVIE VARCHAR(50),
                         DATE VARCHAR(20),
                         MCU_PHASE VARCHAR(50))"""
    cursor.execute(mySQL_CreateTable)

    while path:
        text = path.readline()
        if text == "":
            break
        splitlines = text.split()
        mySQL_InsertTable = """ INSERT INTO NewTable (ID , MOVIE, DATE, MCU_PHASE)
                                VALUES (%s, %s, %s ,%s )"""
        record = (splitlines[0], splitlines[1], splitlines[2], splitlines[3])
        cursor.execute(mySQL_InsertTable, record)
        connection.commit()

    sqlListMovie = "SELECT MOVIE FROM NewTable"
    cursor = connection.cursor()
    cursor.execute(sqlListMovie)
    records = cursor.fetchall()
    for row in records:
        print(row)

    sqlDeleteMovie = "DELETE FROM NewTable WHERE MOVIE = 'TheIncredibleHulk'"
    cursor = connection.cursor()
    cursor.execute(sqlDeleteMovie)
    connection.commit()

    sql_remove = "SELECT * FROM marvel WHERE MCU_PHASE='Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_list)
    records2 = cursorObject.fetchall()
    for row2 in records2:
        print(row2)

sql_update = "UPDATE marvel SET DATE= 'November 3, 2017' WHERE MOVIE='Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_update)
    connection.commit()

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")