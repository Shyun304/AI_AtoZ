
## Exercises.   
1.  How would you define Machine Learning?
    - 사람이 입력에 대한 결과 도출 방법을 제안하지 않고 데이터를 받은 모델이 스스로 학습하는 형식 

2. Can you name four types of problems where it shines?
   - Problems for which existing solutions require a lot of hand-tuning or long lists of rules: one Machine Learning algorithm can often simplify code and perform bettter
   - Complex problems for which there is no good solution at all using a traditional approach: the best Machine Learning techniques can find a solution.
   - Fluctuating environments: a Machine Learning system can adapt to new data.
   - Getting insights about complex problems and large amounts of data.

3. What is a labeled training set?
    - the traing data you feed to the algorithm includes the desired solutions
4. What are the two most common supervised tasks?
   - classification, regression
5. Can you name four common unsupervised tasks?
   - clustering
   - anomaly detection and nvelty detection
   - visualization and dimensionalith reduction
   - association rule learning
6. What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?
   - reinforcement learning
7. What type of algorithm would you use to segment your customers into multiple
groups?
    - clustering
8. Would you frame the problem of spam detection as a supervised learning prob‐
lem or an unsupervised learning problem?
    - unsupervised learning problem
9. What is an online learning system?
    - it train the system incrementally bu feeding it data instances sequentially. 
10. What is out-of-core learning?
    - 메모리에 다 올라가지 않을 정도로 큰 데이터를 학습하는 것
11. What type of learning algorithm relies on a similarity measure to make predic‐
tions?
    - instance-based learning
12. What is the difference between a model parameter and a learning algorithm’s
hyperparameter?
    - ???
13. What do model-based learning algorithms search for? What is the most common
strategy they use to succeed? How do they make predictions?
    - ???
14. Can you name four of the main challenges in Machine Learning?
    - ???
15. If your model performs great on the training data but generalizes poorly to new
instances, what is happening? Can you name three possible solutions?
    - Overfitting이 발생. 
      - 1. 더 적은 parameter 수를 이용
      - 2. 더 많은 training data 수집
      - 3. training data 의 noise 제거 
16. What is a test set and why would you want to use it?
    - 학습에 전혀 사용되지 않은 데이터로 모델을 평가하는 기준이 될 수 있음
17. What is the purpose of a validation set?
    - 특정 test set 에서만 잘 작동하는 모델이 만들어질 수도 있으니 여러 가지의 test set을 통해서 평가를 함
18. What can go wrong if you tune hyperparameters using the test set?
    - test set에 specific하게 학습되어 새로운 데이터에 적용되지 않을 수 있음
19. What is repeated cross-validation and why would you prefer it to using a single
validation set?
    - 다양한 validation set에 대해 모델의 평가가 이루어지기 때문에 객관적임
    
