# # Nesting list in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille"],
#     "Germany": ["Berlin"],
# }

# # Nesting dictionary in a dictionary

# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille"]},
#     "Germany": {"cities_visited": ["Berlin"]},
# }

# # nesting dictionary in a list

# travel_log = [
#     {
#         "country":"France",                     #string
#         "cities_visited":["Paris", "Lille"],    #list
#         "total_visit": 5},                      #number

#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin"],
#         "total_visit": 12},
# ]


# You are going to write a program that adds to a travel_log. 
# Your job is to create a function that can add new countries to this list.

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
    
    new_entry = {"country": country,
                 "visits": visits,
                 "cities": list_of_cities}

    travel_log.append(new_entry)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")