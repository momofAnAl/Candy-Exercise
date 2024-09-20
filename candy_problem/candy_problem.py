'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
# '''
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
def get_friends_favorite_candy_count(favorites):
    candies_counting = {}
    
    for friends_favorites in favorites:
        friend_name = friends_favorites[0]
        candies_name = friends_favorites[1]
        for candy in candies_name: 
            if candy not in candies_counting:
                candies_counting[candy] = 1
            else:
                candies_counting[candy] += 1
    
    return candies_counting
get_friends_favorite_candy_count(friend_favorites)
    

'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candies_favorite = {}
    
    for friends, candies in friend_favorites:
        for candy in candies: 
            if candy not in candies_favorite:
                candies_favorite[candy] = [friends]
            else: 
                candies_favorite[candy].append(friends)
                
    return candies_favorite           
        
print(create_new_candy_data_structure(friend_favorites))
        
'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    
    candy_favorite = create_new_candy_data_structure(data)
    tuple_candies = tuple(candy_favorite[candy_name])
    return tuple_candies

print(get_friends_who_like_specific_candy(friend_favorites, "nerds"))

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    candies_storage = create_new_candy_data_structure(data)
    new_candies_storage = set()
    
    for candies in candies_storage.keys():
        new_candies_storage.add(candies)
     
    return new_candies_storage

print(create_candy_set(friend_favorites))       

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

