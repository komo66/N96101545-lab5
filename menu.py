import pygame
import os

# load image
UpgradeMenu_IMAGE = pygame.image.load(os.path.join("images","upgrade_menu.png"))
upgrde_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join("images","upgrade.png")),(70,40))
sell_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join("images","sell.png")),(50,40))

class UpgradeMenu:
    def __init__(self, x, y):
        self.__buttons = [Button(upgrde_IMAGE,"upgrade",x,y+70),Button(sell_IMAGE,"sell",x,y-70)]  # (Q2) Add buttons here
        self.image=pygame.transform.scale(UpgradeMenu_IMAGE,(200,200))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        #draw menu
        win.blit(self.image,self.rect)
        win.blit(sell_IMAGE,(self.rect.x+72,self.rect.y+10))
        win.blit(upgrde_IMAGE,(self.rect.x+64,self.rect.y+154))

    
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
       

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        #use collidepoint to check whether a point is contained in the Rect object
        return self.rect.collidepoint(x,y)
        

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass






