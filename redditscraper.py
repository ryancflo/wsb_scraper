from psaw import PushshiftAPI
import yfinance as yf
import datetime as dt
import sqlite3

conn = sqlite3.connect('reddit.db')
c = conn.cursor()
c.execute("""
    SELECT symbol FROM stock
""")
stocks = c.fetchall()

api = PushshiftAPI()

start_time = int(dt.datetime(2021, 4, 3).timestamp())

submissions = api.search_submissions(after=start_time,
                            subreddit=['wallstreetbets','investing', 'stocks'],
                            filter=['url','author', 'title', 'subreddit'], limit = 10000)

# stonks = [stock[0] for stock in stocks]
for submission in submissions:
    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(words) > 0:
        print(cashtags)
        print(submission.title)

        for word in cashtags:
            if word in stocks:
                submitted_time = dt.datetime.fromtimestamp(submission.created_utc).isoformat()

                try:
                    #insert scraped reddit data into mention table
                    # share = cashtag.replace("$", "")
                    c.execute("""
                        INSERT INTO mention (dt, symbol, message, source, url)
                        VALUES (?, ?, ?, ?, ?)
                    """, (submitted_time, word, submission.title, submission.subreddit, submission.url))

                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()

print("finished")

# c.execute('SELECT symbol FROM mention') 
# for row in c:
#     data = yf.Ticker(row[0]).info
#     c.execute("""
#         INSERT INTO stock (symbol, name, exchange)
#         VALUES (?, ?, ?)
#     """, (data['symbol'], data['shortName'], data['country']))
#     conn.commit()
#     print(data['shortName'])
#     print(row[0])


