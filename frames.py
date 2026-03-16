from .log4r import logout

class WidgetFrame:
    def __init__(
            self,
            interface,  
            x: int, 
            y: int, 
            width: int | None = None, 
            height: int | None = None, 
            is_visible: bool = True,
        ) -> None:

        self._widget_list: list = []

        self._interface = interface
        self._x, self._y = x, y

        if width is None or height is None: 
            self._width = self._interface._w - self._x
            self._height = self._interface._h - self._y
        
        else:
            self._width, self._height = width, height
    
    def registerWidget(self, widget_self: any) -> None:
        self._widget_list.append(widget_self)

        # Attetion: if widget self have a recalculateCoordinate()!
        if hasattr(widget_self, 'recalculateCoordinate'):
            widget_self.recalculateCoordinate()
        
    def translateToAbsloteAxis(self, relative_x: int, relative_y: int): 
        # Attention: negative number is not allowed!
        # relative_x, relative_y = abs(relative_x), abs(relative_y)
        relative_x, relative_y = max(0, relative_x), max(0, relative_y)

        return self._x + relative_x, self._y + relative_y