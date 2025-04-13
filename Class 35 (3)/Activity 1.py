import pygame
import random

#Initialise Pygame
pygame.init()

#Custom event IDs for colour change events
spritecol = pygame.USEREVENT + 1
backgroundcol = pygame.USEREVENT + 2

#Define basic colour using using - pygame.Color
#Background colours
blue = pygame.Color('blue')
lblue = pygame.Color('lightblue')
dblue = pygame.Color('darkblue')

#Sprite colors
yellow = pygame.Color('yellow')
red = pygame.Color('red')
orange = pygame.Color('orange')
white = pygame.Color('white')

#Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
  #Constructor method
  def __init__(self,color,height,width):
    #Call to the parent class (Sprite) constructor
    super().__init__()
    #Create the sprite's suface with dimensions and color
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    #Get the sprite's rectangle defining its position and size
    self.rect = self.image.get_rect()
    #Set initial velocity with random direction
    self.velocity = [random.choice([-1,1]) , random.choice([-1,1])]
    
  #Method to update's the sprite's position
  def update(self):
    #Move the sprite by its velocity
    self.rect.move_ip(self.velocity)
    #Flag to track if the sprite hits a boundary
    bound_hit = False
    
    #Check for collision with left or right boundaries and reverse direction
    if self.rect.left <= 0 or self.rect.right >= 500:
      self.velocity[0] = -self.velocity[0]
      bound_hit = True
    #Check for collision with top or bottom boundaries and reverse direction
    if self.rect.top <= 0 or self.rect.bottom >= 400:
      self.velocity[1] = -self.velocity[1]
      bound_hit = True
      
    #If a boundary was hit, post events to change colours
    if bound_hit:
      pygame.event.post(pygame.event.Event(spritecol)) 
      pygame.event.post(pygame.event.Event(backgroundcol)) 
      
  #Method to change the sprite's colours
  def change_color(self):
    self.image.fill(random.choice([yellow,red,orange,white]))

#Function to change the background colour    
def change_bgcolor():
  global bg_color
  bg_color = random.choice([blue,lblue,dblue])
  
#Create a group to hold sprites
all_sprites_list = pygame.sprite.Group()

# Instantiate the sprite
sp1 = Sprite(white, 20, 30)

# Randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Boundary Sprite")
# Set the initial background color
bg_color = blue
# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == spritecol:
      sp1.change_color()
    # If the background color change event is triggered, change the background color
    elif event.type == backgroundcol:
      change_bgcolor()

  # Update all sprites
  all_sprites_list.update()
  # Fill the screen with the current background color
  screen.fill(bg_color)
  # Draw all sprites to the screen
  all_sprites_list.draw(screen)

  # Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()