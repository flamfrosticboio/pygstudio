from typing import Any
from collections import deque

class _GameGlobals:
    def __init__(self) -> None:
        self._globals = {}
        
        self._running = False
        self._guis = deque()
        self._interactables = deque()
        
    def __getattribute__(self, name: str) -> Any:
        if name.startswith("_"): return super().__getattribute__(name)
        return self._globals.get(name)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"): super().__setattr__(name, value)
        else: self._globals[name] = value
    
GameGlobals = _GameGlobals()