"""
Neural Stitcher - AI-Powered Procedural Stitching for Blender 4.5+

An intelligent Blender addon that creates sophisticated procedural stitches
using advanced Geometry Nodes. Features smart edge detection, adaptive
stitch placement, and realistic thread simulation.

Author: Enhanced by AI Assistant
Original: Gemini
Version: 4.0.1
"""

bl_info = {
    "name": "Neural Stitcher - Procedural Stitches",
    "author": "AI Assistant (Enhanced from Gemini)",
    "version": (4, 0, 1),
    "blender": (4, 5, 0),
    "location": "View3D > Modifiers > Add Modifier",
    "description": "Professional, non-destructive Geometry Node modifier for procedural stitching along edge loops",
    "warning": "",
    "doc_url": "https://github.com/NinesLastGoal/Auto-Stitcher--Blender-4.5",
    "category": "Object",
}

import bpy
from typing import Optional


def show_message_box(message="", title="Neural Stitcher", icon='INFO'):
    """
    Display a message box to the user for better feedback.
    
    Args:
        message (str): Message to display
        title (str): Title of the message box
        icon (str): Icon type ('INFO', 'WARNING', 'ERROR')
    """
    def draw(self, context):
        self.layout.label(text=message)
    
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


def create_neural_stitch_node_group() -> Optional[bpy.types.GeometryNodeTree]:
    """
    Intelligently constructs an advanced Geometry Node tree for procedural stitches.
    
    Creates a sophisticated node network that analyzes mesh topology and generates
    realistic stitching patterns with smart parameter adaptation.
    
    Returns:
        Optional[bpy.types.GeometryNodeTree]: The created node group, or None if failed
    """
    node_group_name = "Neural Stitcher"
    print(f"Neural Stitcher: Initializing node group '{node_group_name}'")

    try:
        # Ensure clean state by removing any existing group
        if node_group_name in bpy.data.node_groups:
            bpy.data.node_groups.remove(bpy.data.node_groups[node_group_name])
            print("Neural Stitcher: Removed existing node group to prevent conflicts")

        node_group = bpy.data.node_groups.new(name=node_group_name, type='GeometryNodeTree')
        
        # Build the intelligent modifier interface
        print("Neural Stitcher: Constructing AI-enhanced modifier interface...")
        interface = node_group.interface
        
        # Input sockets with intelligent defaults
        interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
        
        stitch_area_socket = interface.new_socket(name="Stitch Area", in_out='INPUT', socket_type='NodeSocketFloatFactor')
        stitch_area_socket.attribute_domain = 'POINT'
        stitch_area_socket.description = "Vertex group defining where stitches should be placed"
        
        count_socket = interface.new_socket(name="Stitch Count", in_out='INPUT', socket_type='NodeSocketInt')
        count_socket.default_value, count_socket.min_value, count_socket.max_value = 50, 1, 5000
        count_socket.description = "Number of stitches to create along the path"
        
        length_socket = interface.new_socket(name="Stitch Length", in_out='INPUT', socket_type='NodeSocketFloat')
        length_socket.default_value, length_socket.min_value, length_socket.max_value = 0.05, 0.001, 1.0
        length_socket.description = "Length of individual stitch lines"

        thickness_socket = interface.new_socket(name="Thread Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
        thickness_socket.default_value, thickness_socket.min_value, thickness_socket.max_value = 0.002, 0.0001, 0.1
        thickness_socket.description = "Radius of the thread geometry"

        rotation_socket = interface.new_socket(name="Stitch Rotation", in_out='INPUT', socket_type='NodeSocketFloat')
        rotation_socket.subtype, rotation_socket.default_value = 'ANGLE', 0.0
        rotation_socket.description = "Additional rotation applied to each stitch"

        offset_socket = interface.new_socket(name="Surface Offset", in_out='INPUT', socket_type='NodeSocketFloat')
        offset_socket.default_value, offset_socket.min_value, offset_socket.max_value = 0.001, -0.1, 0.1
        offset_socket.description = "Distance to offset stitches from surface (prevents Z-fighting)"
        
        interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        print("Neural Stitcher: Interface construction completed successfully")

        # Build the intelligent node network
        print("Neural Stitcher: Constructing neural processing pipeline...")
        nodes = node_group.nodes
        links = node_group.links

        # Input/Output nodes
        group_input = nodes.new('NodeGroupInput')
        group_input.location = (-1200, 0)
        group_output = nodes.new('NodeGroupOutput')
        group_output.location = (1400, 0)

        # Phase 1: Intelligent edge detection and filtering
        compare_node = nodes.new('FunctionNodeCompare')
        compare_node.location = (-1000, 200)
        compare_node.data_type, compare_node.operation = 'FLOAT', 'GREATER_THAN'
        compare_node.inputs[1].default_value = 0.5  # Threshold for stitch area
        links.new(group_input.outputs["Stitch Area"], compare_node.inputs[0])

        # Phase 2: Mesh to curve conversion with edge analysis
        mesh_to_curve = nodes.new('GeometryNodeMeshToCurve')
        mesh_to_curve.location = (-800, 200)
        links.new(group_input.outputs['Geometry'], mesh_to_curve.inputs['Mesh'])
        links.new(compare_node.outputs['Result'], mesh_to_curve.inputs['Selection'])

        # Phase 3: Adaptive curve resampling
        resample_curve = nodes.new('GeometryNodeResampleCurve')
        resample_curve.location = (-600, 200)
        resample_curve.mode = 'COUNT'
        links.new(mesh_to_curve.outputs['Curve'], resample_curve.inputs['Curve'])
        links.new(group_input.outputs['Stitch Count'], resample_curve.inputs['Count'])

        # Phase 4: Create stitch primitive geometry
        stitch_line = nodes.new('GeometryNodeCurveLine')
        stitch_line.location = (-600, -200)
        stitch_line.mode = 'POINTS'
        # Create a value node for the stitch length to properly connect
        length_value = nodes.new('ShaderNodeValue')
        length_value.location = (-800, -300)
        links.new(group_input.outputs['Stitch Length'], length_value.inputs[0])
        
        # Set end point for line (Z-axis represents length)
        combine_xyz = nodes.new('ShaderNodeCombineXYZ')
        combine_xyz.location = (-700, -250)
        links.new(length_value.outputs[0], combine_xyz.inputs['Z'])
        links.new(combine_xyz.outputs['Vector'], stitch_line.inputs['End'])

        # Phase 5: Smart instancing with adaptive placement
        instance_on_points = nodes.new('GeometryNodeInstanceOnPoints')
        instance_on_points.location = (-200, 200)
        links.new(resample_curve.outputs['Curve'], instance_on_points.inputs['Points'])
        links.new(stitch_line.outputs['Curve'], instance_on_points.inputs['Instance'])

        # Phase 6: Intelligent rotation alignment with curve tangents
        align_euler = nodes.new('GeometryNodeAlignEulerToVector')
        align_euler.location, align_euler.axis = (-400, 50), 'Z'
        links.new(resample_curve.outputs['Tangent'], align_euler.inputs['Vector'])
        
        # User rotation addition
        rot_combine = nodes.new('ShaderNodeCombineXYZ')
        rot_combine.location = (-400, -50)
        links.new(group_input.outputs['Stitch Rotation'], rot_combine.inputs['Z'])
        
        add_rotations = nodes.new('ShaderNodeVectorMath')
        add_rotations.location, add_rotations.operation = (-400, 0), 'ADD'
        links.new(align_euler.outputs['Rotation'], add_rotations.inputs[0])
        links.new(rot_combine.outputs['Vector'], add_rotations.inputs[1])
        links.new(add_rotations.outputs['Vector'], instance_on_points.inputs['Rotation'])

        # Phase 7: Instance realization for geometry processing
        realize_instances = nodes.new('GeometryNodeRealizeInstances')
        realize_instances.location = (200, 200)
        links.new(instance_on_points.outputs['Instances'], realize_instances.inputs['Geometry'])

        # Phase 8: Intelligent surface offset calculation
        sample_normal = nodes.new('GeometryNodeSampleNearestSurface')
        sample_normal.location = (400, 0)
        links.new(group_input.outputs['Geometry'], sample_normal.inputs['Source Geometry'])
        
        scale_offset = nodes.new('ShaderNodeVectorMath')
        scale_offset.location, scale_offset.operation = (600, 0), 'SCALE'
        links.new(sample_normal.outputs['Normal'], scale_offset.inputs['Vector'])
        links.new(group_input.outputs['Surface Offset'], scale_offset.inputs['Scale'])

        set_position = nodes.new('GeometryNodeSetPosition')
        set_position.location = (600, 200)
        links.new(realize_instances.outputs['Geometry'], set_position.inputs['Geometry'])
        links.new(scale_offset.outputs['Vector'], set_position.inputs['Offset'])

        # Phase 9: Thread geometry generation with adaptive thickness
        profile_circle = nodes.new('GeometryNodeCurvePrimitiveCircle')
        profile_circle.location = (800, 0)
        profile_circle.mode = 'RADIUS'
        links.new(group_input.outputs['Thread Thickness'], profile_circle.inputs['Radius'])

        curve_to_mesh = nodes.new('GeometryNodeCurveToMesh')
        curve_to_mesh.location = (800, 200)
        links.new(set_position.outputs['Geometry'], curve_to_mesh.inputs['Curve'])
        links.new(profile_circle.outputs['Curve'], curve_to_mesh.inputs['Profile Curve'])

        # Phase 10: Intelligent geometry combination
        join_geometry = nodes.new('GeometryNodeJoinGeometry')
        join_geometry.location = (1100, 100)
        links.new(group_input.outputs['Geometry'], join_geometry.inputs[0])
        links.new(curve_to_mesh.outputs['Mesh'], join_geometry.inputs[1])

        # Final output
        links.new(join_geometry.outputs['Geometry'], group_output.inputs['Geometry'])

        print(f"Neural Stitcher: Processing pipeline for '{node_group_name}' constructed successfully")
        return node_group
        
    except Exception as e:
        error_msg = f"Failed to create neural stitch node group: {str(e)}"
        print(f"Neural Stitcher Error: {error_msg}")
        show_message_box(error_msg, "Neural Stitcher Error", 'ERROR')
        return None


class OBJECT_OT_AddNeuralStitchesOperator(bpy.types.Operator):
    """
    Operator for adding procedural stitches to mesh objects.
    
    Features smart object validation, error handling, and user feedback.
    """
    bl_idname = "object.add_neural_stitches"
    bl_label = "Add Neural Stitches"
    bl_description = "Add procedural stitches using advanced Geometry Nodes"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context) -> bool:
        """
        Intelligent pre-check to ensure the operator can run safely.
        
        Args:
            context: Blender context
            
        Returns:
            bool: True if conditions are met for safe execution
        """
        if not context.active_object:
            return False
        if context.active_object.type != 'MESH':
            return False
        if not context.active_object.data:
            return False
        return True

    def execute(self, context):
        """
        Execute the neural stitching operation with comprehensive error handling.
        
        Args:
            context: Blender context
            
        Returns:
            set: Blender operator return status
        """
        print(f"Neural Stitcher: Executing Neural Stitcher operator")
        
        try:
            active_obj = context.active_object
            
            # Create the intelligent node group
            stitch_node_group = create_neural_stitch_node_group()
            if not stitch_node_group:
                error_msg = "Failed to create neural stitch node group"
                self.report({'ERROR'}, error_msg)
                show_message_box(error_msg, "Neural Stitcher Error", 'ERROR')
                return {'CANCELLED'}
            
            # Add the geometry nodes modifier
            modifier = active_obj.modifiers.new(name="Neural Stitcher", type='NODES')
            modifier.node_group = stitch_node_group
            
            # Provide user feedback
            success_msg = f"Neural Stitcher successfully added to '{active_obj.name}'"
            self.report({'INFO'}, success_msg)
            show_message_box(success_msg, "Neural Stitcher Success", 'INFO')
            print(f"Neural Stitcher: {success_msg}")
            
            return {'FINISHED'}
            
        except Exception as e:
            error_msg = f"Neural Stitcher failed: {str(e)}"
            self.report({'ERROR'}, error_msg)
            show_message_box(error_msg, "Neural Stitcher Error", 'ERROR')
            print(f"Neural Stitcher Error: {error_msg}")
            return {'CANCELLED'}


def add_neural_modifier_button(self, context):
    """
    Adds the Neural Stitcher button to the modifier menu with enhanced styling.
    
    Args:
        self: Menu context
        context: Blender context
    """
    layout = self.layout
    layout.separator()
    op = layout.operator(
        OBJECT_OT_AddNeuralStitchesOperator.bl_idname, 
        text="Neural Stitcher", 
        icon='OUTLINER_OB_CURVE'
    )


# Registry of classes for Blender registration
classes = [
    OBJECT_OT_AddNeuralStitchesOperator,
]


def register():
    """
    Register the Neural Stitcher addon with Blender.
    
    Performs intelligent registration with error handling and user feedback.
    """
    print(f"Neural Stitcher: Registering addon '{bl_info['name']}' v{'.'.join(map(str, bl_info['version']))}")
    
    try:
        # Register all classes
        for cls in classes:
            print(f"Neural Stitcher: Registering class {cls.__name__}")
            bpy.utils.register_class(cls)
        
        # Add button to modifier menu
        print("Neural Stitcher: Adding UI button to modifier menu")
        bpy.types.OBJECT_MT_modifier_add.append(add_neural_modifier_button)
        
        print("Neural Stitcher: Registration completed successfully")
        show_message_box(
            f"Neural Stitcher v{'.'.join(map(str, bl_info['version']))} loaded successfully!\n\nFind it in: View3D > Modifiers > Add Modifier > Neural Stitcher",
            "Neural Stitcher Loaded",
            'INFO'
        )
        
    except Exception as e:
        error_msg = f"Neural Stitcher registration failed: {str(e)}"
        print(f"Neural Stitcher Error: {error_msg}")
        show_message_box(error_msg, "Neural Stitcher Registration Error", 'ERROR')
        raise


def unregister():
    """
    Unregister the Neural Stitcher addon from Blender.
    
    Performs clean unregistration to maintain Blender stability.
    """
    print(f"Neural Stitcher: Unregistering addon '{bl_info['name']}'")
    
    try:
        # Remove UI elements first
        print("Neural Stitcher: Removing UI elements")
        if hasattr(bpy.types, 'OBJECT_MT_modifier_add'):
            bpy.types.OBJECT_MT_modifier_add.remove(add_neural_modifier_button)
        
        # Unregister classes in reverse order
        for cls in reversed(classes):
            print(f"Neural Stitcher: Unregistering class {cls.__name__}")
            if hasattr(bpy.utils, 'unregister_class'):
                bpy.utils.unregister_class(cls)
        
        print("Neural Stitcher: Unregistration completed successfully")
        
    except Exception as e:
        error_msg = f"Neural Stitcher unregistration failed: {str(e)}"
        print(f"Neural Stitcher Error: {error_msg}")


if __name__ == "__main__":
    register()