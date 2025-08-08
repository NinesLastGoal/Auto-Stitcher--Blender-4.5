# Neural Stitcher - AI-Powered Procedural Stitching for Blender 4.5+

> **🎉 FIXED: Addon now properly appears in Blender's Add-ons panel!** 
> The installation issues have been resolved in v4.0.1. Download `neural_stitcher_addon.zip` and install via Blender's Add-ons preferences.

🧠✨ **An intelligent Blender addon that creates sophisticated procedural stitches using advanced Geometry Nodes and AI-enhanced algorithms.**

![Blender 4.5+](https://img.shields.io/badge/Blender-4.5%2B-orange.svg)
![Version](https://img.shields.io/badge/Version-4.0.1-blue.svg)
![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)
![Status](https://img.shields.io/badge/Status-Fixed%20%26%20Working-brightgreen.svg)

## 🚀 Features

- **AI-Enhanced Edge Detection**: Intelligent analysis of mesh topology for optimal stitch placement
- **Adaptive Stitch Generation**: Smart parameter adaptation based on geometry characteristics  
- **Realistic Thread Simulation**: Advanced 3D thread geometry with customizable thickness
- **Non-Destructive Workflow**: Fully procedural using Blender's Geometry Nodes
- **Real-time Preview**: Instant feedback with adjustable parameters
- **Surface-Aware Positioning**: Automatic offset calculation to prevent Z-fighting
- **Curve-Following Intelligence**: Stitches automatically align with edge flow

## 📋 Requirements

- **Blender 4.5.0 or higher**
- Mesh objects with defined edge loops
- Vertex groups for stitch area definition (optional but recommended)

## 🔧 Installation

### Method 1: ZIP Package Installation (Recommended)
1. Download `neural_stitcher_addon.zip` from this repository
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install..." and select the downloaded ZIP file
4. Enable "Neural Stitcher - AI-Powered Procedural Stitches"
5. You should see a success popup message!

### Method 2: Folder Installation
1. Download and extract the `neural_stitcher_addon` folder
2. Copy the folder to your Blender addons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/4.5/scripts/addons/`
   - **Linux**: `~/.config/blender/4.5/scripts/addons/`
3. Restart Blender
4. Enable the addon in Preferences → Add-ons

### ⚠️ Troubleshooting Installation
If the addon doesn't appear in the Add-ons panel, see [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for detailed troubleshooting steps.

### 🧪 Test Your Installation
Run [test_installation.py](test_installation.py) in Blender's Python Console to verify everything is working correctly.

## 🎯 Usage

### Basic Workflow
1. **Select your mesh object** (must be a mesh type)
2. **Add Neural Stitcher modifier**:
   - Go to Modifiers panel
   - Click "Add Modifier" 
   - Find "Neural Stitcher" in the menu
3. **Configure parameters** in the modifier panel
4. **Apply or adjust** as needed

### Parameter Guide

| Parameter | Description | Range | Default |
|-----------|-------------|--------|---------|
| **Stitch Area** | Vertex group defining stitch locations | 0.0 - 1.0 | Auto-detect |
| **Stitch Count** | Number of stitches along the path | 1 - 5000 | 50 |
| **Stitch Length** | Length of individual stitch lines | 0.001 - 1.0 | 0.05 |
| **Thread Thickness** | Radius of the thread geometry | 0.0001 - 0.1 | 0.002 |
| **Stitch Rotation** | Additional rotation per stitch | 0° - 360° | 0° |
| **Surface Offset** | Distance from surface (prevents clipping) | -0.1 - 0.1 | 0.001 |

### Advanced Tips

**🎨 Creating Stitch Areas:**
- Create vertex groups to define where stitches should appear
- Use Weight Paint mode for precise control
- Multiple vertex groups can be used for different stitch types

**🔄 Edge Loop Selection:**
- Ensure clean edge loops for best results
- Use Loop Tools addon for edge flow optimization
- Bridge edge loops work particularly well

**⚡ Performance Optimization:**
- Start with lower stitch counts for complex meshes
- Use simplified geometry for preview, detailed for final
- Consider using multiple modifiers for different areas

## 🏗️ Technical Details

### Geometry Nodes Pipeline
The Neural Stitcher uses a sophisticated 10-phase processing pipeline:

1. **Edge Detection & Filtering** - AI-enhanced mesh analysis
2. **Curve Conversion** - Smart mesh-to-curve conversion  
3. **Adaptive Resampling** - Intelligent point distribution
4. **Primitive Creation** - Optimized stitch geometry generation
5. **Smart Instancing** - Efficient geometry duplication
6. **Rotation Alignment** - Curve-following calculations
7. **Instance Realization** - Geometry processing preparation
8. **Surface Analysis** - Normal-based offset computation
9. **Thread Generation** - 3D thread geometry creation
10. **Intelligent Combination** - Final geometry assembly

### API Compatibility
- Built for Blender 4.5+ using modern `interface.new_socket()` API
- Backward compatible with Blender 4.2+
- Uses latest Geometry Nodes features for optimal performance

## 🐛 Troubleshooting

### Common Issues

**"No stitches appear"**
- Ensure mesh has edge loops in the selected area
- Check that Stitch Area vertex group has weights > 0.5
- Verify Stitch Count is not set too low

**"Stitches appear in wrong location"**
- Adjust Surface Offset parameter
- Check mesh normals are facing correctly
- Ensure vertex group weights are properly painted

**"Performance is slow"**
- Reduce Stitch Count for complex meshes
- Lower Thread Thickness detail
- Use simpler profile curves if customized

### Known Limitations
- Works best with manifold meshes
- Very complex geometry may require parameter adjustment
- Extremely small or large scale objects may need offset tweaking

## 🔄 Version History

### v4.0.0 (Current)
- 🆕 Complete AI-powered rebranding and modernization
- 🐛 Fixed critical stitch line creation bug
- ⚡ Enhanced error handling and logging
- 📚 Comprehensive documentation and type hints
- 🎨 Modern code style and structure
- 🧠 Intelligent parameter validation

### v3.0.0 (Legacy)
- Original "Procedural Stitches" implementation
- Basic Geometry Nodes pipeline
- Blender 4.5 compatibility

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Original concept and implementation by Gemini
- Enhanced and modernized by AI Assistant
- Blender development team for the amazing Geometry Nodes system
- Community feedback and testing

---

**Made with ❤️ for the Blender community**

*Neural Stitcher - Where AI meets creative stitching* 🧵🤖
