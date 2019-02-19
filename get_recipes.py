# 19 Jan 2019 Python 2.7
# v1.0
import csv
import unirest #only compatible with Python2
import json


## output ingredients as lists
def get_ingredients(recipe):
    ingrds = recipe['extendedIngredients']
    ingrd_details = [(i['name'], i['amount'], i['unit']) for i in ingrds]
    return ingrd_details
 
## output instructions as list of steps   
def get_instructions(recipe):
    try:
        cooking_steps = recipe['analyzedInstructions'][0]['steps']
        instructions = [cooking_step['step'] for cooking_step in cooking_steps]
        return instructions        
    except IndexError:
        return 'no instructions'

## output dictionary of recipe attributes
def compile_attributes(recipe):
    ingredients = get_ingredients(recipe)
    instructions = get_instructions(recipe)
    recipe_attributes = {
        'name' : recipe['title'],
        'source' : recipe['sourceUrl'],
        'health_score' : recipe['healthScore'],
        'rating' : recipe['spoonacularScore'],
        'likes' : recipe['aggregateLikes'],
        'ingredient_names' : [i[0] for i in ingredients],
        'ingredient_amts' : [i[1] for i in ingredients],
        'ingredient_units' : [i[2] for i in ingredients],
        'instructions' : instructions       
    }
    return recipe_attributes


if __name__ == '__main__':
    
    ## number of recipes to request per staple
    n = 15
    
    ## only includes staples not present in eightportions.com dataset
    staples_file = 'missing_staples.csv'
    with open(staples_file, 'rb') as f:
        reader = csv.reader(f)
        food_staples = list(reader)[0]
    
    ## request recipes, replace key with personal api key:
    ## https://rapidapi.com/spoonacular/api/recipe-food-nutrition
    key = '<api key>'
    path_get = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number='
    for food in food_staples:
        response = unirest.get(path_get + str(n) + '&tags=' + food,
          headers={
            "X-RapidAPI-Key": key
          }
        )
        print 'fetching '+str(n)+' recipes tagged '+food+' (item '+str(food_staples.index(food))+')'
        
        if 'recipes' not in response.body:
            print 'no recipes tagged ' + food
            continue

        recipes = response.body['recipes']
        recipe_list = [compile_attributes(r) for r in recipes]
        outpath = ''
        outfile = outpath + food + '_recipes.json'
        with open (outfile, 'w') as fp:
            json.dump(recipe_list, fp)
           