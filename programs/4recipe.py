#You have a collection of favorite recipes, but sometimes forget which ingredients you have in
#stock. Can you write a program that allows you to search your recipes and check off the
#ingredients you have, and then suggests which recipe to make based on what you already have?
# dictionary of recipes and their ingredients
recipes = {
    "Egg Curry": ["egg", "tomato sauce", "onion", "garlic", "olive oil", "salt", "pepper"],
    "Chicken Curry": ["chicken breasts", "vegetables", "soy sauce", "sesame oil", "garlic", "cornstarch", "rice"],
    "Cheese Fry": ["bread", "butter", "cheese", "tomato"],
    # add more recipes here
}

# function to search for a recipe
def search_recipe():
    query = input("What ingredient are you looking for? ")
    matching_recipes = []
    for recipe, ingredients in recipes.items():
        if query in ingredients:
            matching_recipes.append(recipe)
    if matching_recipes:
        print(f"Matching recipes: {', '.join(matching_recipes)}")
    else:
        print("No matching recipes found.")

# function to check off ingredients for a recipe
def check_ingredients(recipe):
    ingredients = recipes[recipe]
    in_stock = []
    for ingredient in ingredients:
        answer = input(f"Do you have {ingredient}? (y/n) ")
        if answer.lower() == "y":
            in_stock.append(ingredient)
    return in_stock

# main program loop
while True:
    command = input("What would you like to do? (search/ suggest/ quit) ")
    if command == "search":
        search_recipe()
    elif command == "quit":
        break
    else:
        print("Invalid command.")
