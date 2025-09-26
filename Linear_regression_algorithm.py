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
# Gradient descent algorithm:
def descent(a,b,step):
  maxloop=0
  while maxloop<=10000000:  # Use maxloop to prevent overrun of the code, you may adjust this figure
    sum1=0
    sum2=0
    #calculate derivatives:
    for i in range (datasize):
       sum1=sum1+(1/datasize)*(a*xtrain[i]+b-ytrain[i])*xtrain[i]
       sum2=sum2+(1/datasize)*(a*xtrain[i]+b-ytrain[i])
    # Just in case we need make changes to sum1 and sum2:
    deria = sum1
    derib = sum2
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
w,t=descent(0.8,6.8,0.0025) # I start at a random a,b value for the descent with step of 0.0025
for m in range (4):
   w,t=descent(w, t, 0.0015)
para1,para2= descent(w,t,0.0005)
# print out the function:
print(f"The linear regression function is: {para1}x+{para2}")
# draw:
x=np.linspace(np.min(xtrain)-2, np.max(xtrain)+2, 500*datasize) 
y=para1*x+para2
plt.plot(x, y, label='Linear regression', color='blue') #plot the function
plt.title("Linear Regression (Gradient Descent)")
plt.show()

