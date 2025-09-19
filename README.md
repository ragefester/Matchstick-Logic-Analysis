# Matchstick Analysis Project

## Overview
This project analyses a mathematical game and it uses machine learning techniques. The game originates from a Leaving Certificate question and involves strategic number selection between two players.

## What the Game Does
The game follows these rules:
- Players start with numbers 1 through 15
- Each turn, a player must choose 1, 2, or 3 consecutive numbers
- The player who is forced to choose the number 15 loses
- Turns alternate between players

## Project Structure

### M1_Game_Stage
Contains the core game implementations:
- **V1**: Two human players can play the game
- **V2**: Two computer players compete using random moves
- **V3**: Human vs computer gameplay
- **V4**: Automated iteration of computer vs computer games

### M2_Data_Stage
Handles data collection and storage:
- **CSV_file**: Generates and stores game results and move sequences
- **MySQL_file**: Database operations and data analysis

### M3_Classification_Stage
Implements machine learning:
- Uses scikit-learn to train a Random Forest classifier
- Analyses game data to predict outcomes
- Generates decision tree visualisations

### Miscellaneous
Additional tools and analysis scripts for comparing different playing strategies.

## Technical Approach
The project follows a systematic progression:
1. **Game Development**: Building the core game mechanics
2. **Data Generation**: Running thousands of automated games to collect data
3. **Machine Learning**: Training AI models to understand winning strategies
4. **Analysis**: Visualising decision trees and analysing optimal play patterns

## Purpose
This project demonstrates how to:
- Convert a mathematical problem into a programmable game
- Generate large datasets through simulation
- Apply machine learning to game strategy analysis
- Visualise complex decision-making processes

The codebase serves as an educational example of combining game theory, data science, and artificial intelligence to solve problems.
