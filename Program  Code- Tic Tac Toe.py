import tkinter as tk
from PIL import Image, ImageTk

#Image of the many cursor choices.(n.d.)http://geek.thekramms.com/Oreilly/perl3/tk/ch23_02.htm
#Tic Tac Toe Board Png - Steel Frame Semi Continuous Design[Online image].(n.d.). https://www.pngkey.com/detail/u2w7w7i1u2r5o0y3_tic-tac-toe-board-png-steel-frame-semi/
# the X and O shaped images are self made

class Start():
    def __init__(self, master, turns):
        '''
        board setup
        Args: 
            turns (int) :  # of turns 
            master (Tk) :  the window
            li ([int]) :  1 - 3 is top row, 4-6 middle row, 7- 9 botton row. box coords
            
            self.x_position = ([int]) : locations X is at
            self.o_position ([int]) : locations O is at
           
            
            xscore (int) : score for x
            oscore (int) : score for o

            x_img (Image) : image for x
            o_img (Image) : image for o

            board_img_load (Image) : board image

            ulC (canvas) : upper left canvas
            umC (canvas) : upper mid canvas
            urC (canvas) : upper right canvas
            mlC (canvas) : middle left canvas
            mmC (canvas) : middle middle canvas
            mrC (canvas) : middle right canvas
            blC (canvas) : lower left canvas
            bmC (canvas) : lower mid canvas
            brC (canvas) : lower right canvas

            x_score_label (Label) : score label for x
            o_score_label (Label) : score label for o

        return:
            None 

        '''


        self.turns = turns
        self.master = master
        self.li = [1,2,3,4,5,6,7,8,9] #left to right: 1 - 3 is top row, 4-6 middle row, 7- 9 botton row
        self.x_position = []
        self.o_position = []
        self.master.bind('<Enter>', self.change_cursor)
        self.xscore = 0
        self.oscore = 0

        self.board_img_load = Image.open('Python/tic_tac_toe_folder/Board.png')
        self.board_img_load = self.board_img_load.resize((200, 200), Image.ANTIALIAS)
        self.board_img_load = ImageTk.PhotoImage(master = game, image = self.board_img_load)
        
        self.x_img = Image.open('./tic_tac_toe_folder/X.png').resize((50, 50), Image.ANTIALIAS)# the X and O shaped images are self made
        self.x_img = ImageTk.PhotoImage(image = self.x_img)
        self.o_img = Image.open('./tic_tac_toe_folder/O.png').resize((50, 50), Image.ANTIALIAS)
        self.o_img = ImageTk.PhotoImage(image = self.o_img)

        self.background = tk.Canvas(self.master, width = 500, height = 500, bg = 'white')
        self.background.create_image(250, 150, image = self.board_img_load, tags = 'brd')
        self.background.image = self.board_img_load
        self.background.place(x = 0, y = 0)

        self.ulC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')# ea square is about 10 px apart give or take a few pixels
        self.umC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.urC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.mlC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.mmC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.mrC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.blC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')# ea square is about 10 px apart give or take a few pixels
        self.bmC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')
        self.brC = tk.Canvas(self.background, width = 50, height = 50, bg = 'white')

        
        self.ulC.place(x = 158 , y = 58)
        self.umC.place(x = 224 , y = 58)
        self.urC.place(x = 289 , y = 58)
        self.mlC.place(x = 158 , y = 124)
        self.mmC.place(x = 224 , y = 124)
        self.mrC.place(x = 289, y = 124)
        self.blC.place(x = 158 , y = 189)
        self.bmC.place(x = 224 , y = 189)
        self.brC.place(x = 289 , y = 189)
        self.bind_funct()



        self.x_score_label = tk.Label(self.background, text = f'X: {self.xscore}', bg = 'white', font = ('Ariel', 15))
        self.o_score_label = tk.Label(self.background, text = f'O: {self.oscore}', bg = 'white', font = ('Ariel', 15))
        self.x_score_label.place(x = 20, y = 140)        
        self.o_score_label.place(x = 20, y = 170)



    def bind_funct(self):
        self.ulC.bind('<ButtonRelease-1>', self.UL_click)
        self.umC.bind('<ButtonRelease-1>', self.UM_click)
        self.urC.bind('<ButtonRelease-1>', self.UR_click)
        
        self.mlC.bind('<ButtonRelease-1>', self.ML_click)
        self.mmC.bind('<ButtonRelease-1>', self.MM_click)
        self.mrC.bind('<ButtonRelease-1>', self.MR_click)
        
        self.blC.bind('<ButtonRelease-1>', self.BL_click)
        self.bmC.bind('<ButtonRelease-1>', self.BM_click)
        self.brC.bind('<ButtonRelease-1>', self.BR_click)

    def unbind_funct(self):
        self.ul_unbind = self.ulC.bind('<ButtonRelease-1>', self.UL_click)
        self.um_unbind = self.umC.bind('<ButtonRelease-1>', self.UM_click)
        self.ur_unbind = self.urC.bind('<ButtonRelease-1>', self.UR_click)

        self.ml_unbind = self.mlC.bind('<ButtonRelease-1>', self.ML_click)
        self.mm_unbind = self.mmC.bind('<ButtonRelease-1>', self.MM_click)
        self.mr_unbind = self.mrC.bind('<ButtonRelease-1>', self.MR_click)

        self.bl_unbind = self.blC.bind('<ButtonRelease-1>', self.BL_click)
        self.bm_unbind = self.bmC.bind('<ButtonRelease-1>', self.BM_click)
        self.br_unbind = self.brC.bind('<ButtonRelease-1>', self.BR_click)

        self.ulC.unbind('<ButtonRelease-1>', self.ul_unbind)
        self.umC.unbind('<ButtonRelease-1>', self.um_unbind)
        self.urC.unbind('<ButtonRelease-1>', self.ur_unbind)

        self.mlC.unbind('<ButtonRelease-1>', self.ml_unbind)
        self.mmC.unbind('<ButtonRelease-1>', self.mm_unbind)
        self.mrC.unbind('<ButtonRelease-1>', self.mr_unbind)

        self.blC.unbind('<ButtonRelease-1>', self.bl_unbind)
        self.bmC.unbind('<ButtonRelease-1>', self.bm_unbind)
        self.brC.unbind('<ButtonRelease-1>', self.br_unbind)

        

    def change_cursor(self, event):

        '''
        Change the cursor in the window to know whose turn currently. 
        '''
        if self.turns % 2 == 0:
            self.master['cursor'] = 'x_cursor'
        else:
            self.master['cursor'] = 'circle'

    def UL_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.ulC.delete('all')
        if self.turns%2 == 0:
            self.ulC.create_image(26,27, image = self.x_img)
            self.ulC.image = self.x_img
            self.x_position.append(1)
        else:
            self.ulC.create_image(27,27, image = self.o_img)
            self.ulC.image = self.o_img
            self.o_position.append(1)
        self.turns += 1
        self.ulC.unbind('<ButtonRelease-1>')
        self.li.remove(1)
        self.win_condition()

    
    def UM_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.umC.delete('all')
        if self.turns%2 == 0:
            self.umC.create_image(26,27, image = self.x_img)
            self.umC.image = self.x_img
            self.x_position.append(2)
        else:
            self.umC.create_image(27,27, image = self.o_img)
            self.umC.image = self.o_img
            self.o_position.append(2)
        self.turns += 1
        self.umC.unbind('<ButtonRelease-1>')
        self.li.remove(2)
        self.win_condition()

    
    def UR_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.urC.delete('all')
        if self.turns%2 == 0:
            self.urC.create_image(26,27, image = self.x_img)
            self.urC.image = self.x_img
            self.x_position.append(3)
        else:
            self.urC.create_image(27,27, image = self.o_img)
            self.urC.image = self.o_img
            self.o_position.append(3)
        self.turns += 1
        self.urC.unbind('<ButtonRelease-1>')
        self.li.remove(3)
        self.win_condition()

    def ML_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
                
        self.mlC.delete('all')
        if self.turns % 2 == 0:
            self.mlC.create_image(27, 27, image = self.x_img)
            self.mlC.image = self.x_img
            self.x_position.append(4)
        else:
            self.mlC.create_image(27,27, image = self.o_img)
            self.mlC.image = self.o_img
            self.o_position.append(4)
        self.turns += 1
        self.mlC.unbind('<ButtonRelease-1>')
        self.li.remove(4)
        self.win_condition()
    
    def MM_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.mmC.delete('all')
        if self.turns%2 == 0:
            self.mmC.create_image(27,27, image = self.x_img)
            self.mmC.image = self.x_img
            self.x_position.append(5)
        else:
            self.mmC.create_image(27,27, image = self.o_img)
            self.mmC.image = self.o_img
            self.o_position.append(5)
        self.turns += 1
        self.mmC.unbind('<ButtonRelease-1>')
        self.li.remove(5)
        self.win_condition()
        
    def MR_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.mrC.delete('all')
        if self.turns%2 == 0:
            self.mrC.create_image(27, 27, image = self.x_img)
            self.mrC.image = self.x_img
            self.x_position.append(6)
        else:
            self.mrC.create_image(27,27, image = self.o_img)
            self.mrC.image = self.o_img
            self.o_position.append(6)
        self.turns += 1
        self.mrC.unbind('<ButtonRelease-1>')
        self.li.remove(6)
        self.win_condition()
        
    def BL_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.blC.delete('all')
        if self.turns%2 == 0:
            self.blC.create_image(27,27, image = self.x_img)
            self.blC.image = self.x_img
            self.x_position.append(7)
        else:
            self.blC.create_image(27,27, image = self.o_img)
            self.blC.image = self.o_img
            self.o_position.append(7)
        self.turns += 1
        self.blC.unbind('<ButtonRelease-1>')
        self.li.remove(7)
        self.win_condition()
        
    def BM_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.bmC.delete('all')
        if self.turns%2 == 0:
            self.bmC.create_image(27,27, image = self.x_img)
            self.bmC.image = self.x_img
            self.x_position.append(8)
        else:
            self.bmC.create_image(27,27, image = self.o_img)
            self.bmC.image = self.o_img
            self.o_position.append(8)
        self.turns += 1
        self.bmC.unbind('<ButtonRelease-1>')
        self.li.remove(8)
        self.win_condition()
        
    def BR_click(self, event):
        '''
        Updates the  canvas to the symbol and unbind the canvas 
        '''
        self.brC.delete('all')
        if self.turns%2 == 0:
            self.brC.create_image(27,27, image = self.x_img)
            self.brC.image = self.x_img
            self.x_position.append(9)
        else:
            self.brC.create_image(27,27, image = self.o_img)
            self.brC.image = self.o_img
            self.o_position.append(9)
        self.turns += 1
        self.brC.unbind('<ButtonRelease-1>')
        self.li.remove(9)
        self.win_condition()

    def results(self, i):
        self.win_label = tk.Label(self.master, font = ('Arial', 18))
        self.win_label.place(x = 20, y = 110)
        if i == 'X':
            self.xscore += 1
            self.win_label['text'] = f'{i} wins'
        elif i == 'O':
            self.oscore += 1
            self.win_label['text'] = f'{i} wins'
        else:
            self.win_label['text'] = f'{i}'
        self.x_score_label.configure(text = f'X: {self.xscore}')
        self.o_score_label.configure(text = f'O: {self.oscore}')

        
    def Reset_Group(self):
        '''
        reset game
        '''
        
        self.win_label.destroy()
        self.x_position = []    
        self.o_position = []
        self.turns = 0
        self.li = [1,2,3,4,5,6,7,8,9]   
        self.reset_button.destroy()
        
        self.bind_funct()
        self.ulC.delete('all')
        self.umC.delete('all')
        self.urC.delete('all')

        self.mlC.delete('all')
        self.mmC.delete('all')
        self.mrC.delete('all')

        self.blC.delete('all')
        self.bmC.delete('all')
        self.brC.delete('all')


    def end_(self):
        '''
        end game 
        '''
        self.unbind_funct()
        self.reset_button = tk.Button(self.background, text = 'R E S E T', command = self.Reset_Group, relief = 'flat', cursor = 'arrow')
        self.reset_button.place( x = 20, y = 80 )

        
    def win_condition(self):
        if 1 in self.x_position and 2 in self.x_position and 3 in self.x_position:
            self.results('X')
            self.end_()
            return
        if 4 in self.x_position and 5 in self.x_position and 6 in self.x_position:
            self.results('X')
            self.end_()
            return
            
        if 7 in self.x_position and 8 in self.x_position and 9 in self.x_position:
            self.results('X')
            self.end_()
            return
            
        if 1 in self.x_position and 4 in self.x_position and 7 in self.x_position:
            self.results('X')
            self.end_()
            return
            
        if 2 in self.x_position and 5 in self.x_position and 8 in self.x_position:
            self.results('X')
            self.end_()
            return
            
        if 3 in self.x_position and 6 in self.x_position and 9 in self.x_position:          
            self.results('X')
            self.end_()
            return
            
        if 1 in self.x_position and 5 in self.x_position and 9 in self.x_position:   
            self.results('X')
            self.end_()
            return
            
        if 3 in self.x_position and 5 in self.x_position and 7 in self.x_position:
            self.results('X')
            self.end_()
            return
        
            
        
        if 1 in self.o_position and 2 in self.o_position and 3 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 4 in self.o_position and 5 in self.o_position and 6 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 7 in self.o_position and 8 in self.o_position and 9 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 1 in self.o_position and 4 in self.o_position and 7 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 2 in self.o_position and 5 in self.o_position and 8 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 3 in self.o_position and 6 in self.o_position and 9 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 1 in self.o_position and 5 in self.o_position and 9 in self.o_position:
            self.results('O')
            self.end_()
            return
        if 3 in self.o_position and 5 in self.o_position and 7 in self.o_position:
            self.results('O')
            self.end_()
            return
                 
        if self.li == []:
            self.results('TIE')
            self.end_()
            return
        
        


if __name__ == '__main__':
    game = tk.Tk()
    game.title('Tic Tac Toe')
    game.resizable(False, False)
    Start(game, 0)
    substitute = Start(game, 0)
    substitute.bind_funct()
    game.geometry('500x300')
    game.mainloop()


