import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.pipeline import Pipeline

data_path = "../data/raw/california_housing_0.csv"

data = pd.read_csv(data_path)

data.head()

data.shape

data.isna().sum()

data = data.drop(columns="total_bedrooms")

data_train, data_test = train_test_split(data, test_size=0.33, random_state=0)

data_train.shape, data_test.shape

# # Select X and y values (predictor and outcome)
X_train = data_train.drop(columns="median_house_value")
y_train = data_train["median_house_value"]

X_test = data_test.drop(columns="median_house_value")
y_test = data_test["median_house_value"]

X_train.shape, X_test.shape

sc = StandardScaler()
lin_reg = LinearRegression()
pipeline_mlr = Pipeline([("data_scaling", sc), ("estimator", lin_reg)])

pipeline_mlr.fit(X_train, y_train)

predictions_mlr = pipeline_mlr.predict(X_test)

# Test score
pipeline_mlr.score(X_test, y_test)

print("MAE", metrics.mean_absolute_error(y_test, predictions_mlr))
print("MSE", metrics.mean_squared_error(y_test, predictions_mlr))
print("RMSE", np.sqrt(metrics.mean_squared_error(y_test, predictions_mlr)))
print("Explained Var Score", metrics.explained_variance_score(y_test, predictions_mlr))