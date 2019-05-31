###############################################################################
# "Weather Parser"
###############################################################################
#  Objectives:
#   To create a weather forecast parser using beautiful soup and store the
#       results in a pandas dataframe
#  Source:
#   https://www.dataquest.io/blog/web-scraping-tutorial-python/
#   https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XPGyA3tlD1s
###############################################################################

import requests
import pandas as pd
from bs4 import BeautifulSoup

#############################################################################
# Download page
page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
)
soup = BeautifulSoup(page.content, 'html.parser')

#############################################################################
# Look for the HTML id tag in a browser inspector
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

#############################################################################
# Exploring tonight's forecast
tonight = forecast_items[0]
print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img")
desc = img['title']

#############################################################################
# Get periods' names
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

#############################################################################
# Get descriptions and temperatures
short_descs = [
    sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")
]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#############################################################################
# Creating and extending our dataframe
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

#############################################################################
# Our full dataframe
weather
