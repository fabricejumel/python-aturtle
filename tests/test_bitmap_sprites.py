# ----------------------------------------------------------------------------
# Python A-Turtle
# ----------------------------------------------------------------------------
# Copyright (c) Tiago Montes.
# See LICENSE for details.
# ----------------------------------------------------------------------------

from aturtle import sprites

from . import base
from . import fake_tkinter



class FakeBitmapShape:

    def __init__(self, anchor=(42, 24)):
        self.anchor = anchor

    def __getitem__(self, angle):
        return f'image-at-angle-{angle}'



class TestDefaultSprite(base.TestCase):

    def setUp(self):

        self.canvas = fake_tkinter.Canvas()


    def test_create(self):

        _sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())


    def test_default_anchor(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())
        self.assert_almost_equal_anchor(sprite.anchor, (0, 0), places=1)


    def test_default_angle(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())
        self.assertAlmostEqual(sprite.angle, 0, places=1)


    def test_create_calls_canvas_create_image(self):

        shape = FakeBitmapShape(anchor=(10, 10))
        _sprite = sprites.BitmapSprite(self.canvas, shape)

        create_image = self.canvas.create_image
        create_image.assert_called_once_with(
            -10,
            -10,
            image='image-at-angle-0',
            anchor='sw',
        )


    def test_direct_rotate_calls_canvas_itemconfig_with_rotated_shape(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())
        sprite.direct_rotate(180)

        canvas_itemconfig = self.canvas.itemconfig
        canvas_itemconfig.assert_called_once_with(
            24,
            image='image-at-angle-180',
        )


    def test_direct_rotate_around_point_rotates_anchor(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())

        sprite.direct_rotate(180, around=(1, 1))
        self.assert_almost_equal_anchor(sprite.anchor, (2, 2), places=1)


    def test_direct_rotate_around_point_calls_canvas_itemconfig(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())

        sprite.direct_rotate(180, around=(1, 1))

        canvas_itemconfig = self.canvas.itemconfig
        canvas_itemconfig.assert_called_once_with(
            24,
            image='image-at-angle-180',
        )


    def test_direct_rotate_around_point_calls_canvas_move(self):

        shape = FakeBitmapShape(anchor=(0, 0))
        sprite = sprites.BitmapSprite(self.canvas, shape)

        sprite.direct_rotate(180, around=(1, 1))

        canvas_move = self.canvas.move
        canvas_move.assert_called_once_with(24, 2, 2)


    def test_direct_rotate_does_not_call_canvas_update(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())
        sprite.direct_rotate(1)
        self.canvas.update.assert_not_called()


    def test_direct_rotate_with_update_calls_canvas_update(self):

        sprite = sprites.BitmapSprite(self.canvas, FakeBitmapShape())
        sprite.direct_rotate(1, update=True)
        self.canvas.update.assert_called_once_with()
