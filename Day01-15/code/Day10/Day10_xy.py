import pygame


def main_tkinter():
    import tkinter
    import tkinter.messagebox
    flag = True

    # 修改标签文字
    def change_label_text():
        # 当在一个嵌套的函数中对变量申明为nonlocal时，就明确表示这个变量是外部函数中定义的变量
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') \
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('information', 'Do you want to quit?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    top.geometry('320x240')
    top.title('Game')
    # 创建标签对象
    label = tkinter.Label(top, text='A new game', font='Arial -32', fg='black')
    label.pack(expand=1)  # what is label.pack
    # 创建按钮容器
    pane1 = tkinter.Frame(top)
    # 创建按钮对象，指定添加到哪个容器中，通过command绑定时间回调函数
    button1 = tkinter.Button(pane1, text='Change', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(pane1, text='Quit', command=confirm_to_quit)
    button2.pack(side='right')
    pane1.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


def main_pygame():
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # screen initialize with size
    pygame.display.set_caption('BIG ball eats the little ball')  # title
    x, y = 50, 50
    # screen.fill((242,242,242))  # base color, tuple with RGB values
    # ball_image = pygame.image.load('G:/Python/Python-100-Days/Day01-15/res/ball.png')
    # pygame.draw.circle(screen, (255, 100, 90), (100, 100), 30, 0)  # scree, color, center, radius, 0-circle
    # screen.blit(ball_image, (50, 50))
    # pygame.display.flip()
    running = True

    while running and y < 600:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        pygame.time.delay(50)  # refresh screen in 50 ms
        x, y = x + 5, y + 5


from enum import Enum, unique
from math import sqrt
from random import randint


@unique
class Color(Enum):  # Enum, 枚举，Color直接继承Enum类

    # enum中，成员名不能重复
    # 当Class中有重复值时，会返回第一个，其他忽略（被认为是第一个的别名）
    # 用@unique用来检查重复值，则值也不能重复

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main_ballgame():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('BIG eats small')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10,10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255,255,255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main_ballgame()
