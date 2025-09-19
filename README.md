# Matchstick Game: A Developer's Journey into AI and Game Theory

## Overview

Welcome to the Matchstick Game project! This repository is more than just a collection of scripts; it's a chronicle of a developer's journey into the fascinating world of game theory, data analysis, and artificial intelligence. Inspired by a simple mathematical puzzle from a Leaving Certificate question, this project transforms a classic game into a playground for exploring complex computational concepts.

The game is simple: two players take turns removing 1, 2, or 3 matchsticks from a pile of 15. The player who is forced to take the last matchstick loses. But beneath this simple exterior lies a rich problem space for developing strategic AI, analyzing game data, and even visualizing decision-making processes.

This project is a testament to the power of iterative development and a practical demonstration of how to:

*   **Deconstruct a mathematical problem** into a programmable game.
*   **Simulate thousands of games** to generate a rich dataset.
*   **Apply machine learning** to uncover winning strategies and predict outcomes.
*   **Visualize complex decision trees** to understand the AI's "thinking" process.

Whether you're a student, a developer, or just a curious mind, this project offers a unique and personal look at the intersection of gaming, data, and AI.

## Project Stages

The project is divided into three main stages, each building upon the last to create a comprehensive analysis of the Matchstick Game.

### M1: The Game Stage

This is where it all begins. The core game logic is implemented in Python, with several variations to explore different gameplay scenarios:

*   **V1: Human vs. Human:** A simple implementation for two human players.
*   **V2: Computer vs. Computer:** Two AI players battle it out with random moves.
*   **V3: Human vs. Computer:** Test your skills against a random AI opponent.
*   **V4: Automated Simulations:** An iterated version of the computer vs. computer game, designed to generate data for the next stage.

### M2: The Data Stage

With the game in place, the focus shifts to data. This stage is all about running simulations, collecting data, and preparing it for analysis.

*   **Data Generation:** The project runs thousands of automated games to collect a wealth of data on game outcomes and move sequences.
*   **Data Storage:** The collected data is stored in both CSV files for easy access and a MySQL database for more robust data management.
*   **Data Analysis:** Scripts are included to clean, process, and analyze the data, providing insights into win rates and player strategies.

### M3: The Classification Stage

This is where the magic happens. The data collected in the previous stage is used to train a machine learning model to understand and predict the game.

*   **Machine Learning Model:** A Random Forest Classifier is trained using the popular scikit-learn library.
*   **Predictive Analysis:** The model analyzes game data to predict the winner based on the moves made.
*   **Decision Tree Visualization:** The project includes scripts to generate and visualize decision trees, offering a fascinating glimpse into the AI's decision-making process.

## Key Features

*   **Multiple Game Modes:** Play against a friend, a computer, or watch two AIs battle it out.
*   **Data-Driven AI:** An AI that learns from thousands of simulated games.
*   **Predictive Modeling:** A machine learning model that can predict game outcomes with impressive accuracy.
*   **Visual Insights:** Generates decision tree diagrams to visualize the AI's strategy.
*   **Comprehensive Documentation:** A detailed developer log that chronicles the entire journey, from initial idea to final implementation.

## Visualizing the Logic

To better understand the project's structure and the game's flow, here are a couple of diagrams:

### Project Architecture

```
+-----------------+      +-----------------+      +------------------------+
|                 |      |                 |      |                        |
|  M1_Game_Stage  +------> M2_Data_Stage   +------> M3_Classification_Stage|
| (Game Logic)    |      | (Data & Storage)|      | (Machine Learning)     |
|                 |      |                 |      |                        |
+-----------------+      +-----------------+      +------------------------+
        |                      |                      |
        v                      v                      v
+-----------------+      +-----------------+      +------------------------+
| - Human vs Human|      | - CSV & MySQL   |      | - Random Forest Model  |
| - Comp vs Comp  |      | - Data Cleaning |      | - Prediction Analysis  |
| - Human vs Comp |      | - Graphing Wins |      | - Decision Tree Viz    |
+-----------------+      +-----------------+      +------------------------+
```

### Game Flow

```
+-----------------+
|   Start Game    |
| (15 Matchsticks)|
+-----------------+
        |
        v
+-----------------+
|   Player 1's    |
|      Turn       |
+-----------------+
        |
        v
+-----------------------------+
| Player 1 picks 1, 2, or 3   |
|      matchsticks            |
+-----------------------------+
        |
        v
+-----------------+
|  Any remaining  | --(Yes)--> +-----------------+
|   matchsticks?  |            |   Player 2's    |
+-----------------+            |      Turn       |
        |                      +-----------------+
        |                              |
      (No)                             v
        |                +-----------------------------+
        v                | Player 2 picks 1, 2, or 3   |
+-----------------+      |      matchsticks            |
|  Player 2 Wins! |      +-----------------------------+
+-----------------+                      |
                                         v
                         +-----------------+
                         |  Any remaining  | --(Yes)--> (Back to Player 1's Turn)
                         |   matchsticks?  |
                         +-----------------+
                                 |
                               (No)
                                 |
                                 v
                         +-----------------+
                         |  Player 1 Wins! |
                         +-----------------+
```

## Technology Stack

*   **Language:** Python
*   **Libraries:**
    *   `pandas` for data manipulation and analysis.
    *   `scikit-learn` for machine learning.
    *   `pydot` for decision tree visualization.
    *   `mysql-connector-python` for database connectivity.

## Getting Started

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the required packages:**
    ```bash
    pip install pandas scikit-learn pydot mysql-connector-python
    ```

3.  **Set up the MySQL database:**
    *   Make sure you have a MySQL server running.
    *   Update the database credentials in `M3_Classification_Stage/AAAscikitlearn.py`:
        ```python
        config = {
            "host": "localhost",
            "user": "your_username",
            "password": "your_password",
            "database": "your_database"
        }
        ```

### Running the Project

*   **To play the game:**
    ```bash
    python M1_Game_Stage/V3_Comp_v_human.py
    ```

*   **To generate data:**
    ```bash
    python M2_Data_Stage/CSV_file/V5_Cleaner_Random.py
    ```

*   **To run the machine learning model:**
    ```bash
    python M3_Classification_Stage/AAAscikitlearn.py
    ```

## The Developer's Journey

This project wasn't built in a day. It was a journey of learning, experimenting, and overcoming challenges. The `Miscellaneous/Documentation.txt` file contains a detailed log of this journey, but here are some of the key takeaways:

*   **The Power of Iteration:** The project started small and grew in complexity over time. This iterative approach made it easier to manage and debug.
*   **The Importance of Clean Code:** Early versions of the code were messy, but as the project grew, the developer learned the value of clean, well-documented code.
*   **The "Aha!" Moment of Optimal Strategy:** The developer had a breakthrough when they realized the optimal strategy for the game was to always leave the opponent with a number of matchsticks that is a multiple of 4 (plus 1).
*   **From Theory to Practice:** This project is a great example of how to apply theoretical concepts from computer science and mathematics to a real-world problem.

## Contributing

This project is a personal learning journey, but contributions and suggestions are always welcome! Feel free to open an issue or submit a pull request.
