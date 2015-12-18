import feedparser
import time

feed_rss_url = feedparser.parse('http://weather.yahooapis.com/forecastrss?p=60607')

data = feed_rss_url.feed

# Displays Today's Data
now = feed_rss_url.entries[0].yweather_condition['date']
print "Current Day and Time"  
print "--------------------"
print now + "\n"
# Display the feed title
print "Feed Title -> ", data.title + "\n"

# Display the feed description
print "Feed Description -> ", data.description + "\n"

# Display the feed link URL
#print feed_rss_url.feed.link

# print out the first title entry - just a test
print feed_rss_url.entries[0].title + "\n"

# Astronomy - Sunrise and Sunset Data
print "Astronomy"
print "---------"
print "Sunrise: " + data.yweather_astronomy['sunrise'] + " Sunset: " + data.yweather_astronomy['sunset']
print "\n"
# print out the weather conditions
print "Weather Conditions"
print "------------------"
#print (feed_rss_url['items'][0]['yweather_condition'])
condition = feed_rss_url.entries[0].yweather_condition['text']
fahrenheit = feed_rss_url.entries[0].yweather_condition['temp']
print "Today's Condition: " + condition
print "Temperature: " + fahrenheit + "\"F"
# print out the Forecast
print "\n Weekly Forecast"
print "------------------"
#print (feed_rss_url['items'][0]['yweather_forecast'])
day = feed_rss_url.entries[0].yweather_forecast['day']
date = feed_rss_url.entries[0].yweather_forecast['date']
low = feed_rss_url.entries[0].yweather_forecast['low']
high = feed_rss_url.entries[0].yweather_forecast['high']
text = feed_rss_url.entries[0].yweather_forecast['text']
print "Day:" + day + " date:" + date + " low:" + low + "  high:" + high + " Condition:" + text + "\n"
#print feed_rss_url.entries[0].yweather_forecast['day'] 
print len(feed_rss_url['entries'])
"\n"
# Testing if elements are present
print 'title' in data
print data.get('title', 'No title')

