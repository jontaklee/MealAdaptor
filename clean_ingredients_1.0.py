# Tue Jan 22 13:01:37 2019 python3 
# v1.0


import os
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean_ingredients(ingredient):
    ingrd_tokens = word_tokenize(ingredient)
    words = [word for word in ingrd_tokens if word.isalpha()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in food_descriptors]
    words = [word for word in words if not word in stop_words]
    #words = [x.replace('stock', 'broth') for x in words]
    #words = [x.replace('steak', 'beef') for x in words]
    ingredient_clean = ' '.join(words)
    for staple in food_staples:
        if staple in ingredient_clean:
            ingredient_clean = staple
            break        
    return ingredient_clean


food_descriptors = ["ground", "grated", "all-purpose", "all purpose", "melted", "minced", "softened", "chopped", "shredded", "packed",
                   "beaten", "dried", "sliced", "diced", "skinless", "boneless", "thighs", "thigh", "halves",
                   "rolled", "sweetened", "lean", "distilled", "freshly", "flaked", "granulated", "unsalted", "salted",
                   "crushed", "thawed", "extra", "virgin", "extra-virgin", "extra virgin", "uncooked", "fresh", "large", "dry",
                   "cold", "finely", "drained", "plain", "light", "sifted", "thinly", "rinsed", "and", "juiced", "divided",
                   "whole", "crumbled", "separated", "firmly", "frozen", "small", "skim", "warm", "canned", "unsweetened",
                   "confectioners", "lightly", "peeled", "refrigerated", "slightly", "breast", "breasts", "boiling",
                   "boiled", "hot", "container", "jar", "seasoned", "unseasoned", "pitted", "trimmed", "zested", "prepared",
                   "coarsely", "cooked", "cubed", "mashed", "pulled", "creamed", "whipped", "fat-free",
                   "seeded", "julienned", "undrained", "soaked", "low-fat","low fat", "marinated", "medium", "quartered",
                   "heated", "cored", "powdered", "raw", "thickly", "very", "reduced-fat", "reduced fat", "ripe", "roasted", "halved",
                   "shelled", "smoked", "square", "squares", "squeezed", "toasted", "deveined", "thick", "-", "or",
                   "more", "semisweet", "meat", "stewed", "thin", "cut", "thick-cut", "chops", "spareribs", "tenderloin",
                   "loin", "ribs", "roast", "sirloin", "shoulder", "mild", "smashed", "roughly", "pressed", "chilled",
                   "legs", "leg", "coarse", "kosher", "for", "garnish", "decoration", "dusting", "frying", "coating", "at",
                   "wings", "instant", "nonfat", "non-fat", "sharp", "pure", "seedless", "chunks", "bone-in", "creamy",
                   "crunchy", "hard-boiled", "hard boiled", "loaf", "loaves", "lowfat", "miniature", "soft", "blanched", "slivered",
                   "firm", "extra-firm", "extra firm", "silken", "semi-sweet", "semi sweet", "mini", "hulled", "granules", "strong", 
                   "brewed", "bunch", "stemmed", "drumsticks", "drumettes", "pounded", "tenders", "cube", "cubes", "fine", "grilled", "head",
                   "heads", "florets", "leaves", "long", "grain", "long-grain", "long grain", "lukewarm", "pods", "husked",
                   "tenderloins", "washed", "bulb", "bulbs", "cooled", "strips", "deli", "into", "torn", "bite-size",
                   "bite-sized", "bite sized", "pieces", "piece", "pinch", "pinches", "cracked", "quick-cooking", "quick", "serving",
                   "old-fashioned", "old fashioned", "liquid", "processed", "unbleached", "unwrapped", "100%", "lactose-free", 
                   "lactose free", "all", "purpose", "bunches", "wedges", "dashes", "envelope", "envelopes", "original", "premium", 
                   "regular", "reserved", "hard-cooked", "unpeeled", "whisked", "well", "2%", "low-sodium", "low sodium", 
                   "reduced-sodium", "reduced sodium" "bulk", "links", "no-stick", "nonstick", "fire-roasted", "fire roasted", 
                   "gluten-free", "gluten free" "no-salt-added" "no salt added", "real", "threads", "wheel", "center-cut", "center cut", 
                   "dry-roasted", "dry roasted", "fillets", "plus", "fully", "natural", "cleaned", "new", "non-stick", "non stick",
                   "stick", "sticks", "aged", "box", "jigger", "jiggers", "packet", "part-skim", "part skim"
                   "scrubbed", "skin-on", "skin on", "stripped", "lengthwise", "petite", "splash", "slice", "defrosted", "split",
                   "brisket", "fillet", "leftover", "clove", "cloves", "fat", "low", "sodium", "grainy", "whole-grain", 
                   "multi-grain", "whole-wheat", "zest", "short", "sticky", "stalk", "basmati", "jasmine", "arborio", "parboiled",
                   "sushi", "bomba", "meat", "kernals", "half", "halved", "quarter", "quartered", "&", "natural", "naturally"]

food_staples = ["abalone","adzuki bean","alfalfa sprout","allspice","almond milk","almond","amaranth","anchovy","apricot","artichoke",
                "arugula","asparagus", "avocado oil", "avocado","bamboo shoot","banana","barley","basil","bay lea","bean sprout","beef",
                "beet green","beet","bell pepper","black bean","black eyed pea","black pepper","black tea","blackberr","blueberr","bok choy",
                "fish broth","beef broth","chicken broth","boysenberr","brazil nut","breadfruit","broccoli","wild rice","brown rice","rice milk",
                "rice noodle","rice","brussels sprout","buckwheat","buffalo","bulgar","burdock root","butter","cabbage","cane sugar","caper",
                "caraway seed","cardamom","cardoon","carob","carrot","cashew","cassava","catfish","cauliflower","roe","cayenne pepper","celeriac",
                "celery seed","celery","chard","cottage cheese","cheese","chervil","chestnut","chia seed","chicken","chickpea","chicory","chili powder","cilantro",
                "cinnamon","clove","cocoa","mct oil","coconut milk","coconut oil","coconut water","coconut","cod","coffee","collard green",
                "coriander","corn tortilla","cornish game hen","couscous","cranberr","crayfish","cucumber","cumin","currant","dandelion green",
                "date","dill","duck","dungeness crab","eel","egg white","egg yolk","egg","eggplant","elderberr","emu","endive","escarole",
                "fava bean","fennel seed","fennel","fenugreek seed","fig","hazelnut","flax oil","flax seed","venison","garlic","ghee","ginger",
                "goat cheese","goat milk","goat","goji berr","gooseberr","goose","gourd","grape leaves","grape seed oil","grapefruit","grape",
                "green bean","green tea","guava","haddock","halibut","hard squash","heavy cream","hemp heart","herbal tea","herring","hickory nut",
                "honey","horseradish","hot pepper","huckleberr","jackfruit","jerusalem artichoke","jicama","kale","kamut","kefir","kimchi","kiwi",
                "kohlrabi","kombucha","kumquat","lamb","leek","lemon","lentil","lettuce","lima bean","lime","lobster","loganberr","lotus seed",
                "lychee","macadamia nut","mace","mackerel","mango","mangosteen","maple syrup","marionberr","marjoram","melon","millet","miso",
                "molasses","mulberr","mushroom","mussel","mustard green","mustard seed","natto","nectarine","nutmeg","oat","okra","olive oil",
                "olive","onion","orange","oregano","ostrich","papaya","paprika","parsley","parsnip","passionfruit","peach","peanut","pear","pea",
                "pecan","peppermint","perch","persimmon","pheasant","pickle","pine nut","pineapple","apple","pinto bean","pistachio","plantain",
                "plum","pomegranate","poppy seed","pork","potato","prune","pummelo","pumpkin seed","pumpkin","quail","quinoa","radicchio","radish",
                "trout","raspberr","red bean","rhubarb","rosemary","rutabaga","rye","safflower oil","saffron","sage",
                "salmon","salmonberr","sardine","sauerkraut","scallop","seaweed","sesame seed","sheep cheese","sheep milk","clam","oyster","shrimp",
                "snap pea","sour cherr","soy milk","soybean","spearmint","spinach","spirulina","radish seed","squid","star fruit","stevia","strawberr",
                "summer squash","sunflower seed","taro","tarragon","tempeh","tofu","tomato","triticale","tuna","turbot","turkey","turmeric","turnip",
                "vanilla extract","veal","apple cider vinegar","vinegar","walnut","water chestnut","watercress","wheatgrass","wheat","white bean",
                "white tea","sweet potato","yogurt","zucchini","milk","cherr"]


stop_words = set(stopwords.words('english'))


path = '/Users/Jonathan/Desktop/recipes/'
recipe_lists = os.listdir(path)
recipe_lists = [x for x in recipe_lists if x.endswith('.json')]


with open(path+recipe_lists[0], encoding = 'utf-8') as infile:
    ingrd_recipes = json.loads(infile.read())


ingredient_list = []
for recipe_list in recipe_lists:
    with open(path + recipe_list, encoding = 'utf-8') as infile:
        ingrd_recipes = json.loads(infile.read())
    
    for recipe in ingrd_recipes:
        ingrds_in = recipe['ingredient_names']
        cleaned_ingr_list = [clean_ingredients(item) for item in ingrds_in]
        cleaned_ingr_list = [x for x in cleaned_ingr_list if x]
        ingredient_list.append(list(set(cleaned_ingr_list)))

