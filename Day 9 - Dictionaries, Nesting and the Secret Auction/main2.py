# Nesting list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille"],
    "Germany": ["Berlin"],
}

# Nesting dictionary in a dictionary

travel_log = {
    "France": {"cities_visited":["Paris", "Lille"]},
    "Germany": {"cities_visited": ["Berlin"]},
}

# nesting dictionary in a list

travel_log = [
    {
        "country":"France",                     #string
        "cities_visited":["Paris", "Lille"],    #list
        "total_visit": 5},                      #number

    {
        "country": "Germany", 
        "cities_visited": ["Berlin"],
        "total_visit": 12},
]