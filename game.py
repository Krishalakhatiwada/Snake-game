import pygame
import sys
import random

FOOD_SIZE = 10


class snake:
    def __init__(self, game):
        self.direction = "right"
        self.game = game
        self.snake_length = 4
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.snake_position = [100, 50]
        self.motion = 10
    def key_movement(self, key):
        if key[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"

        elif key[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"

        elif key[pygame.K_UP] and self.direction != "down":
            self.direction = "up"

        elif key[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"

    def draw_snake(self, screen):
        for pos in self.snake_body:
            pygame.draw.rect(screen, (145, 25, 45), pygame.Rect(pos[0], pos[1], FOOD_SIZE, FOOD_SIZE))

    def eat_food(self, food):
        if self.snake_body[0] == food.food_position:
            self.game.game_score += 5
            food.random_food_pos()
            self.snake_length += 1

    def move_snake(self):
        if self.direction == "right":
            new_head = [
                self.snake_position[0] + self.motion,
                self.snake_position[1],
            ]
        if self.direction == "left":
            new_head = [
                self.snake_position[0] - self.motion,
                self.snake_position[1],
            ]
        if self.direction == "up":
            new_head = [
                self.snake_position[0],
                self.snake_position[1] - self.motion,
            ]
        if self.direction == "down":
            new_head = [
                self.snake_position[0],
                self.snake_position[1] + self.motion,
            ]

        self.snake_body.insert(0, new_head)
        self.snake_position = new_head

        if len(self.snake_body) > self.snake_length:
            self.snake_body.pop()
 
        print(self.snake_body)


class food:
    def __init__(self, game):
        self.game = game
        self.food_position = [
            random.randrange(1, (890 // FOOD_SIZE)) * FOOD_SIZE,
            random.randrange(1, (590 // FOOD_SIZE)) * FOOD_SIZE,
        ]

    def random_food_pos(self):
        self.food_position = [
            random.randrange(1, (890 // FOOD_SIZE)) * FOOD_SIZE,
            random.randrange(1, (590 // FOOD_SIZE)) * FOOD_SIZE,
        ]

    def draw_food(self, screen):
        # pygame.draw.circle(screen, (255, 255, 0), self.food_position, FOOD_SIZE)
        pygame.draw.rect(screen, (255, 255, 0), (self.food_position[0], self.food_position[1], FOOD_SIZE, FOOD_SIZE))


class game:
    def __init__(self): 
        self.snake_height = 10
        self.game_score = 0
        self.food = food(self)
        self.snake = snake(self)

    def test_collision(self,screen):
        if (
            self.snake.snake_position[0] < 0
            or self.snake.snake_position[1] > 600
            or self.snake.snake_position[0] > 900
            or self.snake.snake_position[1] < 0
        ):
            self.game_over(screen)
            pygame.quit()
            exit()

    def show_score(self, screen):
        font = pygame.font.Font(None,20)
        score = font.render(f"score : {self.game_score}", True, (144, 238, 144))
        screen.blit(score,(10,10))
    
    def game_over(self,screen):
        font = pygame.font.Font(None,50)
        score = font.render(f"score : {self.game_score}",True, (144,238,144) )
        message = font.render("GAME OVER!!!",True,(144,238,144))
        text_rect = message.get_rect(center = (450,300) )
        score_rect = score.get_rect(center = (450,350))
        screen.blit(message,text_rect)
        screen.blit(score,score_rect)
        pygame.display.update()
        pygame.time.wait(2000)

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Snake Game")
        fps = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    self.snake.key_movement(key)

            screen.fill((0, 0, 0))
            self.snake.move_snake()
            self.snake.eat_food(self.food)
            self.test_collision(screen)
            self.snake.draw_snake(screen)
            self.food.draw_food(screen)
            self.show_score(screen)

            pygame.display.update()

            fps.tick(30)


if __name__ == "__main__":
    snake_game = game()
    snake_game.start()