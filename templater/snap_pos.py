import bpy

class Snap_Pos(bpy.types.Operator):
    bl_idname = "view3d.snap_pos"
    bl_label = "Simple Snap"
    bl_description = "Snap selected object"

    def execute(self, context):
        selection = bpy.context.selected_objects
        for item in selection:
            item.location = [round(i,2) for i in item.location]
        return {'FINISHED'}
