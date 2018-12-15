import tkinter as tk
from PIL import Image, ImageTk
import pygame

WHITECOLOUR = '#FFCC99'
BLACKCOLOUR = '#8F604F'
SQUARESIZE = 60


class KingButton(object):
    piececolour = None
    blackonblacksquare = None
    blackonwhitesquare = None
    whiteonblacksquare = None
    whiteonwhitesquare = None
    blackpiece = None
    whitepiece = None
    onwhatcolour = None
    startx = None
    starty = None
    isapiece = 1
    button = tk.Checkbutton
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_king_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_king_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_king_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_king_white.png")
            
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0)
            print("queen initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour):
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare

    def calcpossiblemoves(self):
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-1)
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-2)
        self.boardstate[self.startx][self.starty-1].button['command'] = self.swap
        self.boardstate[self.startx][self.starty-2].button['command'] = self.swap
        print("calculating...")
                
    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False

class QueenButton(object):
    piececolour = None
    onblacksquare = None
    onwhitesquare = None
    onwhatcolour = None
    startx = None
    starty = None
    isapiece = 1
    button = tk.Checkbutton
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_queen_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_queen_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_queen_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_queen_white.png")
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0)
            print("queen initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour):
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare

    def calcpossiblemoves(self):
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-1)
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-2)
        self.boardstate[self.startx][self.starty-1].button['command'] = self.swap
        self.boardstate[self.startx][self.starty-2].button['command'] = self.swap
        print("calculating...")

    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False


class BishopButton(object):
    onblacksquare = None
    onwhitesquare = None
    onwhatcolour = None
    startx = None
    starty = None
    isapiece = 1
    button = tk.Checkbutton
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_bishop_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_bishop_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_bishop_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_bishop_white.png")
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0)
            print("bishop initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour):
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare
    def calcpossiblemoves(self):
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-1)
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-2)
        self.boardstate[self.startx][self.starty-1].button['command'] = self.swap
        self.boardstate[self.startx][self.starty-2].button['command'] = self.swap
        print("calculating...")

    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False

class RookButton(object):
    hasmoved = 0
    piececolour = None
    onblacksquare = None
    onwhitesquare = None
    squarecolour = None
    startx = None
    starty = None
    isapiece = 1
    button = tk.Checkbutton
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_rook_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_rook_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_rook_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_rook_white.png")
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0, command = self.calcpossiblemoves)
            print("queen initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour, startx, starty):
        self.startx = startx
        self.starty = starty
        self.squarecolour = thesquarecolour
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare

    def calcpossiblemoves(self):
       
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        for x in range(8):

            self.boardstate[x][self.starty].button['command'] = lambda bound_x = x: self.swap(bound_x, self.starty)
            self.boardstate[self.startx][x].button['command'] = lambda bound_y = x: self.swap(self.startx, bound_y)

        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        print("calculating...")
        
    def swap(self, xcoor, ycoor):
        print(xcoor)
        print(ycoor)
        if not self.hasmoved:
            self.hasmoved = 1
        if not self.squarecolour == self.boardstate[xcoor][ycoor].squarecolour:
            self.changetexture()
            self.boardstate[xcoor][ycoor].changetexture()
        var = self.boardstate[xcoor][ycoor]
        self.boardstate[xcoor][ycoor] = self.boardstate[self.startx][self.starty]
        self.boardstate[self.startx][self.starty] = var
        self.boardstate[xcoor][ycoor].button.place(x = xcoor*SQUARESIZE, y = ycoor*SQUARESIZE)
        self.boardstate[self.startx][self.starty].button.place(x = self.startx*SQUARESIZE, y = self.starty*SQUARESIZE)
        self.startx = xcoor
        self.starty = ycoor
        self.ufkedupgoback()
        print("swap completed")
    def ufkedupgoback(self):
        print("fkedupgoback")
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = self.boardstate[c][r].calcpossiblemoves

    def changetexture(self):
        if self.piececolour == 1 and self.squarecolour == 1:
                self.button['image'] = self.blackonwhitesquare
                self.button['fg'] = WHITECOLOUR
                self.button['bg'] = WHITECOLOUR
                self.squarecolour = 0

        elif self.piececolour == 1 and self.squarecolour == 0:
                self.button['image'] = self.blackonblacksquare
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.squarecolour = 1
        elif self.piececolour == 0 and self.squarecolour == 1:
                self.button['image'] = self.whiteonwhitesquare
                self.button['fg'] = WHITECOLOUR
                self.button['bg'] = WHITECOLOUR
                self.squarecolour = 0
        else:
                self.button['image'] = self.whiteonblacksquare
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.squarecolour = 1

    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False


class KnightButton(object):
    piececolour = None
    onblacksquare = None
    onwhitesquare = None
    onwhatcolour = None
    startx = None
    starty = None
    isapiece = 1
    button = tk.Checkbutton
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_knight_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_knight_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_knight_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_knight_white.png")
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0)
            print("knight initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour):
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare
    def calcpossiblemoves(self):
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-1)
        self.possiblemoves.append(self.startx)
        self.possiblemoves.append(self.starty-2)
        self.boardstate[self.startx][self.starty-1].button['command'] = self.swap
        self.boardstate[self.startx][self.starty-2].button['command'] = self.swap
        print("calculating...")


    def swap(self, xcoor, ycoor):
        if not self.hasmoved:
            self.hasmoved = 1
        var = self.boardstate[xcoor][ycoor]
        self.boardstate[xcoor][ycoor] = self.boardstate[self.startx][self.starty]
        self.boardstate[self.startx][self.starty] = var
        self.boardstate[xcoor][ycoor].button.place(x = xcoor*SQUARESIZE, y = ycoor*SQUARESIZE)
        self.boardstate[self.startx][self.starty].button.place(x = self.startx*SQUARESIZE, y = self.starty*SQUARESIZE)
        self.startx = xcoor
        self.starty = ycoor
        self.boardstate[self.startx][self.starty].button['command'] = self.calcpossiblemoves
        self.ufkedupgoback()
        
        print("swap completed")

    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False


class PawnButton(object):
    squarecolour = None
    piececolour = None
    onblacksquare = None
    onwhitesquare = None
    onwhatcolour = None
    startx = None
    startyy = None
    isapiece = 1
    boardstate = [[0 for x in range(8)] for y in range(8)]
    button = tk.Checkbutton

    hasmoved = 0
        
    def __init__(self, how):
            self.blackonblacksquare = ImageTk.PhotoImage(file = "Black_pawn_black.png")
            self.blackonwhitesquare = ImageTk.PhotoImage(file = "Black_pawn_white.png")
            self.whiteonblacksquare = ImageTk.PhotoImage(file = "White_pawn_black.png")
            self.whiteonwhitesquare = ImageTk.PhotoImage(file = "White_pawn_white.png")
            self.onwhatcolour = 0
            self.button = tk.Checkbutton(how, offrelief = tk.FLAT, relief = tk.FLAT, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0, command = self.calcpossiblemoves)
            print("pawn initialized succesfully")
            

    def placethegodamnbutton(self, thesquarecolour, piececolour, startx, starty):
        self.startx = startx
        self.starty = starty
        self.squarecolour = thesquarecolour
        if thesquarecolour == 0:
            self.onwhatcolour = thesquarecolour
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.piececolour = piececolour
            if piececolour == 1:
                self.button['image'] = self.blackonwhitesquare
            else:
                self.button['image'] = self.whiteonwhitesquare
                
        else:
                self.onwhatcolour = thesquarecolour
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.piececolour = piececolour
                if piececolour == 1:
                    
                    self.button['image'] = self.blackonblacksquare
                else:
                    self.button['image'] = self.whiteonblacksquare
######FIXTHISSHIT*##################
    def calcpossiblemoves(self):
        print(self.piececolour)
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = 0
        self.boardstate[self.startx][self.starty].button['command'] = self.ufkedupgoback
        var1 = None
        
            
        if self.piececolour == 0:
            if self.hasmoved:
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty-1]):
                    self.boardstate[self.startx][self.starty-1].button['command'] = lambda: self.swap(self.startx, self.starty-1)
            else:
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty-1]):
                    self.boardstate[self.startx][self.starty-1].button['command'] = lambda: self.swap(self.startx, self.starty-1)
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty-2]):
                    self.boardstate[self.startx][self.starty-2].button['command'] = lambda: self.swap(self.startx, self.starty-2)
        else:
            if self.hasmoved:
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty+1]):
                    self.boardstate[self.startx][self.starty+1].button['command'] = lambda: self.swap(self.startx, self.starty+1)
            else:
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty+1]):
                    self.boardstate[self.startx][self.starty+1].button['command'] = lambda: self.swap(self.startx, self.starty+1)
                if not self.checkIsAPiece(self.boardstate[self.startx][self.starty+2]):
                    self.boardstate[self.startx][self.starty+2].button['command'] = lambda: self.swap(self.startx, self.starty+2)
        print("calculating...")

    def swap(self, xcoor, ycoor):
        if not self.hasmoved:
            self.hasmoved = 1
        if not self.squarecolour == self.boardstate[xcoor][ycoor].squarecolour:
            self.changetexture()
            self.boardstate[xcoor][ycoor].changetexture()
        var = self.boardstate[xcoor][ycoor]
        self.boardstate[xcoor][ycoor] = self.boardstate[self.startx][self.starty]
        self.boardstate[self.startx][self.starty] = var
        self.boardstate[xcoor][ycoor].button.place(x = xcoor*SQUARESIZE, y = ycoor*SQUARESIZE)
        self.boardstate[self.startx][self.starty].button.place(x = self.startx*SQUARESIZE, y = self.starty*SQUARESIZE)
        self.boardstate[xcoor][ycoor].startx = self.startx
        self.boardstate[xcoor][ycoor].starty = self.starty
        self.startx = xcoor
        self.starty = ycoor
        self.ufkedupgoback()
        print("swap completed")

    def changetexture(self):
        if self.piececolour == 1 and self.squarecolour == 1:
                self.button['image'] = self.blackonwhitesquare
                self.button['fg'] = WHITECOLOUR
                self.button['bg'] = WHITECOLOUR
                self.squarecolour = 0

        elif self.piececolour == 1 and self.squarecolour == 0:
                self.button['image'] = self.blackonblacksquare
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.squarecolour = 1
        elif self.piececolour == 0 and self.squarecolour == 1:
                self.button['image'] = self.whiteonwhitesquare
                self.button['fg'] = WHITECOLOUR
                self.button['bg'] = WHITECOLOUR
                self.squarecolour = 0
        else:
                self.button['image'] = self.whiteonblacksquare
                self.button['fg'] = BLACKCOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.squarecolour = 1

######FIXTHISSHIT*##################

    def ufkedupgoback(self):
        print("fkedupgoback")
        for c in range(8):
            for r in range(8):
                self.boardstate[c][r].button['command'] = self.boardstate[c][r].calcpossiblemoves

    def checkIsAPiece(self, somepiece):
        if (somepiece.isapiece == 1):
            return True
        else:
            return False


class EmptyButton(object):
    squarecolour = None
    blacksquare = None
    whitesquare = None
    startx = None
    startyy = None
    boardstate = [[0 for x in range(8)] for y in range(8)]
    button = tk.Checkbutton
    isapiece = 0
    
    def __init__(self, how):
        self.blacksquare = ImageTk.PhotoImage(file = "Black_square.png")
        self.whitesquare = ImageTk.PhotoImage(file = "White_square.png")
        self.button = tk.Checkbutton(how, offrelief = tk.SUNKEN, relief = tk.SUNKEN, bd = 0,
                                  indicatoron = 0, padx = 0, pady = 0, height = SQUARESIZE, width = SQUARESIZE,
                                  highlightthickness = 0)

    def placethegodamnbutton(self, squarecolour):
        self.squarecolour = squarecolour
        if squarecolour == 0:
            self.button['fg'] = WHITECOLOUR
            self.button['bg'] = WHITECOLOUR
            self.button['disabledforeground'] = WHITECOLOUR
            self.button['image'] = self.whitesquare
            
        else:
            self.button['fg'] = BLACKCOLOUR
            self.button['bg'] = BLACKCOLOUR
            self.button['disabledforeground'] = BLACKCOLOUR
            self.button['image'] = self.blacksquare

    def calcpossiblemoves(self):
        print("does nothing")

    def changetexture(self):
        if self.squarecolour == 1:
                self.button['image'] = self.whitesquare
                self.button['fg'] = WHITECOLOUR
                self.button['bg'] = BLACKCOLOUR
                self.squarecolour = 0
        else:
            self.button['image'] = self.blacksquare
            self.button['fg'] = BLACKCOLOUR
            self.button['bg'] = BLACKCOLOUR
            self.squarecolour = 1

    



###########################Where the main application starts
class Application(tk.Frame):
    isGameover = 1
    
    
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("500x500+10+10")
        self.pack()
        
        self.create_chessboard(master)
        
        self.game(master)
        
        
    
    def create_chessboard(self, theboard):
      
        print("this running?")
        var = 0
        count = 0
        self.blacksquare = ImageTk.PhotoImage(file = "Black_square.png")
        self.whitesquare = ImageTk.PhotoImage(file = "White_square.png")
        w,h = 8,8
        self.chessboard = [[0 for x in range(w)] for y in range(h)]
        ##MAKE AND PLACE CHESS PIECES HERE
        ###BLACK PIECES HERE############
        blackKing = KingButton(theboard)
        self.chessboard[4][0] = blackKing
        self.chessboard[4][0].placethegodamnbutton(0,1)
        self.chessboard[4][0].button.place(x = 4*SQUARESIZE, y = 0)
        ##################################
        blackQueen = QueenButton(theboard)
        self.chessboard[3][0] = blackQueen
        self.chessboard[3][0].placethegodamnbutton(1,1)
        self.chessboard[3][0].button.place(x=3*SQUARESIZE, y = 0)
        ##################################
        leftBishop = BishopButton(theboard)
        self.chessboard[2][0]= leftBishop
        self.chessboard[2][0].placethegodamnbutton(0,1)
        self.chessboard[2][0].button.place(x = 2*SQUARESIZE, y = 0)
        rightBishop= BishopButton(theboard)
        self.chessboard[5][0] = rightBishop
        self.chessboard[5][0].placethegodamnbutton(1,1)
        self.chessboard[5][0].button.place(x = 5*SQUARESIZE, y = 0)
        #################################
        leftKnight = KnightButton(theboard)
        self.chessboard[1][0] = leftKnight
        self.chessboard[1][0].placethegodamnbutton(1,1)
        self.chessboard[1][0].button.place(x=SQUARESIZE, y = 0)
        rightKnight = KnightButton(theboard)
        self.chessboard[6][0] = rightKnight
        self.chessboard[6][0].placethegodamnbutton(0,1)
        self.chessboard[6][0].button.place(x=6*SQUARESIZE, y = 0)
        #################################
        leftRook = RookButton(theboard)
        self.chessboard[0][0] = leftRook
        self.chessboard[0][0].placethegodamnbutton(0,1,0,0)
        self.chessboard[0][0].button.place(x=0, y = 0)
        rightRook = RookButton(theboard)
        self.chessboard[7][0] = rightRook
        self.chessboard[7][0].placethegodamnbutton(1,1,7,0)
        self.chessboard[7][0].button.place(x=7*SQUARESIZE, y = 0)
        ################################
        var = 1
        for pos in range(8):
            pawn = PawnButton(theboard)
            self.chessboard[pos][1] = pawn
            self.chessboard[pos][1].placethegodamnbutton(var,1,pos,1)
            self.chessboard[pos][1].button.place(x = pos*60, y = SQUARESIZE)
            if var == 1:
                var = 0
            else:
                var = 1
        ###WHITE PIECES HERE############
        blackKing = KingButton(theboard)
        self.chessboard[4][7] = blackKing
        self.chessboard[4][7].placethegodamnbutton(1,0)
        self.chessboard[4][7].button.place(x = 4*SQUARESIZE, y = 7*SQUARESIZE)
        ##################################
        blackQueen = QueenButton(theboard)
        self.chessboard[3][7] = blackQueen
        self.chessboard[3][7].placethegodamnbutton(0,0)
        self.chessboard[3][7].button.place(x=3*SQUARESIZE, y = 7*SQUARESIZE)
        ##################################
        leftBishop = BishopButton(theboard)
        self.chessboard[2][7]= leftBishop
        self.chessboard[2][7].placethegodamnbutton(1,0)
        self.chessboard[2][7].button.place(x = 2*SQUARESIZE, y = 7*SQUARESIZE)
        rightBishop= BishopButton(theboard)
        self.chessboard[5][7] = rightBishop
        self.chessboard[5][7].placethegodamnbutton(0,0)
        self.chessboard[5][7].button.place(x = 5*SQUARESIZE, y = 7*SQUARESIZE)
        #################################
        leftKnight = KnightButton(theboard)
        self.chessboard[1][7] = leftKnight
        self.chessboard[1][7].placethegodamnbutton(0,0)
        self.chessboard[1][7].button.place(x=SQUARESIZE, y = 7*SQUARESIZE)
        rightKnight = KnightButton(theboard)
        self.chessboard[6][7] = rightKnight
        self.chessboard[6][7].placethegodamnbutton(1,0)
        self.chessboard[6][7].button.place(x=6*SQUARESIZE, y = 7*SQUARESIZE)
        #################################
        leftRook = RookButton(theboard)
        self.chessboard[0][7] = leftRook
        self.chessboard[0][7].placethegodamnbutton(1,0,0,7)
        self.chessboard[0][7].button.place(x=0, y = 7*SQUARESIZE)
        rightRook = RookButton(theboard)
        self.chessboard[7][7] = rightRook
        self.chessboard[7][7].placethegodamnbutton(0,0,7,7)
        self.chessboard[7][7].button.place(x=7*SQUARESIZE, y = 7*SQUARESIZE)
        ################################
        var = 0
        for pos in range(8):
            pawn = PawnButton(theboard)
            self.chessboard[pos][6] = pawn
            self.chessboard[pos][6].placethegodamnbutton(var,0,pos,6)
            self.chessboard[pos][6].button.place(x = pos*60, y = SQUARESIZE*6)
            if var == 1:
                var = 0
            else:
                var = 1

        #####Initialize Empty Squares##
        var = 1
        for r in range(2,6):
            if var == 0:
                var = 1
            else:
                var = 0
            for c in range(8):
                empty = EmptyButton(theboard)
                self.chessboard[c][r] = empty
                self.chessboard[c][r].placethegodamnbutton(var)
                self.chessboard[c][r].button.place(x = c*SQUARESIZE, y = r*SQUARESIZE)
                if var == 0:
                    var = 1
                else:
                    var = 0
        print("all placed")

    def game(self, master):
        self.updateboardstate()
        
        

    
    def updateboardstate(self):
        for pawn in range(8):
             self.chessboard[pawn][6].boardstate = self.chessboard
             self.chessboard[pawn][1].boardstate = self.chessboard
        ##############ROOKS###############################     
        self.chessboard[0][0].boardstate = self.chessboard
        self.chessboard[7][0].boardstate = self.chessboard
        self.chessboard[0][7].boardstate = self.chessboard
        self.chessboard[7][7].boardstate = self.chessboard
        ##################################################
        print("updated pawn states")
    

         

def startthemusic():
    pygame.init()
    pygame.mixer.music.load("Last Surprise.mp3")
    pygame.mixer.music.play()


root = tk.Tk()


app = Application(master=root)
app.mainloop()
pygame.quit()
