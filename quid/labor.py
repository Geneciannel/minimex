import psycopg2

# Assuming 'con' is the database connection
with con.cursor() as cur:
    # Inside this block, 'cur' is the cursor object
    # You can perform database operations using 'cur'

    # Example: Execute a query
    cur.execute("SELECT * FROM my_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# After the block, the cursor is automatically closed and resources are released
