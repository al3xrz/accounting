from .base import BaseDAO
from models.playground import Playground

class PlaygroundDAO(BaseDAO):
    model = Playground
    