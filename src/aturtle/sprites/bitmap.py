# ----------------------------------------------------------------------------
# Python A-Turtle
# ----------------------------------------------------------------------------
# Copyright (c) Tiago Montes.
# See LICENSE for details.
# ----------------------------------------------------------------------------

from . import base


class Sprite(base.Sprite):

    def __init__(self, canvas, shape, *, anchor=(0, 0), angle=0):

        super().__init__(canvas, shape, anchor=anchor, angle=angle)

        sprite_x, sprite_y = anchor
        shape_x, shape_y = shape.anchor
        self._id = self._canvas.create_image(
            sprite_x - shape_x,
            sprite_y - shape_y,
            image=shape[angle],
            anchor='nw',
        )


    def rotate(self, angle=0, *, around=None, update=False):

        # Rotate anchor point if needed.
        super().rotate(angle, around=around, update=False)

        # Anchor point rotated, move the shape.
        if around:
            sprite_x, sprite_y = self._anchor
            shape_x, shape_y = self._shape.anchor
            self._canvas.moveto(
                self._id,
                sprite_x - shape_x,
                sprite_y - shape_y,
            )

        # Use the pre-rendered shape for the new orientation.
        self._canvas.itemconfig(self._id, image=self._shape[self._angle])

        if update:
            self.update()
