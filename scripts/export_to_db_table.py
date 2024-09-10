import psycopg2
import pandas as pd

def export_to_postgres(df, host, user, password, dbname):
    # Ensure columns are converted to native Python types (float and int)
    df['user_id'] = df['user_id'].astype(int)
    df['engagement_score'] = df['engagement_score'].astype(float)
    df['experience_score'] = df['experience_score'].astype(float)
    df['satisfaction_score'] = df['satisfaction_score'].astype(float)

    # Connect to PostgreSQL database
    db_connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=dbname
    )
    cursor = db_connection.cursor()

    # Create the table (if not already created)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_satisfaction (
        user_id BIGINT PRIMARY KEY,
        engagement_score FLOAT,
        experience_score FLOAT,
        satisfaction_score FLOAT
    )
    """)

    # Insert data into the table with conflict handling
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO user_satisfaction (user_id, engagement_score, experience_score, satisfaction_score)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING
        """, (int(row['user_id']), float(row['engagement_score']), float(row['experience_score']), float(row['satisfaction_score'])))

    # Commit the insertions
    db_connection.commit()

    # Run a SELECT query and display the output
    cursor.execute("SELECT * FROM user_satisfaction LIMIT 10")
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    db_connection.close()
