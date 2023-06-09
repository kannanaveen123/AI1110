import random

def simulate(num_trials):
    count = 0
    for i in range(num_trials):
        letters = ['A', 'B', 'C']
        envelopes = ['A', 'B', 'C']
        random.shuffle(envelopes)
        if envelopes != letters:
            count += 1
    return count / num_trials

print(simulate(1000000)) # simulate 1 million trials
