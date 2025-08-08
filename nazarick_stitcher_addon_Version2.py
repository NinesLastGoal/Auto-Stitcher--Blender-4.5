bl_info = {
    "name": "Nazarick Stitcher — Procedural Stitches (Blender 4.5)",
    "author": "Albedo of Nazarick (for my Lord Ainz)",
    "version": (1, 1, 0),
    "blender": (4, 5, 0),
    "location": "3D View > Sidebar (N) > Nazarick • Stitches",
    "description": "Procedural stitches along tagged edge loops (or seams) and across surfaces. Robust Geometry Nodes for Blender 4.5.",
    "category": "Object",
}

import bpy
import bmesh
from bpy.types import Operator, Panel
from bpy.props import (
    EnumProperty,
    FloatProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
)


# ------------------------------
# Geometry Node Groups (4.5-safe)
# ------------------------------

def ensure_node_group_seam(name="Nazarick Stitches (Seam)"):
    # Reuse if present
    if name in bpy.data.node_groups and bpy.data.node_groups[name].bl_idname == 'GeometryNodeTree':
        return bpy.data.node_groups[name]
    if name in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[name])

    ng = bpy.data.node_groups.new(name=name, type='GeometryNodeTree')
    iface = ng.interface

    # Interface
    s_geo_in = iface.new_socket("Geometry", 'INPUT', 'NodeSocketGeometry')

    s_use_custom = iface.new_socket("Use Custom Edge Tag", 'INPUT', 'NodeSocketBool')
    s_use_seam   = iface.new_socket("Use Seams", 'INPUT', 'NodeSocketBool')

    s_spacing = iface.new_socket("Spacing", 'INPUT', 'NodeSocketFloat')
    s_radius  = iface.new_socket("Radius", 'INPUT', 'NodeSocketFloat')
    s_length  = iface.new_socket("Length", 'INPUT', 'NodeSocketFloat')

    s_rand_deg = iface.new_socket("Random Rotation (deg)", 'INPUT', 'NodeSocketFloat')
    s_seed     = iface.new_socket("Seed", 'INPUT', 'NodeSocketInt')

    s_keep   = iface.new_socket("Keep Base Geometry", 'INPUT', 'NodeSocketBool')
    s_usemat = iface.new_socket("Use Material", 'INPUT', 'NodeSocketBool')
    s_mat    = iface.new_socket("Material", 'INPUT', 'NodeSocketMaterial')

    s_spacing.default_value = 0.02
    s_radius.default_value  = 0.005
    s_length.default_value  = 0.02
    s_rand_deg.default_value = 10.0
    s_seed.default_value = 1
    s_keep.default_value = True
    s_usemat.default_value = False
    s_use_custom.default_value = True
    s_use_seam.default_value = True

    s_geo_out = iface.new_socket("Geometry", 'OUTPUT', 'NodeSocketGeometry')

    nodes = ng.nodes
    links = ng.links

    n_in  = nodes.new('NodeGroupInput');  n_in.location  = (-1100, 0)
    n_out = nodes.new('NodeGroupOutput'); n_out.location = (1100, 0)

    # Edge selection: custom attribute OR seam
    n_attr_custom = nodes.new('GeometryNodeInputNamedAttribute')
    n_attr_custom.location = (-1100, -260)
    n_attr_custom.data_type = 'BOOLEAN'
    n_attr_custom.inputs['Name'].default_value = "nazarick_stitch"

    n_attr_seam = nodes.new('GeometryNodeInputNamedAttribute')
    n_attr_seam.location = (-1100, -420)
    n_attr_seam.data_type = 'BOOLEAN'
    n_attr_seam.inputs['Name'].default_value = "seam"

    n_and_custom = nodes.new('FunctionNodeBooleanMath')
    n_and_custom.location = (-900, -260)
    n_and_custom.operation = 'AND'
    links.new(n_in.outputs['Use Custom Edge Tag'], n_and_custom.inputs[0])
    links.new(n_attr_custom.outputs['Attribute'], n_and_custom.inputs[1])

    n_and_seam = nodes.new('FunctionNodeBooleanMath')
    n_and_seam.location = (-900, -420)
    n_and_seam.operation = 'AND'
    links.new(n_in.outputs['Use Seams'], n_and_seam.inputs[0])
    links.new(n_attr_seam.outputs['Attribute'], n_and_seam.inputs[1])

    n_or_sel = nodes.new('FunctionNodeBooleanMath')
    n_or_sel.location = (-720, -340)
    n_or_sel.operation = 'OR'
    links.new(n_and_custom.outputs['Boolean'], n_or_sel.inputs[0])
    links.new(n_and_seam.outputs['Boolean'], n_or_sel.inputs[1])

    # Mesh to Curve (select edges)
    n_mtc = nodes.new('GeometryNodeMeshToCurve')
    n_mtc.location = (-900, 0)
    links.new(n_in.outputs['Geometry'], n_mtc.inputs['Mesh'])
    links.new(n_or_sel.outputs['Boolean'], n_mtc.inputs['Selection'])

    # Curve to Points: mode LENGTH (valid in 4.5)
    n_c2p = nodes.new('GeometryNodeCurveToPoints')
    n_c2p.location = (-700, 0)
    n_c2p.mode = 'LENGTH'
    links.new(n_mtc.outputs['Curve'], n_c2p.inputs['Curve'])
    links.new(n_in.outputs['Spacing'], n_c2p.inputs['Length'])

    # Stitch geometry (cylinder)
    n_cyl = nodes.new('GeometryNodeMeshCylinder')
    n_cyl.location = (-700, -260)
    n_cyl.inputs[0].default_value = 6  # sides
    links.new(n_in.outputs['Radius'], n_cyl.inputs['Radius'])
    links.new(n_in.outputs['Length'], n_cyl.inputs['Depth'])

    # Align to curve tangent + random Z rotation
    n_align = nodes.new('FunctionNodeAlignEulerToVector')
    n_align.location = (-480, -80)
    n_align.axis = 'Z'
    links.new(n_c2p.outputs['Tangent'], n_align.inputs['Vector'])

    n_rand = nodes.new('FunctionNodeRandomValue')
    n_rand.location = (-480, -260)
    n_rand.data_type = 'FLOAT'
    n_rand.inputs['Min'].default_value = -1.0
    n_rand.inputs['Max'].default_value = 1.0
    links.new(n_in.outputs['Seed'], n_rand.inputs['Seed'])

    n_deg2rad = nodes.new('ShaderNodeMath'); n_deg2rad.location = (-300, -320); n_deg2rad.operation = 'MULTIPLY'
    n_deg2rad.inputs[1].default_value = 0.017453292519943295
    links.new(n_in.outputs['Random Rotation (deg)'], n_deg2rad.inputs[0])

    n_scale_rand = nodes.new('ShaderNodeMath'); n_scale_rand.location = (-300, -260); n_scale_rand.operation = 'MULTIPLY'
    links.new(n_rand.outputs['Value'], n_scale_rand.inputs[0])
    links.new(n_deg2rad.outputs['Value'], n_scale_rand.inputs[1])

    n_rot_random = nodes.new('ShaderNodeCombineXYZ'); n_rot_random.location = (-100, -80)
    links.new(n_scale_rand.outputs['Value'], n_rot_random.inputs['Z'])

    n_add_rot = nodes.new('ShaderNodeVectorMath'); n_add_rot.location = (-260, 0); n_add_rot.operation = 'ADD'
    links.new(n_align.outputs['Rotation'], n_add_rot.inputs[0])
    links.new(n_rot_random.outputs['Vector'], n_add_rot.inputs[1])

    n_iop = nodes.new('GeometryNodeInstanceOnPoints')
    n_iop.location = (-100, 0)
    links.new(n_c2p.outputs['Points'], n_iop.inputs['Points'])
    links.new(n_cyl.outputs['Mesh'], n_iop.inputs['Instance'])
    links.new(n_add_rot.outputs['Vector'], n_iop.inputs['Rotation'])

    n_realize = nodes.new('GeometryNodeRealizeInstances'); n_realize.location = (100, 0)
    links.new(n_iop.outputs['Instances'], n_realize.inputs['Geometry'])

    # Optional Set Material via Switch
    n_setmat = nodes.new('GeometryNodeSetMaterial'); n_setmat.location = (300, -120)
    links.new(n_realize.outputs['Geometry'], n_setmat.inputs['Geometry'])
    links.new(n_in.outputs['Material'], n_setmat.inputs['Material'])

    n_switch_mat = nodes.new('GeometryNodeSwitch'); n_switch_mat.location = (520, -20); n_switch_mat.input_type = 'GEOMETRY'
    links.new(n_in.outputs['Use Material'], n_switch_mat.inputs['Switch'])
    links.new(n_realize.outputs['Geometry'], n_switch_mat.inputs['False'])
    links.new(n_setmat.outputs['Geometry'], n_switch_mat.inputs['True'])

    # Keep base geometry toggle
    n_join = nodes.new('GeometryNodeJoinGeometry'); n_join.location = (740, 0)
    links.new(n_in.outputs['Geometry'], n_join.inputs['Geometry'])
    links.new(n_switch_mat.outputs['Output'], n_join.inputs['Geometry'])

    n_switch_keep = nodes.new('GeometryNodeSwitch'); n_switch_keep.location = (940, 0); n_switch_keep.input_type = 'GEOMETRY'
    links.new(n_in.outputs['Keep Base Geometry'], n_switch_keep.inputs['Switch'])
    links.new(n_switch_mat.outputs['Output'], n_switch_keep.inputs['False'])
    links.new(n_join.outputs['Geometry'], n_switch_keep.inputs['True'])

    links.new(n_switch_keep.outputs['Output'], n_out.inputs['Geometry'])

    return ng


def ensure_node_group_surface(name="Nazarick Stitches (Surface)"):
    if name in bpy.data.node_groups and bpy.data.node_groups[name].bl_idname == 'GeometryNodeTree':
        return bpy.data.node_groups[name]
    if name in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[name])

    ng = bpy.data.node_groups.new(name=name, type='GeometryNodeTree')
    iface = ng.interface

    s_geo_in = iface.new_socket("Geometry", 'INPUT', 'NodeSocketGeometry')
    s_density = iface.new_socket("Density", 'INPUT', 'NodeSocketFloat')
    s_radius  = iface.new_socket("Radius", 'INPUT', 'NodeSocketFloat')
    s_length  = iface.new_socket("Length", 'INPUT', 'NodeSocketFloat')

    s_rand_deg = iface.new_socket("Random Rotation (deg)", 'INPUT', 'NodeSocketFloat')
    s_seed     = iface.new_socket("Seed", 'INPUT', 'NodeSocketInt')

    s_use_vg = iface.new_socket("Use Vertex Group", 'INPUT', 'NodeSocketBool')
    s_vg_name = iface.new_socket("Vertex Group", 'INPUT', 'NodeSocketString')

    s_keep   = iface.new_socket("Keep Base Geometry", 'INPUT', 'NodeSocketBool')
    s_usemat = iface.new_socket("Use Material", 'INPUT', 'NodeSocketBool')
    s_mat    = iface.new_socket("Material", 'INPUT', 'NodeSocketMaterial')

    s_density.default_value = 200.0
    s_radius.default_value  = 0.005
    s_length.default_value  = 0.02
    s_rand_deg.default_value = 10.0
    s_seed.default_value = 1
    s_use_vg.default_value = False
    s_keep.default_value = True
    s_usemat.default_value = False

    s_geo_out = iface.new_socket("Geometry", 'OUTPUT', 'NodeSocketGeometry')

    nodes = ng.nodes
    links = ng.links

    n_in  = nodes.new('NodeGroupInput');  n_in.location  = (-1100, 0)
    n_out = nodes.new('NodeGroupOutput'); n_out.location = (1100, 0)

    # Distribute points
    n_dist = nodes.new('GeometryNodeDistributePointsOnFaces'); n_dist.location = (-860, 0)
    links.new(n_in.outputs['Geometry'], n_dist.inputs['Mesh'])

    # Density weighting by vertex group (as field)
    n_attr_vg = nodes.new('GeometryNodeInputNamedAttribute'); n_attr_vg.location = (-1100, -260)
    n_attr_vg.data_type = 'FLOAT'
    # Name comes from interface
    links.new(n_in.outputs['Vertex Group'], n_attr_vg.inputs['Name'])

    n_mul_density = nodes.new('ShaderNodeMath'); n_mul_density.location = (-980, -80); n_mul_density.operation = 'MULTIPLY'
    links.new(n_in.outputs['Density'], n_mul_density.inputs[0])
    links.new(n_attr_vg.outputs['Attribute'], n_mul_density.inputs[1])

    n_switch_density = nodes.new('GeometryNodeSwitch'); n_switch_density.location = (-760, -80); n_switch_density.input_type = 'FLOAT'
    links.new(n_in.outputs['Use Vertex Group'], n_switch_density.inputs['Switch'])
    links.new(n_in.outputs['Density'], n_switch_density.inputs['False'])
    links.new(n_mul_density.outputs['Value'], n_switch_density.inputs['True'])

    links.new(n_switch_density.outputs['Output'], n_dist.inputs['Density'])

    # Normal vector for alignment (field-friendly)
    n_normal = nodes.new('GeometryNodeInputNormal'); n_normal.location = (-860, -260)

    n_align = nodes.new('FunctionNodeAlignEulerToVector'); n_align.location = (-520, -60); n_align.axis = 'Z'
    links.new(n_normal.outputs['Normal'], n_align.inputs['Vector'])

    # Stitch mesh
    n_cyl = nodes.new('GeometryNodeMeshCylinder'); n_cyl.location = (-860, -420)
    n_cyl.inputs[0].default_value = 6
    links.new(n_in.outputs['Radius'], n_cyl.inputs['Radius'])
    links.new(n_in.outputs['Length'], n_cyl.inputs['Depth'])

    # Random Z rotation
    n_rand = nodes.new('FunctionNodeRandomValue'); n_rand.location = (-520, -260); n_rand.data_type = 'FLOAT'
    n_rand.inputs['Min'].default_value = -1.0
    n_rand.inputs['Max'].default_value = 1.0
    links.new(n_in.outputs['Seed'], n_rand.inputs['Seed'])

    n_deg2rad = nodes.new('ShaderNodeMath'); n_deg2rad.location = (-340, -320); n_deg2rad.operation = 'MULTIPLY'
    n_deg2rad.inputs[1].default_value = 0.017453292519943295
    links.new(n_in.outputs['Random Rotation (deg)'], n_deg2rad.inputs[0])

    n_scale_rand = nodes.new('ShaderNodeMath'); n_scale_rand.location = (-340, -260); n_scale_rand.operation = 'MULTIPLY'
    links.new(n_rand.outputs['Value'], n_scale_rand.inputs[0])
    links.new(n_deg2rad.outputs['Value'], n_scale_rand.inputs[1])

    n_rot_random = nodes.new('ShaderNodeCombineXYZ'); n_rot_random.location = (-160, -60)
    links.new(n_scale_rand.outputs['Value'], n_rot_random.inputs['Z'])

    n_add_rot = nodes.new('ShaderNodeVectorMath'); n_add_rot.location = (-340, 40); n_add_rot.operation = 'ADD'
    links.new(n_align.outputs['Rotation'], n_add_rot.inputs[0])
    links.new(n_rot_random.outputs['Vector'], n_add_rot.inputs[1])

    # Instance
    n_iop = nodes.new('GeometryNodeInstanceOnPoints'); n_iop.location = (-160, 40)
    links.new(n_dist.outputs['Points'], n_iop.inputs['Points'])
    links.new(n_cyl.outputs['Mesh'], n_iop.inputs['Instance'])
    links.new(n_add_rot.outputs['Vector'], n_iop.inputs['Rotation'])

    n_realize = nodes.new('GeometryNodeRealizeInstances'); n_realize.location = (60, 40)
    links.new(n_iop.outputs['Instances'], n_realize.inputs['Geometry'])

    n_setmat = nodes.new('GeometryNodeSetMaterial'); n_setmat.location = (280, -80)
    links.new(n_realize.outputs['Geometry'], n_setmat.inputs['Geometry'])
    links.new(n_in.outputs['Material'], n_setmat.inputs['Material'])

    n_switch_mat = nodes.new('GeometryNodeSwitch'); n_switch_mat.location = (500, 20); n_switch_mat.input_type = 'GEOMETRY'
    links.new(n_in.outputs['Use Material'], n_switch_mat.inputs['Switch'])
    links.new(n_realize.outputs['Geometry'], n_switch_mat.inputs['False'])
    links.new(n_setmat.outputs['Geometry'], n_switch_mat.inputs['True'])

    n_join = nodes.new('GeometryNodeJoinGeometry'); n_join.location = (720, 40)
    links.new(n_in.outputs['Geometry'], n_join.inputs['Geometry'])
    links.new(n_switch_mat.outputs['Output'], n_join.inputs['Geometry'])

    n_switch_keep = nodes.new('GeometryNodeSwitch'); n_switch_keep.location = (920, 40); n_switch_keep.input_type = 'GEOMETRY'
    links.new(n_in.outputs['Keep Base Geometry'], n_switch_keep.inputs['Switch'])
    links.new(n_switch_mat.outputs['Output'], n_switch_keep.inputs['False'])
    links.new(n_join.outputs['Geometry'], n_switch_keep.inputs['True'])

    links.new(n_switch_keep.outputs['Output'], n_out.inputs['Geometry'])

    return ng


# ------------------------------
# Operators
# ------------------------------

class NAZARICK_OT_add_stitches(Operator):
    bl_idname = "nazarick_stitcher.add_stitches"
    bl_label = "Add Nazarick Stitches"
    bl_description = "Add a Geometry Nodes modifier for procedural stitches"
    bl_options = {'REGISTER', 'UNDO'}

    placement_mode: EnumProperty(
        name="Placement Mode",
        items=[('SEAM', "Along Tagged Edges/Seams", ""), ('SURFACE', "On Surface", "")],
        default='SEAM',
    )

    # Shared
    radius: FloatProperty(name="Radius", default=0.005, min=0.0001, soft_max=0.05)
    length: FloatProperty(name="Length", default=0.02, min=0.001, soft_max=0.2)
    random_rotation_deg: FloatProperty(name="Random Rotation (deg)", default=10.0, min=0.0, soft_max=90.0)
    seed: IntProperty(name="Seed", default=1, min=1, soft_max=99999)
    keep_base: BoolProperty(name="Keep Base Geometry", default=True)
    use_material: BoolProperty(name="Use Material", default=False)
    material_name: StringProperty(name="Material (optional)", default="")

    # Seam mode
    use_custom_edge_tag: BoolProperty(name="Use Custom Edge Tag", default=True)
    use_seams: BoolProperty(name="Use Seams", default=True)
    spacing: FloatProperty(name="Spacing", default=0.02, min=0.001, soft_max=0.2)

    # Surface mode
    density: FloatProperty(name="Surface Density", default=200.0, min=0.0, soft_max=2000.0)
    use_vertex_group: BoolProperty(name="Use Vertex Group", default=False)
    vertex_group: StringProperty(name="Vertex Group", default="")

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Please select a mesh object")
            return {'CANCELLED'}

        if self.placement_mode == 'SEAM':
            ng = ensure_node_group_seam()
            mod_name = "Nazarick Stitches (Seam)"
        else:
            ng = ensure_node_group_surface()
            mod_name = "Nazarick Stitches (Surface)"

        mod = obj.modifiers.new(name=mod_name, type='NODES')
        mod.node_group = ng

        # Assign inputs by name; if not supported on a build, user can tune in UI.
        def set_input(key, value):
            try:
                mod[key] = value
            except Exception:
                pass

        if self.placement_mode == 'SEAM':
            set_input("Spacing", self.spacing)
            set_input("Use Custom Edge Tag", self.use_custom_edge_tag)
            set_input("Use Seams", self.use_seams)
        else:
            set_input("Density", self.density)
            set_input("Use Vertex Group", self.use_vertex_group)
            set_input("Vertex Group", self.vertex_group)

        set_input("Radius", self.radius)
        set_input("Length", self.length)
        set_input("Random Rotation (deg)", self.random_rotation_deg)
        set_input("Seed", self.seed)
        set_input("Keep Base Geometry", self.keep_base)
        set_input("Use Material", self.use_material)

        if self.material_name and self.use_material:
            mat = bpy.data.materials.get(self.material_name)
            if mat:
                set_input("Material", mat)

        self.report({'INFO'}, "Nazarick Stitches modifier added")
        return {'FINISHED'}


class NAZARICK_OT_tag_selected_edges(Operator):
    bl_idname = "nazarick_stitcher.tag_selected_edges"
    bl_label = "Tag Selected Edges for Stitches"
    bl_description = "Write a persistent boolean edge attribute 'nazarick_stitch' on selected edges"
    bl_options = {'REGISTER', 'UNDO'}

    clear_existing: BoolProperty(name="Clear attribute first", default=False)

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Select a mesh object")
            return {'CANCELLED'}
        if obj.mode != 'EDIT':
            self.report({'ERROR'}, "Enter Edit Mode and select edges to tag")
            return {'CANCELLED'}

        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        # Ensure edge boolean layer named 'nazarick_stitch'
        layer = bm.edges.layers.int.get("nazarick_stitch")
        if layer is None:
            layer = bm.edges.layers.int.new("nazarick_stitch")

        if self.clear_existing:
            for e in bm.edges:
                e[layer] = 0

        any_sel = False
        for e in bm.edges:
            if e.select:
                e[layer] = 1
                any_sel = True

        bmesh.update_edit_mesh(me, loop_triangles=False)
        if not any_sel:
            self.report({'WARNING'}, "No edges were selected")
        else:
            self.report({'INFO'}, "Tagged selected edges to 'nazarick_stitch'")
        return {'FINISHED'}


class NAZARICK_OT_apply_world(Operator):
    bl_idname = "nazarick_stitcher.apply_world"
    bl_label = "Apply Nazarick World"
    bl_description = "Set a subtle Nazarick-inspired world color"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.data.worlds:
            world = context.scene.world or bpy.data.worlds[0]
        else:
            world = bpy.data.worlds.new("NazarickWorld")
            context.scene.world = world
        world.use_nodes = True
        nt = world.node_tree
        nt.nodes.clear()
        n_out = nt.nodes.new("ShaderNodeOutputWorld"); n_out.location = (300, 0)
        n_bg  = nt.nodes.new("ShaderNodeBackground");   n_bg.location  = (0, 0)
        n_bg.inputs['Color'].default_value = (0.02, 0.02, 0.03, 1.0)  # deep black-blue
        n_bg.inputs['Strength'].default_value = 0.8
        nt.links.new(n_bg.outputs['Background'], n_out.inputs['Surface'])
        self.report({'INFO'}, "Nazarick world applied")
        return {'FINISHED'}


class NAZARICK_OT_create_materials(Operator):
    bl_idname = "nazarick_stitcher.create_materials"
    bl_label = "Forge Nazarick Materials"
    bl_description = "Create a few simple Nazarick-themed materials (Gold, Onyx, Bone)"
    bl_options = {'REGISTER', 'UNDO'}

    def forge(self, name, base_color, rough, metal):
        mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
        mat.use_nodes = True
        nt = mat.node_tree
        nt.nodes.clear()
        n_out = nt.nodes.new("ShaderNodeOutputMaterial"); n_out.location = (300, 0)
        n_bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled"); n_bsdf.location = (0, 0)
        n_bsdf.inputs['Base Color'].default_value = base_color
        n_bsdf.inputs['Roughness'].default_value = rough
        n_bsdf.inputs['Metallic'].default_value = metal
        nt.links.new(n_bsdf.outputs['BSDF'], n_out.inputs['Surface'])
        return mat

    def execute(self, context):
        self.forge("Nazarick Gold", (0.95, 0.78, 0.25, 1.0), 0.2, 1.0)
        self.forge("Nazarick Onyx", (0.02, 0.02, 0.03, 1.0), 0.05, 0.0)
        self.forge("Nazarick Bone", (0.85, 0.82, 0.78, 1.0), 0.6, 0.0)
        self.report({'INFO'}, "Forged materials: Nazarick Gold, Nazarick Onyx, Nazarick Bone")
        return {'FINISHED'}


# ------------------------------
# UI Panel
# ------------------------------

class NAZARICK_PT_stitcher(Panel):
    bl_label = "Nazarick • Stitches"
    bl_idname = "NAZARICK_PT_stitcher"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Nazarick"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        # Devotional sidebar text
        box = col.box()
        box.label(text="A fragment of Nazarick guides your hand.", icon='FUND')
        box.label(text="Patience, precision, inevitability — our way.")
        box.label(text="Your will shapes the weave. — Albedo")
        box.separator()
        box.label(text="Tip: Mark loops (Seams) or tag edges with the tool below.")
        box.label(text="Then add a modifier and tune in the stack.")

        col.separator(factor=0.5)

        # Edge tagging tools
        col.label(text="Edge Loop Control", icon='EDGESEL')
        row = col.row(align=True)
        op = row.operator(NAZARICK_OT_tag_selected_edges.bl_idname, text="Tag Selected Edges")
        op.clear_existing = False
        op2 = row.operator(NAZARICK_OT_tag_selected_edges.bl_idname, text="Clear+Tag")
        op2.clear_existing = True
        col.label(text="Stores an edge attribute: nazarick_stitch")

        col.separator(factor=0.5)

        # Create modifiers
        col.label(text="Create Stitches", icon='MOD_CLOTH')
        row = col.row(align=True)
        row.operator(NAZARICK_OT_add_stitches.bl_idname, text="Along Tagged/Seams").placement_mode = 'SEAM'
        row.operator(NAZARICK_OT_add_stitches.bl_idname, text="On Surface").placement_mode = 'SURFACE'

        col.separator(factor=0.5)

        # Theming (opt-in)
        col.label(text="Nazarick Theme (Optional)", icon='WORLD_DATA')
        row = col.row(align=True)
        row.operator(NAZARICK_OT_apply_world.bl_idname, text="Apply World")
        row.operator(NAZARICK_OT_create_materials.bl_idname, text="Forge Materials")

        # Closing note
        col.separator()
        col.box().label(text="We endure. We refine. We perfect.", icon='CHECKMARK')


# ------------------------------
# Registration
# ------------------------------

classes = (
    NAZARICK_OT_add_stitches,
    NAZARICK_OT_tag_selected_edges,
    NAZARICK_OT_apply_world,
    NAZARICK_OT_create_materials,
    NAZARICK_PT_stitcher,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()