# Neural Stitcher - Installation & Troubleshooting Guide

## 🚀 Quick Installation

### Method 1: ZIP Package Installation (Recommended)
1. **Download** the `neural_stitcher_addon.zip` file from the releases
2. **Open Blender** (version 4.5 or higher)
3. **Go to**: Edit → Preferences → Add-ons
4. **Click**: "Install..." button
5. **Select**: the downloaded `neural_stitcher_addon.zip` file
6. **Enable**: Check the box next to "Neural Stitcher - AI-Powered Procedural Stitches"
7. **Verify**: You should see a success message popup

### Method 2: Folder Installation
1. **Extract** the `neural_stitcher_addon` folder
2. **Copy** the folder to your Blender addons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/4.5/scripts/addons/`
   - **Linux**: `~/.config/blender/4.5/scripts/addons/`
3. **Restart Blender**
4. **Enable** the addon in Preferences → Add-ons

## 🔍 Verification Steps

After installation, verify the addon is working:

1. **Check Add-ons Panel**: The addon should appear in the list as "Neural Stitcher - AI-Powered Procedural Stitches"
2. **Check Console**: You should see messages like "Neural Stitcher: Registration completed successfully"
3. **Check UI**: Create a mesh object, go to Modifiers panel → Add Modifier → you should see "Neural Stitcher" option
4. **Test Functionality**: Add the modifier to a mesh to ensure it works

## 🎯 Usage Guide

### Basic Steps:
1. **Select a mesh object** (cube, plane, etc.)
2. **Add Neural Stitcher**:
   - Modifiers Panel → Add Modifier → Neural Stitcher
   - OR Object → Add Neural Stitches (in 3D Viewport)
3. **Configure parameters** in the modifier panel
4. **Enjoy** your procedural stitches!

### Parameter Guide:
- **Stitch Area**: Define where stitches appear (0.0-1.0)
- **Stitch Count**: Number of stitches (1-5000)
- **Stitch Length**: Length of each stitch (0.001-1.0)
- **Thread Thickness**: Thickness of thread geometry (0.0001-0.1)
- **Stitch Rotation**: Additional rotation per stitch (0°-360°)
- **Surface Offset**: Distance from surface to prevent clipping (-0.1-0.1)

## 🐛 Troubleshooting

### Issue: "Addon doesn't appear in Add-ons panel"

**Possible Causes & Solutions:**

1. **Incorrect Blender Version**
   - ✅ **Solution**: Ensure you're using Blender 4.5.0 or higher
   - ❌ **Symptoms**: Addon silently fails to load

2. **ZIP File Structure Issue**
   - ✅ **Solution**: Ensure the ZIP contains `neural_stitcher_addon/` folder with `__init__.py`
   - ❌ **Symptoms**: "No module found" or silent failure

3. **Python Permissions**
   - ✅ **Solution**: Run Blender as administrator/with proper permissions
   - ❌ **Symptoms**: "Permission denied" in console

4. **Conflicting Addons**
   - ✅ **Solution**: Disable other similar addons temporarily
   - ❌ **Symptoms**: Registration conflicts or crashes

### Issue: "Addon appears but UI button missing"

**Solutions:**
1. **Refresh UI**: Go to File → Defaults → Load Factory Settings (save your work first!)
2. **Check Object Selection**: Ensure you have a mesh object selected
3. **Restart Blender**: Sometimes UI elements need a restart to appear

### Issue: "Neural Stitcher modifier doesn't work"

**Solutions:**
1. **Check Mesh Validity**: Ensure your mesh has edges and vertices
2. **Check Parameters**: Ensure Stitch Count > 0 and Stitch Length > 0
3. **Check Geometry Nodes**: Enable Geometry Nodes in viewport shading
4. **Check Console**: Look for error messages in the console (Window → Toggle System Console)

### Issue: "Performance is slow"

**Solutions:**
1. **Reduce Stitch Count**: Start with 10-50 stitches for complex meshes
2. **Optimize Mesh**: Use simpler base geometry
3. **Lower Thread Thickness**: Reduces geometric complexity

## 🔧 Advanced Troubleshooting

### Enable Debug Mode:
1. **Open Console**: Window → Toggle System Console
2. **Check Messages**: Look for "Neural Stitcher:" messages
3. **Error Details**: Full error information will be displayed

### Manual Registration Check:
If addon doesn't register automatically, try:
```python
# In Blender's Python Console:
import bpy
import sys
sys.path.append("/path/to/neural_stitcher_addon")
import neural_stitcher_addon
neural_stitcher_addon.register()
```

### Compatibility Check:
```python
# In Blender's Python Console:
print(f"Blender Version: {bpy.app.version}")
print(f"Python Version: {sys.version}")
# Should show Blender 4.5+ and Python 3.x
```

## 📞 Getting Help

### Before Reporting Issues:
1. ✅ Check this troubleshooting guide
2. ✅ Verify Blender version (4.5+)
3. ✅ Check console for error messages
4. ✅ Try with a simple mesh (cube/plane)
5. ✅ Test with factory defaults

### How to Report Issues:
Include the following information:
- **Blender Version**: Help → About Blender
- **Operating System**: Windows/macOS/Linux + version
- **Installation Method**: ZIP or folder installation
- **Error Messages**: Copy from console
- **Steps to Reproduce**: Detailed steps
- **Screenshots**: If UI-related

## 📋 System Requirements

- **Blender**: 4.5.0 or higher
- **Python**: 3.x (included with Blender)
- **Operating System**: Windows 10+, macOS 10.14+, Linux (modern distros)
- **Memory**: 2GB+ RAM recommended
- **Graphics**: OpenGL 3.3+ compatible

## 🔄 Updates

To update the addon:
1. **Disable** the current version in Add-ons preferences
2. **Install** the new version using the same method
3. **Enable** the new version
4. **Restart** Blender for best results

---

**Neural Stitcher - Making procedural stitching accessible to everyone!** 🧵✨