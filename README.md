# usdanuts
USDA Nutrient Upgraded Tally System

This Python project was inspired in part by the Nutrient Object Management System (noms) package, created by Noah Tren (https://github.com/noahtren/noms). 
The noms package utilizes the USDA Standard Reference Food Composition Database, which is now decommissioned; the nuts package calls the currently active USDA FoodData Central API.

The nuts package is designed to: 
- Take a food query from the user.
- Call the USDA FoodData Central API.
- Repeat API calls for searches returning more than one results page.
- Return a Pandas DataFrame of matching food items and their measured or surveyed nutrient values.
- Export a DataFrame as a timestamped CSV file with optional prefix.

The package contains five functions; the get_df() function returns a Pandas DataFrame from a search query and affords the user almost all utility from the package.
- get_df(query,
         dataType="Foundation,Branded,SRLegacy,Survey(FNDDS)",
         API_KEY="DEMO_KEY")
  - query can be any string of text, such as "lychee", "sugar", or "rice".
  - dataType can be any combination of "Foundation,Branded,SRLegacy,Survey(FNDDS)"
  - API_KEY will use a demo API key by default, which has limited functionality. Users can create their own API key and find more thorough documentation at https://fdc.nal.usda.gov/
- get_csv(df,prefix="")
  - df can be a Pandas DataFrame from a recent search or a larger DataFrame compiled from several searches
  - prefix can be any string or float to lead the filename
- get_url(), get_search_pages(), and get_search_list() are likely not useful to the user except when troubleshooting.

A request will time out if it returns more than 10000 food items. To avoid this, only the 10000 most recently published food items are returned.

Future iterations of nuts will:
- Utilize page tokens to return all matching food items for any valid query without timing out.
- Address filtering challenges including searching for vegan foods without filtering out any vegan foods containing "animal-centric" words, e.g. "plant-based chicken".
- Work in tandem with the Daily Energy Expenditure Zetetic to take arguments from a user such as height, weight, age, sex, pregnancy status, dietary restrictions, and other health conditions to return nutrient requirements and pantry suggestions.
