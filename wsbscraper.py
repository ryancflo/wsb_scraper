import praw
import datetime as dt
import re
import sys
sys.path.insert(0, 'vaderSentiment-master/vaderSentiment')
from vaderSentiment import SentimentIntensityAnalyzer
sys.path.insert(1, 'get_all_tickers-master/')
from get_all_tickers import get_tickers as gt

list_of_tickers = gt.get_tickers_filtered(mktcap_min = 1000)
lookup = set(list_of_tickers)
ticker_dict = {}

reddit = praw.Reddit(
    client_id="***********",
    client_secret="***********",
    password="***********",
    user_agent="***********",
    username="***********",
)

blacklist_words = [
   "YOLO", "TOS", "CEO", "CFO", "CTO", "DD","BRO", "BTFD", "WSB", "OK", "RH",
   "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP",
   "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "HAS", "PR", "PC", "ICE",
   "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD",
   "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM",
   "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW"
   "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ",
   "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG",
   "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE"
   "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT",
   "GG", "ELON"
]

subreddit = reddit.subreddit('WallStreetBets')
submission = subreddit.new(limit=100)

#analyze based on comment upvotes
def analyze(top_level_comment):
   vs = analyzer.polarity_scores(top_level_comment)
   print("{:-<65} {}".format(top_level_comment, str(vs)))

def add_ticker(word):
   if not word in ticker_dict:
         ticker_dict[word] = 1
   else:
         ticker_dict[word] += 1

#Without Dollar Sign
def extract_ticker(post):
   reg_tickers = re.findall(r'[$][A-Z][\S]*', post)
   reg_tickers = [e[1:] for e in reg_tickers]
   other_tickers =  re.findall(r'\b[A-Z][a-zA-Z]{1,4}\b', post)
   all_tick = reg_tickers + other_tickers
   print(all_tick)


#Run
for post in submission: #Loops thru reddit posts
   analyzer = SentimentIntensityAnalyzer()
   post_tickers = extract_ticker(post.title) #Returns list of tickers
   for tick in post_tickers: #Loops thru tickers in the returned list
      if tick.upper() in lookup and tick.upper() not in blacklist_words:
         add_ticker(tick)
   post.comments.replace_more(limit=4) #Max 32 instances
   for top_level_comment in post.comments: #Loops thru comment in post
      comment_tickers = extract_ticker(top_level_comment.body)
      for tick in post_tickers:
         if tick.upper() in lookup and tick.upper() not in blacklist_words:
            add_ticker(tick)

print(ticker_dict)








