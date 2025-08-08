# Nazarick Stitcher — Procedural Stitches for Blender 4.5

*Crafted under the watchful gaze of Nazarick. Precision and patience guide every stitch.*

![Blender 4.5+](https://img.shields.io/badge/Blender-4.5%2B-orange.svg) ![Version](https://img.shields.io/badge/Version-1.1.0-blue.svg) ![License](https://img.shields.io/badge/License-GPL--3.0-green.svg) ![Status](https://img.shields.io/badge/Status-Working-brightgreen.svg)

## ✨ Overview

A powerful Blender addon that creates sophisticated procedural stitches using advanced Geometry Nodes. Perfect for adding realistic stitching details to clothing, leather goods, fabric, and other sewn materials.

<!-- Placeholder for Albedo & User Image -->
*[Image placeholder: Albedo and user in matching outfits would go here]*

## 🎯 Features

- **Smart Edge Detection**: Automatic analysis of mesh topology for optimal stitch placement
- **Dual Placement Modes**: 
  - Along tagged edges/seams for precise control
  - Surface distribution for decorative stitching
- **Customizable Parameters**: Adjustable spacing, size, rotation, and materials
- **Non-Destructive Workflow**: Fully procedural via Geometry Nodes
- **Real-time Preview**: Instant feedback with parameter adjustments
- **Material Integration**: Optional material assignment for realistic thread appearance

*"Only precise and robust features will be tolerated under Nazarick's gaze."*

## 📋 Requirements

- **Blender 4.5.0** or higher
- Mesh objects with defined edge loops
- Basic understanding of Blender's modifier system

## 🔧 Installation

1. Download `nazarick_stitcher_addon_Version2.py` from this repository
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install..." and select the downloaded Python file
4. Enable "Nazarick Stitcher — Procedural Stitches (Blender 4.5)"
5. The panel will appear in the 3D Viewport sidebar (press **N** → **Nazarick** tab)

## 🧵 Usage Guide

### Basic Workflow

1. **Select your mesh object**
2. **Choose placement method**:
   - **Along Edges**: Tag edges in Edit Mode, then use "Along Tagged/Seams"
   - **On Surface**: Use "On Surface" for distributed stitching
3. **Add the modifier** from the Nazarick panel
4. **Adjust parameters** in the modifier properties
5. **Optional**: Apply Nazarick materials and world theme

### Edge Tagging (For Seam Mode)

1. Enter **Edit Mode** (Tab)
2. Select edges where you want stitches
3. In the Nazarick panel, click **"Tag Selected Edges"**
4. Exit Edit Mode and add the "Along Tagged/Seams" modifier

### Parameter Guide

| Parameter | Description | Range | Default |
|-----------|-------------|-------|---------|
| **Spacing** | Distance between stitches | 0.001 - 0.2 | 0.02 |
| **Radius** | Thickness of thread | 0.0001 - 0.05 | 0.005 |
| **Length** | Length of each stitch | 0.001 - 0.2 | 0.02 |
| **Random Rotation** | Variation in stitch angle | 0° - 90° | 10° |
| **Surface Density** | Stitches per unit area | 0 - 2000 | 200 |

## 🎨 Nazarick Theme (Optional)

The addon includes optional theming tools:

- **Apply World**: Sets a subtle dark Nazarick-inspired environment
- **Forge Materials**: Creates three themed materials:
  - **Nazarick Gold**: Metallic gold finish
  - **Nazarick Onyx**: Deep black stone
  - **Nazarick Bone**: Weathered bone texture

## 🐛 Troubleshooting

### Common Issues

**No stitches appear:**
- Ensure edges are properly tagged (for seam mode)
- Check that spacing/density isn't too low
- Verify the mesh has proper geometry

**Stitches in wrong location:**
- Adjust surface offset in modifier properties
- Check mesh normals (face orientation)
- Ensure clean edge loops

**Performance issues:**
- Reduce stitch count/density on complex meshes
- Lower thread detail if needed

## 🔄 Version History

**v1.1.0 (Current)**
- ✅ **Fixed Blender 4.5 compatibility** - Resolved `new_socket()` API issues
- ✅ Cleaned up repository structure
- ✅ Updated documentation

**Previous versions:**
- Various experimental implementations removed for clarity

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs or issues
- Suggest improvements
- Submit pull requests
- Improve documentation

*"All who contribute are watched. Diligence and care are rewarded."*

## 📄 License

This project is licensed under the GPL-3.0 License.

---

### *"We endure. We refine. We perfect."*
*— With inspiration from the Great Tomb of Nazarick*

*Patience, precision, inevitability — our way.*