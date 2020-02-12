#importing required libraries 

import flask, random, os, requests, requests_oauthlib


app = flask.Flask(__name__)

@app.route('/')

def index():

# SPOONACULAR API 

#API to search for indian cuisine 

    url2 = "https://api.spoonacular.com/recipes/search?cuisine=indian%20free&apiKey=SPOONACULAR_KEY"

    response2 = requests.get(url2)
    json_body2 = response2.json()

# getting the size of the cusine to randomly display items

    cuisine_list = [ ]
    cuisine_length = len(json_body2["results"])

        
    randomNum = random.randint(0,cuisine_length-1)
    
#  fetching the recipe title, id and time to cook   
    
    recipe_title = str(json_body2["results"][randomNum]["title"])
    recipe_time = str(json_body2["results"][randomNum]["readyInMinutes"])
    recipe_id = str(json_body2["results"][randomNum]["id"])

# fetching the ingredient list using url3 API
    
    url3 = "https://api.spoonacular.com/recipes/" + recipe_id + "/ingredientWidget.json?apiKey=SPOONACULAR_KEY"
    response3 = requests.get(url3)
    json_body3 = response3.json()

# fetching the size of ingredient to print all the items 

    ingredient_list = [ ]
    ingredient_length = len(json_body3["ingredients"])
    
    
    for i in range(ingredient_length):
        ingredient_list.append(json_body3["ingredients"][i]["name"])
   
    
#changing the list of ingredients to string 

    ingredient_list_String = ""
    for k in ingredient_list:
        ingredient_list_String += k + ", "
    
   
# fetching the recipe website using the url 4
    
    url4 = "https://api.spoonacular.com/recipes/" + recipe_id + "/information?apiKey=SPOONACULAR_KEY"
    response4 = requests.get(url4)
    json_body4 = response4.json()
 
    
    link_recipe = json_body4["sourceUrl"]
    img_url = json_body4["image"]

# TWITTER API  

    url1 = "https://api.twitter.com/1.1/search/tweets.json?q=indiancuisine&result_type=mixed"
    
    oauth = requests_oauthlib.OAuth1(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET_KEY"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET")
    )

    response1 = requests.get(url1, auth=oauth)
    json_body1 = response1.json()
    
    tweet_length = len(json_body1["statuses"])
    
    random_Num_tweet = random.randint(0,tweet_length-1)
    
    rand_tweet = json_body1["statuses"][random_Num_tweet]["text"]
 
# returning the data to html for website display 

    return flask.render_template('index.html', rt = recipe_title, rT =recipe_time , ri =  img_url, ingredient_json = ingredient_list_String, flink = link_recipe, randtweet = rand_tweet)


app.run(
host=os.getenv('IP', '0.0.0.0'),
port=int(os.getenv('PORT', 8080)),
debug = 'True'
)