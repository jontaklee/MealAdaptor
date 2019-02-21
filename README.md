# MealAdaptor

MealAdaptor was developed to to assist [Viome](https://www.viome.com/) users in integrating dietary suggestions into their meals. 

<img src='../master/images/pipe.png' width='600' />


<img src='../master/images/approach.png' width='600' />


## Contents

The **implement_mealadaptor** notebook includes all necessary code to load the trained LDA and Word2Vec models, as well as functions for getting ingredient substitutions.

Notebooks describing preprocessing steps and model training + validation are included in the repository.

Recipes obtained using the spoonacular food API can be found in the *data* folder. The remaining recipes were obtained from, and available at, [eightportions.com](https://eightportions.com/datasets/) in json format. 
The preprocessed recipes are stored as a pandas dataframe in a [Google Drive](https://tinyurl.com/yyanydd4) folder.

### Prerequisites

The nltk and inflect libraries are required to preprocess recipes for downstream use.

The gensim library is required to load and employ the LDA and Word2Vec models.

A [RapidAPI](https://rapidapi.com/spoonacular/api/recipe-food-nutrition) key is required to request recipes from spoonacular using the **get_recipes.py** script. (Note: The unirest library is required for API calls, and is not compatible with Python3.)

## Demo

<img src='../master/images/logo.png' width='400' />

A demo is available at [MealAdaptor.com](http://www.mealadaptor.com/). It was built using:

* Flask
* AWS

## Author

* **Jonathan T Lee** - *jonathantaklee@gmail.com*
