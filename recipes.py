#!/usr/bin/env/ python3

import json
import pip._vendor.requests
api_key = "401f1625a34e4f809fb3b5f60630d64e"
#api_url_base = "https://spoonacular.com/recipes"




headers = {'Content-Type': 'application/json'}


#get user input for ingredients
name = input("What is your name? ")
username = name
add_to_list = pip._vendor.requests.post("https://api.spoonacular.com/mealplanner/{username}/shopping-list/items&ingredients&aisle&price")

recipe = pip._vendor.requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=401f1625a34e4f809fb3b5f60630d64e&query=sandwich&ingreidients=chicken,lettuce&includeIngredients={ingredients}&fillIngredients=false&addRecipeInformation=false&number=1")

#ask user what they have in their fridge
ingredients = input("Which ingredients do you have? ")
print(recipe.json()) #print recipe with ingredients

#check if they like it
like_recipe = input("Do you like the recipe? ")

if like_recipe: ("yes")
add_to_list


while like_recipe: False
print(f"{recipe}")

