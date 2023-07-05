import pygame
import sys
import numpy as np
import random

# Initializes pygame
pygame.init()

# Constants
AI = 'X'
human = 'O'
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = (255, 255, 200)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (255, 66, 66)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# Console Board
board = np.empty([BOARD_ROWS, BOARD_COLS], dtype=str)

# Functions
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == human:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            if board[row][col] == AI:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def areEqual(a, b, c):
    return (a == b and b == c and a != '')

def check_winner():
    winner = 'N'
    # Check horizontally
    for i in range(0, 3):
        if areEqual(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
    # Check vertically
    for i in range(0, 3):
        if areEqual(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]
    # Check diagonally
    if areEqual(board[0][0], board[1][1], board[2][2]) or areEqual(board[0][2], board[1][1], board[2][0]):
        winner = board[1][1]
    emptyPlaces = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '':
                emptyPlaces += 1
    if winner == 'N' and emptyPlaces == 0:
        return 'Tie'
    else:
        return winner

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''
    draw_figures()

draw_lines()

# Variables
player = human
game_over = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player
                draw_figures()

                if check_winner() != 'N' or check_winner() == 'Tie':
                    game_over = True

                if not game_over:
                    if player == human:
                        player = AI
                        ai_move()
                        draw_figures()
                        if check_winner() != 'N' or check_winner() == 'Tie':
                            game_over = True
                        player = human

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                player = human
                restart()

    pygame.display.update()
