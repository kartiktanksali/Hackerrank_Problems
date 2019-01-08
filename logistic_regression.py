import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

pd.set_option('display.expand_frame_repr', False) #To set the frame to full

data = pd.read_csv('banking.csv', header=0) #Importing the data file
data = data.dropna() #Drops all the NA values from the rows
print(data.shape) #Lets us know the number of rows and columns
print(list(data.columns)) #Lists the column names

#Count plot of the binary values of the dependent variable
sns.countplot(x='y',data=data, palette='hls')
plt.show()

count_no_sub = len(data[data['y']==0])
count_sub = len(data[data['y']==1])
pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
print("Percentage of no(0) subscription: ", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)
print("Percentage of yes(1) subscription: ", pct_of_sub*100)

print(data.groupby('y').mean())


#Job Distribution
sns.countplot(y="job", data=data)
plt.show()

#Martial Distribution
sns.countplot(x="marital", data=data)
plt.show()


#Defaulter 
sns.countplot(x="default", data=data)
plt.show()


#Distribution of Housing Loan
sns.countplot(x="housing", data=data)
plt.show()


#Personal Load Distribution
sns.countplot(x="loan", data=data)
plt.show()



#Previous Mmarketing campaign outcome
sns.countplot(x="poutcome", data=data)
plt.show()


#Dropping the Variables we don't need
data.drop(data.columns[[0, 3, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]], axis=1, inplace=True)
print(data.columns)

#Converting Categorical to dummy variable
data2 = pd.get_dummies(data, columns =['job', 'marital', 'default', 'housing', 'loan', 'poutcome'])
print(data2.columns)

print("\n")

#Drop unknown columns
data2.drop(data2.columns[[12, 16, 18, 21, 24]], axis=1, inplace=True)
print(list(data2.columns))


#Heatmap
sns.heatmap(data2.corr())
plt.show()


X = data2.iloc[:,1:]
y = data2.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


#Data Summary
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())

#Applying Regression algorathim
classifier = LogisticRegression(random_state=0)
result = classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#The Confusion Matrix
print("The Confusion Matrix")
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print("\n")
#Accuracy Check
print("The Accuracy of logistic regression classifier on test set: {:.2f}".format(classifier.score(X_test, y_test)))
print("\n")

#Classification Report
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#Mean Absolute Error
from sklearn.metrics import mean_absolute_error
print("The Mean absolute Error:",mean_absolute_error(y_test,y_pred))
print("\n")
#Mean Squared Error
from sklearn.metrics import mean_squared_error
print("The Mean Square Error:",mean_squared_error(y_test,y_pred))

print("\n")
#ROC GRAPH
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, classifier.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
