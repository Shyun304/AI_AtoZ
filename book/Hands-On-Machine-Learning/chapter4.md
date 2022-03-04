학습 목표
1. Linear Regression model 에서, 
   - "closed-form" equation : directly computes the model parameters that best fit the model to the training set
   - iterative optimization approach called Gradient Descent (GD) : gradually tweaks the model parameters to minimize the cost function over the training set 
     - Batch GD, Mini-batch GD, Stochastic GD 
2. Polynomial Regression
   - more complex model that can fit nonlinear datasets
   - more prone to overfitting the training data
   - several regularization techniques that can reduce the risk of overfitting the training set
3. Logistic Regression
4. Softmax Regression



## Exercises 
1. What Linear Regression training algorithm can you use if you have a training set with millions of features?
2. Suppose the features in your training set have very different scales. What algorithms might suffer from this, and how? What can you do about it?
3. Can Gradient Descent get stuck in a local minimum when training a Logistic Regression model?
4. Do all Gradient Descent algorithms lead to the same model provided you let them run long enough?
5. Suppose you use Batch Gradient Descent and you plot the validation error at every epoch. If you notice that the validation error consistently goes up, what is likely going on? How can you fix this?
6. Is it a good idea to stop Mini-batch Gradient Descent immediately when the validation error goes up?
7. Which Gradient Descent algorithm (among those we discussed) will reach the vicinity of the optimal solution the fastest? Which will actually converge? How can you make the others converge as well?
8. Suppose you are using Polynomial Regression. You plot the learning curves and you notice that there is a large gap between the training error and the validation error. What is happening? What are three ways to solve this?
9. Suppose you are using Ridge Regression and you notice that the training error and the validation error are almost equal and fairly high. Would you say that the model suffers from high bias or high variance? Should you increase the regularization hyperparameter α or reduce it?
10. Why would you want to use:
- Ridge Regression instead of plain Linear Regression (i.e., without any regulari‐
zation)?
- Lasso instead of Ridge Regression?
- Elastic Net instead of Lasso?
11. Suppose you want to classify pictures as outdoor/indoor and daytime/nighttime. Should you implement two Logistic Regression classifiers or one Softmax Regression classifier?
12. Implement Batch Gradient Descent with early stopping for Softmax Regression (without using Scikit-Learn).