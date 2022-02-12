# Tic-Tac-Toe

Tic-tac-toe game on terminal. To play the game, run:

~~~
python main.py
~~~

## Software implementation

The game is implemented using MVC (Model View Controller) design pattern.
The controller is implemented using the Command pattern. This allows for easy implementation of undo and redo commands.
The relation View-Model follows the Observer pattern. This allows separation of concerns between the code that handles the View and the code that handles the Model. This separation reduces coupling (spaghetti code).

## AI implementation

The AI evaluates its moves using a max-min algorithm. Then, it randomly chooses one of the best moves (if there are two moves that lead to a forced victory, it plays one of them randomly. If there is no move that allows forced victory, it randomly picks a move that won't let the other player win). The implementation logic is captured in the following pseudo-code:

~~~
MaxMinPositionEvaluation (table, player):
    check for winning condition on table
    if player won then
        return 100
    else if otherPlayer won then
        return -100
    else if players drew then
        return 0
       
    answer = -INF   
       
    for every possible move:
        play the move on the table
        answer = max(answer, -MaxMinEvaluation(table, otherPlayer))
        undo the move on the table
        
    return answer
    
    
AI (table) :
    positionEval = MaxMinPositionEvaluation(table, AI)
    bestMoves = []
    for every possible move:
        play the move on the table
        if new position evaluation equal to positionEval:
            bestMoves.append(move)
        undo the move on the table
    randomly chooses one of bestMoves and return
~~~

### AI performance
To avoid re-computation, the AI also saves its evaluations in a hash-table. In practice, this makes the AI only compute the first move of the match (at most, as previous matches also save the pre-computed positions), as it transverses the entire "tree" (directed graph, to be more precise) of possible moves during the first move calculation.

Let n be the number of possible distinct game positions, the AI will do at most O(n) calculations to decide the first move. For a standard 3x3 tic-tac-toe game, considering either crosses or circles play first, an initial approximation of this value is n <= 2*3^9 = 39.366 (it is a upperbound because not all positions are possible to reach). After that, all moves are O(1).
