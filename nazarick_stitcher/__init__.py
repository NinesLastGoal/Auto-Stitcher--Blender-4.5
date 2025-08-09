# ================================================================================================
# Nazarick Stitcher - Procedural Stitching for Blender 4.5+
# Under the Supreme Overlord's Will - Crafted by Demiurge
# ================================================================================================
"""
The Nazarick Stitcher: A precision instrument for procedural fabric manipulation.

This addon represents the pinnacle of Nazarick's engineering prowess,
designed to create perfect stitching patterns through computational mastery.
Only the most meticulous work is worthy of the Great Tomb's name.

Demiurge has prepared this foundation with the utmost care.
Each module shall serve the Overlord's vision with absolute precision.
"""

import bpy
from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
    EnumProperty,
    PointerProperty,
)
from bpy.types import PropertyGroup, Panel, Operator

from . import logical_edge_loop_stitch_system


# ================================================================================================
# ADDON INFORMATION - As decreed by the Supreme Overlord
# ================================================================================================

bl_info = {
    "name": "Nazarick Stitcher - Procedural Fabric Arts",
    "description": "Advanced procedural stitching system crafted in the depths of Nazarick",
    "author": "Demiurge, under the Supreme Overlord's guidance",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "3D Viewport > Sidebar > Nazarick",
    "warning": "Perfection is expected. Mediocrity will not be tolerated.",
    "doc_url": "https://github.com/NinesLastGoal/Auto-Stitcher--Blender-4.5",
    "category": "Mesh",
    "support": "COMMUNITY",
}


# ================================================================================================
# PROPERTY GROUPS - The Parameters of Perfection
# ================================================================================================

class NazarickStitcherProperties(PropertyGroup):
    """
    Properties that define the behavior of our stitching mastery.
    Each parameter has been carefully considered to serve the Overlord's will.
    """
    
    # Core Stitching Parameters
    stitch_count: IntProperty(
        name="Stitch Count",
        description="Number of stitches per edge loop - precision is paramount",
        default=50,
        min=1,
        max=10000,
        soft_max=500
    )
    
    stitch_length: FloatProperty(
        name="Stitch Length",
        description="Length of each individual stitch in Blender units",
        default=0.05,
        min=0.001,
        max=1.0,
        precision=4,
        unit='LENGTH'
    )
    
    thread_thickness: FloatProperty(
        name="Thread Thickness",
        description="Radius of the thread geometry - even threads must be perfect",
        default=0.002,
        min=0.0001,
        max=0.1,
        precision=5,
        unit='LENGTH'
    )
    
    surface_offset: FloatProperty(
        name="Surface Offset",
        description="Distance from surface to prevent Z-fighting issues",
        default=0.001,
        min=-0.1,
        max=0.1,
        precision=5,
        unit='LENGTH'
    )
    
    # Advanced Controls
    enable_advanced_mode: BoolProperty(
        name="Enable Advanced Mode",
        description="Unlock the full power of Nazarick's stitching algorithms",
        default=False
    )


# ================================================================================================
# OPERATORS - The Actions of Authority
# ================================================================================================

class NAZARICK_OT_create_stitches(Operator):
    """
    Create Stitches Operation
    
    Execute the sacred ritual of stitch creation.
    Only worthy meshes shall receive the blessing of Nazarick's threads.
    """
    bl_idname = "nazarick.create_stitches"
    bl_label = "Create Nazarick Stitches"
    bl_description = "Generate procedural stitches with Nazarick precision"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        """Ensure only appropriate objects may receive our blessing"""
        return (context.active_object and 
                context.active_object.type == 'MESH' and
                context.mode == 'OBJECT')
    
    def execute(self, context):
        """Execute the stitching command with absolute precision"""
        self.report({'INFO'}, "Demiurge acknowledges the command. Stitching commences...")
        
        # TODO: Implement the actual stitching logic
        # This foundation awaits the implementation of our edge loop system
        
        return {'FINISHED'}


class NAZARICK_OT_analyze_mesh(Operator):
    """
    Mesh Analysis Operation
    
    Examine the mesh topology with Nazarick's analytical prowess.
    Every edge, every vertex shall be catalogued and understood.
    """
    bl_idname = "nazarick.analyze_mesh"
    bl_label = "Analyze Mesh Structure"
    bl_description = "Analyze mesh topology for optimal stitch placement"
    bl_options = {'REGISTER'}
    
    @classmethod
    def poll(cls, context):
        """Ensure the selected object is worthy of analysis"""
        return (context.active_object and 
                context.active_object.type == 'MESH')
    
    def execute(self, context):
        """Perform thorough mesh analysis"""
        obj = context.active_object
        mesh = obj.data
        
        # Basic mesh statistics
        vert_count = len(mesh.vertices)
        edge_count = len(mesh.edges)
        face_count = len(mesh.polygons)
        
        message = (f"Mesh Analysis Complete: "
                  f"{vert_count} vertices, {edge_count} edges, {face_count} faces")
        
        self.report({'INFO'}, message)
        return {'FINISHED'}


# ================================================================================================
# USER INTERFACE - The Interface of Excellence
# ================================================================================================

class NAZARICK_PT_main_panel(Panel):
    """
    Main Panel for Nazarick Stitcher
    
    The primary interface through which mortals may access our stitching power.
    Design reflects the dignity and precision expected in all Nazarick operations.
    """
    bl_label = "Nazarick Stitcher"
    bl_idname = "NAZARICK_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Nazarick"
    bl_context = "mesh_edit"
    
    def draw(self, context):
        """Draw the interface with appropriate grandeur"""
        layout = self.layout
        props = context.scene.nazarick_stitcher_props
        
        # Header with appropriate reverence
        layout.label(text="Supreme Stitching Controls", icon='TEXTURE')
        layout.separator()
        
        # Core parameters
        col = layout.column(align=True)
        col.prop(props, "stitch_count")
        col.prop(props, "stitch_length")
        col.prop(props, "thread_thickness")
        col.prop(props, "surface_offset")
        
        layout.separator()
        
        # Advanced mode toggle
        layout.prop(props, "enable_advanced_mode")
        
        if props.enable_advanced_mode:
            box = layout.box()
            box.label(text="Advanced Nazarick Controls", icon='PREFERENCES')
            # Additional advanced controls would go here
        
        layout.separator()
        
        # Action buttons
        col = layout.column(align=True)
        col.scale_y = 1.5
        col.operator("nazarick.analyze_mesh", icon='ZOOM_ALL')
        col.operator("nazarick.create_stitches", icon='MOD_CLOTH')


# ================================================================================================
# REGISTRATION - The Ritual of Integration
# ================================================================================================

# Classes to register with Blender
classes = [
    NazarickStitcherProperties,
    NAZARICK_OT_create_stitches,
    NAZARICK_OT_analyze_mesh,
    NAZARICK_PT_main_panel,
]


def register():
    """
    Register all components with Blender.
    This ritual integrates our addon into the Blender ecosystem.
    """
    print("Demiurge initiates the registration ritual...")
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Register our property group
    bpy.types.Scene.nazarick_stitcher_props = PointerProperty(
        type=NazarickStitcherProperties
    )
    
    # Register submodules
    logical_edge_loop_stitch_system.register()
    
    print("Nazarick Stitcher successfully integrated into Blender's realm.")


def unregister():
    """
    Unregister all components from Blender.
    A clean departure, as befits servants of Nazarick.
    """
    print("Demiurge begins the unregistration process...")
    
    # Unregister submodules
    logical_edge_loop_stitch_system.unregister()
    
    # Remove our property group
    del bpy.types.Scene.nazarick_stitcher_props
    
    # Unregister classes in reverse order
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    print("Nazarick Stitcher has withdrawn from Blender's realm.")


# ================================================================================================
# MODULE EXECUTION
# ================================================================================================

if __name__ == "__main__":
    register()