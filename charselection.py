import pygame
import sys


class char_select():
        def __init__(self, title, image, x1, x2, x3, y1, y2, y3):
            pygame.init()
            self.title = title
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
            self.image = image
            image = pygame.image.load('choosecharbg.jpg')
            self.screen = pygame.display.set_mode((800, 600))
            self.font = pygame.font.Font("ARCADECLASSIC.TTF", 30)
            self.running = True

       
        def run(self):
            self.char_menu(self.image)
 

   

        def char_menu(self, image):
       
            pygame.display.set_caption('Character Menu')

            display = self.screen
            mc_pic = pygame.image.load('mc.png')
            bg = pygame.image.load('choosecharbg.jpg')
            size1 = pygame.transform.scale(bg, (1000,600))
            hmm = pygame.display.set_mode((1000,600))
            
            mc_pic = pygame.image.load('mc.png')
            mc_rect = mc_pic.get_rect(x=400,y=95)
            
            lover_pic = pygame.image.load('lover.png')
            lover_rect = mc_pic.get_rect(x=200,y=200)

            villain_pic = pygame.image.load('villain.png')
            villain_rect = mc_pic.get_rect(x=600,y=100)

            bg_rect = size1.get_rect(x=0,y=0)
            title = self.font.render("Choose your character", True, "White")
            title_rect = title.get_rect(x=320, y=100)
            self.screen.blit(title, title_rect)

            while self.running:
                hmm.blit(size1, bg_rect)
                display.blit(mc_pic, mc_rect)
                display.blit(lover_pic, lover_rect)
                display.blit(villain_pic, villain_rect)
                  
                self.screen.blit(title, title_rect)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    pygame.display.update()
    

            
            
            
            
            
            
            
            
            
            
            # self.image = image
            # image = pygame.surface.Surface('choosecharbg.jpg')
            # title = self.font.render("Choose your story", True, "White")
            # title_rect = title.get_rect(x=100, y=100)
            # self.screen.blit(image, (0,0))
            # self.screen.blit(title, title_rect)

        #mc_pic = pygame.image.load('mc.png')
      

        #lover_pic = 
        #lover_rect = lover_pic.get_rect(x=300, y=250)

        #villain_pic = pygame.image.load('villain.png')
        #villain_rect = villain_pic.get_rect(x=450, y=250)

            # lover = Button(image=pygame.image.load('lover.png'), pos=(0, 0), text_input="LOVER", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
            # lover_scale = pygame.transform.scale(lover.image, (lover.image.get_size()))
            # lover_rect = lover_scale.get_rect(x=0, y=0)
            
            # mc = Button(image=pygame.image.load('mc.png'), pos=(400, 320), text_input="MC", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
            # mc_button = pygame.image.load('mc.png')
            # mc_pic = pygame.surface.Surface(mc_button.get_size())
            # mc_rect = mc_pic.get_rect(x=400, y=250)
            
            # villain = Button(image=pygame.image.load('villain.png'), pos=(420, 320), text_input="VILLAIN", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
            # villain_button = pygame.image.load('villain.png')
            # villain_pic = pygame.surface.Surface(villain_button.get_size())
            # villain_rect = villain_pic.get_rect(x=450, y=250)


            # back_button = Button(image=pygame.image.load("Play Rect.png"), pos=(400, 400), text_input="BACK", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
            # while char_sel:
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             char_sel = False
            #             self.running = False

            #     mouse_pos = pygame.mouse.get_pos()
            #     mouse_pressed = pygame.mouse.get_pressed()
        
            #     if back_button.is_pressed(mouse_pos,mouse_pressed):
            #         Button.main_menu()
            #     elif mc.is_pressed(mouse_pos,mouse_pressed):
            #         char_sel = False
            #         self.char_selection = 1
            #         print("Proceed to story Chap. 1...")
            #     elif lover.is_pressed(mouse_pos,mouse_pressed):
            #         char_sel = False
            #         self.char_selection = 2
            #         print("Complete Story : MC...")
            #     elif villain.is_pressed(mouse_pos,mouse_pressed):
            #         char_sel = False
            #         self.char_selection = 3
            #         print("Complete Story : MC...")
            #     title = self.font.render("Choose your story", True, "White")
            #     title_rect = title.get_rect(x=100, y=100)
            #     choosecharacterbg = pygame.image.load('choosecharbg.jpg')
            #     if back_button.image is not None:
            #         self.screen.blit(back_button.image, back_button.rect)
            #     self.screen.blit(mc.image, mc_rect)
            #     self.screen.blit(lover.image, lover_rect)
            #     self.screen.blit(villain.image, villain_rect)
            #     self.clock.tick(60)
            # pygame.display.update()

charselect = char_select(title = 'Choose your character', image = pygame.image.load('choosecharbg.jpg'), x1=None, x2=None
                         , x3=None, y1=None, y2=None, y3=None)
charselect.run()
