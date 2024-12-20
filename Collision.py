from math import sin, cos, pi, dist, atan2
from Objects import Objects, Circles
import setting as s


class Collsion:
    def __init__(self, l:list=[]):
        self.object_list = l
        self.contact_points = []
    

    def collide_all(self) -> None:
         for i in range(len(self.object_list) - 1):
            for j in range(i + 1, len(self.object_list)):
                if self.object_list[i] == self.object_list[j]:
                    continue

                tempi = self.object_list[i]
                tempj = self.object_list[j]

                #둘 다 circle인 경우
                if tempi.shape_type == "Circle" and tempj.shape_type == "Circle":
                    self.contact_points.append(self.collide_circles(tempi,tempj))
                ##################################################
    
    def collide_wall(self) -> None:
        for i in self.object_list:
            if i.shape_type == "Circle":
                if i.x < i.radius:
                    i.x = i.radius
                    i.velx = -i.velx
                if i.x > s.WIDTH - i.radius:
                    i.x = s.WIDTH - i.radius
                    i.velx = -i.velx
                if i.y < i.radius:
                    i.y = i.radius
                    i.vely = -i.vely
                if i.y > s.HEIGHT - i.radius:
                    i.y = s.HEIGHT - i.radius
                    i.vely = -i.vely
            ################################################
    
    def collide_circles(self, circle1:Circles, circle2:Circles) -> None:
        distance = dist((circle1.x,circle1.y),(circle2.x,circle2.y))
        if distance <= (circle1.radius + circle2.radius):
            normal_vector = [(circle1.x - circle2.x)/distance, (circle1.y - circle2.y)/distance]

            contact_point = [circle1.x - normal_vector[0] * circle1.radius, circle1.y - normal_vector[1] * circle1.radius]

            collide_response_circles(circle1,circle2,normal_vector)

            return contact_point
            


def separate_circles(circle1:Circles, circle2:Circles) -> None:
    d = dist((circle1.x,circle1.y),(circle2.x,circle2.y))
    p = circle1.radius + circle2.radius - d
    x = p * cos(atan2(circle1.y - circle2.y, circle1.x - circle2.x))
    y = p * sin(atan2(circle1.y - circle2.y, circle1.x - circle2.x))

    circle1.x += x/2
    circle2.x -= x/2 
    circle1.y += y/2 
    circle2.y -= y/2


def collide_response_circles(circle1:Circles, circle2:Circles, normal):
    assert len(normal) == 2

    normal = [-normal[0],-normal[1]]
    separate_circles(circle1,circle2)
    relative_vel = [circle2.x - circle1.x, circle2.y - circle1.y]
    penetration_vel = relative_vel[0] * normal[0] + relative_vel[1] * normal[1]
    if penetration_vel > 0:
        return

    j = - 1.5 * penetration_vel / (1/circle1.mass + 1/circle2.mass) 

    # 튕김
    circle1.velx -= j * normal[0] / circle1.mass
    circle1.vely -= j * normal[1] / circle1.mass
    circle2.velx += j * normal[0] / circle2.mass
    circle2.vely += j * normal[1] / circle2.mass
