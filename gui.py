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
    def __init__(self, images, rect, value, selected):
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.rect = rect
        self.value = value
        self.selected = selected

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, selected):
        self._selected = selected

        if self._selected:
            self.image = self.images['selected']
        else:
            self.image = self.images['normal']


class RadioButtons(pygame.sprite.Group):
    """A collection of radio buttons."""
    def __init__(self, on_select=None, initial_value=None):
        pygame.sprite.Group.__init__(self)

        self.on_select = on_select
        self.selected_value = initial_value

    def event_handler(self, event):
        """Handle the PyGame event if related to this radio buttons collection."""
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False

        selected_radio_button = None

        # Check if the user realliy clicked on one of the radio buttons
        for radio_button in self.sprites():
            if radio_button.rect.collidepoint(event.pos):
                selected_radio_button = radio_button

                break

        if not selected_radio_button:
            return False

        # The user clicked on a radio button. Deselecte all other radio buttons of this set
        for radio_button in self.sprites():
            if radio_button == selected_radio_button:
                continue

            radio_button.selected = False

        selected_radio_button.selected = True

        self.selected_value = selected_radio_button.value

        if self.on_select is not None:
            self.on_select(selected_radio_button)

        return True
