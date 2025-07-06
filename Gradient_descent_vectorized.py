# import Libraries:
import numpy as np
import matplotlib.pyplot as plt
datasize=int(input("Enter the size of your model(number of data batches):"))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
# create training data sets:
xtrain=np.zeros(datasize, dtype=float)
ytrain=np.zeros(datasize, dtype=float)
for j in range (datasize):
    # enter dataset:
    xtrain[j]=float(input("Enter value x for the data set:"))
    ytrain[j]=float(input("Enter the y value corresponding with previous x:"))
    plt.plot(xtrain[j], ytrain[j], 'ro')
xtrain_copy=xtrain
ytrain_copy=ytrain
# Scale dataset:
x_mean = np.mean(xtrain)
x_std = np.std(xtrain)
xtrain= (xtrain - x_mean) / x_std
y_mean = np.mean(ytrain)
y_std = np.std(ytrain)
ytrain=(ytrain - y_mean) / y_std
# Choose start parameters:
u=1
v=1
# Gradient descent algorithm:
def descent(a,b,step):
  maxloop=0
  while maxloop<=10000000:  # Use maxloop to prevent overrun of the code, you may adjust this figure
    # create arrays to vectorize the algorithm:
    ypre=a*xtrain+b
    error= ypre-ytrain
    deria = np.dot(error, xtrain)*(1/datasize)
    derib = sum(error)*(1/datasize)
    # Temporarily store the new values to anew and bnew:
    anew=a-step*deria
    bnew=b-(step+0.017)*derib # I need to adjust b to increase step by 0.017, you may also adjust this figure.
    if abs(anew - a) < 0.0011 and abs(bnew - b) < 0.0011: # Compare if the anew, bnew values get close enough to previous a,b values.
     break # end the loop
    else:
       a=anew
       b=bnew
       maxloop=maxloop+1
  return a,b
# I want to run the descent multiple times to make changes to the steps and prevent overload:
w,t=descent(u,v,0.0025)
for m in range (4):
   w,t=descent(w, t, 0.0015)
para1,para2= descent(w,t,0.0005)
# Find real parameters:
para1_true= para1*(y_std / x_std)
para2_true=y_mean-para1_true*x_mean
# print out the function:
print(f"The linear regression function is: {para1_true}x+{para2_true}")
# draw:
x=np.linspace(np.min(xtrain_copy)-2, np.max(xtrain_copy)+2, 500*(int(abs(np.max(xtrain_copy)-np.min(xtrain_copy))))) 
y=para1_true*x+para2_true
plt.plot(x, y, label='Linear regression', color='blue') #plot the function
plt.title("Linear Regression (Gradient Descent)")
plt.show()
