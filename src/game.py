import pygame
import colorsys


class Game:
    def __init__(self, screen, speed, x, y, w, h):
        self.screen = screen
        self.speed1 = speed
        self.speed2 = speed * 0.707
        self.static_gravity = speed
        self.dynamic_gravity = speed
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_loop = .0
        
    def tick(self):
        self.color_loop += .001
        if self.color_loop > 1:
            self.color_loop = .0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
                
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.w, self.h))
        # if (((keys[pygame.K_LEFT] or keys[pygame.K_a]) or
        #     (keys[pygame.K_RIGHT] or keys[pygame.K_d])) and
        #     ((keys[pygame.K_UP] or keys[pygame.K_w]) or
        #     (keys[pygame.K_DOWN] or keys[pygame.K_s]))):
        #     speed = self.speed2
        if (((keys[pygame.K_LEFT] or keys[pygame.K_a]) or
             (keys[pygame.K_RIGHT] or keys[pygame.K_d])) and
                (self.y + self.h < 720)):
            speed = self.speed2
        else:
            speed = self.speed1
            
        if self.x > 1280 + self.w:
            self.x = 1 - self.w
        elif self.x < -self.w:
            self.x = 1280 - self.w - 1
            
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += speed
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     self.y -= speed
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.y += speed
        if self.y + self.h < 720:
            self.y += self.dynamic_gravity
            if self.dynamic_gravity != self.static_gravity:
                self.dynamic_gravity += 0.1
        elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.dynamic_gravity = self.static_gravity * -1.5
            self.y = 719 - self.h
            
        # self.screen.fill((0,0,0))
        color_rgb = colorsys.hsv_to_rgb(self.color_loop, 1, .7)
        pygame.draw.rect(
            self.screen,
            (color_rgb[0] * 255, color_rgb[1] * 255, color_rgb[2] * 255),
            (self.x, self.y, self.w, self.h)
        )
        pygame.display.update()
        
        return False
