# PART 1 INTRODUCTION 
# Set working directory and import the datafiles
setwd("~/Documents/code/r/titanic/")
df_train <- read.csv("~/Documents/bootcamps/data/titanic/train.csv", sep=",")
df_test <- read.csv("~/Documents/bootcamps/data/titanic/test.csv", sep=",")
# PART 2 SLICING AND DICING
str(df_train)
df_train$Survived
table(df_train$Survived)
prop.table(table(df_train$Survived))
# Since a lot of people (almost 62%) died, we can predict that in the test set
# The majority of people will not survive the disaster
# Of course our test file did not contain a column "Survived", because we were
# going to predict that from df_train
# S, we add that column, "Survived" to our test dataframe
df_test$Survived <- rep(0, 418)
# Next we extract our report on what we can predict
submit <- data.frame(PassengerId = df_test$PassengerId, Survived = df_test$Survived)
write.csv(submit, file="theyallperish.csv", row.names = FALSE)
# Not a bad first try. We will probably have guessed around 60% good:-)!
# Quick check: What about "women and children first"?
summary(df_train$Sex)
# So most passengers were male. How were the survival rates cf. gender
# We just have to pass in the extra column in our prop.table snippet above
prop.table(table(df_train$Sex, df_train$Survived))
# Mhh, the proportion is taken from the total number of passengers
# We want a row-wise proportion (proportion of gender survived)
# We need to tell R that we want proportions in the row dimensions: 1
prop.table(table(df_train$Sex, df_train$Survived), 1)
# We can now update our test set in the following way:
df_test$Survived[df_test$Sex == 'female'] <- 1
# Now were we to submit this new prediction, we would have ~ 75% predicted OK!
# Let's generate the new submit file
submit <- data.frame(PassengerId = df_test$PassengerId, Survived = df_test$Survived)
write.csv(submit, file="theyallperish.csv", row.names = FALSE)
# We are getting there - let's have a look at the age variable
# As always we start with the summary function on the column
summary(df_train$Age)
# A few things to notice: Not very many elderly persons. Missing values: 177
# Age is of course a continouous variable, which makes drawing proportion
# tables useless. We are going to add another variable: Child and we put up
# a 1 for TRUE if $Age < 18
# First we fill all values with 0
df_train$Child <- 0 # Check that df_train now has 13 variables
# Then we flip age < 18 to 1
df_train$Child[df_train$Age < 18] <- 1
# What happened with our NA's? All became 0's which is Ok. Would have happened
# if we had assigned them the mean or median age.
# Next we want to generate a table to see how gender and age relate to survival
# This can not be done with prop.table, we have to use the aggregate function
aggregate(Survived ~ Child + Sex, data = df_train, FUN = sum)
# This is ok, but, again, we we do not get the proportions for each group
aggregate(Survived ~ Child + Sex, data = df_train, FUN = function(x) {sum(x)/length(x)})
# Conclusion: Basic image stays the same, so we do not need to re-work pred.
# Other interesting variables to explore: Class, ticketprice
# Class is simple: Int with 3 variants: 1, 2, and 3
# Ticketprices ($Fare) again is a continuous numerical value => bin these
df_train$Fare2 <- '30+'
# Now all Fare2 variables have been assigned the value '30+'
# We are going to construct three more bins selected from Fare variable
df_train$Fare2[df_train$Fare < 30 & df_train$Fare >= 20] <- '20-30'
df_train$Fare2[df_train$Fare < 20 & df_train$Fare >= 10] <- '10-20'
df_train$Fare2[df_train$Fare < 10] <- '<10'
# Now we can run a longer aggregate function
aggregate(Survived ~ Fare2 + Pclass + Sex, data = df_train, FUN = function(x) {sum(x)/length(x)})
df_test$Survived[df_test$Sex == 'female' & df_test$Pclass == 3 & df_test$Fare >= 20] <- 0
# Were we to put our prediction up on Kaggle, we would hit a 77% predicted ok
# So we did a lot of work, but we only got a 2% better score.
# Preliminary conclusion: "Women and children first, travel first class"
# More variables into play, more slicing and dicing, smaller bins?

# Time for reflection: Can we automate this kind of analysis?
# PART 3 DECISION TREES
# Enter machine learning: Decision trees
# We use the R library "rpart"
library(rpart)
# Sofar we looked at Survived in relation to $Gender, $Age, $Pclass, and $Fare
# Some variables are not that interesting: Passenger names, ticket#, cabin#
# Let's put all the other things into rpart and generate a tree
fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
             data = df_train,
             method = "class")
# Mhh, we need some more serious stuff: Better graphics for rpart
install.packages('rpart.plot')
#install.packages('RColorBrewer')
library(rpart.plot)
library(RColorBrewer)
rpart.plot(fit)
# From the model "fit", the tree, we can actually make a prediction without all
# the subsetting and overwriting
Prediction <- predict(fit, df_test, type = "class")
# Now we generate our submit object
submit <- data.frame(PassengerId = df_test$PassengerId, Survived = Prediction)
write.csv(submit, file = "myfirstdtree.csv", row.names = FALSE)
# PART 4 FEATURE ENGINEERING
# Feature engineering is all about human ingenuity and creativity
# Simple models with great features outperform complicated stuff with poor ones
# For example: We did not use the three text fields in our dtree
df_train$Name[1:20]
# We see titles: Mr., Mrs., Miss., Master, etc.
# Let's see if titles, combined with Age and Sex might provide us with xtra
df_test$Survived <- NA
# In order to combine both train and test sets we load the orginal train set
# Because we added two columns: Child and Fare2
train <- read.csv("~/Documents/bootcamps/data/titanic/train.csv", sep=",")
combi <- rbind(train, df_test)
# We have now all our 1309 passengers in one file, but with $Name as a factor
# We want names as strings: The function "as.character" to the rescue
combi$Name <- as.character(combi$Name)
combi$Name[1]
# Next regular expressions to the rescue
strsplit(combi$Name[1], split = '[,.]')
strsplit(combi$Name[1], split = '[,.]')[[1]]
strsplit(combi$Name[1], split = '[,.]')[[1]][2]
# Next we use a mapping function to map our function over all names in the col
combi$Title <- sapply(combi$Name, FUN = function(x) {strsplit(x, split = '[,.]')[[1]][2]})
# Now, and only now, we get rid of the spaces in front of the title
combi$Title <- sub(' ', '', combi$Title)
# Let's have a look
table(combi$Title)
# We should weed out the exotica
# Then cast the column back into to a factor
# We make Mlle and Ms into Miss
combi$Title[combi$Title %in% c('Ms', 'Mlle')] <- 'Miss'
combi$Title[combi$Title %in% c('Mme')] <- 'Mrs'
combi$Title[combi$Title %in% c('Capt', 'Don', 'Major', 'Sir', 'Jonkheer', 'Rev', 'Col', 'Dr')] <- 'Sir'
combi$Title[combi$Title %in% c('Dona', 'Lady', 'the Countess')] <- 'Lady'
table(combi$Title)
combi$Title <- factor(combi$Title)
# Next feature (mind you, the author is using knowledge about the disaster!)
# Alright. We’re done with the passenger’s title now. What else can we think
# up? Well, there’s those two variables SibSb and Parch that indicate the
# number of family members the passenger is travelling with. Seems reasonable
# to assume that a large family might have trouble tracking down little Johnny
# as they all scramble to get off the sinking ship, so let’s combine the two
# variables into a new one, FamilySize:
combi$FamilySize <- combi$SibSp + combi$Parch + 1
# We extract all the surnames
combi$Surname <- sapply(combi$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][1]})
# Then we combine that column with the familysize
combi$FamilyID <- paste(as.character(combi$FamilySize), combi$Surname, sep="")
# We try to knock out the small families
combi$FamilyID[combi$FamilySize <= 2] <- 'Small'
table(combi$FamilyID)
# We missed out on a lot of cases here, let's clean it up
famIDs <- data.frame(table(combi$FamilyID))
famIDs <- famIDs[famIDs$Freq <= 2,]
combi$FamilyID[combi$FamilyID %in% famIDs$Var1] <- 'Small'
combi$FamilyID <- factor(combi$FamilyID)
df_train <- combi[1:891,]
df_test <- combi[892:1309,]
# Try out a new model
fit2 <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Title + FamilySize + FamilyID,
             data = df_train, 
             method = "class")
rpart.plot(fit2)
# PART 5 RANDOM FORESTS
