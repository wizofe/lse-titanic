## datatypes demo
# a = 3
# b = '3'
# a + 3
# b + 3
# if else boolean values
# print(a,b)
# print(a+3)
# print(b+' cats')
# print(type(a))
# print(td)

# now lets say you want to go shopping and you need a collection of items
# shopping_list = ['oat milk', 'apples']
# shopping_list[1]
# phonebook = { 'noel a': '+44010', 'sarah b': '+33212'}
# phonebook['sarah b']



# Main solution
## To show the first 5 entries of the dataset we use the head function of Pandas
# td.head()

## To sort the dataset by the mean value of passenger class
# td.groupby('Pclass').mean()

## Tho show the survival rate depending on the passenger class
## we are using seaborn's barplot function
## The error bars show the variability in the upper quartiles
plot2 = sns.barplot(x=td['Pclass'], y= td['Survived']*100)

## create a new figure
# plt.figure()

## To show the number of persons alive by class
## we are using the countplot from seaborn
## histogram across a categorical (v.s. quantitative) variable
# plot1 = sns.countplot(x = td['Pclass'], 
#                   hue=td['Alive'])
# plt.title('Number of Persons Alive by Class')
