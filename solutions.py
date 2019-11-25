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


sns.set_palette("Paired")

plot2 = sns.barplot(x=td['Pclass'], y= td['Survived'])

td['Alive'] = td['Survived'].apply(convert_survivor)
byPclass = td.groupby('Pclass')
print(byPclass['Survived'].mean())

plt.figure()

# histogram across a categorical (v.s. quantitative) variable
plot1 = sns.countplot(x = td['Pclass'], 
                   hue=td['Alive'])
plt.title('Number of Persons Alive by Class')
