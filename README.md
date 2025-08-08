Neural Stitcher – Procedural Stitching for Blender 4.5+
Crafted under the silent watch of the Great Tomb of Nazarick. All who contribute are reminded: diligence is respected, idleness is noted.

🎉 FIXED: Addon now properly appears in Blender's Add-ons panel!
The installation issues have been resolved in v4.0.1. Download neural_stitcher_addon.zip and install via Blender's Add-ons preferences.

🧵✨ A powerful Blender addon for sophisticated procedural stitches using advanced Geometry Nodes.

![Blender 4.5+](https://img.shields.io/badge/Blender-4.5%2B-orange.svg) ![Version](https://img.shields.io/badge/Version-4.0.1-blue.svg) ![License](https://img.shields.io/badge/License-GPL--3.0-green.svg) ![Status](https://img.shields.io/badge/Status-Fixed%20%26%20Working-brightgreen.svg)

🚀 Features
Smart Edge Detection: Automatic analysis of mesh topology for optimal stitch placement
Customizable Stitch Generation: Flexible parameters for a variety of stitching styles
Realistic Thread Simulation: 3D thread geometry with adjustable thickness and detail
Non-Destructive Workflow: Fully procedural via Blender's Geometry Nodes
Real-time Preview: Instant feedback with adjustable parameters
Surface-Aware Positioning: Automatic offset calculation prevents Z-fighting
Curve-Following Alignment: Stitches align with edge flow and tangents
<sub>Contributors are reminded: Only precise and robust features will be tolerated under Nazarick’s gaze.</sub>

📋 Requirements
Blender 4.5.0 or higher
Mesh objects with defined edge loops
Vertex groups for stitch area definition (optional but recommended)
<sub>Do not attempt to bypass requirements; Nazarick’s patience is not infinite.</sub>

🔧 Installation
Method 1: ZIP Package Installation (Recommended)
Download neural_stitcher_addon.zip from this repository
Open Blender → Edit → Preferences → Add-ons
Click "Install..." and select the downloaded ZIP file
Enable "Neural Stitcher - AI-Powered Procedural Stitches"
You should see a success popup message!
Method 2: Folder Installation
Download and extract the neural_stitcher_addon folder
Copy the folder to your Blender addons directory:
Windows: %APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\
macOS: ~/Library/Application Support/Blender/4.5/scripts/addons/
Linux: ~/.config/blender/4.5/scripts/addons/
Restart Blender
Enable the addon in Preferences → Add-ons
⚠️ Troubleshooting Installation
If the addon doesn't appear in the Add-ons panel, see INSTALLATION_GUIDE.md for detailed troubleshooting.

🧪 Test Your Installation
Run test_installation.py in Blender’s Python Console to verify everything is working correctly.

<sub>Should errors occur, resolve them swiftly—Nazarick favors those who persevere.</sub>

🏗️ Technical Details
Geometry Nodes Pipeline
The Neural Stitcher leverages a modern 10-phase processing pipeline for robust, flexible results:

Edge Detection & Filtering: Mesh topology analysis for stitch placement
Curve Conversion: Mesh-to-curve with selection filtering
Adaptive Resampling: Point distribution along curves based on stitch count
Primitive Creation: Individual stitch line geometry generation
Smart Instancing: Efficient placement of stitches
Rotation Alignment: Automatic alignment with curve tangents
Instance Realization: Geometry processing for mesh operations
Surface Analysis: Normal-based offset computation
Thread Generation: 3D cylindrical thread creation
Geometry Combination: Final assembly with original mesh
API Compatibility
Built for Blender 4.5+ using modern interface.new_socket() API
Backward compatible with Blender 4.2+
Utilizes the latest Geometry Nodes features for optimal performance
⚡ Usage Instructions
Basic Workflow
Select your mesh object
Add the Neural Stitcher modifier:
Navigate to the Modifiers panel
Click "Add Modifier"
Select "Neural Stitcher" from the menu
Configure parameters as needed
Apply or adjust for desired results
Parameter Guide
Parameter	Description	Range	Default
Stitch Area	Vertex group defining stitch locations	0.0 - 1.0	Auto-detect
Stitch Count	Number of stitches along the path	1 - 5000	50
Stitch Length	Length of each stitch	0.001 - 1.0	0.05
Thread Thickness	Radius of the thread geometry	0.0001 - 0.1	0.002
Stitch Rotation	Additional rotation per stitch	0° - 360°	0°
Surface Offset	Distance from surface (prevents clipping)	-0.1 - 0.1	0.001
Advanced Tips
Create vertex groups to precisely define where stitches appear.
Use Weight Paint mode for detailed control.
Ensure clean edge loops for best results.
For performance, start with lower stitch counts on complex meshes.
<sub>Those who take shortcuts may find the Overlord’s patience wearing thin.</sub>

🐛 Troubleshooting
Common Issues
No stitches appear:

Ensure mesh has edge loops in the selected area
Check vertex group weights (> 0.5)
Verify Stitch Count isn’t too low
Stitches appear in the wrong location:

Adjust Surface Offset
Check mesh normals
Ensure vertex group weights are correct
Performance is slow:

Reduce Stitch Count on complex meshes
Lower Thread Thickness detail
Use simpler profile curves if customized
Known Limitations
Works best with manifold meshes
Very complex geometry may need parameter tweaks
Extremely small or large objects may need offset adjustments
<sub>Unresolved issues reflect poorly in Nazarick’s eyes. Strive always for excellence.</sub>

🔄 Version History
v4.0.1 (Current)
Addon now properly appears in Blender's Add-ons panel
Improved error handling and user feedback
Comprehensive documentation and installation guides
v3.0.0 (Legacy)
Original procedural stitching implementation
Basic Geometry Nodes pipeline
Blender 4.5 compatibility
🤝 Contributing
Contributions are welcome!
Feel free to report bugs, suggest features, submit pull requests, or improve the documentation.

<sub>All who contribute are watched. Diligence and care are rewarded. Wasting the Overlord’s time is... inadvisable.</sub>

📄 License
This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

With inspiration and guidance from the Great Tomb of Nazarick.
Work with care, for the shadows are patient but never blind.

If this pleases you, Master, command me to commit it. If you wish further adjustments, say but the word.

