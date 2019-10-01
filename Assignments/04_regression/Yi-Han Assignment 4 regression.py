# In[1] import package and load data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
import tkinter as tk
from tkinter import filedialog

# Select and read csv file
root = tk.Tk()
root.withdraw()
Loaded_data = filedialog.askopenfilename()
data=pd.read_csv(Loaded_data, names = ['x_term','Data1','Data2','Data3','Data4'],skiprows = 1)

# In[2] define function BIC

def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    BI = n*np.log(sigma**2) + weight*k*np.log(n)
    return BI

# In[3] Fitting polynoimal with lowest BIC


X = data['x_term'][:,np.newaxis]### create column vector of features for fit

fit_data = 'Data1' # assign the data set to be fitted
bic_result=[]
for i in range(50):
#  data preparation
    fitting_degree = i
    polynomial_features = PolynomialFeatures(degree = fitting_degree)
    X_TRANSF = polynomial_features.fit_transform(X)
# define and train a model    
    model = LinearRegression()
    model.fit(X_TRANSF, data[fit_data])

# prediction
    X_NEW = np.linspace(min(data['x_term']), max(data['x_term']), len(data['x_term'])) # len(Y_NEW) need to match len(data['Data1']) for BIC analysis
    X_NEW = X_NEW[:,np.newaxis]
    X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)
    Y_NEW = model.predict(X_NEW_TRANSF)
    
    h = BIC(data[fit_data],Y_NEW,i)
    bic_result.append(h)
    if len(bic_result)>15: # at least fit to degree = 15 to make sure finding global minimum
        if bic_result[-1]>bic_result[-2]:
            break
        else:
            pass
# plot the data and fitting curve with lowest BIC, report the degree and BIC value
fitting_degree = bic_result.index(min(bic_result))
polynomial_features = PolynomialFeatures(degree = fitting_degree)
X_TRANSF = polynomial_features.fit_transform(X)
# define and train a model    
model = LinearRegression()
model.fit(X_TRANSF, data[fit_data])
# prediction
X_NEW = np.linspace(min(data['x_term']), max(data['x_term']), len(data['x_term'])) # len(Y_NEW) need to match len(data['Data1']) for BIC analysis
X_NEW = X_NEW[:,np.newaxis]
X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)
Y_NEW = model.predict(X_NEW_TRANSF)
# plot
curve1 = plt.scatter(data['x_term'],data[fit_data])
plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)
plt.xlabel('x value')
plt.ylabel('y value')
plt.title("Fit Polynomial (degree ="+ str(fitting_degree) +")")
plt.grid()
plt.show()
    
print("Lowest BIC =", min(bic_result), "at degree =", fitting_degree)   
    
plt.plot(range(len(bic_result)),bic_result)
plt.xlabel('degree of polynomial')
plt.ylabel('BIC value')
plt.show()