import bpy

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Templater"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.operator('view3d.cursor_center', text="Center 3D cursor")
        row.operator('view3d.snap_pos', text="Snap Selected")
