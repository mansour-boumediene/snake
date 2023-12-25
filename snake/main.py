import random
import pygame
import sys

class Jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True
        self.serpant_position_x = 300
        self.serpant_position_y = 300
        self.serpant_direction_x = 0
        self.serpant_direction_y = 0
        self.serpant_corps = 10
        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.pomme = 10
        self.clock = pygame.time.Clock()

    def fonction_principale(self):
        while self.jeu_encours:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT:
                        self.serpant_direction_x = 10
                        self.serpant_direction_y = 0
                    if evenement.key == pygame.K_LEFT:
                        self.serpant_direction_x = -10
                        self.serpant_direction_y = 0
                    if evenement.key == pygame.K_DOWN:
                        self.serpant_direction_y = 10
                        self.serpant_direction_x = 0
                    if evenement.key == pygame.K_UP:
                        self.serpant_direction_y = -10
                        self.serpant_direction_x = 0

            if self.serpant_position_x <= 100 or self.serpant_position_x >= 700 \
                    or self.serpant_position_y <= 100 or self.serpant_position_y >= 600:
                sys.exit()

            self.serpant_position_x += self.serpant_direction_x
            self.serpant_position_y += self.serpant_direction_y

            if self.pomme_position_y == self.serpant_position_y and self.serpant_position_x == self.pomme_position_x:
                # Augmenter la taille du serpent
                self.serpant_corps += 10

                # Redéfinir la position de la pomme
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)

            self.ecran.fill((0, 0, 0))
            # Dessiner le serpent avec la nouvelle taille
            pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpant_position_x, self.serpant_position_y, self.serpant_corps, self.serpant_corps))
            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))
            self.limiteless()
            self.clock.tick(20)
            pygame.display.flip()

    def limiteless(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)

if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
