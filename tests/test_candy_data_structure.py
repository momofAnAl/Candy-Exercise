import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    assert type(new_candy_data) == dict
    assert len(new_candy_data["lollipop"]) == 2
'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
def test_get_friends_favorite_candy_count():
    
    #Arrange
    favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    expected = {
        'lollipop': 2, 
        'bubble gum': 1, 
        'laffy taffy': 3, 
        'milky way': 2, 
        'licorice': 1, 
        'chocolate bar': 1, 
        'nerds': 1, 
        'sour patch kids': 1
    }
    #Act
    result = get_friends_favorite_candy_count(favorites)
    
    #Assert
    assert  result == expected
    assert type(result) == dict
    assert len(result) == 8
    
def test_get_friends_favorite_candy_count_empty():
    
    #Arrange
    favorites = []
    #Act
    result = get_friends_favorite_candy_count(favorites)
    
    
    #Assert
    assert result == {}
    
def test_create_new_candy_data_structure():
    
    #Arrange
    favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]
    expected = {
        'lollipop': ['Sally', 'Bob'], 
        'bubble gum': ['Sally'], 
        'laffy taffy': ['Sally','Arlene', 'Carlie'], 
        'milky way': ['Bob', 'Arlene'], 
        'licorice': ['Bob'], 
        'chocolate bar': ['Arlene'], 
        'nerds': ['Carlie'], 
        'sour patch kids': ['Carlie']
    }
    
    #Act
    result = create_new_candy_data_structure(favorites)
    
    #Assert
    assert result == expected
    assert type(result) == dict
    assert len(result) == 8
    

def test_get_friends_who_like_specific_candy():
    
    #Arrange
    favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]
    
    candy_type = "laffy taffy"
    
    ##Act
    result = get_friends_who_like_specific_candy(favorites, candy_type)
    
    ##Assert
    assert result == ('Sally', 'Arlene', 'Carlie')
    assert type(result) == tuple
    assert len(result) == 3
    
def create_candy_set():
    
    #Arrange
    favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]
    
    expected = {'sour patch kids', 'bubble gum', 'chocolate bar', \
        'nerds', 'licorice', 'milky way', 'laffy taffy', 'lollipop'}
    
    #Act 
    result = create_candy_set (favorites)
    
    #Assert
    assert result == expected
    assert len(result) == 8
    assert type(result) == set