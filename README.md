# Gradient_descent_one_feature
# 1. Some information you need to know about Gradient descent and this project:
## Linear Regression for 1 feature:
- Definition: An important technique to predict a result in Machine Learning is linear regression. In short, it can be described as the most fixed function that stay close to all data points on graph. For linear regression of 1 feature, the function has an input of just one varible and usually appear as a straight line: f(x)=ax+b. In this repositary, I will focus on figuring out this type of linear regression.
- Example:
![image](https://github.com/user-attachments/assets/d77330dc-cdba-462f-aa29-375864d9d85b)
## Loss function:
- Definition: A cost function is a mathematical formula used to measure how well a model's predictions match the actual outcomes. In machine learning, it evaluates how far the model's predictions are from the true values.
- Formula:
![image](https://github.com/user-attachments/assets/a05b0309-95cc-4df7-a82f-48be340e508e)
## Gradient descent algorithm:
- Description: In general, gradient descent helps find the most suitable parameters to reduce value of loss function (which means finding out the fixed function). This algorithm will find the appropriate parameters by going step by step till the appropriate ones are found. The algorithm would require using derivative to calculate (you can find out the clear use of derivative in my "Gradient_descent_algorithm" file). Gradient descent may also be applied in code more effectively through vectorization (the other file I uploaded) as calculations of derivatives will be based on calculating arrays. Please note that in this code, I will just illustrate my work on gradient descent for linear regression of one feature.
- Details:
  + The algorithm will requires continuously updating new parameter values from the previous ones. This includes calculations on derivatives of the Loss function:
  + ![image](https://github.com/user-attachments/assets/116a39fe-6f05-46f7-a37e-b7a62a48b6e5)
  + Once the values updated get e to the previous ones enough, you may end the process and complete the algorithm.
  + In this repositary, I will make a def function to do the algorithm and I will conduct the function 4 times, you may adjust this based on your need.
# 2. Libraries:
- Numpy: I used this library to calculate and work on arrays or other mathematical calculations, including vectorization.
- Matplotlib: I use this to illustrate the function and how fixed it is to the training data points.
*_The libraries may be installed using pip command on terminal!_
# 3. Some notes for you:
- The dataset to train should be small to be convenient for the code run and prevents overload.
- It is easier to run online on Google Colab, Jupiter Lab,... instead on local computer if yours is not strong enough.
- The step can be adjusted, but ensure not to make it too large or small ( usually <1 and >0 is good).
- I also updated the algorithm using Z-score normalization in order to partly help run the code with greater dataset on local computers.
- Feel free to contact me through my Email if you have any questions or want to make it better! I would also love to learn more to improve this algorithm.

  


