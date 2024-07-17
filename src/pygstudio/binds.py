class _Bindables:
    def __init__(self) -> None:
        self.preinit = lambda: None
        self.preload = lambda: None
        self.exit = lambda: None
        
    def set_preinit(self, function):
        self.preinit = function
        
    def set_preload(self, function):
        self.preload = function
        
    def set_exit(self, function):
        self.exit = function
        
BindFunctions = _Bindables()