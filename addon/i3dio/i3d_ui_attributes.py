#!/usr/bin/env python3

"""
    ##### BEGIN GPL LICENSE BLOCK #####
  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software Foundation,
  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 ##### END GPL LICENSE BLOCK #####
"""

import bpy
from bpy.types import (
    Panel
)

from bpy.props import (
    PointerProperty
)

from . import i3d_properties


class I3D_IO_PT_transform_attributes(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_label = "I3D Transform Attributes"
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        obj = bpy.context.active_object

        layout.prop(obj.i3d_attributes, "clip_distance")
        layout.prop(obj.i3d_attributes, "min_clip_distance")


class I3D_IO_PT_shape_attributes(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_label = "I3D Shape Attributes"
    bl_context = 'data'

    @classmethod
    def poll(cls, context):
        if context.object is not None:
            return context.object.type == 'MESH'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        obj = bpy.context.active_object.data

        layout.prop(obj.i3d_attributes, "casts_shadows")
        layout.prop(obj.i3d_attributes, "receive_shadows")


class I3D_IO_PT_light_attributes(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_label = "I3D Light Attributes"
    bl_context = 'data'

    @classmethod
    def poll(cls, context):
        if context.object is not None:
            return context.object.type == 'LIGHT'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        obj = bpy.context.active_object.data

        layout.prop(obj.i3d_attributes, "depth_map_bias")
        layout.prop(obj.i3d_attributes, "depth_map_slope_scale_bias")


classes = (I3D_IO_PT_transform_attributes,
           I3D_IO_PT_shape_attributes,
           I3D_IO_PT_light_attributes
           )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
