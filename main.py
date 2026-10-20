secret = 7
lr = 0.1     #learning rate
guess = 0.0

def loss(guess):
    return (guess - secret) ** 2




for step in range(10):
    nakl = 2 * (guess - secret)
    
    current_loss = loss(guess)
    
    guess = guess - lr * nakl
    
    print(f"Step {step}: guess={guess:.4f}, loss={current_loss:.4f}, gradient={nakl:.2f}")