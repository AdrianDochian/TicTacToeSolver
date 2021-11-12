## Table of Contents

- **[About the game](#about_the_game)**

- **[My Implementation](#my_implementation)**
  - **[Minimax with alpha beta pruning](#minimax)**

## About the game
<a name="about_the_game"></a>

Tic Tac Toe is a widely worldwide known game played in two. <br>
Each turn every player chose a spot to place their corresponding letter: One is `X` and one is `O`. <br>
Any player that succeeds in placing tree marks in a horizontal, vertical, or diagonal row wins. <br>
**<a name="observation_1">Observation 1:</a>** If players chose their best moves, the game ends with a draw.

<table>
  <tr>
    <th>X</th>
    <th>O</th>
    <th>O</th>
  </tr>
  <tr>
    <th><mark>X</mark></th>
    <th><mark>X</mark></th>
    <th><mark>X</mark></th>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th>O</th>
  </tr>
</table>

## My Implementation
<a name="my_implementation"></a>

   - The game is represented by a 3x3 matrix.
   - Every game the `coin` flips and either the player, either the program starts first.
   - Game interaction is done by pressing keys from `1` to `9`, similar to old mobile phones keyboards.
   - When game ends the play can choose to type `exit` for exiting the game or to press `any other key` to restart the game.

## Minimax with alpha beta pruning
<a name="minimax"></a>
   - Minimax algorithm would generate all the possible game next states starting from the current state of the game to 
all possible endings. It would then evaluate every state and chose one of the paths that takes him to victory. If victory
is not possible then it would choose to draw.
   - Alpha beta pruning optimization saves a lot of state space generation and evaluation. If a path to best possible outcome 
{victory, draw} is found then all the other possible paths remain unprocessed.
   - Due to the fact that the Tic Tac Toe game doesn't imply a big number of possible state space to be generated
and **[Observation 1](#observation_1)** the program cannot lose.
   