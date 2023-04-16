import pygame as py  
import math
from config import WIDTH, HEIGHT, FPS, BLACK, GREEN, ROT, VEL

class Car:
    def __init__(self, x, y):
        # define a surface (RECTANGLE)  
        self.image_orig = py.Surface((50 , 100))  
        # for making transparent background while ROTating an image  
        self.image_orig.set_colorkey(BLACK)  
        # fill the rectangle / surface with green color  
        self.image_orig.fill(GREEN)  
        # creating a copy of orignal image for smooth ROTation  
        self.image = self.image_orig.copy()  
        self.image.set_colorkey(BLACK)  
        # define rect for placing the rectangle at the desired position  
        self.car = self.image.get_rect()

        self.velocity = 2
        self.direction = 0
        self.wheel = 0

        self.image = py.transform.rotate(self.image_orig, self.direction)
        
        self.car = self.image.get_rect()

        self.x = x
        self.y = y

    def acelerate(self):
        self.direction += self.wheel
        self.x += self.velocity * math.cos(math.radians(self.direction))
        self.y += self.velocity * math.sin(math.radians(self.direction))
        self.wheel = 0

    def desacelerate(self):
        self.direction -= self.wheel
        self.x -= self.velocity * math.cos(math.radians(self.direction))
        self.y -= self.velocity * math.sin(math.radians(self.direction))
        self.wheel = 0

    def turnleft(self):
        self.wheel = 1

    def turnright(self):
        self.wheel = -1

    def draw(self, screen):
        self.car.center = (self.y, self.x)
        screen.blit(self.image, self.car)
        car_old_center = self.car.center
        self.image = py.transform.rotate(self.image_orig, self.direction)
        self.car.center = car_old_center

def main():
    py.init()
    screen = py.display.set_mode((WIDTH , HEIGHT))  
    # for setting FPS  
    clock = py.time.Clock() 

    car = Car(WIDTH/2, HEIGHT/2)

    running = True
    while running:
        # Getting Key Press Events
        pressed = py.key.get_pressed()

        if pressed[py.K_UP]:
            car.acelerate()

        if pressed[py.K_DOWN]:
            car.desacelerate()
            
        if pressed[py.K_LEFT]: 
            car.turnleft()
            
        if pressed[py.K_RIGHT]:
            car.turnright()

        # check for the exit  
        for event in py.event.get():  
            if event.type == py.QUIT:  
                running = False 

        clock.tick(FPS)   
        screen.fill(BLACK)  
        # new_image = py.transform.rotate(image_orig ,ROT)  
        #rect = new_image.get_rect()  
        #rect.center = old_center
   
        car.draw(screen)
        py.display.flip()  

    py.quit()  


if __name__ == '__main__':
    main()