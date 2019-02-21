import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600)) # set frame size

pygame.display.set_caption('A bit Racey') #give  caption for game (name)

clock = pygame.time.Clock() # import  clock

crashed = False


while not crashed:
    

    for event in pygame.event.get():
        
        # this will monitored list of event that are happing
        if event.type == pygame.QUIT:
            # exit game
            crashed = True
        print(event)
    pygame.display.update()

    clock.tick()
     
            

pygame.quit()
quit()
     
