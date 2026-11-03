#!/usr/bin/env python3
"""Plots the number of fruits owned by each person."""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
fruit_names = ['apples', 'bananas', 'oranges', 'peaches']
fruit_colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
positions = np.arange(len(people))
bottom = np.zeros(len(people))

for i, name in enumerate(fruit_names):
    plt.bar(positions, fruit[i], width=0.5, bottom=bottom,
            color=fruit_colors[i], label=name)
    bottom += fruit[i]

plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.ylim(0, 80)
plt.xticks(positions, people)
plt.yticks(np.arange(0, 81, 10))
plt.legend()
plt.show()
