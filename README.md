# Chess Arbiter

Welcome to this **Chess Arbiter** repository!

1. [Introduction and Objective](#Introduction-and-Objective)
1. [Tools and Features](#Tools-and-Features)
1. [Next steps](#Next-steps)

<br>

## Introduction and Objective

<br>

The game of chess has received an unprecedented amount of attention recently, partly attributed to the series "The Queen's Gambit" and the increased presence of chess players having their own online channels. When playing chess on online platforms, such as Lichess, the software is built so that illegal moves are not allowed. However, when playing OTB (over the board), though the rules are the same, there's no such digital limitation to which moves players can make. If neither the players nor the arbiter realizes a mistake was made, the game may end up proceeding normally.

The goal of this project is to develop an AI capable of recognizing illegal moves in OTB chess. This may be specially used on small but ranked championships, where the number of arbiters may be limited and the level of players relatively lower.

The overaching objective guiding decision making is to develop a CV solution in order to apply CV principles and techniques being studied by the author.

<br>

## Tools and features

<br>

This project is developed in Python, using OpenCV for visual recognition and numpy.

At it's current stage, the code is able to detect the position of pieces from static images, recognize moves between images and check for move validity. In this early stage, the code only checks for basic piece movement, ignoring more complex rules such as en passant, castling and checks. Captures and conflicts with other pieces are also not yet implemented.

<br>

## Next Steps

<br>

The next steps will focus on implementing further CV features, rather than implementing all complex rules of chess.

* Develop image stream process, based on the computer screen.
* Object recognition via webcam of a physical board.

