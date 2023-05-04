import random

def simulate(num_trials):
    count = 0
    for i in range(num_trials):
        letters = ['A', 'B', 'C']
        random.shuffle(letters)
        if letters == ['A', 'B', 'C']:
            count += 1
    return 1 - (count / num_trials)

print(simulate(1000000)) # simulate 1 million trials
