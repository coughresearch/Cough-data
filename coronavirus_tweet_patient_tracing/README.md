

### Tweeper

Tweeper is an advanced Twitter scraping tool written in Python that allows for scraping Tweets from Twitter profiles **without** using Twitter's API.

Tweep utilizes Twitter's search operators to let you scrape Tweets from specific users, scrape Tweets relating to certain topics, hashtags & trends, or sort out *sensitive* information from Tweets like e-mail and phone numbers for tracing the covid19 data.

## tl;dr Benefits
Some of the benefits of using Tweep vs Twitter API:
- Can fetch almost __all__ Tweets (Twitter API limits to last 3200 Tweets only)
- Fast initial setup
- Can be used anonymously and without sign up
- No rate limitations

## Requirements
- Python 3.6
- `pip3 install -r requirements.txt`

## Usage
- `-u` The user's Tweets you want to scrape.
- `-s` Search for Tweets containing this word or phrase.
- `-g` Retrieve tweets by geolocation. Format of the argument is lat,lon,range(km or mi).
- `-o` Save output to a file.
- `--year` Filter Tweets before the specified year.
- `--fruit` Display Tweets with "low-hanging-fruit".
- `--tweets` Display Tweets only.
- `--verified` Display Tweets only from verified users (Use with `-s`).
- `--users` Display users only (Use with `-s`).
- `--csv` Write as a .csv file.
- `--db` Write as a database.
- `--hashtags` Extract hashtags.
- `--userid` Search from Twitter user's ID.
- `--limit` Number of Tweets to pull (Increments of 20).
- `--count` Display number Tweets scraped at the end of session.
- `--stats` Show number of replies, retweets, and likes.

## Low-Hanging Fruit
The `--fruit` feature will display Tweets that *might* contain sensitive info such as:
- Profiles from leaked databases (Myspace or LastFM)
- Email addresses
- Phone numbers
- Keybase.io profiles

## Basic Examples
A few simple examples to help you understand the basics:

- `python3 tweep.py -u username` - Scrape all the Tweets from *user*'s timeline.
- `python3 tweep.py -u username -s covidpositive` - Scrape all Tweets from the *user*'s timeline containing _pineapple_.
- `python3 tweep.py -s pineapple` - Collect every Tweet containing *pineapple* from everyone's Tweets.
- `python3 tweep.py -u username --year 2020` - Collect Tweets that were tweeted **before** 2014.
- `python3 tweep.py -u username --since 2020-03-23` - Collect Tweets that were tweeted since 2020-03-23 (yyyy-mm-dd).
- `python3 tweep.py -u username -o file.txt` - Scrape Tweets and save to file.txt.
- `python3 tweep.py -u username -o file.csv --csv` - Scrape Tweets and save as a csv file.
- `python3 tweep.py -u username -o file.db --db` - Scrape Tweets and save as a database.
- `python3 tweep.py -u username --fruit` - Show Tweets with low-hanging fruit.
- `python3 tweep.py -s "covid patient" --verified --users` - List verified users that Tweet about Donald Trump.
- `python3 tweep.py -g="148.880048,232.385939,1km" -o file.csv --csv` - Scrape Tweets from a radius of 1km around a place and export them to a csv file.

## Example:

> 1259005647011680258 2020-05-08 06:21:52 UTC <bardoliguide> Covid19 positive Female patient :Patient Name: Samira Huusen MansooriResidential Area: Taivad, Bardoli..Travel history: from Ahmedavad on 7.5.2020 to Bardoli.Currently she was Shifted to Maliba covid care…  https://www.instagram.com/p/B_9PRk_jVYz/?igshid=y06ebos24phj …

>1256229160839778306 2020-05-01 14:29:06 UTC <rajanpalanii> @mybmc @mybmcWardGN @mayor_mumbai @MantralayaRoom Patient diagnosed positive to Covid19. BMC not helping. He is still at home. Name: R Balachandar( 42yrs) _ 9833072646Address: Divine Shelter CHS RNO 405, Opp Dr Ambedkar school Dharavi cross road.
