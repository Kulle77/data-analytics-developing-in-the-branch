"""Functions for querying and processing GWZ sales data."""
import re
import pickle
import sqlite3

def connect_db(db_path):
    '''Create and return a database connection and cursor.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor

def get_gwz_sales_query(table_name="gwz_sales"):
    '''read and return the query from the sql file, replacing the table name'''
    with open("gwz_sales.sql", encoding="utf-8") as f:
        sql = f.read().lower()
    pattern = r"from\s+[`]?[\w\-\.\d]*gwz_sales[`]?"
    replacement = f"FROM {table_name}"
    return re.sub(pattern, replacement , sql, flags=re.IGNORECASE)

def daily_turnover(cursor):
    """Fetch and return the first 5 daily turnover records and the query used."""
    query = get_gwz_sales_query()
    cursor.execute(query)
    results = cursor.fetchall()[0:5]
    if "purchase_cost" in query:
        results = [(date, amount) for date, amount, purchase in results]
    with open('tests/daily_turnover.pkl', 'wb') as f:
        pickle.dump([results,query], f)
    return results, query

def purchase_cost(cursor):
    '''Fetch and return the first 5 records including purchase cost and the query used.'''
    query = get_gwz_sales_query()
    cursor.execute(query)
    results = cursor.fetchall()[0:5]
    with open('tests/purchase_cost.pkl', 'wb') as f:
        pickle.dump([results,query], f)
    return results, query

def rounding(cursor):
    '''Fetch and return the first 5 records including rounding and the query used.'''
    query = get_gwz_sales_query()
    cursor.execute(query)
    results = cursor.fetchall()[0:5]
    with open('tests/rounding.pkl', 'wb') as f:
        pickle.dump([results,query], f)
    return results, query

def date_sort(cursor):
    '''Fetch and return the first 5 records sorted by date.'''
    cursor.execute(get_gwz_sales_query())
    results = cursor.fetchall()[0:5]
    with open('tests/date_sort.pkl', 'wb') as f:
        pickle.dump(results, f)
    return results

if __name__ == "__main__":
    data = connect_db("data/gwz_sales.sqlite")
    daily_turnover(data)
    purchase_cost(data)
    rounding(data)
    date_sort(data)
