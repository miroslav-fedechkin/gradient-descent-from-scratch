secret = 42387326454654645664564584848
lr = 0.1     #learning rate
guess = 0.0

def loss(guess):
    return (guess - secret) ** 2


counter = 0

while True:
    counter += 1

    nakl = 2 * (guess - secret)
    
    current_loss = loss(guess)
    
    guess = guess - lr * nakl
    
    print(f"Step {counter}: guess={guess:.4f}, loss={current_loss:.4f}, gradient={nakl:.2f}")
