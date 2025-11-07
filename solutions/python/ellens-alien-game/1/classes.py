"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    
    def __init__(self, coord_x, coord_y):
        self.x_coordinate = coord_x
        self.y_coordinate = coord_y
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health-=1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, coord_x, coord_y):
        self.x_coordinate += coord_x
        self.y_coordinate += coord_y
        
    def collision_detection(self, other_object):
        # TODO: Implement collision logic later
        pass

    def toral_aliens_created(self):
        return self.count

def new_aliens_collection(list_alien):
    aliens = [Alien(x, y) for x, y in list_alien]
    return aliens

    
    

    

    
        

    

    
        

    pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
