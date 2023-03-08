import sys, pygame
from mira import Mira
from HUD import *
from player import *
from my_tools.mouse_pos_tool import dmp
from inimigos import *
import time



def Iniciar(game = False):
    if game:
        # inicia os modulos
        pygame.init()
        pygame.font.init()

        # janela setup
        RES = 1366,768
        janela = pygame.display.set_mode(RES)
        dark_blue = 8, 25, 100
        pygame.mouse.set_visible(False)
        dt = 0
        last_frame = time.time()
        clock = pygame.time.Clock()
        FPS = 240

        # fonte
        fonte = pygame.font.SysFont('Arial', 30)

        # Som
        som_hit = pygame.mixer.Sound('som\hit.wav')
        som_hit.set_volume(0.5)
        boss_som = pygame.mixer.Sound('som\zking.wav')
        musica = pygame.mixer.music.load('som\musica.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)


        # HUD elements
        vida_fundo = HUD_element('Images\\barra_hp.png',(683,738))
        xp_bar = HUD_element('Images\\barra_xp.png',(683,30))
        arma1 = HUD_element('Images\cajado.png',(1207,660))
        arma1.resize((128,128))
        arma2 = HUD_element('Images\lança.png',(192,660))
        arma2.resize((128,128))

        # timer
        sec = 0
        min = 0


        # Player
        player = Player(janela)
        player.resize((64,64))


        # mapa 
        
        mapa = pygame.image.load('Images\\mapa.png')
        mapa_pos = [RES[0]/2,RES[1]/2]
        speed = player.speed

        # bats 
        bats = []
        bats_bando = 2
        secbat = 1
        # lacs
        lacraias = []
        seclac = 1
        # polvo
        polvos = []
        min_pol = 0
        # zwar
        zwarriors = []
        secz = 1
        # manowar
        manowars = []
        secman = 0
        # zking
        zkings = []
        minking = 1

        # colisao balas e inimigos
        flag_sair = 0

       
    while game:
        # delta time
        now = time.time()
        dt = now - last_frame
        last_frame = now
        clock.tick(FPS)

        # anti-ghosting
        janela.fill(dark_blue)

        # pygame event check para fechar a janela no x
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game = False
                

            # player tiros
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # cria uma instancia de bala quando clica
                    
                    player.balas.append(PlayerBullet(pygame.mouse.get_pos(), janela, player.arma, player.dano))
            teclas = pygame.key.get_pressed()
                    
        # spawn inimigos
        if sec > 0:
            pass
            if sec % 2 == 0 and sec != secbat: # spawna um bat a cada 2 seg
                secbat = sec
                for _ in range(bats_bando+min):
                    bat = Bat(janela)
                    bat.resize((32,16))
                    bats.append(bat)
            if sec % 4 == 0 and sec != seclac: # spawna uma lac a cada 4 seg
                seclac = sec
                for _ in range(min//5 + 1):
                    lac = Lacraia(janela, min)
                    lac.resize((64,64))
                    lacraias.append(lac)
            if min % 1 == 0 and min != min_pol: # spawna um cthulu a cada 1 min
                min_pol = min
                for _ in range(min//10 + 1):
                    boss = Polvo(janela, min)
                    boss.resize((256,256))
                    polvos.append(boss) 
            if sec % 3 == 0 and sec != secz: # spawna um zwarrior a cada 3 seg
                secz = sec
                for _ in range(min//5 + 1):
                    zwarrior = Zwarrior(janela, min)
                    zwarrior.resize((64,64))
                    zwarriors.append(zwarrior)
        if min >= 1:
            if sec % 5 == 0 and sec != secman: # spawna um manowar a cada 10 seg dps de 1 min
                secman = sec
                for _ in range(min//10 + 1):
                    manowar = Manowar(janela, min)
                    manowar.resize((128,128))
                    manowars.append(manowar)
        if min >= 5 and min != minking: #spawna um zking a cada 5 min
            minking = min
            for _ in range(min//20 + 1):
                boss_som.play()
                zking = Zking(janela)
                zking.resize((400,400))
                zkings.append(zking)

        # Mapa display e movimento
        speed = player.speed
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
            # mapa_pos[0] += speed*dt
            
            for bala in player.balas:
                bala.rect.x += speed*dt
            for inimigo in bats:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
            for inimigo in lacraias:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
                inimigo.acido_pos = inimigo.acido_pos[0] + speed*dt, inimigo.acido_pos[1]
            for inimigo in polvos:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
            for inimigo in zwarriors:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
            for inimigo in manowars:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
            for inimigo in zkings:
                inimigo.pos = inimigo.pos[0] + speed*dt, inimigo.pos[1]
                for tiro in inimigo.tiros:
                    tiro.rect.x += speed*dt
        if teclas[pygame.K_d]:
            # mapa_pos[0] -= speed*dt
            
            for bala in player.balas:
                bala.rect.x -= speed*dt
            for inimigo in bats:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
            for inimigo in lacraias:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
                inimigo.acido_pos = inimigo.acido_pos[0] - speed*dt, inimigo.acido_pos[1]
            for inimigo in polvos:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
            for inimigo in zwarriors:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
            for inimigo in manowars:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
            for inimigo in zkings:
                inimigo.pos = inimigo.pos[0] - speed*dt, inimigo.pos[1]
                for tiro in inimigo.tiros:
                    tiro.rect.x -= speed*dt
        if teclas[pygame.K_s]:
            # mapa_pos[1] -= speed*dt
            for bala in player.balas:
                bala.rect.y -= speed*dt
            for inimigo in bats:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
            for inimigo in lacraias:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
                inimigo.acido_pos = inimigo.acido_pos[0], inimigo.acido_pos[1] - speed*dt
            for inimigo in polvos:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
            for inimigo in zwarriors:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
            for inimigo in manowars:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
            for inimigo in zkings:
                inimigo.pos =  inimigo.pos[0], inimigo.pos[1] - speed*dt
                for tiro in inimigo.tiros:
                    tiro.rect.y -= speed*dt
        if teclas[pygame.K_w]:
            # mapa_pos[1] += speed*dt
            for bala in player.balas:
                bala.rect.y += speed*dt
            for inimigo in bats:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
            for inimigo in lacraias:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
                inimigo.acido_pos = inimigo.acido_pos[0], inimigo.acido_pos[1] + speed*dt
            for inimigo in polvos:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
            for inimigo in zwarriors:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
            for inimigo in manowars:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
            for inimigo in zkings:
                inimigo.pos = inimigo.pos[0], inimigo.pos[1] + speed*dt
                for tiro in inimigo.tiros:
                    tiro.rect.y += speed*dt
        mapa_rect = mapa.get_rect(center=mapa_pos)

        janela.blit(mapa,mapa_rect)
        
        
        # inimigo display
        for enemy in bats:
            if enemy.rect.colliderect(player.player_rect):
                player.vida -= enemy.dano
                bats.remove(enemy)
            else:
                enemy.draw(janela, dt)
        
        for enemy in lacraias:
            enemy.tiro(janela, dt, player)
            enemy.draw(janela, dt)
        
        for enemy in polvos:
            enemy.draw(janela, dt, player)

        for enemy in zwarriors:
            enemy.draw(janela, dt, player)
        
        for enemy in manowars:
            enemy.draw(janela, dt, player)
        
        for enemy in zkings:
            enemy.draw(janela, dt, player)
            for tiro in enemy.tiros:
                pegou = tiro.shot(dt, player)
                if pegou:
                    enemy.tiros.remove(tiro)
                    player.vida -= tiro.dano  
                if tiro in enemy.tiros:
                    if tiro.timer >= 3:
                        enemy.tiros.remove(tiro)
                    else:
                        janela.blit(tiro.bullet, tiro.rect)
                    
            
        # balas player display
        for bala in player.balas:
            flag_sair = 0
            if not flag_sair:
                for enemy in bats:
                    if bala.rect.colliderect(enemy.rect):
                        som_hit.play()
                        bats.remove(enemy)
                        player.xp += enemy.xp
                        player.balas.remove(bala)
                        flag_sair = 1
                        break
            if not flag_sair:
                for enemy in lacraias:
                    if bala.rect.colliderect(enemy.rect):
                        
                        enemy.vida -= bala.dano
                        player.balas.remove(bala)
                        if enemy.vida <= 0:
                            lacraias.remove(enemy)
                            player.xp += enemy.xp
                            som_hit.play()                         
                        flag_sair = 1
                        break
            if not flag_sair:
                for enemy in polvos:
                    if bala.rect.colliderect(enemy.rect):
                        
                        enemy.vida -= bala.dano
                        player.balas.remove(bala)
                        if enemy.vida <= 0:
                            # animacao de cura
                            som_hit.play()
                            player.vida += 20
                            polvos.remove(enemy)
                            player.xp += enemy.xp                            
                            player.speed = 400
                        flag_sair = 1
                        break
            if not flag_sair:
                for enemy in zwarriors:
                    if bala.rect.colliderect(enemy.rect):
                        
                        enemy.vida -= bala.dano
                        player.balas.remove(bala)
                        if enemy.vida <= 0:
                            som_hit.play()
                            zwarriors.remove(enemy)
                            player.xp += enemy.xp                            
                        flag_sair = 1
                        break
            if not flag_sair:
                for enemy in manowars:
                    if bala.rect.colliderect(enemy.rect):
                        
                        enemy.vida -= bala.dano
                        player.balas.remove(bala)
                        if enemy.vida <= 0:
                            som_hit.play()
                            manowars.remove(enemy)
                            player.xp += enemy.xp
                            player.speed = 400                            
                        flag_sair = 1
                        break
            if not flag_sair:
                for enemy in zkings:
                    if bala.rect.colliderect(enemy.rect):
                        
                        enemy.vida -= bala.dano
                        player.balas.remove(bala)
                        if enemy.vida <= 0:
                            som_hit.play()
                            zkings.remove(enemy)
                            # tela de drop
                            player.xp += enemy.xp                            
                        flag_sair = 1
                        break
            if not flag_sair:            
                bala.shot()
                if bala in player.balas:
                    if RES[0] < bala.rect.x or bala.rect.x < 0 or RES[1] < bala.rect.y or bala.rect.y < 0:
                        player.balas.remove(bala)
                    else:
                        janela.blit(bala.bullet, bala.rect)
    

        # player display, level e morte
        player.draw(janela)
        if player.vida <= 0:
            game = False
        if player.vida > 100:
            player.vida = 100
        if player.xp >= 1000:
            player.xp -= 1000
            player.nivel += 1
            print(player.nivel)
            print(player.dano)

    
        # HUD display
        vida_fundo.draw(janela)
        pygame.draw.rect(janela, 'GREEN', (vida_fundo.rect.x, vida_fundo.rect.y, player.vida*vida_fundo.rect.width/100, vida_fundo.rect.height))
        xp_bar.draw(janela)
        pygame.draw.rect(janela, 'GREY', (xp_bar.rect.x, xp_bar.rect.y, player.xp*xp_bar.rect.width/1000, xp_bar.rect.height))
        arma1.draw(janela)  
        arma2.draw(janela)

        # mira display
        Mira(janela)

        # timer display
        sec = int(pygame.time.get_ticks()/1000)
        min = int(sec/60)
        sec -= min*60
        tempo = '{:02d}:{:02d}'.format(min,sec)
        timer = fonte.render(tempo, False, (0, 0, 0))
        nivel = fonte.render(str(player.nivel), True, (255, 255, 255))
        t_rect = timer.get_rect(topleft = (10,5))
        pygame.draw.rect(janela, (100,100,100), t_rect)
        janela.blit(timer, t_rect)
        janela.blit(nivel, (xp_bar.rect.x - 30, xp_bar.rect.y))

        # buffer update
        pygame.display.flip()


if __name__ == '__main__':
    Iniciar(game = True)