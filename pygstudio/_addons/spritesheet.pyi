"""Simple spritesheet for game developing. [v1.0]"""

from __future__ import annotations

from pygame import _common, Surface

__all__ = []

class SpriteSheet:
    """A basic spritesheet for basic operations"""
    def __init__(self, image_path: str, spritesheet_details: dict[str, _common.RectValue]) -> None:
        self.spritesheet_details: dict[str, _common.RectValue]
        self.image_path: str
        self.image: Surface

    def get_sprite(self, name: str) -> Surface:
        """Return a sprite's surface given its name."""
        
    def render(self, name: str, surface: Surface, rect: _common.RectValue | _common.Coordinate):
        """Render a sprite from the spritesheet"""

class CostumeSpriteSheet:
    """A spritesheet for costumes like characters or animated sprites."""
    def __init__(self, image_path: str, sprite_size: tuple[int, int], init_number: int = 0) -> None:
        self.image_path: str
        self.sprite_size: tuple[int, int]
        self.current_costume: int
        self.image: Surface
        self.image_size: tuple[int, int]

    def get_sprite_position(self, number: int) -> tuple[int, int]:
        """Get a sprite's position in the spritesheet given the costume number"""

    def get_sprite_rect(self, number: int) -> tuple[int, int, int, int]:
        """Get a sprite's position in the spritesheet given the costume number"""
        
    def render(self, surface: Surface, rect: _common.RectValue) -> None:
        """Render the current sprite from the spritesheet"""

    def set_costume(self, number: int) -> None:
        """Sets the costume number of this sprite"""

    def get_costume(self) -> int:
        """Gets the costume number of this sprite"""

    def get_sprite(self, number) -> Surface:
        """Gets the surface image of the sprite given its costume number"""
