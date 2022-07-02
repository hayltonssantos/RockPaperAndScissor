from util import *
from util import sprites

class Iniciar:
    screen = pygame.display.set_mode((600,600))
    screen.fill((0,0,0))
    
    pygame.font.init()
    jogoFonte = pygame.font.Font(None, 25)
    textVs = jogoFonte.render('VS',True,(255,255,255))
    textRectVs = textVs.get_rect()
    textRectVs.center = (300,150)
    
    textCpu = jogoFonte.render('CPU',True,(255,255,255))
    textRectCpu = textCpu.get_rect()
    textRectCpu.center = (150,80)
    
    textPlayer = jogoFonte.render('Player',True,(255,255,255))
    textRectPlayer = textPlayer.get_rect()
    textRectPlayer.center = (450,80)
    
    screen.blit(textCpu,textRectCpu)
    screen.blit(textPlayer,textRectPlayer)
    screen.blit(textVs,textRectVs)
    
    cpuPoint = 0
    playerPoint = 0

    def start():
        pygame.init()
        pygame.display.set_caption("Jogo")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
  
            sprites.Sprites()
            pygame.display.update()

if __name__ == "__main__":
    Iniciar().start()