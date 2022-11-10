import pygame as pg
import os

class Config:

    def __init__(self):

        self.pieces_themes = [
            'standard', 
            'classic', 
            'alpha'
            ]
        
        self.colors_themes = [
            Color('standard', (218, 218, 218), (173, 173, 173), (244, 247, 116), (172, 195, 51)),
            Color('green', (234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51)),
            Color('brown', (235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59)),
            Color('blue', (229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191)),
            Color('gray', (120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128)),
            ]

        self.theme = Theme(self.pieces_themes[0], self.colors_themes[0])

        self.color_idx = 0
        self.piece_idx = 0

        self.font = pg.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(os.path.join('assets/sounds/capture.wav'))

    def change_theme_color(self):
        
        self.color_idx += 1
        self.color_idx %= len(self.colors_themes)
        self.theme.color = self.colors_themes[self.color_idx]

    def change_theme_piece(self):
        
        self.piece_idx += 1
        self.piece_idx %= len(self.pieces_themes)
        self.theme.piece = self.pieces_themes[self.piece_idx]


class Color:

    def __init__(self, name, light, dark, light_trace, dark_trace):
        self.name = name
        self.light = light
        self.dark = dark
        self.light_trace = light_trace
        self.dark_trace = dark_trace


class Sound:

    def __init__(self, path):
        self.path = path
        self.sound = pg.mixer.Sound(path)
    
    def play(self):
        pg.mixer.Sound.play(self.sound)


class Theme:

    def __init__(self, piece, color):
        self.piece = piece
        self.color = color