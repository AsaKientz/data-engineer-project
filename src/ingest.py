import psycopg2
import csv

# Sample parameters listed
def make_db_conn():
    db_host = "localhost"
    db_port = "5432"
    dbname = "Guild_takehome"
    db_user = "postgres"
    ## password would not be exposed here
    db_pw = "postgres"
    db_conn = psycopg2.connect(host=db_host, port=db_port, dbname=dbname, user=db_user, password=db_pw)
    return db_conn

def execute_query(query_string, new_conn):
    db_cursor = new_conn.cursor()
    db_cursor.execute(query_string)
    new_conn.commit()
    return db_cursor.fetchall()
        
def execute_insert(query_string, new_conn, insert_values):
    db_cursor = new_conn.cursor()
    db_cursor.execute(query_string, insert_values)
    new_conn.commit()
    db_cursor.close()
    new_conn.close()

def movies_ingest(movies_file):
    movies_temp_tbl = []
    with open(filename, 'r', encoding="utf8") as ratings:
        csv_ratings = csv.reader(ratings)
        next(csv_ratings)
        ## pull appropriate data from movies file into temp data structure
        for row in csv_ratings:
            m_id = row[5]
            imdb_id = row[6]
            title = [20]
            tagline = [19]
            overview = row[9]
            homepage = row[4]
            poster_path = row[11]
            original_title = row[8]
            runtime = row[16]
            budget = row[2]
            revenue = row[15]
            release_date = row[14]
            popularity = row[10]
            vote_avg = row[22]
            vote_count = row[23]
            is_adult = row[0]
            is_video = row[21]
        
        # id fields for dependent tables not listed here
        insert_query_string = """ INSERT INTO movie 
            (m_id, imdb_id, title, tagline, overview, homepage, poster_path, original_title,
            runtime, budget, revenue, release_date, popularity, vote_avg, vote_count, is_adult, is_video) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (m_id, imdb_id, title, tagline, overview, homepage, poster_path, original_title,
            runtime, budget, revenue, release_date, popularity, vote_avg, vote_count, is_adult, is_video)
        execute_insert(insert_query_string, new_conn, record_to_insert)

# Another method for a simpler file format
def ratings_ingest(ratings_file):
    with open(ratings_file, 'r') as f:
        next(f)
        db_cursor.copy_from(f, 'user_rating', sep=',', columns = ('id_user','id_rating','rating','rating_timestamp'))
    db_conn.commit()
    db_cursor.close()
    new_conn.close()

# Etcetera, etcetera
def credits_ingest(credits_file):
    pass

def keywords_ingest(keywords_file):
    pass

def links_ingest(links_file):
    pass

def all_ingest(credits_file, keywords_file, links_file, movies_file, ratings_file):
    credits_ingest(credits_file)
    keywords_ingest(keywords_file)
    links_ingest(links_file)
    movies_ingest(movies_file)
    ratings_ingest(ratings_file)
    

if __name__ == "__main__":
    # Files not added to Github due to large file size.  However, "ratings_small.csv" is present for testing.
    movies_file = "data/movies_metadata.csv"
    ratings_file = "data/ratings.csv"
    credits_file = "data/credits.csv"
    keywords_file = "data/keywords.csv"
    links_file = "data/links.csv"
    
    all_ingest(credits_file, keywords_file, links_file, movies_file, ratings_file)
