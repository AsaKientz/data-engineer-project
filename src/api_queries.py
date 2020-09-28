from ingest import make_db_conn, execute_query
import psycopg2

 ## PRODUCTION COMPANY DETAILS
## budget per year
def report_budget_per_yr():
    query_string =
    """SELECT 
        pc.name AS production_company,
        YEAR(m.release_date) AS release_year,
        SUM(m.budget) as total_budget
    FROM
        production_company pc
    LEFT JOIN movie_production_company mpc ON pc.id = mpc.id_production_company
    INNER JOIN movie m ON m.id = mpc.id_movie
    GROUP BY 
        pc.name, YEAR(m.release_date)
    ORDER BY 
        production_company, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)

## revenue per year
def report_revenue_per_yr():
    query_string = 
    """SELECT
        pc.name AS production_company,
        YEAR(m.release_date) AS release_year,
        SUM(m.revenue) as total_revenue
    FROM
        production_company pc
    LEFT JOIN movie_production_company mpc ON pc.id = mpc.id_production_company
    INNER JOIN movie m ON m.id = mpc.id_movie
    GROUP BY 
        pc.name, YEAR(m.release_date)
    ORDER BY 
        production_company, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)

## profit per year
def report_profit_per_yr():
    query_string = 
    """SELECT
        pc.name AS production_company,
        YEAR(m.release_date) AS release_year,
        (SUM(m.revenue) - SUM(m.budget)) as total_profit
    FROM
        production_company pc
    LEFT JOIN movie_production_company mpc ON pc.id = mpc.id_production_company
    INNER JOIN movie m ON m.id = mpc.id_movie
    GROUP BY 
        pc.name, YEAR(m.release_date)
    ORDER BY 
        production_company, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)

## releases by genre per year
def report_release_by_genre_per_yr():
    query_string = 
    """SELECT
        pc.name as production_company,
        YEAR(m.release_date) as release_year,
        g.name as genre,
        COUNT(m.id) as release_count
    FROM
        production_company pc
    LEFT JOIN movie_production_company mpc ON pc.id = mpc.id_production_company
    INNER JOIN movie m ON m.id = mpc.id_movie
    LEFT JOIN movie_genre mg ON m.id = mg.id_movie
    LEFT JOIN genre g ON mg.id_genre = g.id
    GROUP BY
        pc.name, YEAR(m.release_date), g.name
    ORDER BY 
        production_company, release_year, genre;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)


## average popularity of produced movies per year
def report_avg_pop_per_yr():
    query_string = 
        """SELECT
        pc.name as production_company,
        YEAR(m.release_date) as release_year,
        AVG(m.popularity) as avg_popularity
    FROM
        production_company pc
    LEFT JOIN movie_production_company mpc ON pc.id = mpc.id_production_company
    INNER JOIN movie m ON m.id = mpc.id_movie
    GROUP BY 
        pc.name, YEAR(m.release_date)
    ORDER BY 
        production_company, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)

########################################################################

## MOVIE GENRE DETAILS
## -------------------

## most popular genre by year
def report_most_pop_genre_by_yr():
    query_string = 
    """SELECT
        g.name as genre,
        YEAR(m.release_date) as release_year,
        AVG(m.popularity) as avg_popularity
    FROM
        genre g
    LEFT JOIN movie_genre mg ON g.id = mg.id_genre
    INNER JOIN movie m ON mg.id_move = m.id
    GROUP BY
        g.name, YEAR(m.release_date)
    ORDER BY
        genre, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)

## budget by genre by year
def report_budget_by_genre_per_yr():
    query_string = 
    """SELECT
        g.name as genre,
        YEAR(m.release_date) as release_year,
        SUM(m.budget) as total_budget
    FROM
        genre g
    LEFT JOIN movie_genre mg ON g.id = mg.id_genre
    INNER JOIN movie m ON mg.id_move = m.id
    GROUP BY
        g.name, YEAR(m.release_date)
    ORDER BY
        genre, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)
        
## revenue by genre by year
def report_revenue_by_genre_per_yr():
    query_string = 
    """SELECT
        g.name as genre,
        YEAR(m.release_date) as release_year,
        SUM(m.revenue) as total_revenue
    FROM
        genre g
    LEFT JOIN movie_genre mg ON g.id = mg.id_genre
    INNER JOIN movie m ON mg.id_move = m.id
    GROUP BY
        g.name, YEAR(m.release_date)
    ORDER BY
        genre, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)
        
## profit by genre by year
def report_profit_by_genre_per_yr():
    query_string = 
    """SELECT
        g.name as genre,
        YEAR(m.release_date) as release_year,
        (SUM(m.revenue) - SUM(m.budget)) as total_profit
    FROM
        genre g
    LEFT JOIN movie_genre mg ON g.id = mg.id_genre
    INNER JOIN movie m ON mg.id_move = m.id
    GROUP BY
        g.name, YEAR(m.release_date)
    ORDER BY
        genre, release_year;"""
    new_conn = make_db_conn()        
    return execute_query(query_string, new_conn)
        