# 19 Jan 2019 Python 2.7
# v1.0
import csv
import unirest
import json

def get_ingredients(recipe):
    ingrds = recipe['extendedIngredients']
    ingrd_details = [(i['name'], i['amount'], i['unit']) for i in ingrds]
    return ingrd_details
    
def get_instructions(recipe):
    try:
        cooking_steps = recipe['analyzedInstructions'][0]['steps']
        instructions = [cooking_step['step'] for cooking_step in cooking_steps]
        return instructions        
    except IndexError:
        return 'no instructions'


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
    
    n = 15
    
    staples_file = '/Users/Jonathan/Dropbox/viome_proj/missing_staples.csv'
    with open(staples_file, 'rb') as f:
        reader = csv.reader(f)
        food_staples = list(reader)[0]
    
    key = "ae933f0afbmshee55051062da67dp17af13jsn6937b4ef3963"
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
        recipe_list = []
        for recipe in recipes:
            recipe_simplified = compile_attributes(recipe)
            recipe_list.append(recipe_simplified)
        outpath = '/Users/Jonathan/Desktop/spoonacular_recipes/'
        outfile = outpath + food + '_recipes6.json'
        with open (outfile, 'w') as fp:
            json.dump(recipe_list, fp)
           