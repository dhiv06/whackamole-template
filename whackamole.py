import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        x = 0
        y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (x * 32 <= pos[0] < (x + 1) * 32) and (y * 32 <= pos[1] < (y + 1) * 32):
                        x = random.randint(0, 19)
                        y = random.randint(0, 15)


            screen.fill("light blue")

            for i in range(0, 641, 32):
                pygame.draw.line(screen, "dark blue", (i, 0), (i, 512))
            for j in range(0, 513, 32):
                pygame.draw.line(screen, "dark blue", (0, j), (640, j))

            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
