from unittest import result
from util import *
from util import startGame

class Sprites(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sizePiece = (110,110)
        self.spritesCpu()
        self.spritesPlayer()
        self.update()
        
    def spritesCpu(self):
        self.spritesCpu = []
        self.spritesCpu.append(pygame.image.load('./img/cpu/rock.png'))
        self.spritesCpu.append(pygame.image.load('./img/cpu/paper.png'))
        self.spritesCpu.append(pygame.image.load('./img/cpu/scissor.png'))
        
        self.rockCpu = pygame.transform.scale(self.spritesCpu[0], self.sizePiece)
        self.paperCpu = pygame.transform.scale(self.spritesCpu[1], self.sizePiece)
        self.scissorCpu = pygame.transform.scale(self.spritesCpu[2], self.sizePiece)
        
        x = 100
        y = 100
        
        self.rockCpuRect = self.rockCpu.get_rect()
        self.paperCpuRect = self.paperCpu.get_rect()
        self.scissorCpuRect = self.scissorCpu.get_rect()
        
        self.rockCpuRect.center = (x,y)
        self.paperCpuRect.center = (x + 100,y)
        self.scissorCpuRect.center = (x + 200,y)
    
    def spritesPlayer(self):
        self.spritesPlayer = []
        self.spritesPlayer.append(pygame.image.load('img/player/rock.png'))
        self.spritesPlayer.append(pygame.image.load('img/player/paper.png'))
        self.spritesPlayer.append(pygame.image.load('img/player/scissor.png'))
        
        self.rockPlayer = pygame.transform.scale(self.spritesPlayer[0], self.sizePiece)
        self.paperPlayer = pygame.transform.scale(self.spritesPlayer[1], self.sizePiece)
        self.scissorPlayer = pygame.transform.scale(self.spritesPlayer[2], self.sizePiece)
        
        xP = 150
        yP = 350
        
        self.rockPlayerRect = self.rockPlayer.get_rect()
        self.paperPlayerRect = self.paperPlayer.get_rect()
        self.scissorPlayerRect = self.scissorPlayer.get_rect()
        
        self.rockPlayerRect.center = (xP,yP)
        self.paperPlayerRect.center = (xP + 150,yP)
        self.scissorPlayerRect.center = (xP + 300,yP)
        
        startGame.Iniciar.screen.blit(self.rockPlayer, self.rockPlayerRect)
        startGame.Iniciar.screen.blit(self.paperPlayer, self.paperPlayerRect)
        startGame.Iniciar.screen.blit(self.scissorPlayer, self.scissorPlayerRect)
        
    
    def update(self):  
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    toCpu = random.randint(0,2)
                    toCpuPiece = ''
                    cpuPiece = ''
                    cpuPieceRect = 100,100
                    
                    toPlayerPiece = ''
                    playerPiece = ''
                    playerPieceRect = 400,100
                    
                    if toCpu == 0:
                        toCpuPiece = 'rock'
                        cpuPiece = self.rockCpu
                    elif toCpu == 1:
                        toCpuPiece = 'paper'
                        cpuPiece = self.paperCpu
                    elif toCpu == 2:
                        toCpuPiece = 'scissor'
                        cpuPiece = self.scissorCpu
                    
                    if self.rockPlayerRect.collidepoint(x,y):
                        toPlayerPiece = 'rock'
                        playerPiece = self.rockPlayer
                        
                    elif self.paperPlayerRect.collidepoint(x,y):
                        toPlayerPiece = 'paper'
                        playerPiece = self.paperPlayer
                        
                    elif self.scissorPlayerRect.collidepoint(x,y):
                        toPlayerPiece = 'scissor'
                        playerPiece = self.scissorPlayer
                    else:
                        break
                        
                    print(f'Player: {toPlayerPiece} --- CPU: {toCpuPiece}')
                    
                    textEnd = ''
                    
                    
                    if toPlayerPiece == toCpuPiece:
                        textEnd = 'Empate'
                    elif toPlayerPiece == 'rock' and toCpuPiece == 'paper':
                        textEnd = 'CPU ganhou'
                        startGame.Iniciar.cpuPoint += 1
                    elif toPlayerPiece == 'rock' and toCpuPiece == 'scissor':
                        textEnd = 'Player ganhou'
                        startGame.Iniciar.playerPoint += 1
                    elif toPlayerPiece == 'paper' and toCpuPiece == 'scissor':
                        textEnd = 'CPU ganhou'
                        startGame.Iniciar.cpuPoint += 1
                    elif toPlayerPiece == 'paper' and toCpuPiece == 'rock':
                        textEnd = 'Player ganhou'
                        startGame.Iniciar.playerPoint += 1
                    elif toPlayerPiece == 'scissor' and toCpuPiece == 'rock':
                        textEnd = 'CPU ganhou'
                        startGame.Iniciar.cpuPoint += 1
                    elif toPlayerPiece == 'scissor' and toCpuPiece == 'paper':
                        textEnd = 'Player ganhou'
                        startGame.Iniciar.playerPoint += 1
                    
                    self.resultGame(textEnd,cpuPiece,cpuPieceRect,playerPiece,playerPieceRect)
                    pygame.time.delay(500)
        
    def resultGame(self,textEnd,cpuPiece,cpuPieceRect,playerPiece,playerPieceRect):
        startGame.Iniciar.screen.blit(cpuPiece, cpuPieceRect)
        startGame.Iniciar.screen.blit(playerPiece, playerPieceRect)

        surface = startGame.Iniciar.screen 
        color = (0,0,0) 
        pygame.draw.rect(surface, color, pygame.Rect(0, 230, 600, 60)) 
        pygame.draw.rect(surface, color, pygame.Rect(0, 460, 600, 60)) 
        pygame.display.flip() 
        
        textEnded = startGame.Iniciar.jogoFonte.render(textEnd, True, (255,255,255))
        textRectEnded = textEnded.get_rect()
        textRectEnded.center = (300,250)
        
        textPoint = startGame.Iniciar.jogoFonte.render(f'Player: {startGame.Iniciar.playerPoint} --- CPU: {startGame.Iniciar.cpuPoint}', True, (255,255,255))
        textRectPoint = textPoint.get_rect()
        textRectPoint.center = (300,500)
        
        startGame.Iniciar.screen.blit(textPoint, textRectPoint)
        startGame.Iniciar.screen.blit(textEnded, textRectEnded)
       