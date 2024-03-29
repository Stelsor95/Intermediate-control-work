def calculate_popularity(user_id, users):
  """
  Вычисляет коэффициент популярности пользователя по количеству друзей.

  Args:
    user_id: ID пользователя, для которого вычисляется коэффициент популярности.
    users: Словарь пользователей, где ключами являются идентификаторы пользователей, а значениями - словари с информацией о пользователях (включая список друзей).

  Returns:
    Коэффициент популярности пользователя.
  """

  # Получить список друзей пользователя.
  friends = users[user_id]["friends"]

  # Вычислить коэффициент популярности как отношение количества друзей к общему количеству пользователей.
  popularity = len(friends) / len(users)

  return popularity

# Создать словарь пользователей.
users = {
    1: {"friends": [2, 3]},
    2: {"friends": [1, 4]},
    3: {"friends": [1, 5]},
    4: {"friends": [2, 5]},
    5: {"friends": [3, 4]}
}

# Вычислить коэффициент популярности пользователя с ID 1.
user_id = 1
popularity = calculate_popularity(user_id, users)

# Вывести коэффициент популярности.
print(popularity)  # Выведет 0.4

# ИЛИ

def calculate_popularity_coefficient(friends):
    coefficient = friends * 0.1
    return coefficient

user_friends = 500
popularity_coefficient = calculate_popularity_coefficient(user_friends)
print(f"The popularity coefficient of the user is {popularity_coefficient}")