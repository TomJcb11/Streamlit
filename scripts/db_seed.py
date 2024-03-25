import os
import pandas as pd
import psycopg2
from psycopg2 import sql

def createTables():
    conn = psycopg2.connect(
        host="db",
        dbname="postgres",
        user="postgres",
        password="example",
        port="5432"
    )
    cur = conn.cursor()

    directory = './csv'
    files = os.listdir(directory)

    for filename in files:
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(directory, filename))
            table_name = os.path.splitext(filename)[0]

            # Drop table if it already exists
            cur.execute(sql.SQL("DROP TABLE IF EXISTS {};").format(sql.Identifier(table_name)))
            conn.commit()

            # Create table
            create_table_query = "CREATE TABLE {} (".format(table_name)
            for col in df.columns:
                create_table_query += "{} text,".format(col)
            create_table_query = create_table_query[:-1] + ");"  # Remove last comma and add closing parenthesis
            cur.execute(create_table_query)
            conn.commit()

            # Insert data
            for index, row in df.iterrows():
                insert_query = "INSERT INTO {} VALUES (".format(table_name)
                for col in df.columns.str.replace(' ', '_'):
                    # Replace single quotes with two single quotes to escape them in SQL
                    value = str(row[col]).replace("'", "''")
                    insert_query += "'{}',".format(value)
                insert_query = insert_query[:-1] + ");"  # Remove last comma and add closing parenthesis
                cur.execute(insert_query)
                conn.commit()
            print (f"La table {table_name} a été créée et les données ont été insérées avec succès.")


    cur.close()
    conn.close()
createTables()