import math as mt 
import random as rd 

def sigmoide(t):
    return 1/(1 + mt.exp(-t))

def sigmoide_p(t):
    # define the derivata of sigmoide function
    return sigmoide(t)*(1 - sigmoide(t)) 

def train():

    # random weights
    w1 = rd.random()
    w2 = rd.random()
    # random bias
    b = rd.random()

    # initial settings
    iterations = 10000 
    learning_rate = 0.1 # range 0 to 1
    
    for i in range(iterations):
       
        # get random item from dataset
        random_index = rd.randint(0,len(dataset)-1) 
        point = dataset[random_index]

        # preditiction network (with forward propagation)
        # formula is sum of all inputs (in this case just 2) with their weights and the bias
        z = point[0] * w1 + point[1] * w2 + b
        prediction = sigmoide(z) # sigmoide to have range 0 to 1
        
        # get target value
        target = point[2]
        
        # squared error cost function --> indicates how far the neural network's prediction is from the result it should give us
        # formula is: (prediction - target)^2 -->   the goal is to minimize this cost
        cost = (prediction - target)**2 
        
        # calculate partial derivate with formula
        dcost_dpred = 2 * (prediction - target)
        
        # chain rules
        dcost_dz = dcost_dpred * sigmoide_p(z)  # derivata parziale di z rispetto alla previsione
        dcost_dw1 = dcost_dz * point[0]         # derivata parziale del costo rispetto a w1
        dcost_dw2 = dcost_dz * point[1]         # derivata parziale del costo rispetto a w2
        dcost_db = dcost_dz * 1                 # derivata parziale del costo rispetto a b
        
        # refresh dataset with new weight and bias values
        # back propagation
        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db
        
        # return new values
        return w1, w2, b

# just a generic mock dataset used for training
# structur is [value1, value2, target]
dataset=[
    [9,     7.0,    0],
    [2,     5.0,    1],
    [3.2,   4.94,   1],
    [9.1,   7.46,   0],
    [1.6,   4.83,   1],
    [8.4,   7.46,   0],
    [8,     7.28,   0],
    [3.1,   4.58,   1],
    [6.3,   9.14,   0],
    [3.4,   5.36,   1]
]    

rd.seed(1)

# start the train
w1, w2, b = train()

# empty array that will count the predictions
pred=[]

# used to classify anything that can be defined by two main characteristics
for item in dataset:
    z = w1 * item[0] + w2 * item[1] + b
    prediction=sigmoide(z)
    # add label to item
    if prediction <= 0.5:
        pred.append('disc 1')
    else: 
        pred.append('disc 2')

print(pred)