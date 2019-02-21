# MealAdaptor

MealAdaptor was built to help [Viome](https://www.viome.com/) users integrate dietary suggestions into their meals by providing suggested ingredient substitutions. 

Ingredient substitutions are provided using two word embedding models). 

<p align="center">
<img src='../master/images/pipe.png' width='450' />
</p>

The first model is trained on a corpus of 100,000+ recipes. The second is selected from one of four models trained on a topical subset of recipes. Both utilize the Skip Gram method of Word2Vec.

<p align="center">
<img src='../master/images/approach.png' width='450' />
</p>

Topics are assigned based on the cooking directions in a recipe using LDA and represent types of dishes (savory meals, desserts, etc.). In this manner, word embeddings are trained in a more contextual manner that considers the relationship between ingredients only among similar dishes.

The input to MealAdaptor is a recipe, including its ingredients and preparation instructions (cooking directions). The recipe is assigned to a topic and ingredient replacements are proposed using word embeddings trained within the topic, as well as the full corpus of recipes.

For each ingredient in a recipe, cosine similarity is used to select the most similar foods to serve as replacements. Of the two word2vec models, the more coherent set of suggestions is presented to the user (coherence here being the similarity between the suggested replacements). These suggestions are then curated based on the user's dietary suggestions of foods to consume more or less of.

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
