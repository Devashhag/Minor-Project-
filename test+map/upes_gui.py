#code by devashish agarwal
###
import pygame
from tkinter import *
import sys
import os
from tkinter import messagebox
import math
##

screen = pygame.display.set_mode((700, 700))

dimensions = 700
rows = cols = 70
width = dimensions/rows
height = dimensions/cols
openlist = []
closedlist = []
grid = [0 for i in range(cols)]


#####
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (255,255,255)
white = (255, 255, 255)
turq = (64, 224, 208)
yellow = (255, 195, 0)
lightgr = (12, 244, 174)
lightyellow = (230, 244, 12)
#####


class cubes:
    def __init__(self, x, y):
        self.previous = None
        self.barrier = False
        self.closed = False
        self.i = x
        self.j = y
        self.f = self.g = self.h = 0
        self.neighbors = []

        self.value = 1

    def start(self, color, bordercolor):
        if self.closed == False:
            pygame.draw.rect(screen, color, (self.i * width,
                             self.j * height, width, height), bordercolor)
            pygame.display.update()

    def path(self, color, bordercolor):
        pygame.draw.rect(screen, color, (self.i * width,
                         self.j * height, width, height), bordercolor)
        pygame.display.update()

    def update_neighbour(self, grid):
        i = self.i
        j = self.j
        if i < cols-1 and grid[self.i + 1][j].barrier == False:  # down up right left
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].barrier == False:
            self.neighbors.append(grid[self.i - 1][j])
        if j < rows-1 and grid[self.i][j + 1].barrier == False:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and grid[self.i][j - 1].barrier == False:
            self.neighbors.append(grid[self.i][j - 1])


# create 2d array
for i in range(cols):
    grid[i] = [0 for i in range(rows)]

# Create cubes
for i in range(rows):
    for j in range(cols):
        grid[i][j] = cubes(i, j)


# Set start and end node
start = grid[8][57]
end = grid[46][38]
# Show the boxes(cubes)
for i in range(cols):
    for j in range(rows):
        grid[i][j].start(white, 1)


for i in range(0, rows):
    grid[0][12].start(grey, 0)
    grid[0][12].barrier = True
    grid[0][12].start(grey, 0)
    grid[0][12].barrier = True
    grid[0][11].start(grey, 0)
    grid[0][11].barrier = True
    grid[1][10].start(grey, 0)
    grid[1][10].barrier = True
    grid[1][9].start(grey, 0)
    grid[1][9].barrier = True
    grid[2][9].start(grey, 0)
    grid[2][9].barrier = True
    grid[2][8].start(grey, 0)
    grid[2][8].barrier = True
    grid[3][8].start(grey, 0)
    grid[3][8].barrier = True
    grid[3][7].start(grey, 0)
    grid[3][7].barrier = True
    grid[4][7].start(grey, 0)
    grid[4][7].barrier = True
    grid[4][6].start(grey, 0)
    grid[4][6].barrier = True
    grid[4][5].start(grey, 0)
    grid[4][5].barrier = True
    grid[5][5].start(grey, 0)
    grid[5][5].barrier = True
    grid[5][4].start(grey, 0)
    grid[5][4].barrier = True
    grid[6][4].start(grey, 0)
    grid[6][4].barrier = True
    grid[6][3].start(grey, 0)
    grid[6][3].barrier = True
    grid[6][2].start(grey, 0)
    grid[6][2].barrier = True
    grid[7][2].start(grey, 0)
    grid[7][2].barrier = True
    grid[7][2].start(grey, 0)
    grid[7][2].barrier = True
    grid[7][1].start(grey, 0)
    grid[7][1].barrier = True
    grid[8][0].start(grey, 0)
    grid[8][0].barrier = True


    grid[3][19].start(grey, 0)
    grid[3][19].barrier = True
    grid[3][14].start(grey, 0)
    grid[3][14].barrier = True
    grid[5][14].start(grey, 0)
    grid[5][14].barrier = True
    grid[5][17].start(grey, 0)
    grid[5][17].barrier = True
    grid[8][17].start(grey, 0)
    grid[8][17].barrier = True
    grid[8][19].start(grey, 0)
    grid[8][19].barrier = True
    grid[3][19].start(grey, 0)
    grid[3][19].barrier = True
    grid[3][19].start(grey, 0)
    grid[3][19].barrier = True
    grid[4][19].start(grey, 0)
    grid[4][19].barrier = True
    grid[5][19].start(grey, 0)
    grid[5][19].barrier = True
    grid[6][19].start(grey, 0)
    grid[6][19].barrier = True
    grid[7][19].start(grey, 0)
    grid[7][19].barrier = True
    grid[8][19].start(grey, 0)
    grid[8][19].barrier = True
    grid[8][18].start(grey, 0)
    grid[8][18].barrier = True
    grid[8][17].start(grey, 0)
    grid[8][17].barrier = True
    grid[7][17].start(grey, 0)
    grid[7][17].barrier = True
    grid[7][17].start(grey, 0)
    grid[7][17].barrier = True
    grid[6][17].start(grey, 0)
    grid[6][17].barrier = True
    grid[5][17].start(grey, 0)
    grid[5][17].barrier = True
    grid[5][16].start(grey, 0)
    grid[5][16].barrier = True
    grid[5][15].start(grey, 0)
    grid[5][15].barrier = True
    grid[5][14].start(grey, 0)
    grid[5][14].barrier = True
    grid[3][14].start(grey, 0)
    grid[3][14].barrier = True
    grid[3][14].start(grey, 0)
    grid[3][14].barrier = True
    grid[3][15].start(grey, 0)
    grid[3][15].barrier = True
    grid[3][16].start(grey, 0)
    grid[3][16].barrier = True
    grid[3][16].start(grey, 0)
    grid[3][16].barrier = True
    grid[3][17].start(grey, 0)
    grid[3][17].barrier = True
    grid[3][18].start(grey, 0)
    grid[3][18].barrier = True
    grid[3][19].start(grey, 0)
    grid[3][19].barrier = True


    grid[1][21].start(grey, 0)
    grid[1][21].barrier = True
    grid[1][20].start(grey, 0)
    grid[1][20].barrier = True


    grid[0][23].start(grey, 0)
    grid[0][23].barrier = True
    grid[0][24].start(grey, 0)
    grid[0][24].barrier = True
    grid[0][25].start(grey, 0)
    grid[0][25].barrier = True

    grid[2][26].start(grey, 0)
    grid[2][26].barrier = True
    grid[2][27].start(grey, 0)
    grid[2][27].barrier = True
    grid[2][28].start(grey, 0)
    grid[2][28].barrier = True
    grid[2][29].start(grey, 0)
    grid[2][29].barrier = True
    grid[1][29].start(grey, 0)
    grid[1][29].barrier = True


    grid[0][65].start(grey, 0)
    grid[0][65].barrier = True
    grid[0][65].start(grey, 0)
    grid[0][65].barrier = True
    grid[0][65].start(grey, 0)
    grid[0][65].barrier = True
    grid[1][65].start(grey, 0)
    grid[1][65].barrier = True
    grid[1][64].start(grey, 0)
    grid[1][64].barrier = True
    grid[2][64].start(grey, 0)
    grid[2][64].barrier = True
    grid[2][63].start(grey, 0)
    grid[2][63].barrier = True
    grid[3][62].start(grey, 0)
    grid[3][62].barrier = True
    grid[3][61].start(grey, 0)
    grid[3][61].barrier = True
    grid[3][60].start(grey, 0)
    grid[3][60].barrier = True
    grid[3][59].start(grey, 0)
    grid[3][59].barrier = True
    grid[3][58].start(grey, 0)
    grid[3][58].barrier = True
    grid[3][57].start(grey, 0)
    grid[3][57].barrier = True
    grid[3][56].start(grey, 0)
    grid[3][56].barrier = True
    grid[3][55].start(grey, 0)
    grid[3][55].barrier = True
    grid[3][55].start(grey, 0)
    grid[3][55].barrier = True
    grid[3][54].start(grey, 0)
    grid[3][54].barrier = True
    grid[3][53].start(grey, 0)
    grid[3][53].barrier = True
    grid[3][52].start(grey, 0)
    grid[3][52].barrier = True
    grid[3][51].start(grey, 0)
    grid[3][51].barrier = True
    grid[3][50].start(grey, 0)
    grid[3][50].barrier = True
    grid[3][49].start(grey, 0)
    grid[3][49].barrier = True
    grid[3][48].start(grey, 0)
    grid[3][48].barrier = True
    grid[3][47].start(grey, 0)
    grid[3][47].barrier = True
    grid[3][46].start(grey, 0)
    grid[3][46].barrier = True
    grid[3][45].start(grey, 0)
    grid[3][45].barrier = True
    grid[3][44].start(grey, 0)
    grid[3][44].barrier = True
    grid[3][43].start(grey, 0)
    grid[3][43].barrier = True
    grid[4][43].start(grey, 0)
    grid[4][43].barrier = True
    grid[4][43].start(grey, 0)
    grid[4][43].barrier = True
    grid[4][42].start(grey, 0)
    grid[4][42].barrier = True
    grid[4][41].start(grey, 0)
    grid[4][41].barrier = True
    grid[4][39].start(grey, 0)
    grid[4][39].barrier = True
    grid[4][39].start(grey, 0)
    grid[4][39].barrier = True
    grid[4][38].start(grey, 0)
    grid[4][38].barrier = True
    grid[4][37].start(grey, 0)
    grid[4][37].barrier = True
    grid[4][36].start(grey, 0)
    grid[4][36].barrier = True
    grid[4][35].start(grey, 0)
    grid[4][35].barrier = True
    grid[4][34].start(grey, 0)
    grid[4][34].barrier = True
    grid[4][33].start(grey, 0)
    grid[4][33].barrier = True
    grid[4][32].start(grey, 0)
    grid[4][32].barrier = True
    grid[4][31].start(grey, 0)
    grid[4][31].barrier = True
    grid[4][30].start(grey, 0)
    grid[4][30].barrier = True
    grid[4][29].start(grey, 0)
    grid[4][29].barrier = True
    grid[4][28].start(grey, 0)
    grid[4][28].barrier = True
    grid[4][27].start(grey, 0)
    grid[4][27].barrier = True


    grid[4][27].start(grey, 0)
    grid[4][27].barrier = True
    grid[5][27].start(grey, 0)
    grid[5][27].barrier = True
    grid[6][27].start(grey, 0)
    grid[6][27].barrier = True
    grid[6][27].start(grey, 0)
    grid[6][27].barrier = True
    grid[7][27].start(grey, 0)
    grid[7][27].barrier = True
    grid[8][27].start(grey, 0)
    grid[8][27].barrier = True
    grid[9][27].start(grey, 0)
    grid[9][27].barrier = True
    grid[10][27].start(grey, 0)
    grid[10][27].barrier = True
    grid[11][27].start(grey, 0)
    grid[11][27].barrier = True
    grid[12][27].start(grey, 0)
    grid[12][27].barrier = True
    grid[13][27].start(grey, 0)
    grid[13][27].barrier = True
    grid[14][27].start(grey, 0)
    grid[14][27].barrier = True
    grid[15][27].start(grey, 0)
    grid[15][27].barrier = True
    grid[16][27].start(grey, 0)
    grid[16][27].barrier = True
    grid[17][27].start(grey, 0)
    grid[17][27].barrier = True
    grid[18][27].start(grey, 0)
    grid[18][27].barrier = True
    grid[19][27].start(grey, 0)
    grid[19][27].barrier = True
    grid[20][27].start(grey, 0)
    grid[20][27].barrier = True
    grid[21][27].start(grey, 0)
    grid[21][27].barrier = True
    grid[22][27].start(grey, 0)
    grid[22][27].barrier = True
    grid[23][27].start(grey, 0)
    grid[23][27].barrier = True
    grid[24][27].start(grey, 0)
    grid[24][27].barrier = True
    grid[25][27].start(grey, 0)
    grid[25][27].barrier = True
    grid[26][27].start(grey, 0)
    grid[26][27].barrier = True
    grid[27][27].start(grey, 0)
    grid[27][27].barrier = True
    grid[27][26].start(grey, 0)
    grid[27][26].barrier = True
    grid[27][26].start(grey, 0)
    grid[27][26].barrier = True
    grid[27][26].start(grey, 0)
    grid[27][26].barrier = True
    grid[28][27].start(grey, 0)
    grid[28][27].barrier = True
    grid[29][27].start(grey, 0)
    grid[29][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True

    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][26].start(grey, 0)
    grid[30][26].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][26].start(grey, 0)
    grid[30][26].barrier = True
    grid[30][25].start(grey, 0)
    grid[30][25].barrier = True
    grid[30][24].start(grey, 0)
    grid[30][24].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][27].start(grey, 0)
    grid[30][27].barrier = True
    grid[30][26].start(grey, 0)
    grid[30][26].barrier = True
    grid[30][25].start(grey, 0)
    grid[30][25].barrier = True
    grid[30][24].start(grey, 0)
    grid[30][24].barrier = True
    grid[30][23].start(grey, 0)
    grid[30][23].barrier = True
    grid[30][22].start(grey, 0)
    grid[30][22].barrier = True
    grid[30][21].start(grey, 0)
    grid[30][21].barrier = True


    grid[30][21].start(grey, 0)
    grid[30][21].barrier = True
    grid[29][21].start(grey, 0)
    grid[29][21].barrier = True
    grid[29][20].start(grey, 0)
    grid[29][20].barrier = True
    grid[28][20].start(grey, 0)
    grid[28][20].barrier = True
    grid[27][20].start(grey, 0)
    grid[27][20].barrier = True
    grid[26][20].start(grey, 0)
    grid[26][20].barrier = True
    grid[25][20].start(grey, 0)
    grid[25][20].barrier = True
    grid[24][20].start(grey, 0)
    grid[24][20].barrier = True
    grid[23][20].start(grey, 0)
    grid[23][20].barrier = True
    grid[22][20].start(grey, 0)
    grid[22][20].barrier = True
    grid[21][20].start(grey, 0)
    grid[21][20].barrier = True
    grid[20][20].start(grey, 0)
    grid[20][20].barrier = True
    grid[19][20].start(grey, 0)
    grid[19][20].barrier = True
    grid[18][20].start(grey, 0)
    grid[18][20].barrier = True
    grid[17][20].start(grey, 0)
    grid[17][20].barrier = True
    grid[16][20].start(grey, 0)
    grid[16][20].barrier = True
    grid[15][20].start(grey, 0)
    grid[15][20].barrier = True
    grid[14][20].start(grey, 0)
    grid[14][20].barrier = True
    grid[13][20].start(grey, 0)
    grid[13][20].barrier = True
    grid[12][20].start(grey, 0)
    grid[12][20].barrier = True

    grid[12][18].start(grey, 0)
    grid[12][18].barrier = True
    grid[13][18].start(grey, 0)
    grid[13][18].barrier = True
    grid[14][18].start(grey, 0)
    grid[14][18].barrier = True
    grid[15][18].start(grey, 0)
    grid[15][18].barrier = True
    grid[17][18].start(grey, 0)
    grid[17][18].barrier = True
    grid[18][18].start(grey, 0)
    grid[18][18].barrier = True
    grid[19][18].start(grey, 0)
    grid[19][18].barrier = True
    grid[20][18].start(grey, 0)
    grid[20][18].barrier = True
    grid[21][18].start(grey, 0)
    grid[21][18].barrier = True
    grid[22][18].start(grey, 0)
    grid[22][18].barrier = True
    grid[23][18].start(grey, 0)
    grid[23][18].barrier = True
    grid[24][18].start(grey, 0)
    grid[24][18].barrier = True
    grid[25][18].start(grey, 0)
    grid[25][18].barrier = True
    grid[26][18].start(grey, 0)
    grid[26][18].barrier = True
    grid[27][18].start(grey, 0)
    grid[27][18].barrier = True
    grid[28][18].start(grey, 0)
    grid[28][18].barrier = True
    grid[29][18].start(grey, 0)
    grid[29][18].barrier = True


    grid[29][18].start(grey, 0)
    grid[29][18].barrier = True
    grid[29][18].start(grey, 0)
    grid[29][18].barrier = True
    grid[29][17].start(grey, 0)
    grid[29][17].barrier = True
    grid[29][16].start(grey, 0)
    grid[29][16].barrier = True
    grid[29][15].start(grey, 0)
    grid[29][15].barrier = True
    grid[30][14].start(grey, 0)
    grid[30][14].barrier = True
    grid[31][13].start(grey, 0)
    grid[31][13].barrier = True
    grid[31][12].start(grey, 0)
    grid[31][12].barrier = True
    grid[31][11].start(grey, 0)
    grid[31][11].barrier = True
    grid[30][11].start(grey, 0)
    grid[30][11].barrier = True
    grid[30][10].start(grey, 0)
    grid[30][10].barrier = True
    grid[30][9].start(grey, 0)
    grid[30][9].barrier = True
    grid[30][8].start(grey, 0)
    grid[30][8].barrier = True
    grid[29][7].start(grey, 0)
    grid[29][7].barrier = True
    grid[30][7].start(grey, 0)
    grid[30][7].barrier = True
    grid[31][7].start(grey, 0)
    grid[31][7].barrier = True
    grid[32][7].start(grey, 0)
    grid[32][7].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True


    grid[33][7].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True
    grid[34][8].start(grey, 0)
    grid[34][8].barrier = True
    grid[35][8].start(grey, 0)
    grid[35][8].barrier = True
    grid[35][7].start(grey, 0)
    grid[35][7].barrier = True
    grid[36][6].start(grey, 0)
    grid[36][6].barrier = True
    grid[37][6].start(grey, 0)
    grid[37][6].barrier = True
    grid[38][6].start(grey, 0)
    grid[38][6].barrier = True
    grid[39][6].start(grey, 0)
    grid[39][6].barrier = True
    grid[40][6].start(grey, 0)
    grid[40][6].barrier = True
    grid[40][5].start(grey, 0)
    grid[40][5].barrier = True
    grid[40][4].start(grey, 0)
    grid[40][4].barrier = True
    grid[41][3].start(grey, 0)
    grid[41][3].barrier = True
    grid[42][4].start(grey, 0)
    grid[42][4].barrier = True
    grid[42][5].start(grey, 0)
    grid[42][5].barrier = True
    grid[42][6].start(grey, 0)
    grid[42][6].barrier = True
    grid[43][6].start(grey, 0)
    grid[43][6].barrier = True
    grid[44][6].start(grey, 0)
    grid[44][6].barrier = True
    grid[45][6].start(grey, 0)
    grid[45][6].barrier = True
    grid[46][6].start(grey, 0)
    grid[46][6].barrier = True
    grid[47][6].start(grey, 0)
    grid[47][6].barrier = True
    grid[47][5].start(grey, 0)
    grid[47][5].barrier = True
    grid[47][4].start(grey, 0)
    grid[47][4].barrier = True
    grid[47][3].start(grey, 0)
    grid[47][3].barrier = True
    grid[47][2].start(grey, 0)
    grid[47][2].barrier = True
    grid[46][2].start(grey, 0)
    grid[46][2].barrier = True
    grid[46][1].start(grey, 0)
    grid[46][1].barrier = True
    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[45][0].start(grey, 0)
    grid[45][0].barrier = True

    grid[38][2].start(grey, 0)
    grid[38][2].barrier = True
    grid[38][2].start(grey, 0)
    grid[38][2].barrier = True
    grid[40][2].start(grey, 0)
    grid[40][2].barrier = True
    grid[38][2].start(grey, 0)
    grid[38][2].barrier = True
    grid[39][2].start(grey, 0)
    grid[39][2].barrier = True
    grid[39][1].start(grey, 0)
    grid[39][1].barrier = True
    grid[38][1].start(grey, 0)
    grid[38][1].barrier = True
    grid[38][0].start(grey, 0)
    grid[38][0].barrier = True
    grid[39][0].start(grey, 0)
    grid[39][0].barrier = True

    grid[23][5].start(grey, 0)
    grid[23][5].barrier = True
    grid[23][2].start(grey, 0)
    grid[23][2].barrier = True
    grid[33][2].start(grey, 0)
    grid[33][2].barrier = True
    grid[33][5].start(grey, 0)
    grid[33][5].barrier = True
    grid[23][5].start(grey, 0)
    grid[23][5].barrier = True
    grid[24][5].start(grey, 0)
    grid[24][5].barrier = True
    grid[25][5].start(grey, 0)
    grid[25][5].barrier = True
    grid[25][4].start(grey, 0)
    grid[25][4].barrier = True
    grid[25][3].start(grey, 0)
    grid[25][3].barrier = True
    grid[26][3].start(grey, 0)
    grid[26][3].barrier = True
    grid[27][3].start(grey, 0)
    grid[27][3].barrier = True
    grid[28][3].start(grey, 0)
    grid[28][3].barrier = True
    grid[29][3].start(grey, 0)
    grid[29][3].barrier = True
    grid[30][3].start(grey, 0)
    grid[30][3].barrier = True
    grid[31][3].start(grey, 0)
    grid[31][3].barrier = True
    grid[31][4].start(grey, 0)
    grid[31][4].barrier = True
    grid[31][5].start(grey, 0)
    grid[31][5].barrier = True
    grid[32][5].start(grey, 0)
    grid[32][5].barrier = True
    grid[33][5].start(grey, 0)
    grid[33][5].barrier = True
    grid[33][4].start(grey, 0)
    grid[33][4].barrier = True
    grid[33][3].start(grey, 0)
    grid[33][3].barrier = True
    grid[33][2].start(grey, 0)
    grid[33][2].barrier = True
    grid[32][1].start(grey, 0)
    grid[32][1].barrier = True
    grid[31][1].start(grey, 0)
    grid[31][1].barrier = True
    grid[30][1].start(grey, 0)
    grid[30][1].barrier = True
    grid[29][1].start(grey, 0)
    grid[29][1].barrier = True
    grid[28][1].start(grey, 0)
    grid[28][1].barrier = True
    grid[27][1].start(grey, 0)
    grid[27][1].barrier = True
    grid[26][1].start(grey, 0)
    grid[26][1].barrier = True
    grid[25][1].start(grey, 0)
    grid[25][1].barrier = True
    grid[25][1].start(grey, 0)
    grid[25][1].barrier = True
    grid[24][1].start(grey, 0)
    grid[24][1].barrier = True
    grid[23][2].start(grey, 0)
    grid[23][2].barrier = True
    grid[23][3].start(grey, 0)
    grid[23][3].barrier = True
    grid[23][4].start(grey, 0)
    grid[23][4].barrier = True
    grid[23][5].start(grey, 0)
    grid[23][5].barrier = True


    grid[7][29].start(grey, 0)
    grid[7][29].barrier = True
    grid[8][29].start(grey, 0)
    grid[8][29].barrier = True
    grid[9][29].start(grey, 0)
    grid[9][29].barrier = True
    grid[10][29].start(grey, 0)
    grid[10][29].barrier = True
    grid[11][29].start(grey, 0)
    grid[11][29].barrier = True
    grid[12][29].start(grey, 0)
    grid[12][29].barrier = True
    grid[13][29].start(grey, 0)
    grid[13][29].barrier = True
    grid[14][29].start(grey, 0)
    grid[14][29].barrier = True
    grid[15][29].start(grey, 0)
    grid[15][29].barrier = True
    grid[16][29].start(grey, 0)
    grid[16][29].barrier = True
    grid[17][29].start(grey, 0)
    grid[17][29].barrier = True
    grid[17][29].start(grey, 0)
    grid[17][29].barrier = True
    grid[18][29].start(grey, 0)
    grid[18][29].barrier = True
    grid[19][29].start(grey, 0)
    grid[19][29].barrier = True
    grid[20][29].start(grey, 0)
    grid[20][29].barrier = True
    grid[21][29].start(grey, 0)
    grid[21][29].barrier = True
    grid[22][29].start(grey, 0)
    grid[22][29].barrier = True
    grid[23][29].start(grey, 0)
    grid[23][29].barrier = True
    grid[23][29].start(grey, 0)
    grid[23][29].barrier = True
    grid[24][29].start(grey, 0)
    grid[24][29].barrier = True
    grid[25][29].start(grey, 0)
    grid[25][29].barrier = True
    grid[26][29].start(grey, 0)
    grid[26][29].barrier = True
    grid[27][29].start(grey, 0)
    grid[27][29].barrier = True
    grid[28][29].start(grey, 0)
    grid[28][29].barrier = True
    grid[29][29].start(grey, 0)
    grid[29][29].barrier = True
    grid[30][29].start(grey, 0)
    grid[30][29].barrier = True


    grid[30][29].barrier = True
    grid[30][30].start(grey, 0)
    grid[30][30].barrier = True
    grid[30][31].start(grey, 0)
    grid[30][31].barrier = True
    grid[30][32].start(grey, 0)
    grid[30][32].barrier = True
    grid[30][33].start(grey, 0)
    grid[30][33].barrier = True
    grid[29][33].start(grey, 0)
    grid[29][33].barrier = True
    grid[28][33].start(grey, 0)
    grid[28][33].barrier = True
    grid[27][33].start(grey, 0)
    grid[27][33].barrier = True
    grid[26][33].start(grey, 0)
    grid[26][33].barrier = True
    grid[25][33].start(grey, 0)
    grid[25][33].barrier = True
    grid[24][33].start(grey, 0)
    grid[24][33].barrier = True
    grid[23][33].start(grey, 0)
    grid[23][33].barrier = True
    grid[22][33].start(grey, 0)
    grid[22][33].barrier = True
    grid[21][33].start(grey, 0)
    grid[21][33].barrier = True
    grid[20][33].start(grey, 0)
    grid[20][33].barrier = True
    grid[19][33].start(grey, 0)
    grid[19][33].barrier = True
    grid[18][33].start(grey, 0)
    grid[18][33].barrier = True
    grid[18][34].start(grey, 0)
    grid[18][34].barrier = True
    grid[18][35].start(grey, 0)
    grid[18][35].barrier = True
    grid[18][36].start(grey, 0)
    grid[18][36].barrier = True
    grid[18][37].start(grey, 0)
    grid[18][37].barrier = True
    grid[17][38].start(grey, 0)
    grid[17][38].barrier = True

    grid[17][38].start(grey, 0)
    grid[17][38].barrier = True
    grid[16][38].start(grey, 0)
    grid[16][38].barrier = True
    grid[15][38].start(grey, 0)
    grid[15][38].barrier = True
    grid[14][38].start(grey, 0)
    grid[14][38].barrier = True
    grid[13][38].start(grey, 0)
    grid[13][38].barrier = True
    grid[12][38].start(grey, 0)
    grid[12][38].barrier = True
    grid[11][38].start(grey, 0)
    grid[11][38].barrier = True
    grid[10][38].start(grey, 0)
    grid[10][38].barrier = True
    grid[9][38].start(grey, 0)
    grid[9][38].barrier = True
    grid[9][38].start(grey, 0)
    grid[9][38].barrier = True
    grid[9][38].start(grey, 0)
    grid[9][38].barrier = True
    grid[8][38].start(grey, 0)
    grid[8][38].barrier = True
    grid[7][38].start(grey, 0)
    grid[7][38].barrier = True
    grid[7][37].start(grey, 0)
    grid[7][37].barrier = True
    grid[7][36].start(grey, 0)
    grid[7][36].barrier = True
    grid[7][35].start(grey, 0)
    grid[7][35].barrier = True
    grid[7][34].start(grey, 0)
    grid[7][34].barrier = True
    grid[7][33].start(grey, 0)
    grid[7][33].barrier = True
    grid[7][32].start(grey, 0)
    grid[7][32].barrier = True
    grid[7][31].start(grey, 0)
    grid[7][31].barrier = True
    grid[7][30].start(grey, 0)
    grid[7][30].barrier = True
    grid[7][29].start(grey, 0)
    grid[7][29].barrier = True


    grid[8][31].start(grey, 0)
    grid[8][31].barrier = True
    grid[9][31].start(grey, 0)
    grid[9][31].barrier = True
    grid[10][31].start(grey, 0)
    grid[10][31].barrier = True
    grid[11][31].start(grey, 0)
    grid[11][31].barrier = True
    grid[12][31].start(grey, 0)
    grid[12][31].barrier = True
    grid[12][32].start(grey, 0)
    grid[12][32].barrier = True
    grid[12][33].start(grey, 0)
    grid[12][33].barrier = True
    grid[12][34].start(grey, 0)
    grid[12][34].barrier = True
    grid[11][34].start(grey, 0)
    grid[11][34].barrier = True
    grid[10][34].start(grey, 0)
    grid[10][34].barrier = True
    grid[9][34].start(grey, 0)
    grid[9][34].barrier = True
    grid[8][34].start(grey, 0)
    grid[8][34].barrier = True


    grid[14][33].start(grey, 0)
    grid[14][33].barrier = True
    grid[14][33].start(grey, 0)
    grid[14][33].barrier = True
    grid[15][32].start(grey, 0)
    grid[15][32].barrier = True
    grid[15][31].start(grey, 0)
    grid[15][31].barrier = True
    grid[16][31].start(grey, 0)
    grid[16][31].barrier = True
    grid[17][31].start(grey, 0)
    grid[17][31].barrier = True
    grid[17][32].start(grey, 0)
    grid[17][32].barrier = True
    grid[17][33].start(grey, 0)
    grid[17][33].barrier = True
    grid[17][34].start(grey, 0)
    grid[17][34].barrier = True
    grid[17][36].start(grey, 0)
    grid[17][36].barrier = True
    grid[16][36].start(grey, 0)
    grid[16][36].barrier = True
    grid[15][36].start(grey, 0)
    grid[15][36].barrier = True
    grid[14][35].start(grey, 0)
    grid[14][35].barrier = True
    grid[14][34].start(grey, 0)
    grid[14][34].barrier = True
    grid[14][33].start(grey, 0)
    grid[14][33].barrier = True

    grid[25][30].start(grey, 0)
    grid[25][30].barrier = True
    grid[25][30].start(grey, 0)
    grid[25][30].barrier = True
    grid[26][30].start(grey, 0)
    grid[26][30].barrier = True
    grid[27][30].start(grey, 0)
    grid[27][30].barrier = True
    grid[28][30].start(grey, 0)
    grid[28][30].barrier = True
    grid[29][30].start(grey, 0)
    grid[29][30].barrier = True
    grid[28][31].start(grey, 0)
    grid[28][31].barrier = True
    grid[26][31].start(grey, 0)
    grid[26][31].barrier = True
    grid[25][31].start(grey, 0)
    grid[25][31].barrier = True

    grid[20][35].start(grey, 0)
    grid[20][35].barrier = True
    grid[20][35].start(grey, 0)
    grid[20][35].barrier = True
    grid[20][35].start(grey, 0)
    grid[20][35].barrier = True
    grid[21][35].start(grey, 0)
    grid[21][35].barrier = True
    grid[22][35].start(grey, 0)
    grid[22][35].barrier = True
    grid[23][35].start(grey, 0)
    grid[23][35].barrier = True
    grid[24][35].start(grey, 0)
    grid[24][35].barrier = True
    grid[24][36].start(grey, 0)
    grid[24][36].barrier = True
    grid[24][37].start(grey, 0)
    grid[24][37].barrier = True
    grid[24][38].start(grey, 0)
    grid[24][38].barrier = True
    grid[23][38].start(grey, 0)
    grid[23][38].barrier = True
    grid[22][38].start(grey, 0)
    grid[22][38].barrier = True
    grid[21][38].start(grey, 0)
    grid[21][38].barrier = True
    grid[20][38].start(grey, 0)
    grid[20][38].barrier = True
    grid[20][37].start(grey, 0)
    grid[20][37].barrier = True
    grid[20][36].start(grey, 0)
    grid[20][36].barrier = True
    grid[20][35].start(grey, 0)
    grid[20][35].barrier = True


    grid[26][35].start(grey, 0)
    grid[26][35].barrier = True
    grid[26][36].start(grey, 0)
    grid[26][36].barrier = True
    grid[26][36].start(grey, 0)
    grid[26][36].barrier = True
    grid[26][35].start(grey, 0)
    grid[26][35].barrier = True
    grid[27][35].start(grey, 0)
    grid[27][35].barrier = True
    grid[28][35].start(grey, 0)
    grid[28][35].barrier = True
    grid[26][35].start(grey, 0)
    grid[26][35].barrier = True
    grid[26][35].start(grey, 0)
    grid[26][35].barrier = True
    grid[27][35].start(grey, 0)
    grid[27][35].barrier = True
    grid[28][35].start(grey, 0)
    grid[28][35].barrier = True
    grid[29][35].start(grey, 0)
    grid[29][35].barrier = True
    grid[30][35].start(grey, 0)
    grid[30][35].barrier = True
    grid[30][36].start(grey, 0)
    grid[30][36].barrier = True
    grid[30][37].start(grey, 0)
    grid[30][37].barrier = True
    grid[30][38].start(grey, 0)
    grid[30][38].barrier = True
    grid[29][38].start(grey, 0)
    grid[29][38].barrier = True
    grid[28][38].start(grey, 0)
    grid[28][38].barrier = True
    grid[27][38].start(grey, 0)
    grid[27][38].barrier = True
    grid[26][38].start(grey, 0)
    grid[26][38].barrier = True
    grid[26][37].start(grey, 0)
    grid[26][37].barrier = True
    grid[26][36].start(grey, 0)
    grid[26][36].barrier = True


    grid[7][40].start(grey, 0)
    grid[7][40].barrier = True
    grid[30][40].start(grey, 0)
    grid[30][40].barrier = True
    grid[7][40].start(grey, 0)
    grid[7][40].barrier = True
    grid[8][40].start(grey, 0)
    grid[8][40].barrier = True
    grid[9][40].start(grey, 0)
    grid[9][40].barrier = True
    grid[10][40].start(grey, 0)
    grid[10][40].barrier = True
    grid[11][40].start(grey, 0)
    grid[11][40].barrier = True
    grid[13][40].start(grey, 0)
    grid[13][40].barrier = True
    grid[12][40].start(grey, 0)
    grid[12][40].barrier = True
    grid[14][40].start(grey, 0)
    grid[14][40].barrier = True
    grid[15][40].start(grey, 0)
    grid[15][40].barrier = True
    grid[16][40].start(grey, 0)
    grid[16][40].barrier = True
    grid[17][40].start(grey, 0)
    grid[17][40].barrier = True
    grid[18][40].start(grey, 0)
    grid[18][40].barrier = True
    grid[19][40].start(grey, 0)
    grid[19][40].barrier = True
    grid[20][40].start(grey, 0)
    grid[20][40].barrier = True
    grid[21][40].start(grey, 0)
    grid[21][40].barrier = True
    grid[21][40].start(grey, 0)
    grid[21][40].barrier = True
    grid[22][40].start(grey, 0)
    grid[22][40].barrier = True
    grid[23][40].start(grey, 0)
    grid[23][40].barrier = True
    grid[24][40].start(grey, 0)
    grid[24][40].barrier = True
    grid[25][40].start(grey, 0)
    grid[25][40].barrier = True
    grid[26][40].start(grey, 0)
    grid[26][40].barrier = True
    grid[27][40].start(grey, 0)
    grid[27][40].barrier = True
    grid[28][40].start(grey, 0)
    grid[28][40].barrier = True
    grid[29][40].start(grey, 0)
    grid[29][40].barrier = True
    grid[30][40].start(grey, 0)
    grid[30][40].barrier = True


    grid[6][43].start(grey, 0)
    grid[6][43].barrier = True
    grid[30][43].start(grey, 0)
    grid[30][43].barrier = True
    grid[6][43].start(grey, 0)
    grid[6][43].barrier = True
    grid[7][43].start(grey, 0)
    grid[7][43].barrier = True
    grid[8][43].start(grey, 0)
    grid[8][43].barrier = True
    grid[9][43].start(grey, 0)
    grid[9][43].barrier = True
    grid[10][43].start(grey, 0)
    grid[10][43].barrier = True
    grid[11][43].start(grey, 0)
    grid[11][43].barrier = True
    grid[12][43].start(grey, 0)
    grid[12][43].barrier = True
    grid[13][43].start(grey, 0)
    grid[13][43].barrier = True
    grid[14][43].start(grey, 0)
    grid[14][43].barrier = True
    grid[15][43].start(grey, 0)
    grid[15][43].barrier = True
    grid[16][43].start(grey, 0)
    grid[16][43].barrier = True
    grid[17][43].start(grey, 0)
    grid[17][43].barrier = True
    grid[18][43].start(grey, 0)
    grid[18][43].barrier = True
    grid[19][43].start(grey, 0)
    grid[19][43].barrier = True
    grid[20][43].start(grey, 0)
    grid[20][43].barrier = True
    grid[21][43].start(grey, 0)
    grid[21][43].barrier = True
    grid[22][43].start(grey, 0)
    grid[22][43].barrier = True
    grid[23][43].start(grey, 0)
    grid[23][43].barrier = True
    grid[24][43].start(grey, 0)
    grid[24][43].barrier = True
    grid[25][43].start(grey, 0)
    grid[25][43].barrier = True
    grid[26][43].start(grey, 0)
    grid[26][43].barrier = True
    grid[27][43].start(grey, 0)
    grid[27][43].barrier = True
    grid[28][43].start(grey, 0)
    grid[28][43].barrier = True
    grid[29][43].start(grey, 0)
    grid[29][43].barrier = True
    grid[30][43].start(grey, 0)
    grid[30][43].barrier = True


    grid[6][43].start(grey, 0)
    grid[6][43].barrier = True
    grid[6][44].start(grey, 0)
    grid[6][44].barrier = True
    grid[6][45].start(grey, 0)
    grid[6][45].barrier = True
    grid[6][46].start(grey, 0)
    grid[6][46].barrier = True
    grid[6][47].start(grey, 0)
    grid[6][47].barrier = True
    grid[6][48].start(grey, 0)
    grid[6][48].barrier = True
    grid[6][49].start(grey, 0)
    grid[6][49].barrier = True
    grid[6][50].start(grey, 0)
    grid[6][50].barrier = True
    grid[5][51].start(grey, 0)
    grid[5][51].barrier = True
    grid[5][52].start(grey, 0)
    grid[5][52].barrier = True
    grid[5][53].start(grey, 0)
    grid[5][53].barrier = True
    grid[6][53].start(grey, 0)
    grid[6][53].barrier = True
    grid[6][54].start(grey, 0)
    grid[6][54].barrier = True
    grid[6][55].start(grey, 0)
    grid[6][55].barrier = True
    grid[6][56].start(grey, 0)
    grid[6][56].barrier = True


    grid[6][56].start(grey, 0)
    grid[6][56].barrier = True
    grid[6][56].start(grey, 0)
    grid[6][56].barrier = True
    grid[7][56].start(grey, 0)
    grid[7][56].barrier = True
    grid[8][56].start(grey, 0)
    grid[8][56].barrier = True
    grid[8][55].start(grey, 0)
    grid[8][55].barrier = True
    grid[8][54].start(grey, 0)
    grid[8][54].barrier = True
    grid[8][53].start(grey, 0)
    grid[8][53].barrier = True
    grid[8][52].start(grey, 0)
    grid[8][52].barrier = True
    grid[8][51].start(grey, 0)
    grid[8][51].barrier = True
    grid[8][50].start(grey, 0)
    grid[8][50].barrier = True
    grid[8][49].start(grey, 0)
    grid[8][49].barrier = True
    grid[8][48].start(grey, 0)
    grid[8][48].barrier = True
    grid[8][47].start(grey, 0)
    grid[8][47].barrier = True
    grid[8][46].start(grey, 0)
    grid[8][46].barrier = True
    grid[8][45].start(grey, 0)
    grid[8][45].barrier = True


    grid[8][45].barrier = True
    grid[8][45].start(grey, 0)
    grid[8][45].barrier = True
    grid[9][45].start(grey, 0)
    grid[9][45].barrier = True
    grid[8][45].start(grey, 0)
    grid[8][45].barrier = True
    grid[9][45].start(grey, 0)
    grid[9][45].barrier = True
    grid[10][45].start(grey, 0)
    grid[10][45].barrier = True
    grid[11][45].start(grey, 0)
    grid[11][45].barrier = True
    grid[12][45].start(grey, 0)
    grid[12][45].barrier = True
    grid[14][45].start(grey, 0)
    grid[14][45].barrier = True
    grid[14][45].start(grey, 0)
    grid[14][45].barrier = True
    grid[15][45].start(grey, 0)
    grid[15][45].barrier = True
    grid[16][45].start(grey, 0)
    grid[16][45].barrier = True
    grid[17][45].start(grey, 0)
    grid[17][45].barrier = True
    grid[18][45].start(grey, 0)
    grid[18][45].barrier = True
    grid[19][45].start(grey, 0)
    grid[19][45].barrier = True
    grid[20][45].start(grey, 0)
    grid[20][45].barrier = True
    grid[21][45].start(grey, 0)
    grid[21][45].barrier = True
    grid[22][45].start(grey, 0)
    grid[22][45].barrier = True
    grid[23][45].start(grey, 0)
    grid[23][45].barrier = True
    grid[24][45].start(grey, 0)
    grid[24][45].barrier = True
    grid[25][45].start(grey, 0)
    grid[25][45].barrier = True
    grid[26][45].start(grey, 0)
    grid[26][45].barrier = True
    grid[27][45].start(grey, 0)
    grid[27][45].barrier = True
    grid[28][45].start(grey, 0)
    grid[28][45].barrier = True
    grid[29][45].start(grey, 0)
    grid[29][45].barrier = True
    grid[29][45].start(grey, 0)
    grid[29][45].barrier = True
    grid[30][45].start(grey, 0)
    grid[30][45].barrier = True


    grid[30][45].start(grey, 0)
    grid[30][45].barrier = True
    grid[30][46].start(grey, 0)
    grid[30][46].barrier = True
    grid[30][47].start(grey, 0)
    grid[30][47].barrier = True
    grid[30][47].start(grey, 0)
    grid[30][47].barrier = True
    grid[30][48].start(grey, 0)
    grid[30][48].barrier = True
    grid[30][49].start(grey, 0)
    grid[30][49].barrier = True
    grid[30][50].start(grey, 0)
    grid[30][50].barrier = True
    grid[30][51].start(grey, 0)
    grid[30][51].barrier = True
    grid[30][52].start(grey, 0)
    grid[30][52].barrier = True
    grid[30][53].start(grey, 0)
    grid[30][53].barrier = True
    grid[30][54].start(grey, 0)
    grid[30][54].barrier = True
    grid[30][54].start(grey, 0)
    grid[30][54].barrier = True
    grid[30][55].start(grey, 0)
    grid[30][55].barrier = True
    grid[30][56].start(grey, 0)
    grid[30][56].barrier = True
    grid[30][57].start(grey, 0)
    grid[30][57].barrier = True


    grid[10][46].start(grey, 0)
    grid[10][46].barrier = True
    grid[10][45].start(grey, 0)
    grid[10][45].barrier = True
    grid[10][45].start(grey, 0)
    grid[10][45].barrier = True
    grid[10][46].start(grey, 0)
    grid[10][46].barrier = True
    grid[10][47].start(grey, 0)
    grid[10][47].barrier = True
    grid[10][49].start(grey, 0)
    grid[10][49].barrier = True
    grid[10][49].start(grey, 0)
    grid[10][49].barrier = True
    grid[10][50].start(grey, 0)
    grid[10][50].barrier = True
    grid[10][51].start(grey, 0)
    grid[10][51].barrier = True
    grid[10][52].start(grey, 0)
    grid[10][52].barrier = True
    grid[10][53].start(grey, 0)
    grid[10][53].barrier = True
    grid[11][53].start(grey, 0)
    grid[11][53].barrier = True
    grid[10][53].start(grey, 0)
    grid[10][53].barrier = True
    grid[12][53].start(grey, 0)
    grid[12][53].barrier = True
    grid[13][53].start(grey, 0)
    grid[13][53].barrier = True
    grid[14][53].start(grey, 0)
    grid[14][53].barrier = True
    grid[14][53].start(grey, 0)
    grid[14][53].barrier = True
    grid[15][53].start(grey, 0)
    grid[15][53].barrier = True
    grid[16][53].start(grey, 0)
    grid[16][53].barrier = True
    grid[17][53].start(grey, 0)
    grid[17][53].barrier = True
    grid[17][52].start(grey, 0)
    grid[17][52].barrier = True
    grid[17][51].start(grey, 0)
    grid[17][51].barrier = True
    grid[17][50].start(grey, 0)
    grid[17][50].barrier = True
    grid[17][49].start(grey, 0)
    grid[17][49].barrier = True
    grid[17][48].start(grey, 0)
    grid[17][48].barrier = True
    grid[17][47].start(grey, 0)
    grid[17][47].barrier = True
    grid[17][46].start(grey, 0)
    grid[17][46].barrier = True
    grid[17][45].start(grey, 0)
    grid[17][45].barrier = True
    grid[17][45].start(grey, 0)
    grid[17][45].barrier = True


    grid[10][53].barrier = True
    grid[10][53].start(grey, 0)
    grid[10][53].barrier = True
    grid[10][53].start(grey, 0)
    grid[10][53].barrier = True
    grid[10][54].start(grey, 0)
    grid[10][54].barrier = True
    grid[10][56].start(grey, 0)
    grid[10][56].barrier = True
    grid[10][55].start(grey, 0)
    grid[10][55].barrier = True
    grid[10][57].start(grey, 0)
    grid[10][57].barrier = True
    grid[10][57].start(grey, 0)
    grid[10][57].barrier = True
    grid[10][58].start(grey, 0)
    grid[10][58].barrier = True
    grid[10][59].start(grey, 0)
    grid[10][59].barrier = True
    grid[10][61].start(grey, 0)
    grid[10][61].barrier = True
    grid[10][61].start(grey, 0)
    grid[10][61].barrier = True
    grid[10][62].start(grey, 0)
    grid[10][62].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True


    grid[12][58].barrier = True
    grid[12][58].start(grey, 0)
    grid[12][58].barrier = True
    grid[12][58].start(grey, 0)
    grid[12][58].barrier = True
    grid[13][57].start(grey, 0)
    grid[13][57].barrier = True
    grid[14][57].start(grey, 0)
    grid[14][57].barrier = True
    grid[15][58].start(grey, 0)
    grid[15][58].barrier = True
    grid[15][59].start(grey, 0)
    grid[15][59].barrier = True
    grid[14][59].start(grey, 0)
    grid[14][59].barrier = True
    grid[13][60].start(grey, 0)
    grid[13][60].barrier = True
    grid[12][59].start(grey, 0)
    grid[12][59].barrier = True
    grid[12][58].start(grey, 0)
    grid[12][58].barrier = True
    grid[13][58].start(grey, 0)
    grid[13][58].barrier = True
    grid[14][58].start(grey, 0)
    grid[14][58].barrier = True
    grid[14][59].start(grey, 0)
    grid[14][59].barrier = True
    grid[13][59].start(grey, 0)
    grid[13][59].barrier = True


    grid[15][61].start(grey, 0)
    grid[15][61].barrier = True

    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[11][63].start(grey, 0)
    grid[11][63].barrier = True
    grid[12][63].start(grey, 0)
    grid[12][63].barrier = True
    grid[13][63].start(grey, 0)
    grid[13][63].barrier = True
    grid[14][63].start(grey, 0)
    grid[14][63].barrier = True
    grid[15][63].start(grey, 0)
    grid[15][63].barrier = True
    grid[16][63].start(grey, 0)
    grid[16][63].barrier = True
    grid[17][63].start(grey, 0)
    grid[17][63].barrier = True
    grid[18][63].start(grey, 0)
    grid[18][63].barrier = True
    grid[18][62].start(grey, 0)
    grid[18][62].barrier = True
    grid[19][62].start(grey, 0)
    grid[19][62].barrier = True
    grid[19][61].start(grey, 0)
    grid[19][61].barrier = True
    grid[20][61].start(grey, 0)
    grid[20][61].barrier = True
    grid[20][60].start(grey, 0)
    grid[20][60].barrier = True
    grid[21][59].start(grey, 0)
    grid[21][59].barrier = True
    grid[22][58].start(grey, 0)
    grid[22][58].barrier = True
    grid[23][58].start(grey, 0)
    grid[23][58].barrier = True
    grid[24][58].start(grey, 0)
    grid[24][58].barrier = True
    grid[25][58].start(grey, 0)
    grid[25][58].barrier = True
    grid[26][58].start(grey, 0)
    grid[26][58].barrier = True
    grid[27][58].start(grey, 0)
    grid[27][58].barrier = True
    grid[28][57].start(grey, 0)
    grid[28][57].barrier = True
    grid[29][57].start(grey, 0)
    grid[29][57].barrier = True
    grid[30][57].start(grey, 0)
    grid[30][57].barrier = True
    grid[30][56].start(grey, 0)
    grid[30][56].barrier = True

    grid[30][43].start(grey, 0)
    grid[30][43].barrier = True
    grid[30][44].start(grey, 0)
    grid[30][44].barrier = True
    grid[30][45].start(grey, 0)
    grid[30][45].barrier = True
    grid[30][46].start(grey, 0)
    grid[30][46].barrier = True
    grid[30][47].start(grey, 0)
    grid[30][47].barrier = True
    grid[30][48].start(grey, 0)
    grid[30][48].barrier = True
    grid[30][49].start(grey, 0)
    grid[30][49].barrier = True
    grid[30][50].start(grey, 0)
    grid[30][50].barrier = True
    grid[30][52].start(grey, 0)
    grid[30][52].barrier = True
    grid[30][53].start(grey, 0)
    grid[30][53].barrier = True
    grid[30][54].start(grey, 0)
    grid[30][54].barrier = True
    grid[30][55].start(grey, 0)
    grid[30][55].barrier = True
    grid[30][56].start(grey, 0)
    grid[30][56].barrier = True
    grid[30][57].start(grey, 0)
    grid[30][57].barrier = True

    grid[22][46].start(grey, 0)
    grid[22][46].barrier = True
    grid[22][46].start(grey, 0)
    grid[22][46].barrier = True
    grid[22][47].start(grey, 0)
    grid[22][47].barrier = True
    grid[22][48].start(grey, 0)
    grid[22][48].barrier = True
    grid[22][49].start(grey, 0)
    grid[22][49].barrier = True
    grid[22][50].start(grey, 0)
    grid[22][50].barrier = True
    grid[23][50].start(grey, 0)
    grid[23][50].barrier = True
    grid[24][50].start(grey, 0)
    grid[24][50].barrier = True
    grid[24][49].start(grey, 0)
    grid[24][49].barrier = True
    grid[25][49].start(grey, 0)
    grid[25][49].barrier = True
    grid[26][49].start(grey, 0)
    grid[26][49].barrier = True
    grid[27][49].start(grey, 0)
    grid[27][49].barrier = True
    grid[27][50].start(grey, 0)
    grid[27][50].barrier = True
    grid[28][50].start(grey, 0)
    grid[28][50].barrier = True
    grid[28][50].start(grey, 0)
    grid[28][50].barrier = True
    grid[29][50].start(grey, 0)
    grid[29][50].barrier = True
    grid[29][49].start(grey, 0)
    grid[29][49].barrier = True
    grid[29][48].start(grey, 0)
    grid[29][48].barrier = True
    grid[29][47].start(grey, 0)
    grid[29][47].barrier = True
    grid[29][46].start(grey, 0)
    grid[29][46].barrier = True
    grid[29][46].start(grey, 0)
    grid[29][46].barrier = True
    grid[29][45].start(grey, 0)
    grid[29][45].barrier = True
    grid[28][45].start(grey, 0)
    grid[28][45].barrier = True
    grid[27][45].start(grey, 0)
    grid[27][45].barrier = True
    grid[27][46].start(grey, 0)
    grid[27][46].barrier = True
    grid[27][47].start(grey, 0)
    grid[27][47].barrier = True
    grid[26][47].start(grey, 0)
    grid[26][47].barrier = True
    grid[25][47].start(grey, 0)
    grid[25][47].barrier = True
    grid[24][47].start(grey, 0)
    grid[24][47].barrier = True
    grid[24][46].start(grey, 0)
    grid[24][46].barrier = True
    grid[24][45].start(grey, 0)
    grid[24][45].barrier = True
    grid[23][45].start(grey, 0)
    grid[23][45].barrier = True
    grid[22][45].start(grey, 0)
    grid[22][45].barrier = True
    grid[22][46].start(grey, 0)
    grid[22][46].barrier = True


    grid[22][52].start(grey, 0)
    grid[22][52].barrier = True
    grid[23][51].start(grey, 0)
    grid[23][51].barrier = True
    grid[23][51].start(grey, 0)
    grid[23][51].barrier = True
    grid[22][52].start(grey, 0)
    grid[22][52].barrier = True
    grid[22][52].start(grey, 0)
    grid[22][52].barrier = True
    grid[22][52].start(grey, 0)
    grid[22][52].barrier = True
    grid[23][52].start(grey, 0)
    grid[23][52].barrier = True
    grid[24][52].start(grey, 0)
    grid[24][52].barrier = True
    grid[24][53].start(grey, 0)
    grid[24][53].barrier = True
    grid[25][53].start(grey, 0)
    grid[25][53].barrier = True
    grid[26][53].start(grey, 0)
    grid[26][53].barrier = True
    grid[27][53].start(grey, 0)
    grid[27][53].barrier = True
    grid[27][52].start(grey, 0)
    grid[27][52].barrier = True
    grid[28][52].start(grey, 0)
    grid[28][52].barrier = True
    grid[29][52].start(grey, 0)
    grid[29][52].barrier = True
    grid[30][52].start(grey, 0)
    grid[30][52].barrier = True
    grid[30][53].start(grey, 0)
    grid[30][53].barrier = True
    grid[30][54].start(grey, 0)
    grid[30][54].barrier = True
    grid[30][55].start(grey, 0)
    grid[30][55].barrier = True
    grid[30][55].start(grey, 0)
    grid[30][55].barrier = True
    grid[30][56].start(grey, 0)
    grid[30][56].barrier = True
    grid[29][56].start(grey, 0)
    grid[29][56].barrier = True
    grid[28][56].start(grey, 0)
    grid[28][56].barrier = True
    grid[27][56].start(grey, 0)
    grid[27][56].barrier = True
    grid[27][55].start(grey, 0)
    grid[27][55].barrier = True
    grid[26][55].start(grey, 0)
    grid[26][55].barrier = True
    grid[25][55].start(grey, 0)
    grid[25][55].barrier = True
    grid[24][55].start(grey, 0)
    grid[24][55].barrier = True
    grid[24][56].start(grey, 0)
    grid[24][56].barrier = True
    grid[23][56].start(grey, 0)
    grid[23][56].barrier = True
    grid[22][56].start(grey, 0)
    grid[22][56].barrier = True
    grid[22][55].start(grey, 0)
    grid[22][55].barrier = True
    grid[22][54].start(grey, 0)
    grid[22][54].barrier = True
    grid[22][53].start(grey, 0)
    grid[22][53].barrier = True
    grid[22][52].start(grey, 0)
    grid[22][52].barrier = True


    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[10][63].start(grey, 0)
    grid[10][63].barrier = True
    grid[11][63].start(grey, 0)
    grid[11][63].barrier = True
    grid[12][63].start(grey, 0)
    grid[12][63].barrier = True
    grid[13][63].start(grey, 0)
    grid[13][63].barrier = True
    grid[14][63].start(grey, 0)
    grid[14][63].barrier = True
    grid[15][63].start(grey, 0)
    grid[15][63].barrier = True
    grid[16][63].start(grey, 0)
    grid[16][63].barrier = True
    grid[16][63].start(grey, 0)
    grid[16][63].barrier = True
    grid[17][63].start(grey, 0)
    grid[17][63].barrier = True
    grid[17][63].start(grey, 0)
    grid[17][63].barrier = True
    grid[18][63].start(grey, 0)
    grid[18][63].barrier = True
    grid[19][62].start(grey, 0)
    grid[19][62].barrier = True
    grid[20][61].start(grey, 0)
    grid[20][61].barrier = True
    grid[20][60].start(grey, 0)
    grid[20][60].barrier = True
    grid[21][59].start(grey, 0)
    grid[21][59].barrier = True
    grid[22][58].start(grey, 0)
    grid[22][58].barrier = True
    grid[23][58].start(grey, 0)
    grid[23][58].barrier = True
    grid[24][58].start(grey, 0)
    grid[24][58].barrier = True
    grid[25][58].start(grey, 0)
    grid[25][58].barrier = True
    grid[26][58].start(grey, 0)
    grid[26][58].barrier = True
    grid[27][58].start(grey, 0)
    grid[27][58].barrier = True
    grid[27][58].start(grey, 0)
    grid[27][58].barrier = True
    grid[28][57].start(grey, 0)
    grid[28][57].barrier = True
    grid[29][56].start(grey, 0)
    grid[29][56].barrier = True
    grid[30][56].start(grey, 0)
    grid[30][56].barrier = True


    grid[8][58].barrier = True
    grid[8][58].start(grey, 0)
    grid[8][58].barrier = True
    grid[8][59].start(grey, 0)
    grid[8][59].barrier = True
    grid[8][60].start(grey, 0)
    grid[8][60].barrier = True
    grid[8][61].start(grey, 0)
    grid[8][61].barrier = True
    grid[8][62].start(grey, 0)
    grid[8][62].barrier = True
    grid[8][62].start(grey, 0)
    grid[8][62].barrier = True
    grid[7][62].start(grey, 0)
    grid[7][62].barrier = True
    grid[7][61].start(grey, 0)
    grid[7][61].barrier = True
    grid[7][60].start(grey, 0)
    grid[7][60].barrier = True
    grid[7][59].start(grey, 0)
    grid[7][59].barrier = True
    grid[6][60].start(grey, 0)
    grid[6][60].barrier = True
    grid[6][61].start(grey, 0)
    grid[6][61].barrier = True
    grid[6][62].start(grey, 0)
    grid[6][62].barrier = True


    grid[2][69].start(grey, 0)
    grid[2][69].barrier = True
    grid[2][69].start(grey, 0)
    grid[2][69].barrier = True
    grid[3][68].start(grey, 0)
    grid[3][68].barrier = True
    grid[4][67].start(grey, 0)
    grid[4][67].barrier = True
    grid[4][67].start(grey, 0)
    grid[4][67].barrier = True
    grid[5][67].start(grey, 0)
    grid[5][67].barrier = True
    grid[5][66].start(grey, 0)
    grid[5][66].barrier = True
    grid[6][66].start(grey, 0)
    grid[6][66].barrier = True
    grid[7][66].start(grey, 0)
    grid[7][66].barrier = True
    grid[8][66].start(grey, 0)
    grid[8][66].barrier = True
    grid[10][66].start(grey, 0)
    grid[10][66].barrier = True
    grid[9][66].start(grey, 0)
    grid[9][66].barrier = True
    grid[11][66].start(grey, 0)
    grid[11][66].barrier = True
    grid[12][66].start(grey, 0)
    grid[12][66].barrier = True
    grid[13][66].start(grey, 0)
    grid[13][66].barrier = True
    grid[14][66].start(grey, 0)
    grid[14][66].barrier = True
    grid[15][66].start(grey, 0)
    grid[15][66].barrier = True
    grid[16][66].start(grey, 0)
    grid[16][66].barrier = True
    grid[17][66].start(grey, 0)
    grid[17][66].barrier = True
    grid[18][66].start(grey, 0)
    grid[18][66].barrier = True
    grid[19][65].start(grey, 0)
    grid[19][65].barrier = True
    grid[20][65].start(grey, 0)
    grid[20][65].barrier = True
    grid[21][65].start(grey, 0)
    grid[21][65].barrier = True
    grid[22][65].start(grey, 0)
    grid[22][65].barrier = True
    grid[22][65].start(grey, 0)
    grid[22][65].barrier = True
    grid[22][66].start(grey, 0)
    grid[22][66].barrier = True
    grid[22][67].start(grey, 0)
    grid[22][67].barrier = True


    grid[21][65].start(grey, 0)
    grid[21][65].barrier = True
    grid[21][65].start(grey, 0)
    grid[21][65].barrier = True
    grid[21][65].start(grey, 0)
    grid[21][65].barrier = True
    grid[21][65].start(grey, 0)
    grid[21][65].barrier = True
    grid[21][64].start(grey, 0)
    grid[21][64].barrier = True
    grid[21][63].start(grey, 0)
    grid[21][63].barrier = True
    grid[22][62].start(grey, 0)
    grid[22][62].barrier = True
    grid[23][61].start(grey, 0)
    grid[23][61].barrier = True
    grid[24][60].start(grey, 0)
    grid[24][60].barrier = True
    grid[25][60].start(grey, 0)
    grid[25][60].barrier = True
    grid[26][60].start(grey, 0)
    grid[26][60].barrier = True
    grid[27][60].start(grey, 0)
    grid[27][60].barrier = True
    grid[28][60].start(grey, 0)
    grid[28][60].barrier = True
    grid[29][60].start(grey, 0)
    grid[29][60].barrier = True
    grid[30][60].start(grey, 0)
    grid[30][60].barrier = True
    grid[31][60].start(grey, 0)
    grid[31][60].barrier = True
    grid[32][60].start(grey, 0)
    grid[32][60].barrier = True
    grid[33][60].start(grey, 0)
    grid[33][60].barrier = True
    grid[34][60].start(grey, 0)
    grid[34][60].barrier = True
    grid[35][60].start(grey, 0)
    grid[35][60].barrier = True


    grid[25][65].start(grey, 0)
    grid[25][65].barrier = True
    grid[25][65].start(grey, 0)
    grid[25][65].barrier = True
    grid[25][65].start(grey, 0)
    grid[25][65].barrier = True
    grid[25][64].start(grey, 0)
    grid[25][64].barrier = True
    grid[25][63].start(grey, 0)
    grid[25][63].barrier = True
    grid[25][62].start(grey, 0)
    grid[25][62].barrier = True
    grid[26][62].start(grey, 0)
    grid[26][62].barrier = True
    grid[27][62].start(grey, 0)
    grid[27][62].barrier = True
    grid[29][62].start(grey, 0)
    grid[29][62].barrier = True
    grid[27][62].start(grey, 0)
    grid[27][62].barrier = True
    grid[29][62].start(grey, 0)
    grid[29][62].barrier = True
    grid[29][63].start(grey, 0)
    grid[29][63].barrier = True
    grid[29][64].start(grey, 0)
    grid[29][64].barrier = True
    grid[29][65].start(grey, 0)
    grid[29][65].barrier = True
    grid[28][65].start(grey, 0)
    grid[28][65].barrier = True
    grid[27][65].start(grey, 0)
    grid[27][65].barrier = True
    grid[26][65].start(grey, 0)
    grid[26][65].barrier = True
    grid[30][65].start(grey, 0)
    grid[30][65].barrier = True
    grid[31][65].start(grey, 0)
    grid[31][65].barrier = True
    grid[32][64].start(grey, 0)
    grid[32][64].barrier = True
    grid[32][63].start(grey, 0)
    grid[32][63].barrier = True
    grid[32][62].start(grey, 0)
    grid[32][62].barrier = True
    grid[33][62].start(grey, 0)
    grid[33][62].barrier = True
    grid[33][62].start(grey, 0)
    grid[33][62].barrier = True
    grid[34][62].start(grey, 0)
    grid[34][62].barrier = True
    grid[34][63].start(grey, 0)
    grid[34][63].barrier = True
    grid[34][64].start(grey, 0)
    grid[34][64].barrier = True
    grid[34][65].start(grey, 0)
    grid[34][65].barrier = True
    grid[34][66].start(grey, 0)
    grid[34][66].barrier = True
    grid[34][67].start(grey, 0)
    grid[34][67].barrier = True
    grid[34][68].start(grey, 0)
    grid[34][68].barrier = True
    grid[33][68].start(grey, 0)
    grid[33][68].barrier = True
    grid[32][68].start(grey, 0)
    grid[32][68].barrier = True
    grid[34][68].start(grey, 0)
    grid[34][68].barrier = True
    grid[34][68].start(grey, 0)
    grid[34][68].barrier = True
    grid[33][69].start(grey, 0)
    grid[33][69].barrier = True
    grid[32][69].start(grey, 0)
    grid[32][69].barrier = True
    grid[30][69].start(grey, 0)
    grid[30][69].barrier = True


    grid[35][68].start(grey, 0)
    grid[35][68].barrier = True
    grid[35][68].start(grey, 0)
    grid[35][68].barrier = True
    grid[36][68].start(grey, 0)
    grid[36][68].barrier = True
    grid[37][68].start(grey, 0)
    grid[37][68].barrier = True
    grid[38][68].start(grey, 0)
    grid[38][68].barrier = True
    grid[39][68].start(grey, 0)
    grid[39][68].barrier = True
    grid[40][68].start(grey, 0)
    grid[40][68].barrier = True
    grid[41][68].start(grey, 0)
    grid[41][68].barrier = True
    grid[42][68].start(grey, 0)
    grid[42][68].barrier = True
    grid[43][68].start(grey, 0)
    grid[43][68].barrier = True
    grid[44][68].start(grey, 0)
    grid[44][68].barrier = True
    grid[45][68].start(grey, 0)
    grid[45][68].barrier = True
    grid[46][68].start(grey, 0)
    grid[46][68].barrier = True
    grid[47][68].start(grey, 0)
    grid[47][68].barrier = True
    grid[48][68].start(grey, 0)
    grid[48][68].barrier = True
    grid[49][68].start(grey, 0)
    grid[49][68].barrier = True
    grid[50][68].start(grey, 0)
    grid[50][68].barrier = True
    grid[51][68].start(grey, 0)
    grid[51][68].barrier = True
    grid[52][68].start(grey, 0)
    grid[52][68].barrier = True
    grid[52][67].start(grey, 0)
    grid[52][67].barrier = True
    grid[52][66].start(grey, 0)
    grid[52][66].barrier = True
    grid[52][65].start(grey, 0)
    grid[52][65].barrier = True
    grid[52][64].start(grey, 0)
    grid[52][64].barrier = True
    grid[53][63].start(grey, 0)
    grid[53][63].barrier = True
    grid[53][62].start(grey, 0)
    grid[53][62].barrier = True
    grid[53][61].start(grey, 0)
    grid[53][61].barrier = True
    grid[53][60].start(grey, 0)
    grid[53][60].barrier = True
    grid[53][59].start(grey, 0)
    grid[53][59].barrier = True
    grid[54][59].start(grey, 0)
    grid[54][59].barrier = True
    grid[55][59].start(grey, 0)
    grid[55][59].barrier = True
    grid[56][59].start(grey, 0)
    grid[56][59].barrier = True
    grid[56][59].start(grey, 0)
    grid[56][59].barrier = True
    grid[57][59].start(grey, 0)
    grid[57][59].barrier = True
    grid[58][59].start(grey, 0)
    grid[58][59].barrier = True
    grid[59][59].start(grey, 0)
    grid[59][59].barrier = True
    grid[60][59].start(grey, 0)
    grid[60][59].barrier = True
    grid[61][59].start(grey, 0)
    grid[61][59].barrier = True
    grid[61][58].start(grey, 0)
    grid[61][58].barrier = True
    grid[61][57].start(grey, 0)
    grid[61][57].barrier = True
    grid[61][56].start(grey, 0)
    grid[61][56].barrier = True
    grid[61][56].start(grey, 0)
    grid[61][56].barrier = True
    grid[62][56].start(grey, 0)
    grid[62][56].barrier = True
    grid[63][56].start(grey, 0)
    grid[63][56].barrier = True
    grid[64][56].start(grey, 0)
    grid[64][56].barrier = True
    grid[65][56].start(grey, 0)
    grid[65][56].barrier = True
    grid[65][57].start(grey, 0)
    grid[65][57].barrier = True
    grid[66][57].start(grey, 0)
    grid[66][57].barrier = True
    grid[67][57].start(grey, 0)
    grid[67][57].barrier = True
    grid[69][57].start(grey, 0)
    grid[69][57].barrier = True
    grid[68][57].start(grey, 0)
    grid[68][57].barrier = True
    grid[69][57].start(grey, 0)
    grid[69][57].barrier = True


    grid[36][61].start(grey, 0)
    grid[36][61].barrier = True
    grid[36][61].start(grey, 0)
    grid[36][61].barrier = True
    grid[36][61].start(grey, 0)
    grid[36][61].barrier = True
    grid[37][61].start(grey, 0)
    grid[37][61].barrier = True
    grid[38][61].start(grey, 0)
    grid[38][61].barrier = True
    grid[39][61].start(grey, 0)
    grid[39][61].barrier = True
    grid[41][61].start(grey, 0)
    grid[41][61].barrier = True
    grid[36][61].start(grey, 0)
    grid[36][61].barrier = True
    grid[36][61].start(grey, 0)
    grid[36][61].barrier = True
    grid[37][61].start(grey, 0)
    grid[37][61].barrier = True
    grid[38][61].start(grey, 0)
    grid[38][61].barrier = True
    grid[39][61].start(grey, 0)
    grid[39][61].barrier = True
    grid[40][61].start(grey, 0)
    grid[40][61].barrier = True
    grid[41][61].start(grey, 0)
    grid[41][61].barrier = True
    grid[42][61].start(grey, 0)
    grid[42][61].barrier = True
    grid[43][61].start(grey, 0)
    grid[43][61].barrier = True
    grid[43][61].start(grey, 0)
    grid[43][61].barrier = True
    grid[43][61].start(grey, 0)
    grid[43][61].barrier = True
    grid[44][61].start(grey, 0)
    grid[44][61].barrier = True
    grid[45][61].start(grey, 0)
    grid[45][61].barrier = True
    grid[45][61].start(grey, 0)
    grid[45][61].barrier = True
    grid[46][61].start(grey, 0)
    grid[46][61].barrier = True
    grid[46][61].start(grey, 0)
    grid[46][61].barrier = True
    grid[46][61].start(grey, 0)
    grid[46][61].barrier = True
    grid[46][61].start(grey, 0)
    grid[46][61].barrier = True
    grid[46][61].start(grey, 0)
    grid[46][61].barrier = True
    grid[47][61].start(grey, 0)
    grid[47][61].barrier = True
    grid[47][61].start(grey, 0)
    grid[47][61].barrier = True
    grid[48][61].start(grey, 0)
    grid[48][61].barrier = True
    grid[48][61].start(grey, 0)
    grid[48][61].barrier = True
    grid[48][60].start(grey, 0)
    grid[48][60].barrier = True
    grid[48][59].start(grey, 0)
    grid[48][59].barrier = True
    grid[47][58].start(grey, 0)
    grid[47][58].barrier = True
    grid[47][58].start(grey, 0)
    grid[47][58].barrier = True
    grid[46][59].start(grey, 0)
    grid[46][59].barrier = True
    grid[47][59].start(grey, 0)
    grid[47][59].barrier = True
    grid[45][59].start(grey, 0)
    grid[45][59].barrier = True
    grid[45][59].start(grey, 0)
    grid[45][59].barrier = True
    grid[45][59].start(grey, 0)
    grid[45][59].barrier = True
    grid[44][59].start(grey, 0)
    grid[44][59].barrier = True
    grid[44][59].start(grey, 0)
    grid[44][59].barrier = True
    grid[44][59].start(grey, 0)
    grid[44][59].barrier = True
    grid[42][59].start(grey, 0)
    grid[42][59].barrier = True
    grid[41][59].start(grey, 0)
    grid[41][59].barrier = True
    grid[41][59].start(grey, 0)
    grid[41][59].barrier = True
    grid[40][59].start(grey, 0)
    grid[40][59].barrier = True
    grid[39][59].start(grey, 0)
    grid[39][59].barrier = True
    grid[39][59].start(grey, 0)
    grid[39][59].barrier = True
    grid[39][59].start(grey, 0)
    grid[39][59].barrier = True
    grid[38][59].start(grey, 0)
    grid[38][59].barrier = True
    grid[38][59].start(grey, 0)
    grid[38][59].barrier = True
    grid[38][58].start(grey, 0)
    grid[38][58].barrier = True
    grid[37][58].start(grey, 0)
    grid[37][58].barrier = True
    grid[36][58].start(grey, 0)
    grid[36][58].barrier = True
    grid[36][57].start(grey, 0)
    grid[36][57].barrier = True
    grid[35][56].start(grey, 0)
    grid[35][56].barrier = True
    grid[34][56].start(grey, 0)
    grid[34][56].barrier = True
    grid[34][55].start(grey, 0)
    grid[34][55].barrier = True
    grid[33][55].start(grey, 0)
    grid[33][55].barrier = True
    grid[33][54].start(grey, 0)
    grid[33][54].barrier = True
    grid[33][53].start(grey, 0)
    grid[33][53].barrier = True
    grid[33][53].start(grey, 0)
    grid[33][53].barrier = True
    grid[33][52].start(grey, 0)
    grid[33][52].barrier = True
    grid[33][51].start(grey, 0)
    grid[33][51].barrier = True
    grid[33][50].start(grey, 0)
    grid[33][50].barrier = True
    grid[33][49].start(grey, 0)
    grid[33][49].barrier = True
    grid[33][48].start(grey, 0)
    grid[33][48].barrier = True
    grid[33][47].start(grey, 0)
    grid[33][47].barrier = True
    grid[33][46].start(grey, 0)
    grid[33][46].barrier = True
    grid[33][46].start(grey, 0)
    grid[33][46].barrier = True
    grid[33][45].start(grey, 0)
    grid[33][45].barrier = True
    grid[33][44].start(grey, 0)
    grid[33][44].barrier = True
    grid[33][43].start(grey, 0)
    grid[33][43].barrier = True
    grid[34][43].start(grey, 0)
    grid[34][43].barrier = True
    grid[34][43].start(grey, 0)
    grid[34][43].barrier = True
    grid[35][43].start(grey, 0)
    grid[35][43].barrier = True
    grid[36][43].start(grey, 0)
    grid[36][43].barrier = True
    grid[36][43].start(grey, 0)
    grid[36][43].barrier = True
    grid[37][43].start(grey, 0)
    grid[37][43].barrier = True
    grid[38][43].start(grey, 0)
    grid[38][43].barrier = True
    grid[39][43].start(grey, 0)
    grid[39][43].barrier = True
    grid[39][43].start(grey, 0)
    grid[39][43].barrier = True
    grid[40][43].start(grey, 0)
    grid[40][43].barrier = True
    grid[41][43].start(grey, 0)
    grid[41][43].barrier = True
    grid[42][43].start(grey, 0)
    grid[42][43].barrier = True
    grid[43][43].start(grey, 0)
    grid[43][43].barrier = True
    grid[45][43].start(grey, 0)
    grid[45][43].barrier = True
    grid[44][43].start(grey, 0)
    grid[44][43].barrier = True
    grid[46][43].start(grey, 0)
    grid[46][43].barrier = True
    grid[47][43].start(grey, 0)
    grid[47][43].barrier = True
    grid[47][44].start(grey, 0)
    grid[47][44].barrier = True
    grid[47][45].start(grey, 0)
    grid[47][45].barrier = True
    grid[47][46].start(grey, 0)
    grid[47][46].barrier = True
    grid[47][46].start(grey, 0)
    grid[47][46].barrier = True
    grid[47][47].start(grey, 0)
    grid[47][47].barrier = True
    grid[47][48].start(grey, 0)
    grid[47][48].barrier = True
    grid[47][48].start(grey, 0)
    grid[47][48].barrier = True
    grid[47][48].start(grey, 0)
    grid[47][48].barrier = True
    grid[47][49].start(grey, 0)
    grid[47][49].barrier = True
    grid[46][49].start(grey, 0)
    grid[46][49].barrier = True
    grid[45][49].start(grey, 0)
    grid[45][49].barrier = True
    grid[44][49].start(grey, 0)
    grid[44][49].barrier = True
    grid[44][47].start(grey, 0)
    grid[44][47].barrier = True
    grid[44][48].start(grey, 0)
    grid[44][48].barrier = True
    grid[43][48].start(grey, 0)
    grid[43][48].barrier = True
    grid[42][48].start(grey, 0)
    grid[42][48].barrier = True
    grid[42][49].start(grey, 0)
    grid[42][49].barrier = True
    grid[41][49].start(grey, 0)
    grid[41][49].barrier = True
    grid[40][49].start(grey, 0)
    grid[40][49].barrier = True
    grid[40][49].start(grey, 0)
    grid[40][49].barrier = True
    grid[39][49].start(grey, 0)
    grid[39][49].barrier = True
    grid[38][49].start(grey, 0)
    grid[38][49].barrier = True
    grid[37][49].start(grey, 0)
    grid[37][49].barrier = True
    grid[36][48].start(grey, 0)
    grid[36][48].barrier = True
    grid[36][47].start(grey, 0)
    grid[36][47].barrier = True
    grid[36][46].start(grey, 0)
    grid[36][46].barrier = True
    grid[36][45].start(grey, 0)
    grid[36][45].barrier = True
    grid[37][45].start(grey, 0)
    grid[37][45].barrier = True
    grid[37][44].start(grey, 0)
    grid[37][44].barrier = True
    grid[37][44].start(grey, 0)
    grid[37][44].barrier = True
    grid[37][43].start(grey, 0)
    grid[37][43].barrier = True
    grid[38][43].start(grey, 0)
    grid[38][43].barrier = True
    grid[38][42].start(grey, 0)
    grid[38][42].barrier = True
    grid[39][42].start(grey, 0)
    grid[39][42].barrier = True
    grid[40][42].start(grey, 0)
    grid[40][42].barrier = True
    grid[41][42].start(grey, 0)
    grid[41][42].barrier = True
    grid[42][42].start(grey, 0)
    grid[42][42].barrier = True
    grid[43][42].start(grey, 0)
    grid[43][42].barrier = True
    grid[44][42].start(grey, 0)
    grid[44][42].barrier = True
    grid[45][42].start(grey, 0)
    grid[45][42].barrier = True
    grid[46][42].start(grey, 0)
    grid[46][42].barrier = True
    grid[47][42].start(grey, 0)
    grid[47][42].barrier = True


    grid[46][51].start(grey, 0)
    grid[46][51].barrier = True
    grid[46][51].start(grey, 0)
    grid[46][51].barrier = True
    grid[46][51].start(grey, 0)
    grid[46][51].barrier = True
    grid[46][51].start(grey, 0)
    grid[46][51].barrier = True
    grid[46][51].start(grey, 0)
    grid[46][51].barrier = True
    grid[47][51].start(grey, 0)
    grid[47][51].barrier = True
    grid[47][51].start(grey, 0)
    grid[47][51].barrier = True
    grid[46][52].start(grey, 0)
    grid[46][52].barrier = True
    grid[47][52].start(grey, 0)
    grid[47][52].barrier = True
    grid[47][53].start(grey, 0)
    grid[47][53].barrier = True
    grid[46][53].start(grey, 0)
    grid[46][53].barrier = True
    grid[46][54].start(grey, 0)
    grid[46][54].barrier = True
    grid[47][54].start(grey, 0)
    grid[47][54].barrier = True


    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][45].start(grey, 0)
    grid[49][45].barrier = True
    grid[49][44].start(grey, 0)
    grid[49][44].barrier = True
    grid[49][43].start(grey, 0)
    grid[49][43].barrier = True
    grid[49][42].start(grey, 0)
    grid[49][42].barrier = True
    grid[49][42].start(grey, 0)
    grid[49][42].barrier = True
    grid[50][42].start(grey, 0)
    grid[50][42].barrier = True
    grid[51][42].start(grey, 0)
    grid[51][42].barrier = True
    grid[52][42].start(grey, 0)
    grid[52][42].barrier = True
    grid[53][42].start(grey, 0)
    grid[53][42].barrier = True
    grid[54][42].start(grey, 0)
    grid[54][42].barrier = True
    grid[54][43].start(grey, 0)
    grid[54][43].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True
    grid[54][46].start(grey, 0)
    grid[54][46].barrier = True
    grid[54][47].start(grey, 0)
    grid[54][47].barrier = True
    grid[54][48].start(grey, 0)
    grid[54][48].barrier = True
    grid[54][49].start(grey, 0)
    grid[54][49].barrier = True
    grid[54][50].start(grey, 0)
    grid[54][50].barrier = True
    grid[54][51].start(grey, 0)
    grid[54][51].barrier = True
    grid[54][52].start(grey, 0)
    grid[54][52].barrier = True
    grid[54][53].start(grey, 0)
    grid[54][53].barrier = True
    grid[54][54].start(grey, 0)
    grid[54][54].barrier = True
    grid[53][54].start(grey, 0)
    grid[53][54].barrier = True
    grid[53][55].start(grey, 0)
    grid[53][55].barrier = True
    grid[52][55].start(grey, 0)
    grid[52][55].barrier = True
    grid[51][55].start(grey, 0)
    grid[51][55].barrier = True
    grid[52][56].start(grey, 0)
    grid[52][56].barrier = True
    grid[51][56].start(grey, 0)
    grid[51][56].barrier = True
    grid[50][55].start(grey, 0)
    grid[50][55].barrier = True
    grid[50][54].start(grey, 0)
    grid[50][54].barrier = True
    grid[50][53].start(grey, 0)
    grid[50][53].barrier = True
    grid[50][52].start(grey, 0)
    grid[50][52].barrier = True
    grid[50][51].start(grey, 0)
    grid[50][51].barrier = True
    grid[50][50].start(grey, 0)
    grid[50][50].barrier = True
    grid[50][49].start(grey, 0)
    grid[50][49].barrier = True
    grid[50][48].start(grey, 0)
    grid[50][48].barrier = True
    grid[50][47].start(grey, 0)
    grid[50][47].barrier = True
    grid[51][47].start(grey, 0)
    grid[51][47].barrier = True
    grid[51][46].start(grey, 0)
    grid[51][46].barrier = True
    grid[51][45].start(grey, 0)
    grid[51][45].barrier = True
    grid[52][45].start(grey, 0)
    grid[52][45].barrier = True
    grid[53][45].start(grey, 0)
    grid[53][45].barrier = True
    grid[53][45].start(grey, 0)
    grid[53][45].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][42].start(grey, 0)
    grid[54][42].barrier = True


    # dont know its idk
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][45].start(grey, 0)
    grid[49][45].barrier = True
    grid[49][44].start(grey, 0)
    grid[49][44].barrier = True
    grid[49][43].start(grey, 0)
    grid[49][43].barrier = True
    grid[49][42].start(grey, 0)
    grid[49][42].barrier = True
    grid[49][42].start(grey, 0)
    grid[49][42].barrier = True
    grid[50][42].start(grey, 0)
    grid[50][42].barrier = True
    grid[51][42].start(grey, 0)
    grid[51][42].barrier = True
    grid[52][42].start(grey, 0)
    grid[52][42].barrier = True
    grid[53][42].start(grey, 0)
    grid[53][42].barrier = True
    grid[54][42].start(grey, 0)
    grid[54][42].barrier = True
    grid[54][43].start(grey, 0)
    grid[54][43].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True
    grid[54][46].start(grey, 0)
    grid[54][46].barrier = True
    grid[54][47].start(grey, 0)
    grid[54][47].barrier = True
    grid[54][48].start(grey, 0)
    grid[54][48].barrier = True
    grid[54][49].start(grey, 0)
    grid[54][49].barrier = True
    grid[54][50].start(grey, 0)
    grid[54][50].barrier = True
    grid[54][51].start(grey, 0)
    grid[54][51].barrier = True
    grid[54][52].start(grey, 0)
    grid[54][52].barrier = True
    grid[54][53].start(grey, 0)
    grid[54][53].barrier = True
    grid[54][54].start(grey, 0)
    grid[54][54].barrier = True
    grid[53][54].start(grey, 0)
    grid[53][54].barrier = True
    grid[53][55].start(grey, 0)
    grid[53][55].barrier = True
    grid[52][55].start(grey, 0)
    grid[52][55].barrier = True
    grid[51][55].start(grey, 0)
    grid[51][55].barrier = True
    grid[52][56].start(grey, 0)
    grid[52][56].barrier = True
    grid[51][56].start(grey, 0)
    grid[51][56].barrier = True
    grid[50][55].start(grey, 0)
    grid[50][55].barrier = True
    grid[50][54].start(grey, 0)
    grid[50][54].barrier = True
    grid[50][53].start(grey, 0)
    grid[50][53].barrier = True
    grid[50][52].start(grey, 0)
    grid[50][52].barrier = True
    grid[50][51].start(grey, 0)
    grid[50][51].barrier = True
    grid[50][50].start(grey, 0)
    grid[50][50].barrier = True
    grid[50][49].start(grey, 0)
    grid[50][49].barrier = True
    grid[50][48].start(grey, 0)
    grid[50][48].barrier = True
    grid[50][47].start(grey, 0)
    grid[50][47].barrier = True
    grid[51][47].start(grey, 0)
    grid[51][47].barrier = True
    grid[51][46].start(grey, 0)
    grid[51][46].barrier = True
    grid[51][45].start(grey, 0)
    grid[51][45].barrier = True
    grid[52][45].start(grey, 0)
    grid[52][45].barrier = True
    grid[53][45].start(grey, 0)
    grid[53][45].barrier = True
    grid[53][45].start(grey, 0)
    grid[53][45].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][44].start(grey, 0)
    grid[54][44].barrier = True
    grid[54][42].start(grey, 0)
    grid[54][42].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][46].start(grey, 0)
    grid[49][46].barrier = True
    grid[49][45].start(grey, 0)
    grid[49][45].barrier = True
    grid[49][44].start(grey, 0)
    grid[49][44].barrier = True
    grid[49][43].start(grey, 0)
    grid[49][43].barrier = True
    grid[49][42].start(grey, 0)
    grid[49][42].barrier = True
    grid[50][42].start(grey, 0)
    grid[50][42].barrier = True
    grid[51][42].start(grey, 0)
    grid[51][42].barrier = True
    grid[52][42].start(grey, 0)
    grid[52][42].barrier = True
    grid[52][42].start(grey, 0)
    grid[52][42].barrier = True
    grid[53][42].start(grey, 0)
    grid[53][42].barrier = True
    grid[54][42].start(grey, 0)
    grid[54][42].barrier = True
    grid[54][43].start(grey, 0)
    grid[54][43].barrier = True
    grid[54][43].start(grey, 0)
    grid[54][43].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True
    grid[54][46].start(grey, 0)
    grid[54][46].barrier = True
    grid[54][47].start(grey, 0)
    grid[54][47].barrier = True
    grid[54][47].start(grey, 0)
    grid[54][47].barrier = True
    grid[54][48].start(grey, 0)
    grid[54][48].barrier = True
    grid[54][49].start(grey, 0)
    grid[54][49].barrier = True
    grid[54][50].start(grey, 0)
    grid[54][50].barrier = True
    grid[54][51].start(grey, 0)
    grid[54][51].barrier = True
    grid[54][51].start(grey, 0)
    grid[54][51].barrier = True
    grid[54][52].start(grey, 0)
    grid[54][52].barrier = True
    grid[54][53].start(grey, 0)
    grid[54][53].barrier = True
    grid[54][54].start(grey, 0)
    grid[54][54].barrier = True
    grid[53][54].start(grey, 0)
    grid[53][54].barrier = True
    grid[53][54].start(grey, 0)
    grid[53][54].barrier = True
    grid[53][55].start(grey, 0)
    grid[53][55].barrier = True
    grid[52][55].start(grey, 0)
    grid[52][55].barrier = True
    grid[51][55].start(grey, 0)
    grid[51][55].barrier = True
    grid[51][56].start(grey, 0)
    grid[51][56].barrier = True
    grid[52][56].start(grey, 0)
    grid[52][56].barrier = True
    grid[50][55].start(grey, 0)
    grid[50][55].barrier = True
    grid[50][54].start(grey, 0)
    grid[50][54].barrier = True
    grid[50][53].start(grey, 0)
    grid[50][53].barrier = True
    grid[50][52].start(grey, 0)
    grid[50][52].barrier = True
    grid[50][51].start(grey, 0)
    grid[50][51].barrier = True
    grid[50][50].start(grey, 0)
    grid[50][50].barrier = True
    grid[50][49].start(grey, 0)
    grid[50][49].barrier = True
    grid[50][48].start(grey, 0)
    grid[50][48].barrier = True
    grid[50][47].start(grey, 0)
    grid[50][47].barrier = True
    grid[51][47].start(grey, 0)
    grid[51][47].barrier = True
    grid[51][47].start(grey, 0)
    grid[51][47].barrier = True
    grid[51][46].start(grey, 0)
    grid[51][46].barrier = True
    grid[51][45].start(grey, 0)
    grid[51][45].barrier = True
    grid[51][45].start(grey, 0)
    grid[51][45].barrier = True
    grid[52][45].start(grey, 0)
    grid[52][45].barrier = True
    grid[53][45].start(grey, 0)
    grid[53][45].barrier = True
    grid[54][45].start(grey, 0)
    grid[54][45].barrier = True


    grid[56][42].start(grey, 0)
    grid[56][42].barrier = True
    grid[56][43].start(grey, 0)
    grid[56][43].barrier = True
    grid[56][44].start(grey, 0)
    grid[56][44].barrier = True
    grid[56][45].start(grey, 0)
    grid[56][45].barrier = True
    grid[56][46].start(grey, 0)
    grid[56][46].barrier = True
    grid[57][46].start(grey, 0)
    grid[57][46].barrier = True
    grid[57][46].start(grey, 0)
    grid[57][46].barrier = True
    grid[58][46].start(grey, 0)
    grid[58][46].barrier = True
    grid[58][47].start(grey, 0)
    grid[58][47].barrier = True
    grid[57][47].start(grey, 0)
    grid[57][47].barrier = True
    grid[56][47].start(grey, 0)
    grid[56][47].barrier = True
    grid[56][48].start(grey, 0)
    grid[56][48].barrier = True
    grid[56][49].start(grey, 0)
    grid[56][49].barrier = True
    grid[57][49].start(grey, 0)
    grid[57][49].barrier = True
    grid[58][49].start(grey, 0)
    grid[58][49].barrier = True
    grid[58][50].start(grey, 0)
    grid[58][50].barrier = True
    grid[57][50].start(grey, 0)
    grid[57][50].barrier = True
    grid[56][50].start(grey, 0)
    grid[56][50].barrier = True
    grid[56][51].start(grey, 0)
    grid[56][51].barrier = True
    grid[57][51].start(grey, 0)
    grid[57][51].barrier = True
    grid[58][51].start(grey, 0)
    grid[58][51].barrier = True
    grid[59][51].start(grey, 0)
    grid[59][51].barrier = True
    grid[60][51].start(grey, 0)
    grid[60][51].barrier = True
    grid[61][51].start(grey, 0)
    grid[61][51].barrier = True
    grid[62][51].start(grey, 0)
    grid[62][51].barrier = True
    grid[63][51].start(grey, 0)
    grid[63][51].barrier = True
    grid[64][51].start(grey, 0)
    grid[64][51].barrier = True
    grid[65][51].start(grey, 0)
    grid[65][51].barrier = True
    grid[65][50].start(grey, 0)
    grid[65][50].barrier = True
    grid[64][50].start(grey, 0)
    grid[64][50].barrier = True
    grid[63][50].start(grey, 0)
    grid[63][50].barrier = True
    grid[62][50].start(grey, 0)
    grid[62][50].barrier = True
    grid[62][49].start(grey, 0)
    grid[62][49].barrier = True
    grid[63][49].start(grey, 0)
    grid[63][49].barrier = True
    grid[64][49].start(grey, 0)
    grid[64][49].barrier = True
    grid[65][49].start(grey, 0)
    grid[65][49].barrier = True
    grid[65][49].start(grey, 0)
    grid[65][49].barrier = True
    grid[65][48].start(grey, 0)
    grid[65][48].barrier = True
    grid[65][47].start(grey, 0)
    grid[65][47].barrier = True
    grid[65][47].start(grey, 0)
    grid[65][47].barrier = True
    grid[64][47].start(grey, 0)
    grid[64][47].barrier = True
    grid[63][47].start(grey, 0)
    grid[63][47].barrier = True
    grid[62][47].start(grey, 0)
    grid[62][47].barrier = True
    grid[62][46].start(grey, 0)
    grid[62][46].barrier = True
    grid[63][46].start(grey, 0)
    grid[63][46].barrier = True
    grid[64][46].start(grey, 0)
    grid[64][46].barrier = True
    grid[65][46].start(grey, 0)
    grid[65][46].barrier = True
    grid[65][45].start(grey, 0)
    grid[65][45].barrier = True
    grid[65][44].start(grey, 0)
    grid[65][44].barrier = True
    grid[64][44].start(grey, 0)
    grid[64][44].barrier = True
    grid[64][44].start(grey, 0)
    grid[64][44].barrier = True
    grid[63][44].start(grey, 0)
    grid[63][44].barrier = True
    grid[62][44].start(grey, 0)
    grid[62][44].barrier = True
    grid[65][43].start(grey, 0)
    grid[65][43].barrier = True
    grid[65][42].start(grey, 0)
    grid[65][42].barrier = True
    grid[64][42].start(grey, 0)
    grid[64][42].barrier = True
    grid[64][42].start(grey, 0)
    grid[64][42].barrier = True
    grid[63][42].start(grey, 0)
    grid[63][42].barrier = True
    grid[62][42].start(grey, 0)
    grid[62][42].barrier = True
    grid[61][42].start(grey, 0)
    grid[61][42].barrier = True
    grid[60][42].start(grey, 0)
    grid[60][42].barrier = True
    grid[59][42].start(grey, 0)
    grid[59][42].barrier = True
    grid[59][43].start(grey, 0)
    grid[59][43].barrier = True
    grid[60][43].start(grey, 0)
    grid[60][43].barrier = True
    grid[60][44].start(grey, 0)
    grid[60][44].barrier = True
    grid[59][44].start(grey, 0)
    grid[59][44].barrier = True
    grid[58][42].start(grey, 0)
    grid[58][42].barrier = True


    grid[55][53].start(grey, 0)
    grid[55][53].barrier = True
    grid[54][53].start(grey, 0)
    grid[54][53].barrier = True
    grid[69][57].start(grey, 0)
    grid[69][57].barrier = True
    grid[55][53].start(grey, 0)
    grid[55][53].barrier = True
    grid[55][53].start(grey, 0)
    grid[55][53].barrier = True
    grid[55][53].start(grey, 0)
    grid[55][53].barrier = True
    grid[55][53].start(grey, 0)
    grid[55][53].barrier = True
    grid[56][53].start(grey, 0)
    grid[56][53].barrier = True
    grid[57][53].start(grey, 0)
    grid[57][53].barrier = True
    grid[57][54].start(grey, 0)
    grid[57][54].barrier = True
    grid[56][54].start(grey, 0)
    grid[56][54].barrier = True
    grid[56][55].start(grey, 0)
    grid[56][55].barrier = True
    grid[56][55].start(grey, 0)
    grid[56][55].barrier = True
    grid[57][55].start(grey, 0)
    grid[57][55].barrier = True
    grid[58][56].start(grey, 0)
    grid[58][56].barrier = True
    grid[57][56].start(grey, 0)
    grid[57][56].barrier = True
    grid[57][56].start(grey, 0)
    grid[57][56].barrier = True
    grid[58][57].start(grey, 0)
    grid[58][57].barrier = True
    grid[58][53].start(grey, 0)
    grid[58][53].barrier = True
    grid[59][53].start(grey, 0)
    grid[59][53].barrier = True
    grid[60][53].start(grey, 0)
    grid[60][53].barrier = True
    grid[61][53].start(grey, 0)
    grid[61][53].barrier = True
    grid[62][53].start(grey, 0)
    grid[62][53].barrier = True
    grid[62][53].start(grey, 0)
    grid[62][53].barrier = True
    grid[63][53].start(grey, 0)
    grid[63][53].barrier = True
    grid[64][53].start(grey, 0)
    grid[64][53].barrier = True
    grid[65][53].start(grey, 0)
    grid[65][53].barrier = True
    grid[66][53].start(grey, 0)
    grid[66][53].barrier = True
    grid[67][53].start(grey, 0)
    grid[67][53].barrier = True
    grid[67][52].start(grey, 0)
    grid[67][52].barrier = True
    grid[67][51].start(grey, 0)
    grid[67][51].barrier = True
    grid[67][50].start(grey, 0)
    grid[67][50].barrier = True
    grid[67][49].start(grey, 0)
    grid[67][49].barrier = True
    grid[67][48].start(grey, 0)
    grid[67][48].barrier = True
    grid[67][47].start(grey, 0)
    grid[67][47].barrier = True
    grid[67][46].start(grey, 0)
    grid[67][46].barrier = True
    grid[67][45].start(grey, 0)
    grid[67][45].barrier = True
    grid[67][44].start(grey, 0)
    grid[67][44].barrier = True
    grid[67][43].start(grey, 0)
    grid[67][43].barrier = True
    grid[67][42].start(grey, 0)
    grid[67][42].barrier = True
    grid[67][41].start(grey, 0)
    grid[67][41].barrier = True
    grid[67][40].start(grey, 0)
    grid[67][40].barrier = True
    grid[66][40].start(grey, 0)
    grid[66][40].barrier = True
    grid[65][40].start(grey, 0)
    grid[65][40].barrier = True
    grid[64][40].start(grey, 0)
    grid[64][40].barrier = True
    grid[63][40].start(grey, 0)
    grid[63][40].barrier = True
    grid[62][40].start(grey, 0)
    grid[62][40].barrier = True
    grid[61][40].start(grey, 0)
    grid[61][40].barrier = True
    grid[60][40].start(grey, 0)
    grid[60][40].barrier = True
    grid[59][40].start(grey, 0)
    grid[59][40].barrier = True
    grid[58][40].start(grey, 0)
    grid[58][40].barrier = True
    grid[57][40].start(grey, 0)
    grid[57][40].barrier = True
    grid[56][40].start(grey, 0)
    grid[56][40].barrier = True
    grid[55][40].start(grey, 0)
    grid[55][40].barrier = True
    grid[54][39].start(grey, 0)
    grid[54][39].barrier = True
    grid[54][39].start(grey, 0)
    grid[54][39].barrier = True
    grid[55][40].start(grey, 0)
    grid[55][40].barrier = True
    grid[55][40].start(grey, 0)
    grid[55][40].barrier = True
    grid[55][40].start(grey, 0)
    grid[55][40].barrier = True
    grid[54][40].start(grey, 0)
    grid[54][40].barrier = True
    grid[53][40].start(grey, 0)
    grid[53][40].barrier = True
    grid[52][40].start(grey, 0)
    grid[52][40].barrier = True
    grid[51][40].start(grey, 0)
    grid[51][40].barrier = True
    grid[50][40].start(grey, 0)
    grid[50][40].barrier = True
    grid[49][40].start(grey, 0)
    grid[49][40].barrier = True
    grid[48][40].start(grey, 0)
    grid[48][40].barrier = True
    grid[47][40].start(grey, 0)
    grid[47][40].barrier = True
    grid[46][40].start(grey, 0)
    grid[46][40].barrier = True
    grid[45][40].start(grey, 0)
    grid[45][40].barrier = True
    grid[44][40].start(grey, 0)
    grid[44][40].barrier = True
    grid[43][40].start(grey, 0)
    grid[43][40].barrier = True
    grid[43][40].start(grey, 0)
    grid[43][40].barrier = True
    grid[42][40].start(grey, 0)
    grid[42][40].barrier = True
    grid[41][40].start(grey, 0)
    grid[41][40].barrier = True


    grid[36][40].start(grey, 0)
    grid[36][40].barrier = True
    grid[36][40].start(grey, 0)
    grid[36][40].barrier = True
    grid[36][39].start(grey, 0)
    grid[36][39].barrier = True
    grid[35][39].start(grey, 0)
    grid[35][39].barrier = True
    grid[35][40].start(grey, 0)
    grid[35][40].barrier = True
    grid[34][40].start(grey, 0)
    grid[34][40].barrier = True
    grid[34][39].start(grey, 0)
    grid[34][39].barrier = True


    grid[45][38].start(grey, 0)
    grid[45][38].barrier = True
    grid[45][39].start(grey, 0)
    grid[45][39].barrier = True
    grid[48][37].start(grey, 0)
    grid[48][37].barrier = True
    grid[49][38].start(grey, 0)
    grid[49][38].barrier = True
    grid[49][39].start(grey, 0)
    grid[49][39].barrier = True
    grid[48][39].start(grey, 0)
    grid[48][39].barrier = True

    grid[56][33].start(grey, 0)
    grid[56][33].barrier = True
    grid[56][33].start(grey, 0)
    grid[56][33].barrier = True
    grid[56][33].start(grey, 0)
    grid[56][33].barrier = True
    grid[56][33].start(grey, 0)
    grid[56][33].barrier = True
    grid[57][33].start(grey, 0)
    grid[57][33].barrier = True
    grid[58][33].start(grey, 0)
    grid[58][33].barrier = True
    grid[59][33].start(grey, 0)
    grid[59][33].barrier = True
    grid[59][33].start(grey, 0)
    grid[59][33].barrier = True
    grid[61][33].start(grey, 0)
    grid[61][33].barrier = True
    grid[60][33].start(grey, 0)
    grid[60][33].barrier = True
    grid[62][33].start(grey, 0)
    grid[62][33].barrier = True
    grid[62][34].start(grey, 0)
    grid[62][34].barrier = True
    grid[62][35].start(grey, 0)
    grid[62][35].barrier = True
    grid[62][36].start(grey, 0)
    grid[62][36].barrier = True
    grid[61][36].start(grey, 0)
    grid[61][36].barrier = True
    grid[60][36].start(grey, 0)
    grid[60][36].barrier = True
    grid[59][36].start(grey, 0)
    grid[59][36].barrier = True
    grid[59][37].start(grey, 0)
    grid[59][37].barrier = True
    grid[60][37].start(grey, 0)
    grid[60][37].barrier = True
    grid[58][36].start(grey, 0)
    grid[58][36].barrier = True
    grid[57][36].start(grey, 0)
    grid[57][36].barrier = True
    grid[57][35].start(grey, 0)
    grid[57][35].barrier = True
    grid[56][35].start(grey, 0)
    grid[56][35].barrier = True
    grid[56][34].start(grey, 0)
    grid[56][34].barrier = True
    grid[56][33].start(grey, 0)
    grid[56][33].barrier = True


    grid[57][30].start(grey, 0)
    grid[57][30].barrier = True
    grid[57][31].start(grey, 0)
    grid[57][31].barrier = True
    grid[58][31].start(grey, 0)
    grid[58][31].barrier = True
    grid[58][30].start(grey, 0)
    grid[58][30].barrier = True
    grid[59][30].start(grey, 0)
    grid[59][30].barrier = True
    grid[59][31].start(grey, 0)
    grid[59][31].barrier = True
    grid[58][29].start(grey, 0)
    grid[58][29].barrier = True

    grid[37][37].start(grey, 0)
    grid[37][37].barrier = True
    grid[37][37].start(grey, 0)
    grid[37][37].barrier = True
    grid[37][37].start(grey, 0)
    grid[37][37].barrier = True
    grid[38][37].start(grey, 0)
    grid[38][37].barrier = True
    grid[39][37].start(grey, 0)
    grid[39][37].barrier = True
    grid[41][37].start(grey, 0)
    grid[41][37].barrier = True
    grid[41][37].start(grey, 0)
    grid[41][37].barrier = True
    grid[40][37].start(grey, 0)
    grid[40][37].barrier = True
    grid[42][37].start(grey, 0)
    grid[42][37].barrier = True
    grid[43][37].start(grey, 0)
    grid[43][37].barrier = True
    grid[44][37].start(grey, 0)
    grid[44][37].barrier = True
    grid[45][37].start(grey, 0)
    grid[45][37].barrier = True
    grid[46][37].start(grey, 0)
    grid[46][37].barrier = True
    grid[47][37].start(grey, 0)
    grid[47][37].barrier = True
    grid[47][37].start(grey, 0)
    grid[47][37].barrier = True
    grid[48][37].start(grey, 0)
    grid[48][37].barrier = True
    grid[49][37].start(grey, 0)
    grid[49][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[51][37].start(grey, 0)
    grid[51][37].barrier = True
    grid[52][37].start(grey, 0)
    grid[52][37].barrier = True
    grid[53][37].start(grey, 0)
    grid[53][37].barrier = True
    grid[53][36].start(grey, 0)
    grid[53][36].barrier = True
    grid[54][36].start(grey, 0)
    grid[54][36].barrier = True
    grid[54][35].start(grey, 0)
    grid[54][35].barrier = True
    grid[54][34].start(grey, 0)
    grid[54][34].barrier = True
    grid[54][33].start(grey, 0)
    grid[54][33].barrier = True
    grid[54][32].start(grey, 0)
    grid[54][32].barrier = True
    grid[54][31].start(grey, 0)
    grid[54][31].barrier = True
    grid[54][30].start(grey, 0)
    grid[54][30].barrier = True
    grid[53][28].start(grey, 0)
    grid[53][28].barrier = True
    grid[53][28].start(grey, 0)
    grid[53][28].barrier = True
    grid[53][27].start(grey, 0)
    grid[53][27].barrier = True
    grid[52][26].start(grey, 0)
    grid[52][26].barrier = True
    grid[51][25].start(grey, 0)
    grid[51][25].barrier = True

    grid[51][25].barrier = True
    grid[51][25].start(grey, 0)
    grid[51][25].barrier = True
    grid[51][24].start(grey, 0)
    grid[51][24].barrier = True
    grid[50][24].start(grey, 0)
    grid[50][24].barrier = True
    grid[51][24].start(grey, 0)
    grid[51][24].barrier = True
    grid[51][24].start(grey, 0)
    grid[51][24].barrier = True
    grid[51][24].start(grey, 0)
    grid[51][24].barrier = True
    grid[50][23].start(grey, 0)
    grid[50][23].barrier = True
    grid[50][22].start(grey, 0)
    grid[50][22].barrier = True
    grid[50][21].start(grey, 0)
    grid[50][21].barrier = True
    grid[49][21].start(grey, 0)
    grid[49][21].barrier = True
    grid[49][20].start(grey, 0)
    grid[49][20].barrier = True
    grid[48][19].start(grey, 0)
    grid[48][19].barrier = True
    grid[47][19].start(grey, 0)
    grid[47][19].barrier = True
    grid[46][19].start(grey, 0)
    grid[46][19].barrier = True
    grid[45][20].start(grey, 0)
    grid[45][20].barrier = True
    grid[45][21].start(grey, 0)
    grid[45][21].barrier = True
    grid[45][22].start(grey, 0)
    grid[45][22].barrier = True
    grid[45][22].start(grey, 0)
    grid[45][22].barrier = True
    grid[45][24].start(grey, 0)
    grid[45][24].barrier = True
    grid[46][25].start(grey, 0)
    grid[46][25].barrier = True
    grid[47][26].start(grey, 0)
    grid[47][26].barrier = True
    grid[48][26].start(grey, 0)
    grid[48][26].barrier = True
    grid[49][26].start(grey, 0)
    grid[49][26].barrier = True
    grid[50][27].start(grey, 0)
    grid[50][27].barrier = True
    grid[51][28].start(grey, 0)
    grid[51][28].barrier = True
    grid[51][29].start(grey, 0)
    grid[51][29].barrier = True
    grid[51][30].start(grey, 0)
    grid[51][30].barrier = True
    grid[51][31].start(grey, 0)
    grid[51][31].barrier = True
    grid[51][32].start(grey, 0)
    grid[51][32].barrier = True
    grid[51][33].start(grey, 0)
    grid[51][33].barrier = True
    grid[51][33].start(grey, 0)
    grid[51][33].barrier = True
    grid[51][34].start(grey, 0)
    grid[51][34].barrier = True
    grid[51][35].start(grey, 0)
    grid[51][35].barrier = True

    grid[47][21].start(grey, 0)
    grid[47][21].barrier = True
    grid[47][21].start(grey, 0)
    grid[47][21].barrier = True
    grid[47][22].start(grey, 0)
    grid[47][22].barrier = True
    grid[47][24].start(grey, 0)
    grid[47][24].barrier = True

    grid[46][35].start(grey, 0)
    grid[46][35].barrier = True
    grid[46][35].start(grey, 0)
    grid[46][35].barrier = True
    grid[46][35].start(grey, 0)
    grid[46][35].barrier = True
    grid[46][35].start(grey, 0)
    grid[46][35].barrier = True
    grid[46][34].start(grey, 0)
    grid[46][34].barrier = True
    grid[46][33].start(grey, 0)
    grid[46][33].barrier = True
    grid[47][33].start(grey, 0)
    grid[47][33].barrier = True
    grid[48][33].start(grey, 0)
    grid[48][33].barrier = True
    grid[49][33].start(grey, 0)
    grid[49][33].barrier = True
    grid[50][33].start(grey, 0)
    grid[50][33].barrier = True
    grid[51][33].start(grey, 0)
    grid[51][33].barrier = True
    grid[51][34].start(grey, 0)
    grid[51][34].barrier = True
    grid[51][35].start(grey, 0)
    grid[51][35].barrier = True
    grid[50][35].start(grey, 0)
    grid[50][35].barrier = True
    grid[49][35].start(grey, 0)
    grid[49][35].barrier = True
    grid[48][35].start(grey, 0)
    grid[48][35].barrier = True
    grid[47][35].start(grey, 0)
    grid[47][35].barrier = True
    grid[46][35].start(grey, 0)
    grid[46][35].barrier = True
    grid[45][35].start(grey, 0)
    grid[45][35].barrier = True
    grid[44][35].start(grey, 0)
    grid[44][35].barrier = True
    grid[44][34].start(grey, 0)
    grid[44][34].barrier = True
    grid[44][33].start(grey, 0)
    grid[44][33].barrier = True
    grid[44][33].start(grey, 0)
    grid[44][33].barrier = True
    grid[44][32].start(grey, 0)
    grid[44][32].barrier = True
    grid[43][32].start(grey, 0)
    grid[43][32].barrier = True
    grid[43][31].start(grey, 0)
    grid[43][31].barrier = True
    grid[43][30].start(grey, 0)
    grid[43][30].barrier = True
    grid[42][30].start(grey, 0)
    grid[42][30].barrier = True
    grid[41][30].start(grey, 0)
    grid[41][30].barrier = True
    grid[41][31].start(grey, 0)
    grid[41][31].barrier = True
    grid[41][32].start(grey, 0)
    grid[41][32].barrier = True
    grid[41][33].start(grey, 0)
    grid[41][33].barrier = True
    grid[41][34].start(grey, 0)
    grid[41][34].barrier = True
    grid[41][35].start(grey, 0)
    grid[41][35].barrier = True
    grid[42][35].start(grey, 0)
    grid[42][35].barrier = True
    grid[43][35].start(grey, 0)
    grid[43][35].barrier = True
    grid[44][35].start(grey, 0)
    grid[44][35].barrier = True


    grid[36][30].start(grey, 0)
    grid[36][30].barrier = True
    grid[36][30].start(grey, 0)
    grid[36][30].barrier = True
    grid[37][30].start(grey, 0)
    grid[37][30].barrier = True
    grid[38][30].start(grey, 0)
    grid[38][30].barrier = True
    grid[36][31].start(grey, 0)
    grid[36][31].barrier = True
    grid[37][31].start(grey, 0)
    grid[37][31].barrier = True
    grid[38][31].start(grey, 0)
    grid[38][31].barrier = True
    grid[39][31].start(grey, 0)
    grid[39][31].barrier = True
    grid[39][32].start(grey, 0)
    grid[39][32].barrier = True
    grid[38][32].start(grey, 0)
    grid[38][32].barrier = True
    grid[37][32].start(grey, 0)
    grid[37][32].barrier = True
    grid[36][32].start(grey, 0)
    grid[36][32].barrier = True
    grid[39][33].start(grey, 0)
    grid[39][33].barrier = True
    grid[39][34].start(grey, 0)
    grid[39][34].barrier = True
    grid[39][35].start(grey, 0)
    grid[39][35].barrier = True
    grid[38][35].start(grey, 0)
    grid[38][35].barrier = True
    grid[37][35].start(grey, 0)
    grid[37][35].barrier = True
    grid[36][35].start(grey, 0)
    grid[36][35].barrier = True
    grid[35][36].start(grey, 0)
    grid[35][36].barrier = True
    grid[34][36].start(grey, 0)
    grid[34][36].barrier = True
    grid[34][35].start(grey, 0)
    grid[34][35].barrier = True
    grid[34][34].start(grey, 0)
    grid[34][34].barrier = True
    grid[34][33].start(grey, 0)
    grid[34][33].barrier = True
    grid[34][33].start(grey, 0)
    grid[34][33].barrier = True
    grid[34][32].start(grey, 0)
    grid[34][32].barrier = True
    grid[34][31].start(grey, 0)
    grid[34][31].barrier = True
    grid[34][30].start(grey, 0)
    grid[34][30].barrier = True
    grid[34][29].start(grey, 0)
    grid[34][29].barrier = True
    grid[34][28].start(grey, 0)
    grid[34][28].barrier = True
    grid[34][27].start(grey, 0)
    grid[34][27].barrier = True
    grid[34][26].start(grey, 0)
    grid[34][26].barrier = True
    grid[34][25].start(grey, 0)
    grid[34][25].barrier = True
    grid[34][24].start(grey, 0)
    grid[34][24].barrier = True
    grid[34][23].start(grey, 0)
    grid[34][23].barrier = True
    grid[34][22].start(grey, 0)
    grid[34][22].barrier = True
    grid[33][22].start(grey, 0)
    grid[33][22].barrier = True
    grid[33][21].start(grey, 0)
    grid[33][21].barrier = True
    grid[33][20].start(grey, 0)
    grid[33][20].barrier = True
    grid[33][19].start(grey, 0)
    grid[33][19].barrier = True
    grid[33][18].start(grey, 0)
    grid[33][18].barrier = True
    grid[33][17].start(grey, 0)
    grid[33][17].barrier = True
    grid[33][17].start(grey, 0)
    grid[33][17].barrier = True
    grid[33][16].start(grey, 0)
    grid[33][16].barrier = True
    grid[33][15].start(grey, 0)
    grid[33][15].barrier = True
    grid[33][14].start(grey, 0)
    grid[33][14].barrier = True
    grid[34][13].start(grey, 0)
    grid[34][13].barrier = True
    grid[35][12].start(grey, 0)
    grid[35][12].barrier = True
    grid[36][11].start(grey, 0)
    grid[36][11].barrier = True
    grid[36][10].start(grey, 0)
    grid[36][10].barrier = True


    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][7].start(grey, 0)
    grid[37][7].barrier = True
    grid[37][6].start(grey, 0)
    grid[37][6].barrier = True
    grid[37][7].start(grey, 0)
    grid[37][7].barrier = True
    grid[37][6].start(grey, 0)
    grid[37][6].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][9].start(grey, 0)
    grid[37][9].barrier = True
    grid[37][8].start(grey, 0)
    grid[37][8].barrier = True
    grid[38][8].start(grey, 0)
    grid[38][8].barrier = True
    grid[39][8].start(grey, 0)
    grid[39][8].barrier = True
    grid[40][8].start(grey, 0)
    grid[40][8].barrier = True
    grid[41][8].start(grey, 0)
    grid[41][8].barrier = True
    grid[41][8].start(grey, 0)
    grid[41][8].barrier = True
    grid[42][8].start(grey, 0)
    grid[42][8].barrier = True
    grid[42][8].start(grey, 0)
    grid[42][8].barrier = True
    grid[43][8].start(grey, 0)
    grid[43][8].barrier = True
    grid[44][8].start(grey, 0)
    grid[44][8].barrier = True
    grid[45][8].start(grey, 0)
    grid[45][8].barrier = True
    grid[46][8].start(grey, 0)
    grid[46][8].barrier = True
    grid[47][8].start(grey, 0)
    grid[47][8].barrier = True
    grid[48][8].start(grey, 0)
    grid[48][8].barrier = True
    grid[49][8].start(grey, 0)
    grid[49][8].barrier = True
    grid[49][8].start(grey, 0)
    grid[49][8].barrier = True
    grid[49][8].start(grey, 0)
    grid[49][8].barrier = True
    grid[50][8].start(grey, 0)
    grid[50][8].barrier = True
    grid[50][9].start(grey, 0)
    grid[50][9].barrier = True
    grid[50][10].start(grey, 0)
    grid[50][10].barrier = True
    grid[50][10].start(grey, 0)
    grid[50][10].barrier = True
    grid[51][10].start(grey, 0)
    grid[51][10].barrier = True
    grid[51][11].start(grey, 0)
    grid[51][11].barrier = True
    grid[52][11].start(grey, 0)
    grid[52][11].barrier = True
    grid[52][12].start(grey, 0)
    grid[52][12].barrier = True
    grid[53][12].start(grey, 0)
    grid[53][12].barrier = True
    grid[53][13].start(grey, 0)
    grid[53][13].barrier = True
    grid[53][14].start(grey, 0)
    grid[53][14].barrier = True
    grid[54][15].start(grey, 0)
    grid[54][15].barrier = True
    grid[55][16].start(grey, 0)
    grid[55][16].barrier = True
    grid[56][17].start(grey, 0)
    grid[56][17].barrier = True
    grid[57][18].start(grey, 0)
    grid[57][18].barrier = True
    grid[58][19].start(grey, 0)
    grid[58][19].barrier = True
    grid[59][20].start(grey, 0)
    grid[59][20].barrier = True
    grid[60][21].start(grey, 0)
    grid[60][21].barrier = True
    grid[61][22].start(grey, 0)
    grid[61][22].barrier = True
    grid[61][23].start(grey, 0)
    grid[61][23].barrier = True
    grid[62][23].start(grey, 0)
    grid[62][23].barrier = True
    grid[62][24].start(grey, 0)
    grid[62][24].barrier = True
    grid[63][25].start(grey, 0)
    grid[63][25].barrier = True
    grid[63][26].start(grey, 0)
    grid[63][26].barrier = True
    grid[63][27].start(grey, 0)
    grid[63][27].barrier = True
    grid[64][27].start(grey, 0)
    grid[64][27].barrier = True
    grid[64][27].start(grey, 0)
    grid[64][27].barrier = True
    grid[64][28].start(grey, 0)
    grid[64][28].barrier = True
    grid[64][29].start(grey, 0)
    grid[64][29].barrier = True
    grid[65][29].start(grey, 0)
    grid[65][29].barrier = True
    grid[65][29].start(grey, 0)
    grid[65][29].barrier = True
    grid[66][30].start(grey, 0)
    grid[66][30].barrier = True
    grid[66][30].start(grey, 0)
    grid[66][30].barrier = True
    grid[66][30].start(grey, 0)
    grid[66][30].barrier = True
    grid[66][30].start(grey, 0)
    grid[66][30].barrier = True
    grid[66][31].start(grey, 0)
    grid[66][31].barrier = True
    grid[66][32].start(grey, 0)
    grid[66][32].barrier = True
    grid[67][33].start(grey, 0)
    grid[67][33].barrier = True
    grid[67][33].start(grey, 0)
    grid[67][33].barrier = True
    grid[67][34].start(grey, 0)
    grid[67][34].barrier = True
    grid[67][35].start(grey, 0)
    grid[67][35].barrier = True
    grid[68][36].start(grey, 0)
    grid[68][36].barrier = True
    grid[68][37].start(grey, 0)
    grid[68][37].barrier = True
    grid[68][37].start(grey, 0)
    grid[68][37].barrier = True
    grid[69][37].start(grey, 0)
    grid[69][37].barrier = True


    grid[43][10].start(grey, 0)
    grid[43][10].barrier = True
    grid[43][10].start(grey, 0)
    grid[43][10].barrier = True
    grid[43][10].start(grey, 0)
    grid[43][10].barrier = True
    grid[44][10].start(grey, 0)
    grid[44][10].barrier = True
    grid[44][11].start(grey, 0)
    grid[44][11].barrier = True
    grid[43][11].start(grey, 0)
    grid[43][11].barrier = True
    grid[43][12].start(grey, 0)
    grid[43][12].barrier = True
    grid[44][12].start(grey, 0)
    grid[44][12].barrier = True

    grid[36][14].start(grey, 0)
    grid[36][14].barrier = True
    grid[36][14].start(grey, 0)
    grid[36][14].barrier = True
    grid[37][14].start(grey, 0)
    grid[37][14].barrier = True
    grid[38][14].start(grey, 0)
    grid[38][14].barrier = True
    grid[38][15].start(grey, 0)
    grid[38][15].barrier = True
    grid[37][15].start(grey, 0)
    grid[37][15].barrier = True
    grid[36][15].start(grey, 0)
    grid[36][15].barrier = True


    grid[40][14].start(grey, 0)
    grid[40][14].barrier = True
    grid[41][14].start(grey, 0)
    grid[41][14].barrier = True
    grid[41][15].start(grey, 0)
    grid[41][15].barrier = True
    grid[40][15].start(grey, 0)
    grid[40][15].barrier = True


    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True
    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True
    grid[38][19].start(grey, 0)
    grid[38][19].barrier = True
    grid[38][20].start(grey, 0)
    grid[38][20].barrier = True
    grid[38][21].start(grey, 0)
    grid[38][21].barrier = True
    grid[39][21].start(grey, 0)
    grid[39][21].barrier = True
    grid[40][21].start(grey, 0)
    grid[40][21].barrier = True
    grid[41][21].start(grey, 0)
    grid[41][21].barrier = True
    grid[42][21].start(grey, 0)
    grid[42][21].barrier = True
    grid[43][21].start(grey, 0)
    grid[43][21].barrier = True
    grid[43][20].start(grey, 0)
    grid[43][20].barrier = True
    grid[43][19].start(grey, 0)
    grid[43][19].barrier = True
    grid[43][18].start(grey, 0)
    grid[43][18].barrier = True
    grid[42][18].start(grey, 0)
    grid[42][18].barrier = True
    grid[41][18].start(grey, 0)
    grid[41][18].barrier = True
    grid[40][18].start(grey, 0)
    grid[40][18].barrier = True
    grid[39][18].start(grey, 0)
    grid[39][18].barrier = True
    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True
    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True
    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True
    grid[38][19].start(grey, 0)
    grid[38][19].barrier = True
    grid[38][20].start(grey, 0)
    grid[38][20].barrier = True
    grid[38][20].start(grey, 0)
    grid[38][20].barrier = True
    grid[39][21].start(grey, 0)
    grid[39][21].barrier = True
    grid[40][21].start(grey, 0)
    grid[40][21].barrier = True
    grid[41][21].start(grey, 0)
    grid[41][21].barrier = True
    grid[42][21].start(grey, 0)
    grid[42][21].barrier = True
    grid[43][21].start(grey, 0)
    grid[43][21].barrier = True
    grid[43][20].start(grey, 0)
    grid[43][20].barrier = True
    grid[43][19].start(grey, 0)
    grid[43][19].barrier = True
    grid[43][18].start(grey, 0)
    grid[43][18].barrier = True
    grid[42][18].start(grey, 0)
    grid[42][18].barrier = True
    grid[41][18].start(grey, 0)
    grid[41][18].barrier = True
    grid[40][18].start(grey, 0)
    grid[40][18].barrier = True
    grid[39][18].start(grey, 0)
    grid[39][18].barrier = True
    grid[38][18].start(grey, 0)
    grid[38][18].barrier = True


    grid[56][12].start(grey, 0)
    grid[56][12].barrier = True
    grid[56][12].start(grey, 0)
    grid[56][12].barrier = True
    grid[56][12].start(grey, 0)
    grid[56][12].barrier = True
    grid[56][13].start(grey, 0)
    grid[56][13].barrier = True
    grid[56][14].start(grey, 0)
    grid[56][14].barrier = True
    grid[57][15].start(grey, 0)
    grid[57][15].barrier = True
    grid[58][16].start(grey, 0)
    grid[58][16].barrier = True
    grid[58][16].start(grey, 0)
    grid[58][16].barrier = True
    grid[59][17].start(grey, 0)
    grid[59][17].barrier = True
    grid[60][18].start(grey, 0)
    grid[60][18].barrier = True
    grid[61][19].start(grey, 0)
    grid[61][19].barrier = True
    grid[61][19].start(grey, 0)
    grid[61][19].barrier = True
    grid[62][20].start(grey, 0)
    grid[62][20].barrier = True
    grid[62][20].start(grey, 0)
    grid[62][20].barrier = True
    grid[62][20].start(grey, 0)
    grid[62][20].barrier = True
    grid[63][21].start(grey, 0)
    grid[63][21].barrier = True
    grid[64][22].start(grey, 0)
    grid[64][22].barrier = True
    grid[65][22].start(grey, 0)
    grid[65][22].barrier = True
    grid[65][23].start(grey, 0)
    grid[65][23].barrier = True
    grid[65][24].start(grey, 0)
    grid[65][24].barrier = True
    grid[66][25].start(grey, 0)
    grid[66][25].barrier = True
    grid[67][26].start(grey, 0)
    grid[67][26].barrier = True
    grid[67][26].start(grey, 0)
    grid[67][26].barrier = True
    grid[67][27].start(grey, 0)
    grid[67][27].barrier = True
    grid[68][28].start(grey, 0)
    grid[68][28].barrier = True
    grid[68][29].start(grey, 0)
    grid[68][29].barrier = True
    grid[69][29].start(grey, 0)
    grid[69][29].barrier = True


    grid[56][12].start(grey, 0)
    grid[56][12].barrier = True
    grid[57][12].start(grey, 0)
    grid[57][12].barrier = True
    grid[58][12].start(grey, 0)
    grid[58][12].barrier = True
    grid[59][12].start(grey, 0)
    grid[59][12].barrier = True
    grid[60][12].start(grey, 0)
    grid[60][12].barrier = True
    grid[61][12].start(grey, 0)
    grid[61][12].barrier = True
    grid[62][12].start(grey, 0)
    grid[62][12].barrier = True
    grid[63][12].start(grey, 0)
    grid[63][12].barrier = True
    grid[64][12].start(grey, 0)
    grid[64][12].barrier = True
    grid[65][12].start(grey, 0)
    grid[65][12].barrier = True
    grid[66][12].start(grey, 0)
    grid[66][12].barrier = True
    grid[67][12].start(grey, 0)
    grid[67][12].barrier = True
    grid[68][12].start(grey, 0)
    grid[68][12].barrier = True
    grid[69][12].start(grey, 0)
    grid[69][12].barrier = True

    grid[54][10].start(grey, 0)
    grid[54][10].barrier = True
    grid[54][9].start(grey, 0)
    grid[54][9].barrier = True
    grid[53][8].start(grey, 0)
    grid[53][8].barrier = True
    grid[53][7].start(grey, 0)
    grid[53][7].barrier = True
    grid[53][6].start(grey, 0)
    grid[53][6].barrier = True
    grid[52][6].start(grey, 0)
    grid[52][6].barrier = True
    grid[52][5].start(grey, 0)
    grid[52][5].barrier = True
    grid[51][5].start(grey, 0)
    grid[51][5].barrier = True
    grid[51][4].start(grey, 0)
    grid[51][4].barrier = True
    grid[51][3].start(grey, 0)
    grid[51][3].barrier = True
    grid[50][3].start(grey, 0)
    grid[50][3].barrier = True
    grid[50][2].start(grey, 0)
    grid[50][2].barrier = True
    grid[49][1].start(grey, 0)
    grid[49][1].barrier = True
    grid[49][0].start(grey, 0)
    grid[49][0].barrier = True

    grid[57][9].start(grey, 0)
    grid[57][9].barrier = True
    grid[57][9].start(grey, 0)
    grid[57][9].barrier = True
    grid[57][9].start(grey, 0)
    grid[57][9].barrier = True
    grid[57][8].start(grey, 0)
    grid[57][8].barrier = True
    grid[57][7].start(grey, 0)
    grid[57][7].barrier = True
    grid[58][7].start(grey, 0)
    grid[58][7].barrier = True
    grid[59][7].start(grey, 0)
    grid[59][7].barrier = True
    grid[60][7].start(grey, 0)
    grid[60][7].barrier = True
    grid[61][7].start(grey, 0)
    grid[61][7].barrier = True
    grid[61][8].start(grey, 0)
    grid[61][8].barrier = True
    grid[61][9].start(grey, 0)
    grid[61][9].barrier = True
    grid[63][9].start(grey, 0)
    grid[63][9].barrier = True
    grid[63][8].start(grey, 0)
    grid[63][8].barrier = True
    grid[63][7].start(grey, 0)
    grid[63][7].barrier = True
    grid[64][7].start(grey, 0)
    grid[64][7].barrier = True
    grid[65][7].start(grey, 0)
    grid[65][7].barrier = True
    grid[65][7].start(grey, 0)
    grid[65][7].barrier = True
    grid[66][7].start(grey, 0)
    grid[66][7].barrier = True
    grid[66][8].start(grey, 0)
    grid[66][8].barrier = True
    grid[66][8].start(grey, 0)
    grid[66][8].barrier = True
    grid[66][9].start(grey, 0)
    grid[66][9].barrier = True
    grid[66][10].start(grey, 0)
    grid[66][10].barrier = True


    grid[59][3].start(grey, 0)
    grid[59][3].barrier = True
    grid[59][3].start(grey, 0)
    grid[59][3].barrier = True
    grid[59][3].start(grey, 0)
    grid[59][3].barrier = True
    grid[60][3].start(grey, 0)
    grid[60][3].barrier = True
    grid[61][3].start(grey, 0)
    grid[61][3].barrier = True
    grid[61][4].start(grey, 0)
    grid[61][4].barrier = True
    grid[61][5].start(grey, 0)
    grid[61][5].barrier = True
    grid[60][5].start(grey, 0)
    grid[60][5].barrier = True
    grid[59][5].start(grey, 0)
    grid[59][5].barrier = True
    grid[59][4].start(grey, 0)
    grid[59][4].barrier = True

    grid[66][2].start(grey, 0)
    grid[66][2].barrier = True
    grid[66][2].start(grey, 0)
    grid[66][2].barrier = True
    grid[67][2].start(grey, 0)
    grid[67][2].barrier = True
    grid[68][2].start(grey, 0)
    grid[68][2].barrier = True
    grid[69][2].start(grey, 0)
    grid[69][2].barrier = True
    grid[69][3].start(grey, 0)
    grid[69][3].barrier = True
    grid[69][4].start(grey, 0)
    grid[69][4].barrier = True
    grid[69][5].start(grey, 0)
    grid[69][5].barrier = True
    grid[68][5].start(grey, 0)
    grid[68][5].barrier = True
    grid[67][5].start(grey, 0)
    grid[67][5].barrier = True
    grid[66][5].start(grey, 0)
    grid[66][5].barrier = True
    grid[66][4].start(grey, 0)
    grid[66][4].barrier = True
    grid[66][3].start(grey, 0)
    grid[66][3].barrier = True

    grid[54][2].start(grey, 0)
    grid[54][2].barrier = True
    grid[54][2].start(grey, 0)
    grid[54][2].barrier = True
    grid[54][1].start(grey, 0)
    grid[54][1].barrier = True
    grid[55][1].start(grey, 0)
    grid[55][1].barrier = True
    grid[55][2].start(grey, 0)
    grid[55][2].barrier = True
    grid[56][2].start(grey, 0)
    grid[56][2].barrier = True
    grid[56][1].start(grey, 0)
    grid[56][1].barrier = True
    grid[57][1].start(grey, 0)
    grid[57][1].barrier = True
    grid[57][2].start(grey, 0)
    grid[57][2].barrier = True
    grid[58][1].start(grey, 0)
    grid[58][1].barrier = True
    grid[58][0].start(grey, 0)
    grid[58][0].barrier = True
    grid[57][0].start(grey, 0)
    grid[57][0].barrier = True
    grid[56][0].start(grey, 0)
    grid[56][0].barrier = True
    grid[55][0].start(grey, 0)
    grid[55][0].barrier = True


    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[46][1].start(grey, 0)
    grid[46][1].barrier = True
    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[46][0].start(grey, 0)
    grid[46][0].barrier = True
    grid[46][1].start(grey, 0)
    grid[46][1].barrier = True
    grid[46][2].start(grey, 0)
    grid[46][2].barrier = True
    grid[47][2].start(grey, 0)
    grid[47][2].barrier = True
    grid[47][3].start(grey, 0)
    grid[47][3].barrier = True
    grid[47][3].start(grey, 0)
    grid[47][3].barrier = True
    grid[47][4].start(grey, 0)
    grid[47][4].barrier = True
    grid[47][5].start(grey, 0)
    grid[47][5].barrier = True
    grid[47][6].start(grey, 0)
    grid[47][6].barrier = True
    grid[46][6].start(grey, 0)
    grid[46][6].barrier = True
    grid[45][6].start(grey, 0)
    grid[45][6].barrier = True
    grid[44][6].start(grey, 0)
    grid[44][6].barrier = True
    grid[43][6].start(grey, 0)
    grid[43][6].barrier = True
    grid[42][6].start(grey, 0)
    grid[42][6].barrier = True
    grid[42][5].start(grey, 0)
    grid[42][5].barrier = True
    grid[42][4].start(grey, 0)
    grid[42][4].barrier = True
    grid[41][3].start(grey, 0)
    grid[41][3].barrier = True
    grid[40][4].start(grey, 0)
    grid[40][4].barrier = True
    grid[40][5].start(grey, 0)
    grid[40][5].barrier = True
    grid[40][6].start(grey, 0)
    grid[40][6].barrier = True
    grid[39][6].start(grey, 0)
    grid[39][6].barrier = True
    grid[38][6].start(grey, 0)
    grid[38][6].barrier = True
    grid[36][6].start(grey, 0)
    grid[36][6].barrier = True
    grid[36][6].start(grey, 0)
    grid[36][6].barrier = True
    grid[36][5].start(grey, 0)
    grid[36][5].barrier = True
    grid[36][5].start(grey, 0)
    grid[36][5].barrier = True
    grid[36][4].start(grey, 0)
    grid[36][4].barrier = True
    grid[36][4].start(grey, 0)
    grid[36][4].barrier = True
    grid[35][7].start(grey, 0)
    grid[35][7].barrier = True
    grid[35][7].start(grey, 0)
    grid[35][7].barrier = True
    grid[34][8].start(grey, 0)
    grid[34][8].barrier = True
    grid[33][7].start(grey, 0)
    grid[33][7].barrier = True
    grid[32][7].start(grey, 0)
    grid[32][7].barrier = True
    grid[31][7].start(grey, 0)
    grid[31][7].barrier = True
    grid[30][7].start(grey, 0)
    grid[30][7].barrier = True
    grid[30][8].start(grey, 0)
    grid[30][8].barrier = True
    grid[30][9].start(grey, 0)
    grid[30][9].barrier = True
    grid[30][9].start(grey, 0)
    grid[30][9].barrier = True
    grid[30][10].start(grey, 0)
    grid[30][10].barrier = True
    grid[30][11].start(grey, 0)
    grid[30][11].barrier = True
    grid[31][11].start(grey, 0)
    grid[31][11].barrier = True
    grid[31][12].start(grey, 0)
    grid[31][12].barrier = True
    grid[31][13].start(grey, 0)
    grid[31][13].barrier = True
    grid[30][14].start(grey, 0)
    grid[30][14].barrier = True
    grid[29][15].start(grey, 0)
    grid[29][15].barrier = True


def onclick():
    global start
    global end
    sta = start_box.get().split(',')
    en_ = end_box.get().split(',')
    start = grid[int(sta[0])][int(sta[1])]
    end = grid[int(en_[0])][int(en_[1])]
    window_tk.quit()  # imp otherwise
    window_tk.destroy()


window_tk = Tk()
label = Label(window_tk, text='start(x,y)--> ')
start_box = Entry(window_tk)
new_label = Label(window_tk, text='endpos(x,y)->: ')
end_box = Entry(window_tk)


submit = Button(window_tk, text='Click Me', command=onclick)  # onclick fnctn

submit.grid(columnspan=3, row=3)
new_label.grid(row=1, pady=4)
end_box.grid(row=1, column=1, pady=4)
start_box.grid(row=0, column=1, pady=4)
label.grid(row=0, pady=4)

window_tk.update()
mainloop()

pygame.init()
openlist.append(start)  # add the start node


end.start(green, 0)
start.start(red, 0)

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # RETURN COMMAND TO RUNN
                loop = False
                break

for i in range(cols):
    for j in range(rows):
        grid[i][j].update_neighbour(grid)


def heurestic_fn(a, b):

    distance = math.sqrt((a.i - b.i)**2 + (a.j - b.j)**2)
    return distance


def main():
    end.start(lightgr, 0)
    # lowest is the current index
    while len(openlist) > 0:  # while destination is not reached
        lowestIndex = 0  # get the current node
        for i in range(len(openlist)):  # consider node with lowest f score
            if openlist[i].f < openlist[lowestIndex].f:
                lowestIndex = i

        # current is the lowest value as of now
        current = openlist[lowestIndex]
        if current == end:  # if its a final node
            print('done', current.f)  # stop algo
            start.start(red, 0)
            tempg = current.f  # temp is the current here
            for i in range(round(current.f)):  # putting current in closed list
                # while current is not the none
                current.closed = False  # add the current position
                current.start(blue, 0)
                current = current.previous  # previous node
            end.start(lightgr, 0)
            # if program executed show up message

            result = messagebox.askokcancel('program', ("executed"))
            if result == True:
                os.execl(sys.executable, sys.executable, *sys.argv)

            pygame.quit()
        # pushing and poping is done simultaenously to check node is done or not
        openlist.pop(lowestIndex)  # poping is done here
        closedlist.append(current)
# we can say neighbour or children
# neighbours=[]
        # setting neighbour of current node
        neighbors = current.neighbors

        for i in range(len(neighbors)):
            neighbor = neighbors[i]  # getting all the position neighbours
            # if its not in closed list  its in openlist (a)
            if neighbor not in closedlist:
                tempg = current.g + current.value  # temg g to calc the current position
                if neighbor in openlist:  # for open list
                    if neighbor.g > tempg:
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    # (a ) part here means neighbour is in openlist
                    openlist.append(neighbor)
                # calc the f,g,h values
            neighbor.h = heurestic_fn(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            # now this goes on till it find its path and checking neighbour updated value
            if neighbor.previous == None:
                neighbor.previous = current

    current.closed = True


while True:

    pygame.display.update()
    main()
