import pygame, os, random, sys, time
currDir = os.path.dirname(__file__)
os.chdir(currDir)

## use this command to build on Windows
## pyinstaller.exe '.\Honka_fullscreen.py' --onefile --noconsole --add-data='*.png;.'

pic_file_prefix    = 'honk'
pic_number         = 5
pic_file_extention = 'png'

MAX_X = 1920
MAX_Y = 1080

particles_num = 100
img_size = 150

x_multiplier = 50

class Image():
    def __init__(self, filename):
        self.filename = filename
        self.img_original = pygame.image.load(self.filename).convert_alpha()
        self.img_original = pygame.transform.scale(self.img_original, (img_size, img_size))

    def generate_rotated(self):
        self.img_rotated = []
        for angl in range(0, 360):
            self.img_rotated.append(pygame.transform.rotate(self.img_original, angl))

    def get_rotated(self, angle):
        return self.img_rotated[angle]

class Particle():
    def __init__(self, x, y):
        self.x        = x
        self.y        = y
        self.speed_y  = random.randint(1, 4)
        # self.speed_y  = 0
        

        self.img_num  = random.randint(0, pic_number - 1)
        self.x_dest     = x
        self.rotate_r   = random.randint(0, 1)
        self.angle      = 0
        self.speed_angl = random.randint(0, 3)

    def move(self):
        # # Y axis movement
        self.y += self.speed_y
        if self.y > MAX_Y + img_size:
            self.y = 0 - img_size

        # # X axis movement
        if self.x < self.x_dest:
            self.x += 1
            if self.x > MAX_X + img_size:
                self.x = 0 - img_size
        elif self.x > self.x_dest:
            self.x -= 1
            if self.x < (0 - img_size):
                self.x = MAX_X + img_size

        if self.x_dest == self.x:
            i = random.randint(0, 1)
            if i == 1:
                self.x_dest += self.speed_y * x_multiplier
            elif i == 0:
                self.x_dest -= self.speed_y * x_multiplier

        # # rotation
        if self.rotate_r == 1:
            self.angle += self.speed_angl
            if self.angle > 359:
                self.angle = 0
        elif self.rotate_r == 0:
            self.angle -= self.speed_angl
            if self.angle < 0:
                self.angle = 359

    def draw(self):
        pos = (self.x, self.y)
        self.image = pics[self.img_num].get_rotated(self.angle)
        rotated_image_rect = self.image.get_rect(center = pos)

        surf.blit(self.image, rotated_image_rect)

def add_particle(particles_num, particles):
    for i in range(0, particles_num):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        particles.append(Particle(xx, yy))

def do_exit() -> bool:
    for event in pygame.event.get():
        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

########## MAIN ##########

pygame.init()
surf = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("Honks are everywhere!")

bg_color = (0, 0, 0)

particles = []
add_particle(particles_num, particles)

pics = []
for i in range(0, pic_number):
    pic_filename = pic_file_prefix + str(i) + '.' + pic_file_extention
    pics.append(Image(pic_filename))
    pics[i].generate_rotated()

while not do_exit():
    surf.fill(bg_color)
    for i in particles:
        i.move()
        i.draw()
    time.sleep(0.01)
    pygame.display.flip()