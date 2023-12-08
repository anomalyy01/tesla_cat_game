# Project : Tesla_Cat_Game
# A game in which a cat named Tesla must fight to survive against aliens;
# the only way to stay alive is by shooting rays at the aliens;
#accumulate a score, each time the cat Tesla eliminates enemies;
###################################################################################

#bring in external modules or libraries into your Python script.

import pygame #Pygame is a set of Python modules/It provides functionalities 
import sys #provides access to variables used /interact with the interpreter.
import random #provides functions for generating random numbers

#______________________________Init Tesla Game_________________________________#
pygame.init() # initializes all these modules. such as graphics, sound, and input

#________________________________Display______________________________________#
width, height = 900, 850 #the a window sizes
screen = pygame.display.set_mode((width, height))#dimensions
pygame.display.set_caption("Tesla Cat Game")#title
#______________________________ Background image______________________________#
background_image = pygame.image.load("background.bmp")#function to load backimg
background_rect = background_image.get_rect()#rectangle/bounding box/stored variable
background_image = pygame.transform.scale(background_image, (width, height)) #dimensions
background_rect = background_image.get_rect()#stored in the variable
#________________________________Tesla image_____________________________________#

tesla_pict = "tesla_cat_pic.bmp" #filename tesla
tesla_img = pygame.image.load(tesla_pict)#this load the pict using pygame function
tesla_rect = tesla_img.get_rect()# gets the rectangle (bounding box) store var tesla_rect
tesla_size = (80, 80)#defines the tesla size
tesla_img = pygame.transform.scale(tesla_img, tesla_size)#pygame.transform.scale function_#
tesla_rect = tesla_img.get_rect()#After scaling the image, a new rectangle is obtained from the scaled image using get_rect(). This new rectangle is stored in the variable tesla_rect.#

tesla_x, tesla_y = (width - tesla_rect.width) // 3, (height - tesla_rect.height) // 3
#This line calculates the initial position (x, y) of the Tesla cat on the game window. The x-coordinate is set to one-third of the remaining width after subtracting the width of the Tesla cat image from the total width, and the y-coordinate is similarly calculated based on the height.#
tesla_speed = 5
# This line sets the speed of the Tesla cat to 5 pixels per frame. This variable is likely to be used later to update the position of the Tesla cat in the game loop.#

#__________________________________ Alien image _________________________________#
alien_pict = "alienigena.bmp"
alien_img = pygame.image.load(alien_pict)
alien_rect = alien_img.get_rect()
alien_size = (100, 100)
#function that takes two arguments the alien and alien size/ the scaled image is then #assigned back to the variable alien.img ##
alien_img = pygame.transform.scale(alien_img, alien_size)
alien_rect = alien_img.get_rect()
alien_x, alien_y = random.randint(1, width - alien_rect.width), 1
alien_speed = 0.5

######### -------STARS ------########################

# Load stars image
stars_pict = "stars.bmp"
stars_img = pygame.image.load(stars_pict)
stars_size = (850, 350)
stars_img = pygame.transform.scale(stars_img, stars_size)
stars_rect = stars_img.get_rect()
stars_x, stars_y = random.randint(1, width - stars_rect.width), 1
stars_speed = 0.05
############## -------nivi-blue------#############
# Load starpink
starpink_pict = "navi.bmp"
starpink_img = pygame.image.load(starpink_pict)
starpink_size = (100, 50)
starpink_img = pygame.transform.scale(starpink_img, starpink_size)
starpink_rect = starpink_img.get_rect()
starpink_x, starpink_y = random.randint(1, width - starpink_rect.width), 1
starpink_speed = 1

############ -------navipink------##########
# Load starswhite
starswhite_pict = "navi2.bmp"
starswhite_img = pygame.image.load(starswhite_pict)
starswhite_size = (100, 50)
starswhite_img = pygame.transform.scale(starswhite_img, starswhite_size)
starswhite_rect = starswhite_img.get_rect()
starswhite_x, starswhite_y = random.randint(1, width - starswhite_rect.width), 1
# This part generates a random integer within the range from 1 to width - starswhite_rect.width. It appears to be determining the x-coordinate of the object, ensuring that the entire object fits within the window width.#
starswhite_speed = 0.1
###############___________navi amarela__________########

starsimple_pict = "naviamarela.bmp"
starsimple_img = pygame.image.load(starsimple_pict)
starsimple_size = (150, 75)
starsimple_img = pygame.transform.scale(starsimple_img, starsimple_size)
starsimple_rect = starsimple_img.get_rect()
starsimple_x, starsimple_y = random.randint(5,
 width - starsimple_rect.width), 5
starsimple_speed = 0.05

#########_________broke alien image___________############
broke_alien_pict = "broke_alien.bmp" # This line defines the filename of the image to be used for the broke alien, and it's stored in the variable #
broke_alien_img = pygame.image.load(broke_alien_pict)
broke_alien_rect = broke_alien_img.get_rect()

#########_________rays /raio image___________############
raio_pict = "raios.bmp"
raio_img = pygame.image.load(raio_pict)
raio_rect = raio_img.get_rect()
raio_size = (40, 50)
raio_img = pygame.transform.scale(raio_img, raio_size)
raio_rect = raio_img.get_rect()
raios = []

#########___________  ____________#########

alien_hit_timer = 0
alien_hit_duration = 30
#########___________  ____________#########
if alien_y > height:
  alien_x, alien_y = random.randint(0, width - alien_rect.width), 0

# displaying broken alien image
if alien_hit_timer > 0:
    alien_hit_timer -= 1
    alien_img = broke_alien_img
    alien_size = (50, 50)
    alien_img = pygame.transform.scale(alien_img, alien_size)
    alien_rect = alien_img.get_rect()
else:
    alien_img = pygame.image.load(alien_pict)
    alien_img = pygame.transform.scale(alien_img, alien_size)
    alien_rect = alien_img.get_rect()

# Draw alien
screen.blit(alien_img, (alien_x, alien_y))

# #########_________score___________############
# score = 0
font = pygame.font.Font(None, 30)

#########_________Game loop___________############
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
#########_________________________________________#########

# Move stars
  stars_y += stars_speed
  ############################
  starpink_y += starpink_speed
  ###################################
  starswhite_y += starswhite_speed
  ####################################
  starsimple_y += starsimple_speed

  ####################################

  # Reset stars position if they go off the screen
  if stars_y > height:
    stars_y = 1
    stars_x = random.randint(1, width - stars_rect.width)

  # Reset starpink
  if starpink_y > height:
    starpink_y = 1
    starpink_x = random.randint(1, width - starpink_rect.width)

######################________  starswhite_______#############################



  def disintegrate_alien():

    ##########___________ Iterate through each raio  ____________#########
    for raio in raios:
      # #  mask for the raio image
      # raio_mask = pygame.mask.from_surface(raio_img)

      #########___________offset of the raio relative to the alien____________#########
      offset = (raio.x - alien_x, raio.y - alien_y)

      # #########___________  overlap____________#########
      # overlap = alien_mask.overlap(raio_mask, offset)

      if overlap:
        #########___________remove the raio and update the alien image _____#########

        raios.remove(raio)
        # score += 1
        alien_hit_timer = alien_hit_duration
        alien_x, alien_y = random.randint(0, width - alien_rect.width), 0

        #########___________   # Disintegrate  ____________#########
        disintegrated_img = pygame.Surface(alien_size, pygame.SRCALPHA)
        screen.blit(disintegrated_img, (alien_x, alien_y))

############_____Collisions  ______############

    for raio in raios:
      if alien_rect.colliderect(raio):
        disintegrate_alien()

############_____Move the tesla ______############
#left

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and tesla_x > 0:
    tesla_x -= tesla_speed

  #right
  if keys[pygame.K_RIGHT] and tesla_x < width - tesla_rect.width:
    tesla_x += tesla_speed

  #up
  if keys[pygame.K_UP] and tesla_y > 0:
    tesla_y -= tesla_speed

  #down
  if keys[pygame.K_DOWN] and tesla_y < height - tesla_rect.height:
    tesla_y += tesla_speed

  # Move alien
  alien_y += alien_speed
  if alien_y > height:
    alien_x, alien_y = random.randint(0, width - alien_rect.width), 0

  # Shoot raios
  if keys[pygame.K_SPACE]:
    raio = pygame.Rect(tesla_x + tesla_rect.width // 2 - raio_rect.width // 2,
                       tesla_y, raio_rect.width, raio_rect.height)
    raios.append(raio)

  ############_____Update raios______############
  raios = [raio for raio in raios if raio.y > 0]
  for raio in raios:
    raio.y -= 10
  #########___________  ____________#########

  for raio in raios:

    alien_collision_rect = alien_rect.inflate(alien_rect.width // 2, alien_rect.height // 2)

    if alien_collision_rect.colliderect(raio):
        raios.remove(raio)
        # score += 1
        alien_hit_timer = alien_hit_duration
        alien_x, alien_y = random.randint(0, width - alien_rect.width), 0


  ############_____displaying broken alien image______############

  if alien_hit_timer > 0:
    alien_hit_timer -= 1
    alien_img = broke_alien_img
    alien_size = (50, 50)
    alien_img = pygame.transform.scale(alien_img, alien_size)
    alien_rect = alien_img.get_rect()
  else:
    alien_img = pygame.image.load(alien_pict)
    alien_img = pygame.transform.scale(alien_img, alien_size)
    alien_rect = alien_img.get_rect()
##################_____________STARS____________##################

#########___________ broken alien or original alien ____________##########
  if alien_y < height:
    screen.blit(alien_img, (alien_x, alien_y))

  ############_____background______############

  screen.blit(background_image, background_rect)
  screen.blit(tesla_img, (tesla_x, tesla_y))
  screen.blit(stars_img, (stars_x, stars_y))
  screen.blit(starpink_img, (starpink_x, starpink_y))
  screen.blit(starswhite_img, (starswhite_x, starswhite_y))
  screen.blit(starsimple_img, (starsimple_x, starsimple_y))

  ############_____broken alien______############
  if alien_y < height:
    screen.blit(alien_img, (alien_x, alien_y))

  for raio in raios:
    screen.blit(raio_img, (raio.x, raio.y))

  ############_____score______############
  # score_text = font.render("Score: " + str(score), True, (255, 255, 255))
  # screen.blit(score_text, (10, 10))

  ############_____Update the display______############
  pygame.display.flip()

  ############_____the frame rate______############

  pygame.time.Clock().tick(60)

###########################################################################
