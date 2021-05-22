from collections import Counter
from dateutil.parser import parse

from Week4.TwitterAPI.twitter_api import repos ## imports twitter_api to work with, should change name to gihub from twitter

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print(dates,month_counts,weekday_counts)