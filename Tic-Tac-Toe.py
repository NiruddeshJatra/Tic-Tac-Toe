import os
# Initialize Pygame mixer and hide support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import turtle
import pygame
import time



class TicTacToe:
    def __init__(self):
        pygame.mixer.init()
        self.setup_screen()
        self.play_welcome_message()
        self.number_of_players = self.get_number_of_players()
        self.number_of_squares = (self.number_of_players + 1) ** 2
        self.players = self.setup_players()
        self.draw_grid()
        self.squares = self.setup_squares()
        self.matches = self.setup_matches()
        self.count = 0
        self.game_over_flag = False  # Flag to track if the game is over


    def setup_screen(self):
        self.wn = turtle.Screen()
        self.wn.title("Tic-Tac-Toe Game by NJ Production")
        self.wn.setup(width=750, height=625)
        self.wn.bgcolor("#BCDD7A")


    def play_sound(self, sound_path):
        sound = pygame.mixer.Sound(sound_path)
        sound.play()


    def play_welcome_message(self):
        self.play_sound("sound/message_box.mp3")
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.color("#072A16")
        self.text.write("Welcome to Tic-Tac-Toe Game.\n\n2 to 4 players can play this game.\n\nFor 2 players, there will be a 3x3 grid.\n\nFor 3 players, there will be a 4x4 grid.\n\nFor 4 players, there will be a 5x5 grid.",
                        align="center", font=("cheri", 20, "bold"))
        time.sleep(5)
        self.wn.tracer(0)


    def get_number_of_players(self):
        valid_input = False
        while not valid_input:
            number_of_players = int(turtle.textinput("Tic-Tac-Toe", "Enter number of Players: "))
            if 2 <= number_of_players <= 4:
                valid_input = True
                self.text.clear()
                self.play_sound("sound/message_box.mp3")
            else:
                self.play_sound("sound/error.wav")
        return number_of_players


    def setup_players(self):
        return {
            1: {'marker': 'X', 'color': '#2A4A1A', 'squares': []},
            2: {'marker': 'O', 'color': '#7E412E', 'squares': []},
            3: {'marker': 'S', 'color': '#050B2B', 'squares': []},
            4: {'marker': 'V', 'color': '#2B112A', 'squares': []},
        }


    def draw_grid(self):
        self.play_sound("sound\message_box.mp3")
        grid = turtle.Turtle()
        grid.hideturtle()
        for i in range(self.number_of_players):
            grid.setheading(270)
            grid.penup()
            grid.goto(-150+i*100, 250)
            grid.pensize(5)
            grid.pendown()
            grid.forward(100*(self.number_of_players+1))

        for i in range(self.number_of_players):
            grid.setheading(0)
            grid.penup()
            grid.goto(-250, 150-i*100)
            grid.pensize(5)
            grid.pendown()
            grid.forward(100*(self.number_of_players+1))

        self.wn.update()


    def setup_squares(self):
        return [(-203, 145), (-103, 145), (-3, 145), (-203, 45), (-103, 45), (-3, 45), (-203, -55), (-103, -55), (-3, -55), (93, 145),  (93, 45), (93, -55), (-203, -155), (-103, -155), (-3, -155), (93, -155), (193, 145), (193, 45), (193, -55), (193, -155), (-203, -255), (-103, -255), (-3, -255), (93, -255), (193, -255)]


    def setup_matches(self):
        if self.number_of_players == 2:
            return ["abc", "def", "ghi", "adg", "beh", "cfi", "aei", "ceg"]
        elif self.number_of_players == 3:
            return ["abc", "def", "ghi", "adg", "beh", "cfi", "aei", "ceg", "bcj", "efk", "hil", "mno", "nop", "dgm", "ehn", "fio", "jkl", "klp", "eip", "bfl", "dho", "fjh", "fhm", "ikn"]
        else:
            return ["abc", "def", "ghi", "adg", "beh", "cfi", "aei", "ceg", "bcj", "efk", "hil", "mno", "nop", "dgm", "ehn", "fio", "jkl", "klp", "eip", "bfl", "dho", "fjh", "fhm", "ikn", "cjq", "fkr", "ils", "opt", "uvw", "vwx", "wxy", "gmu", "hnv", "iow", "lpx", "qrs", "rst", "sty", "ipy", "flt", "cks", "hox", "gnw", "ikq", "inu", "lor", "lov", "psw"]


    def draw_marker(self, x, y, marker, color):
        point = turtle.Turtle()
        point.speed(0)
        point.hideturtle()
        point.penup()
        point.goto(x, y)
        point.pencolor(color)
        point.write(marker, align="center", font=("Comic Sans MS", 65, "bold"))


    def click_handler(self, x, y, player):
        if self.game_over_flag:  # Check if the game is over before handling clicks
            return
        
        player_squares = self.players[player]['squares']
        other_players_squares = [sq for p, data in self.players.items() if p != player for sq in data['squares']]
        for i, square in enumerate(self.squares[:self.number_of_squares]):
            if self.is_within_square(x, y, square):
                square_label = chr(ord('a') + i)
                if square_label not in player_squares and square_label not in other_players_squares:
                    self.draw_marker(*square, self.players[player]['marker'], self.players[player]['color'])
                    player_squares.append(square_label)
                    self.count += 1
                    break


    def is_within_square(self, x, y, square):
        return square[0] - 50 < x < square[0] + 50 and square[1] < y < square[1] + 100


    def add_click_listeners(self, x, y):
        if self.game_over_flag:  # Check if the game is over before handling clicks
            return
        
        self.play_sound("sound\click.wav")
        
        if self.number_of_players == 2:
            if self.count % 2 == 0:
                self.click_handler(x, y, 1)
            else:
                self.click_handler(x, y, 2)
                
        elif self.number_of_players == 3:
            if self.count % 3 == 0:
                self.click_handler(x, y, 1)
            elif self.count % 3 == 1:
                self.click_handler(x, y, 2)
            else:
                self.click_handler(x, y, 3)
                
        else:
            if self.count % 4 == 0:
                self.click_handler(x, y, 1)
            elif self.count % 4 == 1:
                self.click_handler(x, y, 2)
            elif self.count % 4 == 2:
                self.click_handler(x, y, 3)
            else:
                self.click_handler(x, y, 4)
                
        self.check_winner()


    def game_over(self, winner):
        self.wn.update()
        time.sleep(1)
        self.wn.clear()
        self.wn.bgcolor("#5CB9BA")
        self.play_sound("sound\got_bonus.wav")
        
        message = turtle.Turtle()
        message.speed(0)
        message.hideturtle()
        message.penup()
        message.pencolor("#00011C")
        message.write("GAME OVER", align="center", font=("Jokerman", 40, "normal"))
        
        self.wn.update()
        time.sleep(3)
        message.clear()
        self.wn.clear()
        self.wn.bgcolor("#5CB9BA")
        self.play_sound("sound\end.mp3")
        
        if winner == 0:
            message.write(f"IT'S A DRAW!", align="center", font=("Jokerman", 30, "normal"))
        else:
            message.write(f"PLAYER {winner} WINS!", align="center", font=("Jokerman", 30, "normal"))
        self.wn.update()
        time.sleep(5)
        self.game_over_flag = True  # Set the flag to True to indicate the game is over
        turtle.bye()
    
    def check_winner(self):
        if self.game_over_flag:  # Check if the game is already over
            return
        
        for player in range(1, self.number_of_players + 1):
            for match in self.matches:
                if all(grid in self.players[player]['squares'] for grid in match):
                    self.game_over(player)
                    return
            
        if self.count == self.number_of_squares:
            self.game_over(0)
            return
    
    
    def run(self):
        turtle.onscreenclick(self.add_click_listeners)
        turtle.mainloop()
        
        
if __name__ == "__main__":
    game = TicTacToe()
    game.run()