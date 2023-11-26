import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Решение
pd.get_dummies(data['whoAmI'])

# Решение без get_dummies
human_lst = list(map(lambda el: 1 if el == 'human' else 0, lst))
robot_lst = list(map(lambda el: 1 if el == 'robot' else 0, lst))

data = {'human': human_lst, 'robot': robot_lst}
new_df = pd.DataFrame(data)
