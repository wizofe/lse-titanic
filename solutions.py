## datatypes demo
# a = 3
# b = '3'
# a + 3
# b + 3
# if else boolean values
# 
# print(a,b)
# print(a+3)
# print(b+' cats')
# print(type(a))
# print(td)

## Show the first 5 entries of the dataset 
# td.head()

## Sort the dataset by the mean value of passenger class
# td.groupby('Pclass').mean()
# pclass = td.pivot_table(index="Pclass",values="Survived")
# pclass.plot.bar()

c1 = sns.countplot(x = td['Pclass'], 
                   hue=td["Alive"],
                   palette = ["#95a5a6", "#2ecc71"])

plt.title("Number of Persons Alive by Class")
