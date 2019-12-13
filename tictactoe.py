import tkinter
import random


class Game(object):
    """
    Enter the class docstring here
    """
    block_size = 100
    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent

        self.initialize_game()

    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts
        self.board = [None, None, None, None, None, None, None, None, None]  # game board as a instance variable
        self.map = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5, (2, 0): 6, (2, 1): 7,
                    (2, 2): 8}  # map to self.board
        self.top_frame = tkinter.Frame(self.parent)
        self.top_frame.pack(side=tkinter.TOP)

        # add restart button on top frame
        restart_button = tkinter.Button(self.top_frame, text='Restart', width=20,
                                        command=self.restart)
        restart_button.pack()  # register restart_button with geometry manager

        # create bottom frame for group the label below
        self.bottom_frame=tkinter.Frame(self.parent)
        self.bottom_frame.pack(side=tkinter.BOTTOM)

        # create label for displaying game result text
        self.my_lbl=tkinter.Label(self.bottom_frame,text=None)
        self.my_lbl.pack()

        # create a canvas to draw our board on the top frame
        self.canvas = tkinter.Canvas(self.top_frame,
                                     width=self.block_size * 3,
                                     height=self.block_size * 3)

        # draw 3x3 visible blocks on the canvas
        for ro in range(3):
            for col in range(3):

                self.canvas.create_rectangle(self.block_size * col,
                                             self.block_size * ro,
                                             self.block_size * (col + 1),
                                             self.block_size * (ro + 1),fill='white')

        # bind entire canvas with left click  handler (play function)
        self.canvas.bind("<Button-1>", self.play)
        self.canvas.pack()                  # register canvas with a geometry manager

    def board_full(self):
        if None not in self.board:
            return True            # true for full
        else:
            return False           # false for not full


    def possible_moves(self):
        """return: list of possible moves"""
        possible_moves = []                 # list for possible moves
        for i in range(0, 9):
            if self.board[i] is None:       # if cell un-taken
                possible_moves.append(i)    # append the cell number to list
            else:
                pass              # cell taken, don't append
        return possible_moves     # return list of possible moves

    def pc_move(self):
        m = True
        while m:
            pc_move = random.randint(0, 8)    # random generate a number from 0 to 8
            if pc_move in self.possible_moves():  # if the number is a possible move
                self.board[pc_move] = 'O'         # mark O
                self.canvas.itemconfigure(tagOrId=(pc_move+1),fill='blue')
                m = False                        # exit loop
            else:                                # not a possible movie
                continue                          # re-do
        return self

    def draw_out(self):
        """to be deleted"""
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])

    def play(self, event):  # This method is invoked when the user clicks on a square.
        """
        when the player clicks on a un-taken square, this method first translate cursor into cell number,
        then update game board and check game result based on condition
        :parameter: click
        :return: updated game object
        """
        # after the click: part 1     human play first
        print('clicked', event.y, event.x)  # to be deleted  show window coordinate
        cx = self.canvas.canvasx(event.x)   # window coordinate to canvas coordinate
        cy = self.canvas.canvasy(event.y)   # window coordinate to canvas coordinate
        cid = self.canvas.find_closest(cx,cy)[0] # find the closet colored widget by click point
        my_move = self.map[(cy // self.block_size, cx // self.block_size)]  # map cursor
        if self.board[my_move] is None:            # check if cell is empty
            self.board[my_move] = 'X'              # if cell empty mark X for my play
            self.canvas.itemconfigure(cid,fill='green') # fill green color for player
            #self.canvas.itemconfigure(tagOrId=(my_move+1),fill='green')
        else:              # if the cell taken, do nothing until click on empty square
            return None
                                      #  check game result and board full:
        self.draw_out()                          # DEBUGGING line
        if self.check_game()is not None:
            print(self.check_game())             # DEBUGGING line
        else:
            pass
        # part 2: while not filled, PC make one move right after my move:
        self.possible_moves()                     # check possible moves for PC
        self.pc_move()                            # pc make move
        self.draw_out()                           # DELETE LATER
        # part3: check game result and board full
        if self.check_game()is not None:
            print(self.check_game())             # DEBUGGING line
        else:
            pass
        return self  # when board is filled, return

    def check_game(self):
        """
        Check if the game is win or lost or a tie
        Return:  win, lose, tie, none """
        result=None
        if (self.board[0] == self.board[1] == self.board[2] == 'X') or (
                            self.board[3] == self.board[4] == self.board[5] == 'X') or (
                            self.board[6] == self.board[7] == self.board[8] == 'X') or (
                            self.board[0] == self.board[3] == self.board[6] == 'X') or (
                            self.board[1] == self.board[4] == self.board[7] == 'X') or (
                            self.board[2] == self.board[5] == self.board[8] == 'X') or (
                            self.board[0] == self.board[4] == self.board[8] == 'X') or (
                            self.board[2] == self.board[4] == self.board[6] == 'X'):
            result = 'You win!'  # player win
            self.my_lbl.configure(text=result)
        elif (self.board[0] == self.board[1] == self.board[2] == 'O') or (
                            self.board[3] == self.board[4] == self.board[5] == 'O') or (
                            self.board[6] == self.board[7] == self.board[8] == 'O') or (
                            self.board[0] == self.board[3] == self.board[6] == 'O') or (
                            self.board[1] == self.board[4] == self.board[7] == 'O') or (
                            self.board[2] == self.board[5] == self.board[8] == 'O') or (
                            self.board[0] == self.board[4] == self.board[8] == 'O') or (
                            self.board[2] == self.board[4] == self.board[6] == 'O'):
            result = 'You lost!'  # player lose
            self.my_lbl.config(text=result)
        elif self.board_full()is True:
                result = 'A tie!'  # tie
                self.my_lbl.configure(text=result)
        else:
            pass
        return result


    def restart(self):
        """ Reinitialize the game and board after restart button is pressed """
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        self.initialize_game()


def main():
    root = tkinter.Tk()  # Instantiate a root window
    my_game = Game(root)  # Instantiate a Game object
    root.mainloop()  # Enter the main event loop


if __name__ == '__main__':
    main()
