# 12 Mar 2019 Python 2.7
# v1.4
import csv
import json

import unirest #only compatible with Python2

def get_ingredients(recipe):
    
    ## output ingredients as lists
    
    ingrds = recipe['extendedIngredients']
    ingrd_details = [(i['name'], i['amount'], i['unit']) for i in ingrds]
    return ingrd_details
 
def get_instructions(recipe):
    
    ## output instructions as list of cooking steps   
    
    try:
        cooking_steps = recipe['analyzedInstructions'][0]['steps']
        instructions = [cooking_step['step'] for cooking_step in cooking_steps]
        return instructions        
    except IndexError:
        return 'no instructions'

def compile_attributes(recipe):
    
    ## output dictionary of recipe attributes
    
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

def load_staples_list(infile):
    with open(staples_file, 'rb') as f:
        reader = csv.reader(f)
        food_staples = list(reader)[0]
    return food_staples

def request_recipes(food):
    
    ## requests recipes from spoonacular, replace key with personal api key:
    ## https://rapidapi.com/spoonacular/api/recipe-food-nutrition
    
    key = '<api key>'
    path_get = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number='
    response = unirest.get(path_get + str(n) + '&tags=' + food,
      headers={
        "X-RapidAPI-Key": key
      }
    )
    
    ## prints the current recipe being retrieved 
    print 'fetching '+str(n)+' recipes tagged '+food+' (item '+str(food_staples.index(food))+')'
        
    return response

def make_outfiles(recipe_list, food):
    
    ## saves recipes for a given food staple to a json file
    
    outpath = ''
    outfile = outpath + food + '_recipes.json'
    with open (outfile, 'w') as fp:
        json.dump(recipe_list, fp)
    
def main():
    
    ## number of recipes to request per staple
    n = 15
    
    ## only includes staples not present in eightportions.com dataset
    food_staples = load_staples_list('missing_staples.csv')
    
    ## gets recipes for each food staple ##
    for food in food_staples:
        response = request_response(food)
        
        if 'recipes' not in response.body:
            print 'no recipes tagged ' + food
            continue
        
        ## store attributes of the recipe in dictionaries
        recipe_list = [compile_attributes(r) for r in response.body['recipes']]
        
        ## output recipes for each food staple to json files
        make_outfiles(recipe_list, food)

if __name__ == '__main__':
    main()
           