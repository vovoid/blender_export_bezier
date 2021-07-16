# <pep8-80 compliant>

bl_info = {
    "name": "Bezier Exporter",
    "author": "Jonatan Wallmander",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "File > Export",
    "description": "Export beziers (VBZ) to VSXu",
    "warning": "",
    "wiki_url": "",
    "support": 'OFFICIAL',
    "category": "Import-Export"}

if "bpy" in locals():
     import importlib
     if "export_vbz" in locals():
         importlib.reload(export_vbz)

import bpy
from bpy.props import (
        BoolProperty,
        FloatProperty,
        StringProperty,
        EnumProperty,
        )
from bpy_extras.io_utils import (
        ImportHelper,
        ExportHelper,
        orientation_helper,
        path_reference_mode,
        axis_conversion,
        )

@orientation_helper(axis_forward='-Z', axis_up='Y')
class ExportBezier(bpy.types.Operator, ExportHelper):
    """Save a VBZ File"""

    bl_idname = "export_scene.vbz"
    bl_label = 'Export VBZ'
    bl_options = {'PRESET'}

    filename_ext = ".vbz"
    filter_glob: StringProperty(
            default="*.vbz",
            options={'HIDDEN'},
            )

    path_mode: path_reference_mode

    check_extension = True

    def execute(self, context):
        from . import export_vbz

        from mathutils import Matrix
        keywords = self.as_keywords()

        # global_matrix = (Matrix.Scale(self.global_scale, 4) @
        #                  axis_conversion(to_forward=self.axis_forward,
        #                                  to_up=self.axis_up,
        #                                  ).to_4x4())

        # keywords["global_matrix"] = global_matrix
        return export_vbz.save(context, keywords['filepath'])


def menu_func_export(self, context):
    self.layout.operator(ExportBezier.bl_idname, text="VSXu Bezier [Selected] (.vbz)")


classes = (
    ExportBezier,
)


def register():
    bpy.utils.register_class(ExportBezier)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.utils.unregister_class(ExportBezier)


if __name__ == "__main__":
    register()
