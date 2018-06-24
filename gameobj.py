import pygame
pygame.init()

charImg_left = pygame.image.load('chars_left.png')
charImg_right = pygame.image.load('chars_right.png')

game_width = 800
game_height = 600

clock = pygame.time.Clock()

white = (255,255,255)

gameDisplay = pygame.display.set_mode((game_width, game_height))

x = game_width * 0.5
y = game_height * 0.8



class gamelog:

    # Sprite saver
    imgload = charImg_right

    # Movement changes
    x_change = 0
    y_change = 0

    # Initializes objects for use
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self. y = y
        self.jumping = False
        self.jumpcount = 10
        self.negincr = -1

    # Window Display
    def windowDisplay(self, width_change, height_change):
        self.width_change = width_change
        self.height_change = height_change
        self.window = pygame.display.set_mode((width_change, height_change))
        return window

    # Changes window size
    def windowChange(self, width, height):
        self.width_change = self.width
        self.heighit_change = self.height

    # Changes sprites if wanted
    def spriteupdate(self, sprite):
        self.sprite = sprite
        self.a = a
        self.b = b
        self.imglog = pygame.image.load(sprite)


    # Movement on X axis
    def x_movement(self):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gamelog.x_change = 5
            if event.key == pygame.K_LEFT:
                gamelog.x_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                gamelog.x_change = 0



    def y_movement(self):



    # Orientation of sprite according to key pressed
    def char(self, x, y, sprita, spritb):
        self.x = x
        self.y = y
        self.sprita = sprita
        self.spritb = spritb
        gameDisplay.blit(gamelog.imgload,(x,y))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gameDisplay.blit(spritb,(x,y))
                gamelog.imgload = spritb

            if event.key == pygame.K_RIGHT:
                gameDisplay.blit(sprita,(x,y))
                gamelog.imgload = sprita

        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT:
                gameDisplay.blit(spritb,(x,y))

            if event.type == pygame.K_RIGHT:
                gameDisplay.blit(sprita,(x,y))



# Instance of class gamelog
start = gamelog(0,0,800,600)

cond = False

# Game loop
while not cond:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = True

        print(event)
    gameDisplay.fill(white)
    start.x_movement()
    start.char(x, y, charImg_right, charImg_left)

    x += start.x_change

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
