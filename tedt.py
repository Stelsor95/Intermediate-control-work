def calculate_popularity_coefficient(friends):
    coefficient = friends * 0.1
    return coefficient

user_friends = 5
popularity_coefficient = calculate_popularity_coefficient(user_friends)
print(f"The popularity coefficient of the user is {popularity_coefficient}")