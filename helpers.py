import settings
import pygame
import os


def _get_resource_path(res_type, filename):
    """Get the path to a resource."""
    path = os.path.join(settings.RESOURCES_ROOT, res_type, filename)

    if not os.path.isfile(path):
        raise ValueError('The file ' + path + ' doesn\'t exist')

    return path


def load_image(filename):
    """Load an image."""
    path = _get_resource_path('images', filename)

    return pygame.image.load(path).convert_alpha()


def load_font(filename, size):
    """Load a font file."""
    path = _get_resource_path('fonts', filename)

    return pygame.font.Font(path, size)
