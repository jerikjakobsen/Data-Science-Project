import sklearn
import xgboost as xgb
import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.metrics import precision_score, recall_score, accuracy_score, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from numpy import absolute

df = pd.read_csv("../CSVFiles/EncodedSalesListing.csv")

data = df.drop(columns=["Days on Market"])
labels = df['Days on Market']
X_train, X_test, Y_train, Y_test = train_test_split(data, labels, test_size=0.2, random_state=254)
evalset = [(X_train, Y_train), (X_test, Y_test)]

xgbRGR = xgb.XGBRegressor(verbosity=0)
parameters = {
     "eta"    : [0.1, 0.2, 0.25, 0.3] ,
     "max_depth"        : [2 ,3, 6, 8, 10, 15, 20],
     "min_child_weight" : [0.1, 0.5, 0.8 ,1, 7, 10 ]
    }
CV = GridSearchCV(xgbRGR, parameters,n_jobs=-1,
                    scoring="neg_root_mean_squared_error",
                    cv=3)
CV.fit(X_train, Y_train, eval_set=evalset, eval_metric='rmse')
print("XGBoost Grid Search Best params: ", CV.best_params_)
best = CV.best_estimator_
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
scores = cross_val_score(best, X_test, Y_test, scoring='neg_root_mean_squared_error', cv=cv, n_jobs=-1, error_score="raise")
scores = absolute(scores)
print('First Model Mean Root Mean Squared Error: %.3f (%.3f)' % (scores.mean(), scores.std()) )
results = best.evals_result()
plt.title("Grid Searched XGBoost Model")
plt.ylabel("Root Mean Squared Error")
plt.xlabel("Iteration")
plt.plot(results['validation_0']['rmse'], label='train')
plt.plot(results['validation_1']['rmse'], label='test')
# show the legend
plt.legend()
# show the plot
plt.show()





xgbRGR2 = xgb.XGBRegressor()
xgbRGR2.fit(X_train, Y_train, eval_set=evalset, eval_metric='rmse')
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
scores = cross_val_score(xgbRGR2, X_test, Y_test, scoring='neg_root_mean_squared_error', cv=cv, n_jobs=-1, error_score="raise")
scores = absolute(scores)
print('Second Model Mean Root Mean Squared Error: %.3f (%.3f)' % (scores.mean(), scores.std()) )
results = xgbRGR2.evals_result()

# plot learning curves
plt.title("Default XGBoost Model")
plt.ylabel("Root Mean Squared Error")
plt.xlabel("Iteration")
plt.plot(results['validation_0']['rmse'], label='train')
plt.plot(results['validation_1']['rmse'], label='test')
# show the legend
plt.legend()
# show the plot
plt.show()