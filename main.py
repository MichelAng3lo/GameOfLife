import pygame
width, height = 70, 70
block_size = 10
s_zywe = [2,3]
s_martwe =[3]
WIN = pygame.display.set_mode((width*block_size, height*block_size))
pygame.draw.rect(WIN, "white", (0, 0, width*block_size, height*block_size), 0)
grid = [[0 for i in range(width)]for j in range(height)]

grid[0][2] = 1
grid[1][2] = 1
grid[2][2] = 1
grid[1][0] = 1
grid[2][1] = 1
grid[2][3] = 1
grid[2][4] = 1
grid[2][5] = 1
grid[6][5] = 1
grid[7][5] = 1
grid[8][5] = 1
grid[5][5] = 1
grid[4][5] = 1


def count_neighbours(y,x):
    neighbours = 0
    for i in range(y-1, y+2):
        for j in range(x - 1, x + 2):
            if (i == y) & (x == j):
                pass
            elif (i == -1) | (i == height) | (j == -1) | (j == width):
                pass
            else:
                if grid[i][j] == 1:
                    neighbours += 1
    return neighbours


def create_next_grid():
    new_grid = [[0 for i in range(width)] for j in range(height)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbours = count_neighbours(i,j)
            if grid[i][j] == 1:
                if neighbours in s_zywe:
                    new_grid[i][j] = 1
            elif grid[i][j] == 0:
                if neighbours in s_martwe:
                    new_grid[i][j] = 1

    return new_grid


def show_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                pygame.draw.rect(WIN,"black",(j*block_size,i*block_size,block_size,block_size),0)
            else:
                pygame.draw.rect(WIN, "white", (j * block_size, i * block_size, block_size, block_size), 0)


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                pass
        pygame.display.update()
        show_grid()

        global grid
        grid = create_next_grid()

    pygame.quit()


if __name__ == "__main__":
    main()
