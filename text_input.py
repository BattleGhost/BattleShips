import pygame as pg


pg.init()

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 60)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        pressed = False
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos[0], event.pos[1]):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            pressed = True
        if event.type == pg.KEYUP:
            pressed = False

        if self.active and pressed == True:
            if event.key == pg.K_ESCAPE:
                self.active = False
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            elif event.key == pg.K_RETURN or event.key == pg.K_TAB or event.key == pg.K_KP_ENTER:
                pass
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pg.K_DELETE:
                self.text = ''
            else:
                if len(self.text) < 15:
                    self.text += event.unicode

        # Re-render the text
        self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
