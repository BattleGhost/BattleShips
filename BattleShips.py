import pygame
import json
from text_input import *
from singleton import *


class GameManager(metaclass=Singleton):
    def __init__(self):
        pygame.init()
        self.display_width = 1920
        self.display_height = 1080
        self.Display = pygame.display.set_mode((self.display_width, self.display_height), pygame.FULLSCREEN)
        self.ip = ImageProcessor()
        pygame.display.set_icon(self.ip.icon)
        pygame.display.set_caption("BattleShips")
        self.clock = pygame.time.Clock()
        self.sp = SoundProcessor()
        self.sp.play()

    def main_menu(self, Display, ip, clock):

        closed = False
        down = True
        bsy = 62
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.sure_check(self.Display, self.ip, self.clock)

            Display.blit(ip.background, (0, 0))
            Display.blit(ip.bs, (576, bsy))

            mp = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if self.display_width / 2 - ip.start1.get_rect().size[0] / 2 + 15 < mp[0] < self.display_width / 2 +\
               ip.start1.get_rect().size[0] / 2 + 15 and 350 < mp[1] < 350 + ip.start1.get_rect().size[1]:
                Display.blit(ip.start2, (self.display_width / 2 - ip.start1.get_rect().size[0] / 2 + 15, 350))
                if click[0] == 1:
                    self.game_loop()
            else:
                Display.blit(ip.start1, (self.display_width / 2 - ip.start1.get_rect().size[0] / 2 + 15, 350))

            if self.display_width / 2 - ip.settings1.get_rect().size[0] / 2 + 15 < mp[0] < self.display_width / 2 +\
                    ip.settings1.get_rect().size[0] / 2 + 15 and 500 < mp[1] < 500 +\
                    ip.settings1.get_rect().size[1]:
                Display.blit(ip.settings2, (self.display_width / 2 - ip.settings1.get_rect().size[0] / 2 + 15, 500))
                if click[0] == 1:
                    self.open_settings(self.Display, self.ip, self.clock)
            else:
                Display.blit(ip.settings1, (self.display_width / 2 - ip.settings1.get_rect().size[0] / 2 + 15, 500))

            if self.display_width / 2 - ip.guide1.get_rect().size[0] / 2 + 15 < mp[0] < self.display_width / 2 +\
               ip.guide1.get_rect().size[0] / 2 + 15 and 650 < mp[1] < 650 + ip.guide1.get_rect().size[1]:
                Display.blit(ip.guide2, (self.display_width / 2 - ip.guide1.get_rect().size[0] / 2 + 15, 650))
            else:
                Display.blit(ip.guide1, (self.display_width / 2 - ip.guide1.get_rect().size[0] / 2 + 15, 650))

            if self.display_width / 2 - ip.exit1.get_rect().size[0] / 2 + 15 < mp[0] < self.display_width / 2 +\
               ip.exit1.get_rect().size[0] / 2 + 15 and 800 < mp[1] < 800 + ip.exit1.get_rect().size[1]:
                Display.blit(ip.exit2, (self.display_width / 2 - ip.exit1.get_rect().size[0] / 2 + 15, 800))
                if click[0] == 1:
                    self.sure_check(self.Display, self.ip, self.clock)

            else:
                Display.blit(ip.exit1, (self.display_width / 2 - ip.exit1.get_rect().size[0] / 2 + 15, 800))

            if down:
                bsy += 1
            elif not down:
                bsy -= 1

            if bsy == 52:
                down = True
            if bsy == 82:
                down = False

            pygame.display.update()
            clock.tick(100)

    def open_settings(self, Display, ip, clock):

        closed = False
        down = True
        bsy = 62




        try:
            file = open('settings.bs', 'r')
            settings = file.read()
            file.close()
            options = json.loads(settings)
            all_volume = options["volume"]["all_volume"]
            music_volume = options["volume"]["music_volume"]
            effects_volume = options["volume"]["effects_volume"]
            nickname = options["player"]["nickname"]
        except:
            all_volume = 800
            music_volume = 800
            effects_volume = 800
            nickname = "Player"


        volumes = [all_volume, music_volume, effects_volume]
        for i in range(len(volumes)):
            if type(volumes[i]) != int:
                volumes[i] = 800
            elif volumes[i] < 780 or volumes[i] > 1140:
                volumes[i] = 800


        all_volume = volumes[0]
        music_volume = volumes[1]
        effects_volume = volumes[2]

        if type(nickname) != str or len(nickname) < 1 or len(nickname) > 15:
            nickname = "Player"

        input_box = InputBox(750, 750, 400, 50, nickname)

        settings = {
            "volume": {
                "all_volume": all_volume,
                "music_volume": music_volume,
                "effects_volume": effects_volume
            },
            "player": {
                "nickname": nickname
            }
        }
        file = open('settings.bs', 'w')
        file.write(json.dumps(settings))
        file.close()

        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
                input_box.handle_event(event)

            Display.blit(ip.background, (0, 0))
            Display.blit(ip.bs, (576, bsy))

            mp = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            Display.blit(ip.start1, (self.display_width / 2 - ip.start1.get_rect().size[0] / 2 + 15, 350))
            Display.blit(ip.settings1, (self.display_width / 2 - ip.settings1.get_rect().size[0] / 2 + 15, 500))
            Display.blit(ip.guide1, (self.display_width / 2 - ip.guide1.get_rect().size[0] / 2 + 15, 650))
            Display.blit(ip.exit1, (self.display_width / 2 - ip.exit1.get_rect().size[0] / 2 + 15, 800))

            Display.blit(ip.settings_bar, (self.display_width / 2 - ip.settings_bar.get_rect().size[0] / 2 + 15, 200))

            if self.display_width / 2 + ip.settings_bar.get_rect().size[0] / 2 + 13 -\
                ip.cross1.get_rect().size[0] < mp[0] < self.display_width / 2 +\
                ip.settings_bar.get_rect().size[0] / 2 + 13 and 203 < mp[1] < 203 + ip.cross1.get_rect().size[1]:
                Display.blit(ip.cross2, (self.display_width / 2 + ip.settings_bar.get_rect().size[0] / 2 + 13 -
                                     ip.cross1.get_rect().size[0], 203))
                if click[0] == 1:

                    settings = {
                        "volume": {
                            "all_volume": all_volume,
                            "music_volume": music_volume,
                            "effects_volume": effects_volume
                        },
                        "player": {
                            "nickname": nickname
                        }
                    }
                    file = open('settings.bs', 'w')
                    file.write(json.dumps(settings))
                    file.close()
                    self.main_menu(self.Display, self.ip, self.clock)
            else:
                Display.blit(ip.cross1, (self.display_width / 2 + ip.settings_bar.get_rect().size[0] / 2 + 13 -
                                         ip.cross1.get_rect().size[0], 203))


            if 780 + ip.slider1.get_rect().size[0] /2 < mp[0] < 1140 + ip.slider1.get_rect().size[0] /2 and\
                                    368 < mp[1] < 368 + ip.slider1.get_rect().size[1]\
                    and click[0] == 1:
                all_volume = int(mp[0] - ip.slider1.get_rect().size[0] /2)
                Display.blit(ip.slider2, (all_volume, 368))
            else:
                Display.blit(ip.slider1, (all_volume, 368))

            if 780 + ip.slider1.get_rect().size[0] /2 < mp[0] < 1140 + ip.slider1.get_rect().size[0] /2 and\
                                    438 < mp[1] < 438 + ip.slider1.get_rect().size[1]\
                    and click[0] == 1:
                music_volume = int(mp[0] - ip.slider1.get_rect().size[0] /2)
                Display.blit(ip.slider2, (music_volume, 438))
            else:
                Display.blit(ip.slider1, (music_volume, 438))

            if 780 + ip.slider1.get_rect().size[0] /2 < mp[0] < 1140 + ip.slider1.get_rect().size[0] /2 and\
                                    518 < mp[1] < 518 + ip.slider1.get_rect().size[1]\
                    and click[0] == 1:
                effects_volume = int(mp[0] - ip.slider1.get_rect().size[0] /2)
                Display.blit(ip.slider2, (effects_volume, 518))
            else:
                Display.blit(ip.slider1, (effects_volume, 518))

            if down:
                bsy += 1
            elif not down:
                bsy -= 1

            if bsy == 52:
                down = True
            if bsy == 82:
                down = False

            self.sp.set_effects_volume((effects_volume - 780) / 360)
            self.sp.set_music_volume((music_volume-780)/360)
            self.sp.set_master_volume((all_volume-780)/360)

            input_box.update()

            input_box.draw(Display)
            nickname = input_box.text

            pygame.display.update()
            clock.tick(100)

    def sure_check(self, Display, ip, clock):
        self.sp.play_kar()
        closed = False
        down = True
        bsy = 62
        spos = -ip.sure.get_rect().size[1]
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.main_menu(self.Display, self.ip, self.clock)

            Display.blit(ip.background, (0, 0))
            Display.blit(ip.bs, (576, bsy))

            if spos < 300:
                spos += 400
                if spos > 320:
                    spos = 320

            mp = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            Display.blit(ip.start1, (self.display_width / 2 - ip.start1.get_rect().size[0] / 2 + 15, 350))
            Display.blit(ip.settings1, (self.display_width / 2 - ip.settings1.get_rect().size[0] / 2 + 15, 500))
            Display.blit(ip.guide1, (self.display_width / 2 - ip.guide1.get_rect().size[0] / 2 + 15, 650))
            Display.blit(ip.exit1, (self.display_width / 2 - ip.exit1.get_rect().size[0] / 2 + 15, 800))

            Display.blit(ip.sure, (self.display_width / 2 - ip.sure.get_rect().size[0] / 2 + 15, spos))

            if spos == 320:
                if self.display_width / 2 - ip.sure.get_rect().size[0] / 2 + 50 < mp[0] < self.display_width / 2 -\
                                ip.sure.get_rect().size[0] / 2 + 50 + ip.yes1.get_rect().size[0] and 700 < mp[1] < 700\
                        + ip.yes1.get_rect().size[1]:
                    Display.blit(ip.yes2, (self.display_width / 2 - ip.sure.get_rect().size[0] / 2 + 50, 700))
                    if click[0] == 1:
                        closed = True
                        pygame.quit()
                        quit()
                else:
                    Display.blit(ip.yes1, (self.display_width / 2 - ip.sure.get_rect().size[0] / 2 + 50, 700))

                if self.display_width / 2 + ip.sure.get_rect().size[0] / 2 - ip.no1.get_rect().size[0] - 20 < mp[0] <\
                   self.display_width / 2 + ip.sure.get_rect().size[0] / 2 - 20 and 700 < mp[1] < 700 +\
                   ip.no1.get_rect().size[1]:
                    Display.blit(ip.no2, (self.display_width / 2 + ip.sure.get_rect().size[0] / 2 -
                                          ip.no1.get_rect().size[0] - 20, 700))
                    if click[0] == 1:
                        self.main_menu(self.Display, self.ip, self.clock)
                else:
                    Display.blit(ip.no1, (self.display_width / 2 + ip.sure.get_rect().size[0] / 2 -
                                          ip.no1.get_rect().size[0] - 20, 700))

            if down:
                bsy += 1
            elif not down:
                bsy -= 1

            if bsy == 52:
                down = True
            if bsy == 82:
                down = False

            pygame.display.update()
            clock.tick(100)

    def game_loop(self):
        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
                    pygame.quit()
                    quit()

            self.Display.blit(self.ip.background, (0, 0))

            pygame.display.update()
            self.clock.tick(60)


class ImageProcessor:
    def __init__(self):
        self.icon = pygame.image.load("img/icon.png")
        self.background = pygame.image.load("img/backgroundhd.png")
        self.bs = pygame.image.load("img/battleships2.png")
        self.start1 = pygame.image.load("img/start1.png")
        self.start2 = pygame.image.load("img/start2.png")
        self.settings1 = pygame.image.load("img/settings1.png")
        self.settings2 = pygame.image.load("img/settings2.png")
        self.guide1 = pygame.image.load("img/guide1.png")
        self.guide2 = pygame.image.load("img/guide2.png")
        self.exit1 = pygame.image.load("img/exit1.png")
        self.exit2 = pygame.image.load("img/exit2.png")
        self.yes1 = pygame.image.load("img/yes1.png")
        self.yes2 = pygame.image.load("img/yes2.png")
        self.no1 = pygame.image.load("img/no1.png")
        self.no2 = pygame.image.load("img/no2.png")
        self.sure = pygame.image.load("img/sure.png")
        self.settings_bar = pygame.image.load("img/settings_bar.png")
        self.cross1 = pygame.image.load("img/cross1.png")
        self.cross2 = pygame.image.load("img/cross2.png")
        self.slider1 = pygame.image.load("img/slider1.png").convert_alpha()
        self.slider2 = pygame.image.load("img/slider2.png").convert_alpha()


class SoundProcessor:
    def __init__(self):
        pygame.mixer.init(44100, 0, -1, 8192)
        self.sound = pygame.mixer.Sound("sounds\oka.ogg")
        self.kar = pygame.mixer.Sound("sounds\kar.ogg")
        try:
            file = open('settings.bs', 'r')
            settings = file.read()
            file.close()
            options = json.loads(settings)
            self.set_music_volume((options["volume"]["music_volume"] - 780) / 360)
            self.set_effects_volume((options["volume"]["effects_volume"] - 780) / 360)
            self.set_master_volume((options["volume"]["all_volume"] - 780) / 360)
        except:
            self.set_music_volume(1/18)
            self.set_effects_volume(1/18)
            self.set_master_volume(1/18)

    def play(self):
        self.sound.play(-1)

    def play_kar(self):
        self.kar.play(0)

    def set_music_volume(self, volume):
        self.sound.set_volume(volume)

    def set_effects_volume(self, volume):
        self.kar.set_volume(volume)

    def set_master_volume(self, volume):
        self.sound.set_volume(self.sound.get_volume() * volume)
        self.kar.set_volume(self.kar.get_volume() * volume)


gm = GameManager()
gm.main_menu(gm.Display, gm.ip, gm.clock)
