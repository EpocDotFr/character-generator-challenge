import pygame

elements = []


def draw(surface):
    """Draw all the GUI elements on the specified surface."""
    for element in elements:
        if isinstance(element, pygame.sprite.Group):
            element.draw(surface)
        elif isinstance(element, pygame.sprite.Sprite):
            surface.blit(element.image, element.rect)


def add(element):
    """Add an element to the GUI elements list."""
    elements.append(element)


def event_handler(event):
    """Handles all GUI-related events."""
    for element in elements:
        if element.event_handler(event):
            return True

    return False


class Button(pygame.sprite.Sprite):
    """A simple button."""
    def __init__(self, image, rect, on_click=None):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = rect
        self.on_click = on_click

    def event_handler(self, event):
        """Handle the PyGame event and run the appropriate callbacks if related to this button."""
        if self.on_click is None or event.type != pygame.MOUSEBUTTONDOWN or not self.rect.collidepoint(event.pos):
            return False

        self.on_click(self)

        return True


class RadioButton(pygame.sprite.Sprite):
    """A radio button."""
    def __init__(self, images, rects, value):
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.rects = rects
        self.value = value
        self.selected = False

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, selected):
        self._selected = selected

        if self._selected:
            self.image = self.images['normal']
            self.rect = self.rects['normal']
        else:
            self.image = self.images['selected']
            self.rect = self.rects['selected']


class RadioButtons(pygame.sprite.Group):
    """A collection of radio buttons."""
    def __init__(self, on_select):
        pygame.sprite.Group.__init__(self)

        self.on_select = on_select

    def event_handler(self, event):
        """Handle the PyGame event and run the appropriate callbacks if related to this radio buttons collection."""
        if self.on_select is None or event.type != pygame.MOUSEBUTTONDOWN:
            return False

        for radio_button in self.sprites():
            if radio_button.rect.collidepoint(event.pos):
                self.on_select(radio_button)

                radio_button.selected = True

                return True
            # else:
            #    radio_button.selected = False

        return False
