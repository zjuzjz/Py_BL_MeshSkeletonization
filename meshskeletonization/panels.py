import bpy;
from meshskeletonization.operators import MeshContractionByLaplacian

#
#    Menu in UI region
#
class MeshContractionPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_meshcontractionpanel"
    bl_label = "Mesh Contraction";
    bl_space_type = "VIEW_3D";
    bl_region_type = "TOOLS";
    bl_category = "Mesh Skeletonization"
    bl_description = "Panel to operate on the mesh contraction process"
    
    def draw(self, context):
        
        if(context.active_object):
            layout = self.layout;
            row = layout.row(align=True);
            row.prop(context.active_object, "iterations");
            
            row = layout.row(align=True);
            row.prop(context.active_object, "sl");
            
            row = layout.row(align=True);
            row.prop(context.active_object, "wc");
            
            row = layout.row(align=True);
            row.operator(MeshContractionByLaplacian.bl_idname);


def register():
    bpy.utils.register_class(MeshContractionPanel);

def unregister():
    bpy.utils.unregister_class(MeshContractionPanel);