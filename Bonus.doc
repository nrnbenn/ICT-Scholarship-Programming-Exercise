import random

print("Simple guessing game!")

n = random.randint(1,20)

running = True
guesses = 0
while running:
    guesses += 1
    if guesses > 5:
        running = False
        print(f"You ran out of guesses! The answer was: {n}")
    else:
        guess = input("Please guess a number: ")
        if guess == n:
            print("Correct!")
            running = False
        elif guess > n:
            print("To high...")
        elif guess < n:
            print("To low...")


print("")

print("Advanced guessing game (unfinished!)")

class tile():
    def __init__(self,name,x,y):
        self.name = name
        self.overturned = False
        self.unlocked = True
        self.x = x
        self.y = y

    def overturn(self):
        self.overturned = False
        return(name)

    def unlock(self):
        self.unlocked = True


#initiate board
board = []
chars = ["a","b","c","d","e","f","g","h","i","j"]
for i in range(1,21):
    board.append(tile(chars[i/2-1],i%4,i-i%4))
    board.append(tile(chars[i/2-1],i%4,i-i%4))
board = random.shuffle(board)

foundpairs = 0
while not foundpairs >= 10:
    x1 = int(input("Please input the x of your first tile: "))
    y1 = int()
