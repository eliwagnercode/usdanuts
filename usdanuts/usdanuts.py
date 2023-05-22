# import libraries
import requests, pandas as pd, math, datetime
from tqdm import tqdm, trange # used for progress bars

# Builds URL for initial API call
# Accepts query, data types, and API key
# Returns url to call API
def get_url(query, 
              dataType = "Foundation,Branded,SRLegacy,Survey(FNDDS)", 
              API_KEY="DEMO_KEY", 
              pageNumber=1):
  query, dataType, API_KEY, pageNumber = \
  str(query), str(dataType), str(API_KEY), str(pageNumber)
  url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}"\
        f"&sortBy=publishedDate&sortOrder=desc&pageSize=100"\
        f"&dataType={dataType}&pageNumber={pageNumber}&query={query}"
  return url

# Makes API call for each results page
# Accepts query, data types, and API key
# Requests and parses JSON file for each results page
# Returns list containing dictionaries for each food item on each results page
def get_search_pages(query, 
              dataType = "Foundation,Branded,SRLegacy,Survey(FNDDS)", 
              API_KEY="DEMO_KEY", 
              pageNumber=1):
  url = get_url(query, dataType, API_KEY, pageNumber)
  response = requests.get(url).json()
  totalHits, totalPages, = response['totalHits'], response['totalPages']
  pageSize = response['foodSearchCriteria']['pageSize']
  print(f"Total search results: {totalHits}\n\
        API will return up to 10000 most recently published results \n\
        Total pages: {totalPages} \n\
        Results per page: {pageSize}")
  totalPages = 100 if totalPages > 100 else totalPages # Prevents timeout

  search_pages = []
  for i in trange(totalPages, desc = 'Downloading data:'):
    pageNumber = str(i + 1)
    url = get_url(query, dataType, API_KEY, pageNumber)
    response = requests.get(url).json() if totalPages > 1 else response
    page = response['foods']
    search_pages.append(page)
  return search_pages

# Parses data from all results pages
# Accepts list of dictionaries for each food item on each results page
# Returns list of dictionaries with selected column names
def get_search_list(search_pages):
  search_list = []
  for page in tqdm(search_pages, desc = 'Parsing data:'):
    page_list = []
    for food_item in page:
      food_item_dict = {}
      cols = ['foodDescription','fdcId','dataType','publishedDate',
                   'foodCategory','servingSize','servingSizeUnit','brandName']
      for col in cols:
        food_item_dict[col] = food_item[col] if col in food_item else math.nan
      for nutrient in food_item['foodNutrients']:
        name = nutrient['nutrientName'] + '(' + nutrient['unitName'] +')'
        name.replace(" ", "")
        value = nutrient['value']
        food_item_dict[name] = value
      page_list.append(food_item_dict)
    search_list = search_list + page_list     
  return search_list

# Builds Pandas DataFrame
# Accepts query to call FoodData Central API and parse data
# Returns Pandas DataFrame
def get_df(query,
           dataType="Foundation,Branded,SRLegacy,Survey(FNDDS)",
           API_KEY="DEMO_KEY"):
  search_pages = get_search_pages(query, dataType, API_KEY)
  search_list = get_search_list(search_pages)
  df = pd.DataFrame(data=search_list, index = range(len(search_list)))
  return df

# Accepts Pandas DataFrame and optional filename prefix
# Exports Pandas DataFrame as CSV
def get_csv(df,prefix=""):
  prefix = str(prefix)
  df.to_csv(f"FDC_Search_{datetime.datetime.now()}.csv",index=False)
