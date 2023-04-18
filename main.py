import pygame as py  
import math
from config import WIDTH, HEIGHT, FPS, BLACK, GREEN , FONT, MAXVELOCITY, MINVELOCITY, CONVERSIONTAX

class Car:
    def __init__(self, x, y):
        self.cameray = 0
        self.camerax = 0
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
        self.velocity = 0
        self.direction = 180
        self.wheel = 0

        self.image = py.transform.rotate(self.image_orig, self.direction)
        
        self.car = self.image.get_rect()

        self.x = x
        self.y = y

    def velocity(self):
        return self.velocity

    def camera(self):
        return [self.cameray,self.camerax]

    def acelerate(self):
        self.direction += self.wheel
        self.x += (self.velocity/CONVERSIONTAX) * math.cos(math.radians(self.direction))
        self.y += (self.velocity/CONVERSIONTAX) * math.sin(math.radians(self.direction))
        self.wheel = 0
        if self.velocity < MAXVELOCITY:
            self.velocity += 10
            if self.velocity > MAXVELOCITY:
                self.velocity = MAXVELOCITY

    def desacelerate(self):
        if self.velocity > MINVELOCITY:
            self.velocity -= 10
            if self.velocity < MINVELOCITY:
                self.velocity = MINVELOCITY
        self.direction -= self.wheel
        self.x += (self.velocity/CONVERSIONTAX) * math.cos(math.radians(self.direction))
        self.y += (self.velocity/CONVERSIONTAX) * math.sin(math.radians(self.direction))
        self.wheel = 0
        
    def turnleft(self):
        self.wheel = 2

    def turnright(self):
        self.wheel = -2

    def draw(self, screen):
        #Calculating the diference between the middle of the screen and where the car is
        self.cameray = (self.x - HEIGHT/2)
        self.camerax = (self.y - WIDTH/2)
        #Decreasing the velocity pear inercia and drag
        if self.velocity != 0:
            if self.velocity > 0:
                self.velocity -= 5
                if self.velocity < 0:
                    self.velocity = 0
            else:
                self.velocity += 5
                if self.velocity > 0:
                    self.velocity = 0
            self.x += (self.velocity/CONVERSIONTAX) * math.cos(math.radians(self.direction))
            self.y += (self.velocity/CONVERSIONTAX) * math.sin(math.radians(self.direction))
        self.car.center = (WIDTH/2,HEIGHT/2)
        screen.blit(self.image, self.car)
        car_old_center = self.car.center
        self.image = py.transform.rotate(self.image_orig, self.direction)
        self.car.center = car_old_center

def main():
    py.init()
    screen = py.display.set_mode((WIDTH , HEIGHT))  
    # for setting FPS  
    clock = py.time.Clock() 

    car = Car(HEIGHT/2, WIDTH/2)

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

        #Print the car velocity on the screen
        velocity_text = FONT.render("velocity:" + str(car.velocity), True, (200,0,0))
        screen.blit(velocity_text,(0,0))
        py.draw.rect(screen,(105,105,105),(490-car.camera()[1],0-car.camera()[0],150,900))
        car.draw(screen)
        py.display.flip()  

    py.quit()  

if __name__ == '__main__':
    main()