"""Restaurant rating lister."""


file = open("scores.txt")

restaurant_ratings = {}

def restaurant(file):


    """ takes in a file, reads it, then gives the restaurant name and the rating. """

    for line in file:
        line = line.rstrip().split(":")
        name = line[0]
        rating = line[1]
        restaurant_ratings[name] = rating

    for name,rating in sorted(restaurant_ratings.items()):
        print(f"{name} is rated at {rating}.")

def add_restaurant():
    """add the restaurant by user"""
    print("Please add a rating for your favorite restaurant!")
    new_restaurant = input("res_name:")
    new_rating = int(input("rating:"))

    restaurant_ratings[new_restaurant] = new_rating

add_restaurant()
restaurant(file)
