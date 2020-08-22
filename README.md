# pygame

on linux <br>
sudo apt-get install python-pygame


## mouse pressed

        if event.type == pygame.MOUSEBUTTONDOWN:    <br>
            print(pygame.mouse.get_pressed())       <br>
            if pygame.mouse.get_pressed()[0]:       //left click<br>
            if pygame.mouse.get_pressed()[2]:       //right click<br>
                bird_movement = 0                   <br>  
                bird_movement -= 6                  <br>
