import random

def recommend_users(user_id):
  """
  Выбирает 5 пользователей в случайной комбинации, которые удовлетворяют хотя бы одному критерию:
  а) из одного города
  б) состоят в одной группе
  в) друзья друзей

  Args:
    user_id: ID текущего пользователя.

  Returns:
    Список из 5 рекомендованных пользователей.
  """

  # Получить список всех пользователей.
  users = get_all_users()

  # Создать пустой список рекомендованных пользователей.
  recommended_users = []

  # Проверить всех пользователей, кроме текущего, по трем критериям.
  for user in users:
    if user != user_id:
      if users[user]["city"] == users[user_id]["city"]:
        recommended_users.append(user)
      elif users[user]["group"] == users[user_id]["group"]:
        recommended_users.append(user)
      else:
        for friend in users[user_id]["friends"]:
          if friend in users[user]["friends"]:
            recommended_users.append(user)

  # Выбрать 5 случайных пользователей из списка рекомендованных пользователей.
  return random.sample(recommended_users, 5)

def get_all_users():
  """
  Возвращает словарь со всеми пользователями.

  Returns:
    Словарь, в котором ключами являются идентификаторы пользователей, а значениями - словари с информацией о пользователях.
  """

  users = {
    1: {"city": "Москва", "group": "Группа 1", "friends": [2, 3]},
    2: {"city": "Москва", "group": "Группа 1", "friends": [1, 4]},
    3: {"city": "Санкт-Петербург", "group": "Группа 2", "friends": [1, 5]},
    4: {"city": "Москва", "group": "Группа 3", "friends": [2, 5]},
    5: {"city": "Санкт-Петербург", "group": "Группа 2", "friends": [3, 4]}
  }

  return users

# Получить ID текущего пользователя.
user_id = 1

# Получить список рекомендованных пользователей.
recommended_users = recommend_users(user_id)

# Вывести список рекомендованных пользователей.
print(recommended_users)