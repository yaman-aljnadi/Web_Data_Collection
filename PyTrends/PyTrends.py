from pytrends.request import TrendReq
import pytrends
import pandas as pd
import os 
pytrends = TrendReq()

kw_list = ["social development bank"]

START_YEAR = int(input("Enter the starting year: "))
START_MONTH = int(input("Enter the starting month: "))
START_DAY = int(input("Enter the starting day: "))

END_YEAR = int(input("Enter the ending year: "))
END_MONTH = int(input("Enter the ending month: "))
END_DAY = int(input("Enter the ending day: "))

historicaldf = pytrends.get_historical_interest(kw_list, year_start=START_YEAR, month_start=START_MONTH, day_start=START_DAY, hour_start=0, year_end=END_YEAR, month_end=END_MONTH, day_end=END_MONTH, hour_end=0, cat=0, geo='SA', gprop='', sleep=0)

df = pd.DataFrame(historicaldf)
os.makedirs("dataframes/", exist_ok=True)
df.to_csv("dataframes/test.csv")
print(historicaldf)



OPTIONS  = ["now 1-H", "now 4-H", "now 1-d", "now 7-d", "today 1-m", "today 3-m", "today 12-m", "today 5-y", "all"]
# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrends.build_payload(kw_list=kw_list, timeframe=OPTIONS[5], geo="SA")

# Interest Over Time
interest_over_time_df = pytrends.interest_over_time()
print(interest_over_time_df)

# Interest by Region
interest_by_region_df = pytrends.interest_by_region()
print(interest_by_region_df)
df2 = [interest_over_time_df, interest_by_region_df]
df2_2 = pd.concat(df2)
df2_2.to_csv("dataframes/test2.csv")

