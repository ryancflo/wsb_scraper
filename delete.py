import sqlite3

conn = sqlite3.connect('reddit.db')

cur = conn.cursor()
cur.execute("""DELETE FROM mention""");
# cur.execute("""DELETE FROM stock""");
cur.execute("""DELETE FROM sqlite_sequence WHERE name='mention'""");
conn.commit()
conn.close()