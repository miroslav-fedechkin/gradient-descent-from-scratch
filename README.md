# Gradient Descent From Scratch

A simple implementation of gradient descent on a single parameter, written from scratch in Python without any machine learning libraries.

## The Idea
The goal is to find a secret number (7) by minimizing the Mean Squared Error (MSE) loss function.


## How it works
1. Start with a random guess (0).
2. Calculate the gradient (slope).
3. Update the guess by moving against the gradient.
4. Repeat 10 times.

## The Math
The goal is to minimize the Mean Squared Error loss function for a single parameter:

$$L = (guess - secret)^2$$

To find the minimum, we calculate the gradient (derivative) of the loss function:

$$\frac{\partial L}{\partial guess} = 2(guess - secret)$$

Then, we update our guess by moving against the gradient:

$$guess = guess - \alpha \cdot \frac{\partial L}{\partial guess}$$

## How to run
1. Download ```main.py```
2. Run it in terminal 