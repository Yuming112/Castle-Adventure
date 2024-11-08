import pygame
import sys
import os

# 初始化 Pygame
pygame.init()

# 定义屏幕的宽度和高度
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 50  # 每个单元格的大小

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 创建屏幕对象并设置窗口大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 设置窗口标题
pygame.display.set_caption("Castle Adventure")

# 设置帧率
FPS = 60
clock = pygame.time.Clock()

# 定义素材目录的路径
assets_dir = os.path.join( "素材", "古堡冒险素材")  # 确保素材文件路径正确

# 定义并加载素材文件路径
player_image_path = os.path.join(assets_dir, "正.bmp")
monster_a_image_path = os.path.join(assets_dir, "蝙蝠.bmp")
monster_b_image_path = os.path.join(assets_dir, "蛇.bmp")
monster_c_image_path = os.path.join(assets_dir, "鬼魂.bmp")
monster_d_image_path = os.path.join(assets_dir, "恐龙.bmp")
wall_image_path = os.path.join(assets_dir, "墙壁.bmp")
floor_image_path = os.path.join(assets_dir, "地面.bmp")
door_image_path = os.path.join(assets_dir, "门.bmp")
key_image_path = os.path.join(assets_dir, "钥匙.bmp")
treasure_image_path = os.path.join(assets_dir, "宝珠.bmp")

# 定义怪物类型及其战斗力
monster_types = {
    4: {"image": pygame.transform.scale(pygame.image.load(monster_a_image_path), (TILE_SIZE, TILE_SIZE)), "power": 5},
    6: {"image": pygame.transform.scale(pygame.image.load(monster_b_image_path), (TILE_SIZE, TILE_SIZE)), "power": 20},
    7: {"image": pygame.transform.scale(pygame.image.load(monster_c_image_path), (TILE_SIZE, TILE_SIZE)), "power": 40},
    8: {"image": pygame.transform.scale(pygame.image.load(monster_d_image_path), (TILE_SIZE, TILE_SIZE)), "power": 100}
}

# 地图数据定义（0 表示地板，1 表示墙壁，2 表示门，3 表示钥匙，4-8 表示不同种类的怪物，5 表示宝藏）
map_data_level1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 6, 0, 0, 0, 3, 1],
    [1, 1, 1, 0, 0, 4, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

map_data_level2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 7, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 7, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 地图类定义
class Map:
    def __init__(self, map_data, tile_size):
        self.map_data = map_data
        self.tile_size = tile_size
        # 加载并缩放地图元素
        self.floor_img = pygame.transform.scale(pygame.image.load(floor_image_path), (tile_size, tile_size))
        self.wall_img = pygame.transform.scale(pygame.image.load(wall_image_path), (tile_size, tile_size))
        self.door_img = pygame.transform.scale(pygame.image.load(door_image_path), (tile_size, tile_size))
        self.key_img = pygame.transform.scale(pygame.image.load(key_image_path), (tile_size, tile_size))
        self.treasure_img = pygame.transform.scale(pygame.image.load(treasure_image_path), (tile_size, tile_size))

    def draw(self, screen):
        """绘制地图上的每一个元素（地板、墙壁、门、钥匙、宝藏和怪物）"""
        for row in range(len(self.map_data)):
            for col in range(len(self.map_data[row])):
                x = col * self.tile_size
                y = row * self.tile_size
                tile = self.map_data[row][col]

                if tile == 0:
                    screen.blit(self.floor_img, (x, y))
                elif tile == 1:
                    screen.blit(self.wall_img, (x, y))
                elif tile == 2:
                    screen.blit(self.door_img, (x, y))
                elif tile == 3:
                    screen.blit(self.key_img, (x, y))
                elif tile == 5:
                    screen.blit(self.treasure_img, (x, y))  # 绘制宝藏
                elif tile in monster_types:
                    screen.blit(monster_types[tile]["image"], (x, y))  # 绘制不同种类的怪物


# 玩家类定义
class Player:
    def __init__(self, x, y, speed, power):
        # 初始化玩家属性和图像
        self.image = pygame.transform.scale(pygame.image.load(player_image_path), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 525)
        self.speed = speed
        self.power = power
        self.has_key = False
        self.is_alive = True

    def move(self, dx, dy, game_map):
        """移动玩家，检查碰撞和阻挡"""
        new_x, new_y = self.rect.x + dx, self.rect.y + dy
        for row in range(len(game_map.map_data)):
            for col in range(len(game_map.map_data[row])):
                if game_map.map_data[row][col] == 1:  # 墙壁
                    wall_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if wall_rect.collidepoint(new_x, new_y) or wall_rect.collidepoint(new_x + TILE_SIZE - 1,
                                                                                      new_y) or wall_rect.collidepoint(
                            new_x, new_y + TILE_SIZE - 1) or wall_rect.collidepoint(new_x + TILE_SIZE - 1,
                                                                                    new_y + TILE_SIZE - 1):
                        return
        self.rect.x, self.rect.y = new_x, new_y

    def draw(self, screen):
        """绘制玩家"""
        screen.blit(self.image, self.rect.topleft)


# 游戏开始和结束的滚动字幕类
class ScrollingText:
    def __init__(self, text, font, speed):
        self.text = text
        self.font = font
        self.speed = speed
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.rect = self.text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        self.finished = False

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.finished = True

    def draw(self, screen):
        screen.blit(self.text_surface, self.rect.topleft)


# 创建玩家对象
player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT - TILE_SIZE, speed=5, power=5)

# 层数
current_level = 1  # 当前层级
game_map = Map(map_data_level1, TILE_SIZE)  # 加载第一层地图

# 游戏开始滚动字幕
font = pygame.font.Font(None, 36)
intro_text = "Welcome to the Castle Adventure! Can you find the treasure?"
intro_scrolling_text = ScrollingText(intro_text, font, speed=2)

# 游戏结束滚动字幕
win_text = "Congratulations! You found the treasure! Game cleared!"
lose_text = "Unfortunately, the adventure has failed! Try again next time!"
end_scrolling_text = None

# 游戏状态变量
show_intro = True
show_ending = False
game_over = False

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充屏幕背景为白色
    screen.fill(WHITE)

    if show_intro:
        # 播放游戏开始的滚动字幕
        intro_scrolling_text.update()
        intro_scrolling_text.draw(screen)
        if intro_scrolling_text.finished:
            show_intro = False  # 滚动字幕结束，开始游戏
    elif show_ending:
        # 播放游戏结束滚动字幕
        end_scrolling_text.update()
        end_scrolling_text.draw(screen)
        if end_scrolling_text.finished:
            running = False  # 滚动字幕结束后退出游戏
    elif not game_over:
        # 游戏逻辑
        # 获取按键输入以移动玩家
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -player.speed
        if keys[pygame.K_RIGHT]:
            dx = player.speed
        if keys[pygame.K_UP]:
            dy = -player.speed
        if keys[pygame.K_DOWN]:
            dy = player.speed

        # 移动玩家
        player.move(dx, dy, game_map)

        # 检测玩家是否触碰怪物并战斗
        for row in range(len(game_map.map_data)):
            for col in range(len(game_map.map_data[row])):
                tile = game_map.map_data[row][col]
                if tile in monster_types:
                    monster_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    monster_power = monster_types[tile]["power"]
                    if player.rect.colliderect(monster_rect):
                        if player.power >= monster_power:
                            player.power += monster_power  # 玩家胜利
                            game_map.map_data[row][col] = 0  # 移除怪物
                        else:
                            game_over = True  # 游戏失败
                            show_ending = True
                            end_scrolling_text = ScrollingText(lose_text, font, speed=2)

        # 绘制地图和玩家
        game_map.draw(screen)
        player.draw(screen)

        # 显示玩家的战斗力
        power_text = font.render(f"战斗力: {player.power}", True, RED)
        screen.blit(power_text, (10, 10))

        # 绘制地图和玩家
        game_map.draw(screen)
        player.draw(screen)

        # 显示玩家的战斗力
        power_text = font.render(f"战斗力: {player.power}", True, RED)
        screen.blit(power_text, (10, 10))

        # 检测玩家是否触碰到钥匙或门
        for row in range(len(game_map.map_data)):
            for col in range(len(game_map.map_data[row])):
                tile = game_map.map_data[row][col]

                # 检查玩家是否拾取钥匙
                if tile == 3:  # 钥匙
                    key_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if player.rect.colliderect(key_rect):
                        player.has_key = True
                        game_map.map_data[row][col] = 0  # 移除钥匙

                # 检查玩家是否触碰到门
                if tile == 2:  # 门
                    door_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if player.rect.colliderect(door_rect):
                        if player.has_key:
                            print("进入第二层！")
                            current_level = 2
                            game_map = Map(map_data_level2, TILE_SIZE)  # 切换到第二层地图
                            player.rect.topleft = (13 * TILE_SIZE, 2 * TILE_SIZE)  # 将玩家重置到第二层起始位置
                            player.has_key = False  # 使用完钥匙，重置为没有钥匙
                        else:
                            print("需要钥匙才能打开门！")

                # 检测玩家是否触碰宝藏
            for row in range(len(game_map.map_data)):
                for col in range(len(game_map.map_data[row])):
                    tile = game_map.map_data[row][col]
                    if tile == 5:  # 5 表示宝藏
                        treasure_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        if player.rect.colliderect(treasure_rect):
                            found_treasure = True  # 标记宝藏找到
                            game_over = True
                            show_ending = True
                            end_scrolling_text = ScrollingText(win_text, font, speed=2)  # 显示通关字幕

        # 绘制地图和玩家
        game_map.draw(screen)
        player.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()
    clock.tick(FPS)

# 退出 Pygame
pygame.quit()
sys.exit()