import psycopg2
from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(
    database="library_api",
    user="app",
    password=os.getenv"db_pass",
    port = "5432",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()