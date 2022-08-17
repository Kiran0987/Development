import random

def flipCoin():
    heads = 0 
    tails = 0 
    headspercent = 0
    tailspercent = 0 

    for i in range(int(input("Enter number of times to flip coin:"))):
      coin=random.randint(1,2) 

      if coin==1:
          heads+=1 
      else: 
          tails+=1 

    headspercent = heads / 100 
    tailspercent = 100.0 - headspercent 

    print("Heads percent: " + str(headspercent)) 
    print("Tails percent: " + str(tailspercent)) 

flipCoin()