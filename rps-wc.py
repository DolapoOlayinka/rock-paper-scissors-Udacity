# Create a parent class called Player which would contain the behavior of the subclasses HumanPlayer,
# CyclePlayer, reflectPlayer and RandomPlayer

# the humanPlayer subclass is asked for an input and plays against the computer players
#randomPlayer plays random moves against the humanPlayer
#cyclePlayer subclass is the computer player that remembers the humanPlayer last moves and cycles through different moves
# from the last move played

#reflectPlayer remembers the last move of humanPlayer and plays that move in the next round
# add functions to these subclasses to create game moves

# add functions to the Game class to print out questions and player scores to the terminal
#game should continue running until player types quit or a player is three rounds ahead of its opponent
#at the end of the game, announce the winner and print out the player scores.

import random

#stores game moves rock, paper, scissors
gameMoves = ['rock', 'paper', 'scissors']

#Player class is defined 
class Player:
    def __init__(self):
        self.score = 0
        
    def move(self):
        return 'rock'
    def learn(self, my_move):
        pass
        
    
#creates the humanPlayer subclass that selects game moves   
class humanPlayer(Player):
    def move(self):
        self.my_move = gameInput("rock, paper, scissors >\n", gameMoves)
        if self.my_move in gameMoves:
             return self.my_move
        elif self.my_move not in gameMoves:
            print("You've entered the wrong input, please try again") 
        else:
            endGame()
            
 # creates the randomPlayer subclass that plays random moves       
class randomPlayer(Player):
    def move(self):
        return random.choice(gameMoves)   

#reflectPlayer learns the previous move of the humanPlayer and plays it on the next round     
class reflectPlayer(Player):   
    def move(self):
        self.formerMove = random.choice(gameMoves)
        return self.formerMove
    
    def learn(self, my_move):
        self.formerMove = my_move
        
#cyclePlayer learns the previous move of the human player and cycles through the moves        
class cyclePlayer(Player): 
    def __init__(self):
        self.my_move = ' '
        self.score = 0
        
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(gameMoves)
        
#to compare game moves of players        
def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
        
# this class contains all the functions to make game work        
class Game:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    #plays game rounds and displays scores for each round played
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1)
        
        if move1 == move2:
            print(f"Player 1: {move1}, Player 2: {move2}")
            print(f"Player 1: {self.p1.score}, Player 2: {self.p2.score}")
            print("It's a tie in this round!\n")
             
        elif beats(move1, move2):
            print(f"Player 1: {move1}, Player 2: {move2}")
            self.p1.score += 1
            print(f"Player 1: {self.p1.score}, Player 2: {self.p2.score}")
            print("Player 1 Wins in this round!\n")
            
        elif beats(move2, move1):
            print(f"Player 1: {move1}, Player 2: {move2}")
            self.p2.score += 1
            print(f"Player 1: {self.p1.score}, Player 2: {self.p2.score}")
            print("Player 2 Wins in this round!\n")
            
        
        
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)

    #this contains all the functions to activate game mode
    def play_game(self):
        print("Welcome to the game of rock, paper, scissors")
        print("There are 5 rounds in this game")
        print("Choose an option of rock, paper, scissors\n")
        print("Game start!\n")
        for round in range(5):
            print(f"Round {round + 1}:")
            round += 1
            self.play_round()
        self.winner()
        print("Game over!\n")
        endGame()
    
    #terminal displays game scores and winner
    def winner(self):
        print("Final score:")
        print(f"Player 1: {self.p1.score}, Player 2 : {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("Player 1 wins!\n")
        elif self.p2.score > self.p1.score:
            print("Player 2 wins!\n")
        else:
            print("Game ended in a draw! Congratulations to both players\n")
        
#function to get response from player
def gameInput(question, playerMove):
    while True:
        choice = input(question).lower()
        if choice in playerMove:
            return choice
        
#to end game
def endGame():
    print("Thank you for playing rock, paper, scissors."
         "\nGoodbye")

#creates a match between humanPlayer and computer players
def game():
    comp = []
    comp.append(Player())
    comp.append(randomPlayer())
    comp.append(cyclePlayer())
    comp.append(reflectPlayer())
    
    while True:
        randomGame = random.randint(0, 3)
        game = Game(humanPlayer(), comp[randomGame])
        game.play_game()
        break
if __name__ == '__main__':
    game()