from pytrends.request import TrendReq
import pytrends
import pandas as pd                        


pytrends = TrendReq()

START_YEAR = int(input("Enter the starting year: "))
START_MONTH = int(input("Enter the starting month: "))
START_DAY = int(input("Enter the starting day: "))

END_YEAR = int(input("Enter the ending year: "))
END_MONTH = int(input("Enter the ending month: "))
END_DAY = int(input("Enter the ending day: "))

kw_list = ["social development bank"]
test = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='US', gprop='')
# test2 = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2022, month_end=2, day_end=1, hour_end=0, cat=0, geo='US', gprop='', sleep=1)
# test4 = pytrends.trending_searches(pn='japan')
test5 = pytrends.top_charts(2021, hl='en-US', tz=300, geo='SA')
# test3 = pytrends.realtime_trending_searches(pn='SA')
print(test5)


historicaldf = pytrends.get_historical_interest(kw_list, year_start=START_YEAR, month_start=START_MONTH, day_start=START_DAY, hour_start=0, year_end=END_YEAR, month_end=END_MONTH, day_end=END_MONTH, hour_end=0, cat=0, geo='SA-RUH', gprop='', sleep=0)

print(historicaldf)
# #provide your search terms
# kw_list=['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google']
# #search interest per region
# #run model for keywords (can also be competitors)
# pytrends.build_payload(kw_list, timeframe='today 1-m')

# # Interest by Region
# regiondf = pytrends.interest_by_region()
# #looking at rows where all values are not equal to 0
# regiondf = regiondf[(regiondf != 0).all(1)]

# #drop all rows that have null values in all columns
# regiondf.dropna(how='all',axis=0, inplace=True)

# #visualise
# regiondf.plot(figsize=(20, 12), y=kw_list, kind ='bar')




#install pytrends

#import the libraries

#build model

#provide your search terms
kw_list=["social development bank"]
payload = pytrends.build_payload(kw_list=kw_list)

#get related queries
related_queries = pytrends.related_queries()
related_queries.values()

#build lists dataframes

top = list(related_queries.values())[0]['top']
rising = list(related_queries.values())[0]['rising']

#convert lists to dataframes

dftop = pd.DataFrame(top)
dfrising = pd.DataFrame(rising)

#join two data frames
joindfs = [dftop, dfrising]
allqueries = pd.concat(joindfs, axis=1)

#function to change duplicates

cols=pd.Series(allqueries.columns)
for dup in allqueries.columns[allqueries.columns.duplicated(keep=False)]: 
    cols[allqueries.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
                                     if d_idx != 0 
                                     else dup 
                                     for d_idx in range(allqueries.columns.get_loc(dup).sum())]
                                    )
allqueries.columns=cols

#rename to proper names

allqueries.rename({'query': 'top query', 'value': 'top query value', 'query.1': 'related query', 'value.1': 'related query value'}, axis=1, inplace=True) 

#check your dataset
allqueries.head(50)

#save to csv
allqueries.to_csv('allqueries.csv')

#download from collab