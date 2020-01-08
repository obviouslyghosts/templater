#
#
#

bl_info = {
    "name" : "templater",
    "author" : "Obviously Ghosts",
    "location" : "View3D",
    "version" : (0, 0, 1),
    "blender" : (2, 80, 0),
    "description" : "template",
    "warning" : "personal use only!",
    "category" : "3D View"
}

import bpy
from . test_op import Test_OT_Operator
from . test_panel import Test_PT_Panel
from . snap_pos import Snap_Pos

def register():
    bpy.utils.register_class(Test_OT_Operator)
    bpy.utils.register_class(Test_PT_Panel)
    bpy.utils.register_class(Snap_Pos)

def unregister():
    bpy.utils.unregister_class(Test_OT_Operator)
    bpy.utils.unregister_class(Test_PT_Panel)
    bpy.utils.unregister_class(Snap_Pos)


#register, unregister = bpy.utils.register_classes_factory(classes)
if __name__ == "__main__":
    register()
