import pygame

class Ball:
    """ The ball that the enimies and player shoot.

        Attributes:
            x (int): The x coordinate.
            y (int): The y coordinate.
            img (image): The image.
            mask: Pygame element.
    """

    def __init__(self, x, y, img):
        """ Constructs a new ball.
            Paramaters:
                x (int): The x coordinate.
                y (int): The y coordinate.
                img (image): The image.
        """
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        """ Places the ball in the game.
        """
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        """ Moves the ball according to its velocity.
            Paramaters:
                vel (int): The velocity of the ball.
        """
        self.y += vel

    def off_screen(self, height):
        """ Checks to see if the ball is off screen.
            Paramaters:
                height (int): The height of the screen.
            Returns:
                Booleen: If the ball is off screen.
        """
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        """ Calls the collision with another object.
            Paramaters:
                obj (ball, robot, or cowboy): Object 1
            Returns:
                Pygame Mask
        """
        return collide(self, obj)
        

def collide(obj1, obj2):
    """ Collides two objects.
        Paramaters:
            obj1 (ball): Object 1
            obj2 (ball, robot, or cowboy): Object 2
        Returns:
            Pygame Mask
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
