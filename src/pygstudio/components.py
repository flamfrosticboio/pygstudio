from typing import Tuple, Union, List, Iterable, Protocol, Optional, overload, runtime_checkable

from pygstudio import utils
from pygame import Rect, Surface
from pygame.display import get_window_size

number = Union[int, float]
coordinate = Union[Tuple[number, number], List[number]]
rect_type = Union[Tuple[number, number, number, number], List[number], Rect]
@runtime_checkable
class ParentType(Protocol):
    def get_bounds(self) -> Tuple[number, number, number, number]: ...
parent_type = Union[rect_type, Rect, ParentType]

# will make pyi after completion

class Udim2:
    @overload
    def __init__(self, scale: coordinate, offset: coordinate, /): ...
    @overload
    def __init__(self, scale_x: number, offset_x: number, scale_y: number, offset_y: number, /): ...
    @overload
    def __init__(self, iterable: Iterable[number], /): ...
    
    # Actual Implementation
    def __init__(self, *args) -> None:
        self.scale: tuple[number, number]
        self.offset: tuple[number, number]
        
        _signature_length = len(args)
        if _signature_length == 2:
            self.scale = tuple(args[0])
            self.offset = tuple(args[1])
        elif _signature_length == 4:
            self.scale = args[0], args[1]
            self.offset = args[2], args[3]
        elif _signature_length == 1:
            _iter = iter(args[0])
            self.scale = next(_iter), next(_iter)
            self.offset = next(_iter), next(_iter)
        else:
            raise TypeError("Invalid arguments passed!")
        
    def point(self, parent_rect: rect_type = (0, 0, 0, 0)):
        return self.offset[0] + parent_rect[0] + parent_rect[2] * self.scale[0], \
            self.offset[1] + parent_rect[1] + parent_rect[3] * self.scale[1]

class BaseGui:
    def __init__(self, position: Udim2, size: Udim2, parent: Optional[parent_type] = None, zindex: int = 0) -> None:
        self.position: Udim2 = position
        self.size: Udim2 = size
        self.parent: Optional[parent_type] = parent
        self.zindex: int = zindex
        
    def set_position(self, position: Udim2): self.position = position
    def set_size(self, size: Udim2): self.size = size
    def set_parent(self, parent: Optional[parent_type]): self.parent = parent
    def set_zindex(self, zindex: int = 0): self.zindex = zindex
    def render(self, surface: Surface): raise NotImplementedError("This method is an abstract")
    
    def get_parent_value(self) -> rect_type:
        if not self.parent:
            return 0, 0, *get_window_size()
        elif isinstance(self.parent, ParentType):
            return self.parent.get_bounds()
        return self.parent
    
class Frame(BaseGui):
    def __init__(self, position: Udim2, size: Udim2, parent: Optional[parent_type] = None) -> None:
        super().__init__(position, size, parent)
        self.image = Surface(self.size.point(self.get_parent_value()))
    
    def get_bounds(self):
        parent_value = self.get_parent_value()
        return *self.position.point(parent_value), *self.size.point(parent_value)
    
    def render(self, surface: Surface):
        surface.blit(self.image, self.position.point(self.get_parent_value()))
        