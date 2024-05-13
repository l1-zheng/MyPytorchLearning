import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(al_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, al_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship, al_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(al_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 快捷键Q退出
        sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(al_settings, screen, ship, bullets, aliens):
    # 每次循环时都重绘屏幕
    screen.fill(al_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blit_me()
    # aliens.blit_me()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    if check_aliens_bottom(al_settings, aliens):
        print("Game Over!!!")
        sleep(3)
        sys.exit()


def update_bullets(bullets, aliens, al_settings, screen, ship):
    """更新子弹位置，并删除消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 碰撞时，子弹不消失，外星人消失,并不断产生新的外星人
    check_bullet_alien_collisions(al_settings, screen, ship, aliens, bullets)


def update_aliens(al_settings, aliens,ship):
    """检查是否到达边缘"""
    check_fleet_edges(al_settings, aliens)
    # 更新外星人的位置
    aliens.update()
    # 外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # 外星人与飞船碰撞音~
        sound = pygame.mixer.Sound('musics/collision_ship.mp3')
        sound.play()
        print("Ship is dangerous!!!")


def fire_bullet(al_settings, screen, ship, bullets):
    # 创建一颗子弹，并加入到Group,数量不超过预设
    if len(bullets) < al_settings.bullet_allowed:
        new_bullet = Bullet(al_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(al_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    available_space_x = al_settings.screen_width - 2 * alien_width
    number_aliens_x = get_number_aliens_x(al_settings, alien_width)
    number_rows = get_number_rows(al_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        # 创建每行外星人
        for alien_number in range(number_aliens_x):
            create_alien(al_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(al_settings,alien_width):
    """计算一行可容纳多少个外星人"""
    available_space_x = al_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(al_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (al_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(al_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2*alien.rect.height * row_number
    aliens.add(alien)


def check_fleet_edges(al_settings, aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(al_settings, aliens)
            break


def check_aliens_bottom(al_settings, aliens):
    """检查是否有外星人到达屏幕底部"""
    for alien in aliens.sprites():
        if alien.check_bottom():
            return True


def change_fleet_direction(al_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += al_settings.fleet_drop_speed
    al_settings.fleet_direction *= -1


def check_bullet_alien_collisions(al_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 子弹与外星人碰撞音~
        sound = pygame.mixer.Sound('musics/collision_gun.mp3')
        sound.play(1)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(al_settings, screen, ship, aliens)
