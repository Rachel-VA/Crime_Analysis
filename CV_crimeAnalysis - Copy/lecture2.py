#this program created on 03/24/23,used python 3.10.10 64bit
#lecture demo Reinforcement Learning with Q-table

#this program use RL playing a game (Openai gym CartPole-v1)
import gym
import numpy as np # for using Q-table to manipulate game
#q-table is a numpy array containing columns and rows
import time #for using time lib to slow down to human speed so humans can see it

#create an env and pass in the name as string
env = gym.make("CartPole-v1",render_mode = "human")

#define the numbs of bins for each observation dimension
#4 observations  (rows in Q-table)

#create a var for bin and assign it to 10 (rows)
num_bins = 10

#define theedges of the bins for each observation dimension
#we have 4 observations for this environment:columns in q-table
##the edges are the values will be used to determined which bin to use in the Q-table
#simply: a bin is a row
# we will use min and max values each obs
bin_edges = [np.linspace(-4.8,4.8,num_bins + 1) [1:-1],
             np.linspace(-5,5,num_bins + 1) [1:-1],
             np.linspace(-.418,.418, num_bins + 1) [1:-1],
             np.linspace(-5,5,num_bins + 1) [1:-1]
             
             ]
            
#define the Q-table to store the Q-value for each state
q_table = np.zeros((num_bins, num_bins, num_bins, num_bins, env.action_space.n))

#define the hyperpameters for the Q-learning algorithm
alpha = 0.1 #learning rate

#the discount factor
gamma = 0.99
#exploration the rate
epsilon = 0.1


#define the # of episoles we use to train the agent
#we can play with the numbers to see the effects
#the more episoles the more agent learn
# range can be 50 - 50,000

num_episoles = 200

#create a function to descrete the observation
#this func will take in an obs and return the descret obs
#the descret will be used to determine which row in our q table
def discretize_state(observation):
    return tuple(np.digitize(observation[i], bin_edges[i]) for i in range(len(observation)))

#---------------TRAIN THE AGEN USING Q-LEARNING -------------------------
#**********************************************************************

#
print("\n\n\t\t ********** Welcome to CartPole-v1 training program****************")
print("\nwe only train the best cart here!")
print("the goal is to train the agent to balance on the cart as long as possible\n")
print("We do this by applying forces to the always-moving cart")
print("The cart move left or right\n")
print("The training will begin in 5s\n")
time.sleep(5)
print("Training has begin\n\n")

#create a loop to run 
for episole in range(num_episoles):
    #print abar to seperate the episole
    print("-"*50)
    
    #current episole
    print("Current episole numb:", episole)
    
    #reset
    observation =env.reset()
    
    print("initial observation:", observation)
    
    #create a boolean var to keep track the episole
    done = False
    
    #now loop the episole until it's done (lost/won)
    ##lost: fell or goes off the obs screen
    while not done:
        #render the env for human to see
        env.render()
        #add a small delay
        time.sleep(0.5)#1/2 second
        #have the agent choose the action using epsilon policy for **EXPLORATION policy**
        if np.random.rand() < epsilon:
            #choose a random action which mean the agent explore on its own
            action = env.action_space.sample()
            print("\n\nThe agent is exploring by taking random action: ", action)
            
        else:
            #choose the action with the highest Qvalue from the q-table
            #by row-column for this state
            #agent is using its experience to EXPLOIT what it has to learn
            action = np.argmax(q_table[discretize_state(observation)])
            print("The agent is EXPLOITING by taking the action with the highest Q-value.")
            #agent will EXPLOIT what it has to learn
            print("\nThe action is(EXPLOIT): ", action)
        
            next_observation, reward, don, info = env.step(action)
            print("\nthe agent receive a reward of:", reward, "for taking the action", action)
            
            #update the Q-value for the current state
            old_q_value = q_table[discretize_state(observation)[action]]
            new_q_value = old_q_value + alpha * (reward + gamma * np.max(q_table[discretize_state(next_observation)] - old_q_value))
        q_table[discretize_state(observation)][action] = new_q_value
        
        
        #explain q table
        print("the old q value for the current state action pair was:",old_q_value)
        print("the new q value for the current state action pair is:",new_q_value)
         
         
         #move to next state obs
        observation = next_observation
        
        #result
    print("\n\ntraining episole num:", episole, "is complete")
    print("\n\nthe agent successfull balanced on the pole for ", env._elapsed_steps,"time steps")
    
    
    print("******************TRAINING PART IS COMPLETED AND ENDED HERE*************************")
    
    
    #end of training**********************
    
    
    #################start testing the agent
    
    print("\n\n\t**************************TESTING THE AGENT*******************************************")
    time.sleep(5)
    #set test episole
    num_test_episoles = 10
    print("\n\t TESTING HAS BEGIN")
    for episole in range(num_test_episoles):
        #reset the env
        next_observation = env.reset()
        #show episole numbers
        
        print("\nTest episole numb:", episole)
        
        while not done:
            #render the env
            env.render()
            #delay
            time.sleep(0.05)
            
            #let agent choose an action from Qtable (EXPLOIT)
            
            #*********NO EXPLORATION IN TESTING**************
            print("\ntNO EXPLORATION IN TESTING")
            print("agent will EXPLOIT from Q-TABLE")
            
            action = np.argmax(q_table[discretize_state(observation)])
            
            print("agent recieved a reward of:", reward, "for taking action", action)
            
            """
            Note: it's much easier to test the ganet than TRAIN
            """
            #move to the next state
            observation = next_observation
            
                
        print("\n\tTesting episole:", episole, "is complete")
        print("the agent successfully balance the pole:", env._elapsed_steps,"time step")
        

# Close the environment after testing is complete
env.close()
# Tell the user that testing is complete
print("_" * 50)
print("\nTesting is complete! The agent has learned to balance the pole on the cart.\n\n\n")

    
    