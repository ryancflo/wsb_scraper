# get-all-tickers

forked from shilewenuw/get_all_tickers, and uses different API

## features
-  getting a list of tickers from chosen US exchanges (all of them by default)
-  getting a list of tickers filtered by market caps, sector, region, country, and rating
-  getting the top n biggest tickers, filtered by sector, region, country, and rating
-  saving tickers to a CSV

### install

## methods & classes
```
get_tickers(NYSE=True, NASDAQ=True, AMEX=True)
```
Returns a list of tickers, set an exchange to false to exclude.
***
```
def get_tickers_filtered(NYSE=True, NASDAQ=True, AMEX=True,mktcap_min=None, mktcap_max=None, sectors=None, regions=None, countries=None, analystRatings=None):
```
Minimum and maximum market caps are set through mktcap_min and mktcap_max, respectively (numbers are in millions).
You can have no upper bound for market cap if you leave mktcap_max as its default value, so `get_tickers_filtered(mktcap_min=200)` will
get tickers of market caps 200 million and up. 
Can sort also sort by valid sectors, regions, countries, analystRatings
***
```
def get_biggest_n_tickers(top_n, NYSE=True, NASDAQ=True, AMEX=True,mktcap_min=None, mktcap_max=None, sectors=None, regions=None, countries=None, analystRatings=None):
```
Returns a list of top_n biggest tickers by market cap. Can apply same filters as get_tickers_filtered

```
save_tickers(NYSE=True, NASDAQ=True, AMEX=True, filename='tickers.csv')
```
Set any exchange to False if you don't want to include it. Saves tickers to a csv file.  
***
```
def save_tickers_filtered(NYSE=True, NASDAQ=True, AMEX=True,mktcap_min=None, mktcap_max=None, sectors=None, regions=None, countries=None, analystRatings=None, filename='tickers_by_region.csv'):
```

### examples
```
# tickers of all exchanges
tickers = get_tickers()
print(tickers[:5])

# tickers from NYSE and NASDAQ only
tickers = get_tickers(AMEX=False)

# default filename is tickers.csv, to specify, add argument filename='yourfilename.csv'
save_tickers()

# save tickers from NYSE and AMEX only
save_tickers(NASDAQ=False)

# get tickers filtered by market cap (in millions)
filtered_tickers = get_tickers_filtered(mktcap_min=500, mktcap_max=2000)
print(filtered_tickers[:5])

# not setting max will get stocks with $2000 million market cap and up.
filtered_tickers = get_tickers_filtered(mktcap_min=2000)
print(filtered_tickers[:5])

# get tickers filtered by multiple params, None should exist
filtered_by_sector = get_tickers_filtered(mktcap_min=200e3, sectors=[SectorConstants.FINANCE,SectorConstants.BASICS,SectorConstants.CAPITAL_GOODS],analystRatings=[AnalystRating.SELL,AnalystRating.BUY],countries=[Country.ARGENTINA])
print(filtered_by_sector)

# get tickers filtered by multiple params
filtered_by_sector = get_tickers_filtered(mktcap_min=200e3, sectors=[SectorConstants.FINANCE,SectorConstants.BASICS,SectorConstants.CAPITAL_GOODS],analystRatings=[AnalystRating.SELL,AnalystRating.BUY],countries=[Country.UNITED_STATES])
print(filtered_by_sector[:5])

# get tickers of 5 largest companies by market cap (specify sectors=SECTOR)
top_5 = get_biggest_n_tickers(5)
print(top_5)
```
