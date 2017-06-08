"""
"""
from ipywidgets import widget_serialization, Color
from traitlets import (
    Unicode, CInt, Instance, Float, Tuple, link)

from ..enums import *
from ..traits import *

from .._base.Three import RenderableWidget
from ..scenes.Scene_autogen import Scene
from ..cameras.Camera_autogen import Camera
from ..controls.Controls_autogen import Controls

to_json = widget_serialization['to_json']
from_json = widget_serialization['from_json']

class Renderer(RenderableWidget):
    """Renderer

    Author: @vidartf
    """

    _view_name = Unicode('RendererView').tag(sync=True)
    _model_name = Unicode('RendererModel').tag(sync=True)

    width = CInt(200)
    height = CInt(200)
    scene = Instance(Scene).tag(sync=True, **widget_serialization)
    camera = Instance(Camera).tag(sync=True, **widget_serialization)
    controls = Tuple(Instance(Controls)).tag(sync=True, **widget_serialization)
    #effect = Instance(Effect, allow_none=True).tag(sync=True, **widget_serialization)
    background = Color('black', allow_none=True).tag(sync=True)
    background_opacity = Float(min=0.0, max=1.0).tag(sync=True)

    def __init__(self, **kwargs):
        super(Renderer, self).__init__(**kwargs)
        link((self, 'width'), (self, '_width'))
        link((self, 'height'), (self, '_height'))

    def render(self, scene, camera):
        content = {
            "type": "render",
            "scene": to_json(scene, None),
            "camera": to_json(camera, None)
        }
        self.send(content)

    def freeze(self):
        content = {
            "type": "freeze"
        }
        self.send(content)

