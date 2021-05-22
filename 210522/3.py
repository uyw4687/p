sns.heatmap(abs(data.corr()), annot=True)

data['Clicked'].value_counts()

X = data[['Daily Time Spent on Site','Daily Internet Usage']]
y = data['Clicked']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3)
model = LogisticRegression(solver='lbfgs')
model.fit(X_train, y_train)

model.score(X_val, y_val)

model.fit(X, y)
model.predict(test_data[['Daily Time Spent on Site','Daily Internet Usage']])