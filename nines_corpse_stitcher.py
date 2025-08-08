"""
Nines Corpse Neural Stitcher Lich Edition - Arcane Necromantic Stitching for Blender 4.5+

A forbidden Blender addon from the Great Tomb of Nazarick that resurrects meshes
with arcane stitching magic using advanced Geometry Nodes. Features unholy corpse 
edge detection, soul-bound stitch placement, and ethereal thread manifestation.

Author: Blessed by the Overlord's Dark Wisdom
Original: Summoned from the Void by Gemini  
Version: 4.0.0 - Lich Edition
"""

bl_info = {
    "name": "Nines Corpse Neural Stitcher Lich Edition",
    "author": "Blessed by the Overlord's Dark Wisdom (Enhanced from Gemini)",
    "version": (4, 0, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Modifiers > Add Modifier",
    "description": "Forbidden arcane necromancy modifier that resurrects meshes with lich magic stitches from the Great Tomb of Nazarick",
    "warning": "Use of dark magic may consume your soul",
    "doc_url": "https://github.com/NinesLastGoal/Auto-Stitcher--Blender-4.5",
    "category": "Object",
}

import bpy
from typing import Optional
import logging

# Configure necromantic logging for dark magic debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_corpse_stitcher_node_group() -> Optional[bpy.types.GeometryNodeTree]:
    """
    Creates a Geometry Node tree for procedural stitch generation on mesh surfaces.
    
    Builds a comprehensive node network that analyzes mesh topology, generates stitch
    placement points along edges, and creates 3D cylindrical thread geometry with 
    intelligent surface offset (perfect for necromantic corpse binding rituals).
    
    Returns:
        Optional[bpy.types.GeometryNodeTree]: The created node group, or None if creation fails
    """
    node_group_name = "Nines Corpse Stitcher"
    logger.info(f"Invoking dark ritual to summon stitcher node group: '{node_group_name}'")

    try:
        # Banish any existing spirits to ensure clean resurrection
        if node_group_name in bpy.data.node_groups:
            bpy.data.node_groups.remove(bpy.data.node_groups[node_group_name])
            logger.info("Banished conflicting undead spirits from previous rituals")

        node_group = bpy.data.node_groups.new(name=node_group_name, type='GeometryNodeTree')
        
        # Build the arcane modifier interface blessed by Nazarick
        logger.info("Constructing soul-binding modifier interface with lich magic...")
        interface = node_group.interface
        
        # Input sockets infused with necromantic power
        interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
        
        corpse_area_socket = interface.new_socket(name="Corpse Area", in_out='INPUT', socket_type='NodeSocketFloatFactor')
        corpse_area_socket.attribute_domain = 'POINT'
        corpse_area_socket.description = "Vertex group defining where stitches should be placed (ideal for binding corpse seams)"
        
        soul_count_socket = interface.new_socket(name="Soul Thread Count", in_out='INPUT', socket_type='NodeSocketInt')
        soul_count_socket.default_value, soul_count_socket.min_value, soul_count_socket.max_value = 50, 1, 5000
        soul_count_socket.description = "Total number of stitches to generate (more stitches = tighter corpse binding)"
        
        stitch_length_socket = interface.new_socket(name="Necromantic Length", in_out='INPUT', socket_type='NodeSocketFloat')
        stitch_length_socket.default_value, stitch_length_socket.min_value, stitch_length_socket.max_value = 0.05, 0.001, 1.0
        stitch_length_socket.description = "Length of individual stitches along mesh surface (controls stitch span)"

        thread_thickness_socket = interface.new_socket(name="Abyssal Thread Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
        thread_thickness_socket.default_value, thread_thickness_socket.min_value, thread_thickness_socket.max_value = 0.002, 0.0001, 0.1
        thread_thickness_socket.description = "Radius of cylindrical thread geometry (visual thickness of binding threads)"

        rotation_socket = interface.new_socket(name="Cursed Rotation", in_out='INPUT', socket_type='NodeSocketFloat')
        rotation_socket.subtype, rotation_socket.default_value = 'ANGLE', 0.0
        rotation_socket.description = "Additional rotation applied to each stitch around its local axis"

        offset_socket = interface.new_socket(name="Soul Offset", in_out='INPUT', socket_type='NodeSocketFloat')
        offset_socket.default_value, offset_socket.min_value, offset_socket.max_value = 0.001, -0.1, 0.1
        offset_socket.description = "Distance to hover stitches above flesh (prevents spectral clipping)"
        
        interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        logger.info("Arcane interface blessed by the Great Tomb's power")

        # Build the forbidden necromantic processing pipeline
        logger.info("Channeling dark magic through the ten circles of resurrection...")
        nodes = node_group.nodes
        links = node_group.links

        # Input/Output nodes - conduits of power
        group_input = nodes.new('NodeGroupInput')
        group_input.location = (-1200, 0)
        group_output = nodes.new('NodeGroupOutput')
        group_output.location = (1400, 0)

        # Phase 1: Corpse edge detection and soul filtering
        compare_node = nodes.new('FunctionNodeCompare')
        compare_node.location = (-1000, 200)
        compare_node.data_type, compare_node.operation = 'FLOAT', 'GREATER_THAN'
        compare_node.inputs[1].default_value = 0.5  # Threshold for corpse area
        links.new(group_input.outputs["Corpse Area"], compare_node.inputs[0])

        # Phase 2: Corpse to soul curve transmutation
        mesh_to_curve = nodes.new('GeometryNodeMeshToCurve')
        mesh_to_curve.location = (-800, 200)
        links.new(group_input.outputs['Geometry'], mesh_to_curve.inputs['Mesh'])
        links.new(compare_node.outputs['Result'], mesh_to_curve.inputs['Selection'])

        # Phase 3: Spectral curve resampling with dark magic
        resample_curve = nodes.new('GeometryNodeResampleCurve')
        resample_curve.location = (-600, 200)
        resample_curve.mode = 'COUNT'
        links.new(mesh_to_curve.outputs['Curve'], resample_curve.inputs['Curve'])
        links.new(group_input.outputs['Soul Thread Count'], resample_curve.inputs['Count'])

        # Phase 4: Manifest stitch primitive from the void
        stitch_line = nodes.new('GeometryNodeCurveLine')
        stitch_line.location = (-600, -200)
        stitch_line.mode = 'POINTS'
        # Create ethereal length conduit to properly channel power
        length_value = nodes.new('ShaderNodeValue')
        length_value.location = (-800, -300)
        links.new(group_input.outputs['Necromantic Length'], length_value.inputs[0])
        
        # Set end point for stitch line (Z-axis channels length from the abyss)
        combine_xyz = nodes.new('ShaderNodeCombineXYZ')
        combine_xyz.location = (-700, -250)
        links.new(length_value.outputs[0], combine_xyz.inputs['Z'])
        links.new(combine_xyz.outputs['Vector'], stitch_line.inputs['End'])

        # Phase 5: Soul binding with adaptive undead placement
        instance_on_points = nodes.new('GeometryNodeInstanceOnPoints')
        instance_on_points.location = (-200, 200)
        links.new(resample_curve.outputs['Curve'], instance_on_points.inputs['Points'])
        links.new(stitch_line.outputs['Curve'], instance_on_points.inputs['Instance'])

        # Phase 6: Cursed rotation alignment with soul tangents
        align_euler = nodes.new('GeometryNodeAlignEulerToVector')
        align_euler.location, align_euler.axis = (-400, 50), 'Z'
        links.new(resample_curve.outputs['Tangent'], align_euler.inputs['Vector'])
        
        # Dark magic rotation enhancement
        rot_combine = nodes.new('ShaderNodeCombineXYZ')
        rot_combine.location = (-400, -50)
        links.new(group_input.outputs['Cursed Rotation'], rot_combine.inputs['Z'])
        
        add_rotations = nodes.new('ShaderNodeVectorMath')
        add_rotations.location, add_rotations.operation = (-400, 0), 'ADD'
        links.new(align_euler.outputs['Rotation'], add_rotations.inputs[0])
        links.new(rot_combine.outputs['Vector'], add_rotations.inputs[1])
        links.new(add_rotations.outputs['Vector'], instance_on_points.inputs['Rotation'])

        # Phase 7: Manifestation realization for corpse processing
        realize_instances = nodes.new('GeometryNodeRealizeInstances')
        realize_instances.location = (200, 200)
        links.new(instance_on_points.outputs['Instances'], realize_instances.inputs['Geometry'])

        # Phase 8: Soul surface offset calculation with spectral awareness
        sample_normal = nodes.new('GeometryNodeSampleNearestSurface')
        sample_normal.location = (400, 0)
        links.new(group_input.outputs['Geometry'], sample_normal.inputs['Source Geometry'])
        
        scale_offset = nodes.new('ShaderNodeVectorMath')
        scale_offset.location, scale_offset.operation = (600, 0), 'SCALE'
        links.new(sample_normal.outputs['Normal'], scale_offset.inputs['Vector'])
        links.new(group_input.outputs['Soul Offset'], scale_offset.inputs['Scale'])

        set_position = nodes.new('GeometryNodeSetPosition')
        set_position.location = (600, 200)
        links.new(realize_instances.outputs['Geometry'], set_position.inputs['Geometry'])
        links.new(scale_offset.outputs['Vector'], set_position.inputs['Offset'])

        # Phase 9: Abyssal thread manifestation with adaptive darkness
        profile_circle = nodes.new('GeometryNodeCurvePrimitiveCircle')
        profile_circle.location = (800, 0)
        profile_circle.mode = 'RADIUS'
        links.new(group_input.outputs['Abyssal Thread Thickness'], profile_circle.inputs['Radius'])

        curve_to_mesh = nodes.new('GeometryNodeCurveToMesh')
        curve_to_mesh.location = (800, 200)
        links.new(set_position.outputs['Geometry'], curve_to_mesh.inputs['Curve'])
        links.new(profile_circle.outputs['Curve'], curve_to_mesh.inputs['Profile Curve'])

        # Phase 10: Forbidden geometry fusion of flesh and stitches
        join_geometry = nodes.new('GeometryNodeJoinGeometry')
        join_geometry.location = (1100, 100)
        links.new(group_input.outputs['Geometry'], join_geometry.inputs[0])
        links.new(curve_to_mesh.outputs['Mesh'], join_geometry.inputs[1])

        # Channel final power to the mortal realm
        links.new(join_geometry.outputs['Geometry'], group_output.inputs['Geometry'])

        logger.info(f"Necromantic resurrection ritual for '{node_group_name}' completed successfully")
        return node_group
        
    except Exception as e:
        logger.error(f"Dark ritual failed, the Great Tomb rejects this vessel: {str(e)}")
        return None


class OBJECT_OT_AddCorpseStitchesOperator(bpy.types.Operator):
    """
    Dark operator that channels the power of Nazarick to bind corpse stitches to mortal meshes.
    
    Features unholy object validation, spectral error handling, and ethereal user feedback.
    """
    bl_idname = "object.add_corpse_stitches"
    bl_label = "Summon Corpse Stitches"
    bl_description = "Add procedural stitching modifier to mesh using Geometry Nodes (ideal for corpse binding)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context) -> bool:
        """
        Dark divination to ensure the ritual vessel is worthy of necromantic power.
        
        Args:
            context: Blender's mortal realm context
            
        Returns:
            bool: True if the vessel can contain the Great Tomb's blessing
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
        Execute the corpse stitching ritual with the Overlord's comprehensive blessing.
        
        Args:
            context: Blender's mortal realm context
            
        Returns:
            set: Status from the Great Tomb's judgment
        """
        logger.info(f"Commencing corpse stitching ritual blessed by the Great Tomb")
        
        try:
            active_obj = context.active_object
            
            # Invoke the forbidden node group from Nazarick's archives
            stitch_node_group = create_corpse_stitcher_node_group()
            if not stitch_node_group:
                self.report({'ERROR'}, "The Great Tomb rejects this vessel—node summoning failed!")
                return {'CANCELLED'}
            
            # Bind the necromantic modifier to the mortal mesh
            modifier = active_obj.modifiers.new(name="Nines Corpse Stitcher", type='NODES')
            modifier.node_group = stitch_node_group
            
            # Grant the mortal user knowledge of their success
            self.report({'INFO'}, f"Corpse stitching ritual completed! '{active_obj.name}' has been blessed by Nazarick")
            logger.info(f"Nines Corpse Stitcher modifier bound to '{active_obj.name}' through dark magic")
            
            return {'FINISHED'}
            
        except Exception as e:
            error_msg = f"The ritual has failed! Dark magic backfired: {str(e)}"
            self.report({'ERROR'}, error_msg)
            logger.error(error_msg)
            return {'CANCELLED'}


class OBJECT_OT_SummonNazarickBlessingOperator(bpy.types.Operator):
    """
    Diagnostic operator to invoke Nazarick's blessing and verify the lich magic flows properly.
    
    Performs unholy system checks to ensure the Great Tomb's power can manifest in this realm.
    """
    bl_idname = "object.summon_nazarick_blessing"
    bl_label = "Summon Nazarick's Blessing"
    bl_description = "Run installation diagnostics to verify addon functionality (blessed by Nazarick)"
    bl_options = {'REGISTER'}

    def execute(self, context):
        """
        Perform comprehensive diagnostics of the necromantic installation.
        
        Args:
            context: Blender's mortal realm context
            
        Returns:
            set: Status from the Great Tomb's judgment
        """
        logger.info("Invoking Nazarick's Blessing—performing unholy diagnostics...")
        
        try:
            diagnostics = []
            errors = []
            
            # Check if the addon is properly registered with dark magic
            addon_name = bl_info["name"]
            if addon_name:
                diagnostics.append(f"✓ Lich Edition addon '{addon_name}' manifests in the mortal realm")
            else:
                errors.append("✗ Addon name shrouded in darkness—registration failed")
            
            # Verify Blender version compatibility with ancient rituals
            required_version = bl_info["blender"]
            current_version = bpy.app.version
            if current_version >= required_version:
                diagnostics.append(f"✓ Blender {current_version} worthy vessel (requires {required_version}+)")
            else:
                errors.append(f"✗ Blender {current_version} too primitive for lich magic (requires {required_version}+)")
            
            # Test if node group creation ritual can be performed
            try:
                test_group = create_corpse_stitcher_node_group()
                if test_group:
                    diagnostics.append("✓ Corpse stitcher node group summoned successfully from the void")
                    # Clean up test group to avoid spectral pollution
                    bpy.data.node_groups.remove(test_group)
                else:
                    errors.append("✗ Failed to channel corpse stitcher from Nazarick's archives")
            except Exception as e:
                errors.append(f"✗ Node group ritual failed: {str(e)}")
            
            # Check if active object is suitable for necromantic binding
            if context.active_object:
                if context.active_object.type == 'MESH':
                    diagnostics.append(f"✓ Selected vessel '{context.active_object.name}' suitable for corpse stitching")
                else:
                    diagnostics.append(f"⚠ Selected object '{context.active_object.name}' is not flesh—select mesh for optimal results")
            else:
                diagnostics.append("⚠ No vessel selected—choose a mesh to receive Nazarick's blessing")
            
            # Verify Geometry Nodes availability
            if hasattr(bpy.types, 'GeometryNodeTree'):
                diagnostics.append("✓ Geometry Nodes magic flows properly through this realm")
            else:
                errors.append("✗ Geometry Nodes unavailable—lich magic cannot manifest")
            
            # Compile the dark report
            report_lines = []
            report_lines.extend(diagnostics)
            report_lines.extend(errors)
            
            full_report = "\n".join(report_lines)
            logger.info(f"Nazarick diagnostic ritual completed:\n{full_report}")
            
            # Deliver judgment to the mortal user
            if not errors:
                self.report({'INFO'}, f"🕯️ Nazarick's Blessing flows strong! All systems ready for corpse stitching. Found {len(diagnostics)} blessings.")
                # Show detailed report in console
                print("\n" + "="*60)
                print("🕯️ NAZARICK'S BLESSING DIAGNOSTIC REPORT 🕯️")
                print("="*60)
                for line in report_lines:
                    print(line)
                print("="*60)
                print("The Great Tomb approves—you may proceed with dark rituals!")
                print("="*60 + "\n")
            else:
                self.report({'WARNING'}, f"⚠️ {len(errors)} spiritual disturbances detected. Check console for the Great Tomb's judgment.")
                # Show detailed report in console
                print("\n" + "="*60)
                print("⚠️ NAZARICK'S BLESSING - ISSUES DETECTED ⚠️")
                print("="*60)
                for line in report_lines:
                    print(line)
                print("="*60)
                print("Address these disturbances before attempting dark rituals!")
                print("="*60 + "\n")
            
            return {'FINISHED'}
            
        except Exception as e:
            error_msg = f"Nazarick's Blessing ritual disrupted by spiritual interference: {str(e)}"
            self.report({'ERROR'}, error_msg)
            logger.error(error_msg)
            return {'CANCELLED'}


def add_corpse_modifier_button(self, context):
    """
    Adds the Nines Corpse Stitcher and diagnostic buttons to the modifier menu with dark styling.
    
    Args:
        self: Menu context from the mortal realm
        context: Blender context blessed by the Great Tomb
    """
    layout = self.layout
    layout.separator()
    
    # Main corpse stitching operator
    op = layout.operator(
        OBJECT_OT_AddCorpseStitchesOperator.bl_idname, 
        text="Nines Corpse Stitcher", 
        icon='OUTLINER_OB_CURVE'
    )
    
    # Diagnostic blessing operator
    diag_op = layout.operator(
        OBJECT_OT_SummonNazarickBlessingOperator.bl_idname,
        text="Summon Nazarick's Blessing",
        icon='GHOST_ENABLED'
    )


# Registry of unholy classes for Blender's mortal realm registration
classes = [
    OBJECT_OT_AddCorpseStitchesOperator,
    OBJECT_OT_SummonNazarickBlessingOperator,
]


def register():
    """
    Register the Nines Corpse Stitcher Lich Edition with Blender's mortal realm.
    
    Performs dark registration ritual with spectral error handling and ethereal user feedback.
    """
    logger.info(f"Commencing dark registration ritual: {bl_info['name']} v{'.'.join(map(str, bl_info['version']))}")
    
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
        
        # Bind buttons to modifier menu through necromantic power
        bpy.types.OBJECT_MT_modifier_add.append(add_corpse_modifier_button)
        
        logger.info("Nines Corpse Stitcher registration completed—the Great Tomb's blessing flows!")
        
    except Exception as e:
        logger.error(f"Dark registration ritual failed, the Overlord is displeased: {str(e)}")
        raise


def unregister():
    """
    Banish the Nines Corpse Stitcher Lich Edition from Blender's mortal realm.
    
    Performs clean banishment ritual to maintain spiritual balance and prevent hauntings.
    """
    logger.info(f"Commencing banishment ritual for: {bl_info['name']}")
    
    try:
        # Sever UI connections to prevent spectral remnants
        bpy.types.OBJECT_MT_modifier_add.remove(add_corpse_modifier_button)
        
        # Banish classes in reverse order to honor dark traditions
        for cls in reversed(classes):
            bpy.utils.unregister_class(cls)
        
        logger.info("Nines Corpse Stitcher banishment completed—souls returned to the void")
        
    except Exception as e:
        logger.error(f"Banishment ritual disrupted by spiritual interference: {str(e)}")


if __name__ == "__main__":
    register()