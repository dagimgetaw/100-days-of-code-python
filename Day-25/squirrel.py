import pandas as pd

squirrel = pd.read_csv('squirrel_dataset.csv')

print(squirrel['Primary Fur Color'].value_counts())

gray_squirrel = len(squirrel[squirrel['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel = len(squirrel[squirrel['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(squirrel[squirrel['Primary Fur Color'] == 'Black'])

data = {
    "Primary Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

data_frame = pd.DataFrame(data)
data_frame.to_csv('squirrel_count.csv')
