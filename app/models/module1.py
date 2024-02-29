
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

data = pd.read_excel("../datasets/Fact_hyg_imp.xlsx")
data1 = pd.read_excel("../datasets/snap_ben.xlsx")
data2 = pd.read_excel("../datasets/access_imp4.xlsx")

X = data[['Nbr_Resto', 'Nbr_GYM', 'DIRSALES_FARMS', 'FRESHVEG_FARMS', 'FOOD_INSEC']]
y = data[['OBESE_POP']]

X1 = data[['Nbr_Resto', 'OBESE_POP', 'DIRSALES_FARMS', 'FRESHVEG_FARMS', 'LOWACCESS_POP', 'FOOD_INSEC']]
y1 = data[['Nbr_GYM']]

X2 = data1[['Household_size__people', 'Gross_countable_income_as_a_percentage_of_poverty',
            'Gross_countable_household_income__dollars_month', 'SNAP_certification_period__months']]
y2 = data1[['SNAP_household_benefit__dollars_month']]

y3 = data2[['Store_Non_AP']]
X3 = data2[['AP_Population', 'Total_Stores', 'FOOD_INSECURITY', 'LOWACCESS_POP', 'Population_State', 'FOOD_BANKS']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)
log_reg = RandomForestRegressor(n_estimators=100, random_state=5)
log_reg.fit(X_train, y_train)

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=5)
log_reg1 = LinearRegression()
log_reg1.fit(X1_train, y1_train)

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=5)
log_reg2 = LinearRegression()
log_reg2.fit(X2_train, y2_train)

X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=5)
DtReg = DecisionTreeRegressor(random_state=0)
DtReg.fit(X3_train, y3_train)

pickle.dump(log_reg, open('../serialized/model.pkl', 'wb'))
model = pickle.load(open('../serialized/model.pkl', 'rb'))

pickle.dump(log_reg1, open('../serialized/model1.pkl', 'wb'))
model1 = pickle.load(open('../serialized/model1.pkl', 'rb'))

pickle.dump(log_reg2, open('../serialized/model2.pkl', 'wb'))
model2 = pickle.load(open('../serialized/model2.pkl', 'rb'))

pickle.dump(DtReg, open('../serialized/model3.pkl', 'wb'))
model3 = pickle.load(open('../serialized/model3.pkl', 'rb'))
