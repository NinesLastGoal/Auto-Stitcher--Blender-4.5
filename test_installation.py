"""
Neural Stitcher Installation Test Script

Run this script in Blender's Python Console to test if the addon is properly installed.

Instructions:
1. Open Blender
2. Go to: Scripting workspace or Window > Toggle System Console  
3. In the Python Console, copy and paste this entire script
4. Press Enter to run

This will test the addon installation and provide detailed feedback.
"""

import bpy
import sys

print("=" * 60)
print("NEURAL STITCHER INSTALLATION TEST")
print("=" * 60)

# Test 1: Blender Version
print(f"\n1. Blender Version Check:")
version = bpy.app.version
version_str = f"{version[0]}.{version[1]}.{version[2]}"
print(f"   Current version: {version_str}")

if version >= (4, 5, 0):
    print("   ✅ Blender version is compatible")
else:
    print("   ❌ Blender version too old (need 4.5.0+)")

# Test 2: Addon Registration Check
print(f"\n2. Addon Registration Check:")
try:
    # Check if the operator exists
    if hasattr(bpy.ops.object, 'add_neural_stitches'):
        print("   ✅ Neural Stitcher operator is registered")
    else:
        print("   ❌ Neural Stitcher operator not found")
    
    # Check if the addon is in preferences
    addon_found = False
    for addon in bpy.context.preferences.addons:
        if "neural_stitcher" in addon.module.lower():
            print(f"   ✅ Addon found in preferences: {addon.module}")
            addon_found = True
            break
    
    if not addon_found:
        print("   ❌ Addon not found in preferences")
        
except Exception as e:
    print(f"   ❌ Error checking registration: {e}")

# Test 3: UI Integration Check
print(f"\n3. UI Integration Check:")
try:
    # Check if modifier menu has been modified
    if hasattr(bpy.types, 'OBJECT_MT_modifier_add'):
        print("   ✅ Modifier menu accessible")
    else:
        print("   ❌ Modifier menu not accessible")
        
except Exception as e:
    print(f"   ❌ Error checking UI: {e}")

# Test 4: Geometry Nodes Check
print(f"\n4. Geometry Nodes Check:")
try:
    # Check if we can create a geometry node tree
    test_group = bpy.data.node_groups.new(name="Test_Neural_Stitcher", type='GeometryNodeTree')
    if test_group:
        print("   ✅ Geometry Nodes system is functional")
        # Clean up test
        bpy.data.node_groups.remove(test_group)
    else:
        print("   ❌ Geometry Nodes system not available")
        
except Exception as e:
    print(f"   ❌ Error testing Geometry Nodes: {e}")

# Test 5: Functional Test
print(f"\n5. Functional Test:")
try:
    # Create a test cube
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    
    if cube and cube.type == 'MESH':
        print("   ✅ Test mesh created")
        
        # Try to add neural stitcher
        try:
            bpy.ops.object.add_neural_stitches()
            
            # Check if modifier was added
            neural_modifier = None
            for mod in cube.modifiers:
                if "Neural Stitcher" in mod.name:
                    neural_modifier = mod
                    break
            
            if neural_modifier:
                print("   ✅ Neural Stitcher modifier added successfully")
                print(f"      Modifier type: {neural_modifier.type}")
                print(f"      Node group: {neural_modifier.node_group.name if neural_modifier.node_group else 'None'}")
            else:
                print("   ❌ Neural Stitcher modifier not added")
                
        except Exception as e:
            print(f"   ❌ Error adding Neural Stitcher: {e}")
    
    # Clean up test object
    if cube:
        bpy.data.objects.remove(cube, do_unlink=True)
        
except Exception as e:
    print(f"   ❌ Error in functional test: {e}")

# Summary
print(f"\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)

# Provide recommendations
print("\nRecommendations:")
print("- If all tests pass: ✅ Neural Stitcher is working correctly!")
print("- If some tests fail: Check the INSTALLATION_GUIDE.md for troubleshooting")
print("- If many tests fail: Try reinstalling the addon")

print("\nTo use Neural Stitcher:")
print("1. Select a mesh object")
print("2. Go to Modifiers panel → Add Modifier → Neural Stitcher")
print("3. Adjust parameters as needed")

print(f"\nFor more help, see: https://github.com/NinesLastGoal/Auto-Stitcher--Blender-4.5")
print("=" * 60)