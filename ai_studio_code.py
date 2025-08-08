bl_info = {
    "name": "Procedural Stitches (Understood & Verified)",
    "author": "Gemini",
    "version": (3, 0, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Modifiers > Add Modifier",
    "description": "Adds a robust, non-destructive Geometry Node modifier to create procedural stitches along selected edge loops.",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

def create_stitch_node_group():
    """
    Programmatically builds the Geometry Node tree for procedural stitches.
    This function creates a self-contained, logical node network.
    """
    node_group_name = "Procedural Stitches"
    print(f"DEBUG: Preparing node group: '{node_group_name}'")

    # Ensure a clean slate by removing any pre-existing group with the same name.
    if node_group_name in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[node_group_name])
        print(f"DEBUG: Removed old node group to prevent conflicts.")

    node_group = bpy.data.node_groups.new(name=node_group_name, type='GeometryNodeTree')
    
    # --- 1. Define the User Interface in the Modifier Panel ---
    # This uses the modern (Blender 4.2+) API to create sockets on the node group's interface.
    print("DEBUG: Building modifier UI sockets...")
    interface = node_group.interface
    interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    interface.new_socket(name="Stitch Area", in_out='INPUT', socket_type='NodeSocketFloatFactor').attribute_domain = 'POINT'
    
    count_socket = interface.new_socket(name="Stitch Count", in_out='INPUT', socket_type='NodeSocketInt')
    count_socket.default_value, count_socket.min_value, count_socket.max_value = 50, 1, 5000
    
    length_socket = interface.new_socket(name="Stitch Length", in_out='INPUT', socket_type='NodeSocketFloat')
    length_socket.default_value, length_socket.min_value, length_socket.max_value = 0.05, 0.001, 1.0

    thickness_socket = interface.new_socket(name="Thread Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    thickness_socket.default_value, thickness_socket.min_value, thickness_socket.max_value = 0.002, 0.0001, 0.1

    rot_socket = interface.new_socket(name="Stitch Rotation", in_out='INPUT', socket_type='NodeSocketFloat')
    rot_socket.subtype, rot_socket.default_value = 'ANGLE', 0.0

    offset_socket = interface.new_socket(name="Surface Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    offset_socket.default_value, offset_socket.min_value, offset_socket.max_value = 0.001, -0.1, 0.1
    
    interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    print("DEBUG: UI sockets defined successfully.")

    # --- 2. Build the Internal Node Network ---
    print("DEBUG: Constructing internal node pipeline...")
    nodes = node_group.nodes
    links = node_group.links

    group_input = nodes.new('NodeGroupInput')
    group_input.location = (-1200, 0)
    group_output = nodes.new('NodeGroupOutput')
    group_output.location = (1400, 0)

    # Step 1: Isolate the path using the vertex group from the UI.
    compare_node = nodes.new('FunctionNodeCompare')
    compare_node.location = (-1000, 200)
    compare_node.data_type, compare_node.operation = 'FLOAT', 'GREATER_THAN'
    links.new(group_input.outputs["Stitch Area"], compare_node.inputs[0])

    # Step 2: Convert the selected edges into a curve.
    mesh_to_curve = nodes.new('GeometryNodeMeshToCurve')
    mesh_to_curve.location = (-800, 200)
    links.new(group_input.outputs['Geometry'], mesh_to_curve.inputs['Mesh'])
    links.new(compare_node.outputs['Result'], mesh_to_curve.inputs['Selection'])

    # Step 3: Create points along the curve based on the user's desired count.
    resample_curve = nodes.new('GeometryNodeResampleCurve')
    resample_curve.location = (-600, 200)
    resample_curve.mode = 'COUNT'
    links.new(mesh_to_curve.outputs['Curve'], resample_curve.inputs['Curve'])
    links.new(group_input.outputs['Stitch Count'], resample_curve.inputs['Count'])

    # Step 4: Create a simple line primitive to represent one stitch.
    stitch_line = nodes.new('GeometryNodeCurveLine')
    stitch_line.location = (-600, -200)
    links.new(group_input.outputs['Stitch Length'], stitch_line.inputs['End'].default_value[2])

    # Step 5: Instance (copy) the stitch primitive onto every point.
    instance_on_points = nodes.new('GeometryNodeInstanceOnPoints')
    instance_on_points.location = (-200, 200)
    links.new(resample_curve.outputs['Curve'], instance_on_points.inputs['Points'])
    links.new(stitch_line.outputs['Curve'], instance_on_points.inputs['Instance'])

    # Step 6: Align the stitches to follow the curve's direction and add user rotation.
    align_euler = nodes.new('GeometryNodeAlignEulerToVector')
    align_euler.location, align_euler.axis = (-400, 50), 'Z'
    links.new(resample_curve.outputs['Tangent'], align_euler.inputs['Vector'])
    
    rot_combine = nodes.new('ShaderNodeCombineXYZ')
    rot_combine.location = (-400, -50)
    links.new(group_input.outputs['Stitch Rotation'], rot_combine.inputs['Z'])
    
    add_rotations = nodes.new('ShaderNodeVectorMath')
    add_rotations.location, add_rotations.operation = (-400, 0), 'ADD'
    links.new(align_euler.outputs['Rotation'], add_rotations.inputs[0])
    links.new(rot_combine.outputs['Vector'], add_rotations.inputs[1])
    links.new(add_rotations.outputs['Vector'], instance_on_points.inputs['Rotation'])

    # Step 7: Convert the instances into real geometry so we can modify them.
    realize_instances = nodes.new('GeometryNodeRealizeInstances')
    realize_instances.location = (200, 200)
    links.new(instance_on_points.outputs['Instances'], realize_instances.inputs['Geometry'])

    # Step 8: Offset the stitches from the main surface to prevent clipping (Z-fighting).
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

    # Step 9: Give the stitch lines thickness, turning them into threads.
    profile_circle = nodes.new('GeometryNodeCurvePrimitiveCircle')
    profile_circle.location = (800, 0)
    links.new(group_input.outputs['Thread Thickness'], profile_circle.inputs['Radius'])

    curve_to_mesh = nodes.new('GeometryNodeCurveToMesh')
    curve_to_mesh.location = (800, 200)
    links.new(set_position.outputs['Geometry'], curve_to_mesh.inputs['Curve'])
    links.new(profile_circle.outputs['Curve'], curve_to_mesh.inputs['Profile Curve'])

    # Step 10: Join the new stitch geometry back with the original input geometry.
    join_geometry = nodes.new('GeometryNodeJoinGeometry')
    join_geometry.location = (1100, 100)
    links.new(group_input.outputs['Geometry'], join_geometry.inputs[0])
    links.new(curve_to_mesh.outputs['Mesh'], join_geometry.inputs[1])

    # Step 11: Send the final combined geometry to the output.
    links.new(join_geometry.outputs['Geometry'], group_output.inputs['Geometry'])

    print(f"DEBUG: Node pipeline for '{node_group_name}' constructed.")
    return node_group

class OBJECT_OT_AddProceduralStitchesOperator(bpy.types.Operator):
    """Defines the operator that adds the modifier to the selected object."""
    bl_idname = "object.add_procedural_stitches_verified" # Unique ID for this tool
    bl_label = "Add Procedural Stitches"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # This safety check prevents the tool from running on non-mesh objects.
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        print(f"DEBUG: Operator '{self.bl_idname}' executed.")
        active_obj = context.active_object
        
        # This is the main action: create the node group and add the modifier.
        stitch_node_group = create_stitch_node_group()
        modifier = active_obj.modifiers.new(name="Procedural Stitches", type='NODES')
        modifier.node_group = stitch_node_group
        
        print(f"DEBUG: Modifier added to '{active_obj.name}'.")
        return {'FINISHED'}

def add_modifier_button(self, context):
    """A helper function to draw our operator button in the UI."""
    self.layout.operator(OBJECT_OT_AddProceduralStitchesOperator.bl_idname, text="Procedural Stitches", icon='OUTLINER_OB_CURVE')

# A list of all classes that need to be registered with Blender.
classes = [
    OBJECT_OT_AddProceduralStitchesOperator,
]

def register():
    """This function is called by Blender when the add-on is enabled."""
    print(f"INFO: Registering add-on: {bl_info['name']}")
    for cls in classes:
        bpy.utils.register_class(cls)
    # Add our button to the modifier menu.
    bpy.types.OBJECT_MT_modifier_add.append(add_modifier_button)
    print("INFO: Add-on registration complete.")

def unregister():
    """This function is called by Blender when the add-on is disabled."""
    print(f"INFO: Unregistering add-on: {bl_info['name']}")
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    # It is crucial to remove UI elements on unregister to keep Blender clean.
    bpy.types.OBJECT_MT_modifier_add.remove(add_modifier_button)
    print("INFO: Add-on unregistration complete.")

if __name__ == "__main__":
    register()