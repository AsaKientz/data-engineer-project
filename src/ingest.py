import psycopg2

# Class 
def make_db_conn(db_host, db_port, dbname, db_user, db_pw):
    db_conn = psycopg2.connect(host=db_host, port=db_port, dbname=dbname, user=db_user, password=db_pw)
    db_cursor = db_conn.cursor()
    return db_conn, db_cursor

def ratings_ingest(ratings_file):
    with open(ratings_file, 'r') as f:
        next(f)
        db_cursor.copy_from(f, 'user_rating', sep=',', columns = ('id_user','id_rating','rating','rating_timestamp'))
    db_conn.commit()
    
def all_ingest(credits_file, keywords_file, links_file, movies_file, ratings_file):
    ratings_ingest(ratings_file)
    

if __name__ == "__main__":
    db_host = "localhost" # either "localhost", a domain name, or an IP address.
    db_port = "5432" # default postgres port
    dbname = "Guild_takehome"
    db_user = "postgres"
    db_pw = "postgres"
    db_conn, db_cursor = make_db_conn(db_host, db_port, dbname, db_user, db_pw)
    
    ratings_ingest("data/ratings.csv")
