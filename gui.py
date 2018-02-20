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
    def __init__(self, images, rect, name, value, on_click=None, selected=False):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.images = images
        self.rect = rect
        self.value = value
        self.on_click = on_click
        self.selected = selected

        self.update()
        self.update_buttons_group()

    def event_handler(self, event):
        """Handle the PyGame event if related to this radio buttons collection."""
        if event.type != pygame.MOUSEBUTTONDOWN or not self.rect.collidepoint(event.pos):
            return False

        for element in elements:
            if not isinstance(element, RadioButton) or element.name != self.name:
                continue

            element.selected = False

        self.selected = True

        self.update_buttons_group()

        if self.on_click:
            self.on_click(self)

        return True

    def update(self):
        if self.selected:
            self.image = self.images['selected']
        else:
            self.image = self.images['normal']

    def update_buttons_group(self):
        for element in elements:
            if not isinstance(element, RadioButton) or element.name != self.name:
                continue

            element.update()
