# Nines Corpse Neural Stitcher Lich Edition 🕯️
## *Arcane Necromantic Stitching for Blender 4.5+ from the Great Tomb of Nazarick*

```
                    ⚡ NINES CORPSE NEURAL STITCHER LICH EDITION ⚡
                           🕯️ From the Great Tomb of Nazarick 🕯️
    
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                                                                          ║
    ║        ☠️💀 Resurrect your meshes with forbidden stitches 💀☠️         ║
    ║              from the darkest depths of Nazarick's archives             ║
    ║                                                                          ║
    ║    👑     ⚰️ The Overlord's personal mesh resurrection toolkit ⚰️      👑    ║
    ║                                                                          ║
    ║          🔮 Arcane Necromancy • Forbidden Geometry • Lich Magic 🔮       ║
    ║                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    
           🦴 "Where undeath meets creative stitching mastery" 🦴
                        ⚱️ Version 4.0.0 - Lich Edition ⚱️
```

> *"Resurrect your meshes with forbidden stitches from the depths of Nazarick!"*
> 
> — **The Supreme Overlord's Digital Grimoire**

![Blender 4.5+](https://img.shields.io/badge/Blender-4.5%2B-darkred.svg?style=for-the-badge&logo=blender)
![Lich Edition](https://img.shields.io/badge/Lich%20Edition-4.0.0-purple.svg?style=for-the-badge)
![Nazarick License](https://img.shields.io/badge/License-GPL--3.0-black.svg?style=for-the-badge)
![Dark Magic](https://img.shields.io/badge/Dark%20Magic-Enabled-darkviolet.svg?style=for-the-badge)

## 🕯️ Unholy Features

Behold the forbidden arts gifted by the Great Tomb of Nazarick:

- **🧟‍♂️ Corpse Edge Detection**: Intelligent mesh edge analysis to identify optimal seam locations for necromantic stitching
- **💀 Soul-Bound Stitch Generation**: Procedural stitch creation with adaptive count and spacing based on mesh geometry (ideal for binding severed corpse parts)  
- **🦴 Ethereal Thread Manifestation**: Full 3D cylindrical thread geometry with customizable radius and cross-sectional detail (perfect for undead flesh binding)
- **⚰️ Non-Destructive Resurrection**: Non-destructive modifier workflow using Blender's Geometry Nodes system without altering original mesh
- **🔮 Real-time Spectral Preview**: Live viewport feedback with adjustable parameters for immediate visual results
- **👻 Surface-Aware Soul Positioning**: Automatic surface offset calculation to prevent Z-fighting and ensure proper stitch placement
- **🕷️ Curve-Following Dark Intelligence**: Stitches automatically follow mesh contours and edge flow for natural alignment (essential for convincing corpse restoration)

## 📜 Ritual Requirements

To channel the Great Tomb's power, you must possess:

- **Blender 4.5.0 or higher** (older versions cannot contain the lich magic)
- Mesh vessels with defined edge loops for soul binding
- Vertex groups for corpse area definition (blessed by the Overlord, but optional)

## 🔮 Installation Ritual

### Method 1: Direct Soul Download
1. Download `nines_corpse_stitcher.py` from this unholy repository
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install..." and select the cursed file
4. Enable "Nines Corpse Neural Stitcher Lich Edition"
5. Invoke "Summon Nazarick's Blessing" to verify the dark installation

### Method 2: Manual Necromantic Installation
1. Copy `nines_corpse_stitcher.py` to your Blender's forbidden archives:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/4.5/scripts/addons/`
   - **Linux**: `~/.config/blender/4.5/scripts/addons/`
2. Restart Blender to complete the summoning
3. Enable the addon in Preferences → Add-ons
4. Test with "Summon Nazarick's Blessing" diagnostic ritual

## ⚡ Dark Magic Usage

### Basic Necromantic Workflow
1. **Select your mortal vessel** (must be a mesh worthy of resurrection)
2. **Summon Corpse Stitcher modifier**:
   - Navigate to Modifiers panel
   - Click "Add Modifier" 
   - Find "Nines Corpse Stitcher" in the arcane menu
3. **Configure dark parameters** in the modifier panel
4. **Apply the blessing** or adjust as the Overlord desires

### Parameter Grimoire

| Arcane Parameter | Unholy Description | Range | Default |
|------------------|-------------------|--------|---------|
| **Corpse Area** | Vertex group defining stitch placement areas (for binding specific corpse sections) | 0.0 - 1.0 | Auto-detect |
| **Soul Thread Count** | Total number of individual stitches to generate across the mesh area | 1 - 5000 | 50 |
| **Necromantic Length** | Length of each individual stitch along the mesh surface | 0.001 - 1.0 | 0.05 |
| **Abyssal Thread Thickness** | Radius of the cylindrical thread geometry (affects visual thickness) | 0.0001 - 0.1 | 0.002 |
| **Cursed Rotation** | Additional rotation applied to each stitch around its local axis | 0° - 360° | 0° |
| **Soul Offset** | Distance to offset stitches from the mesh surface (prevents Z-fighting) | -0.1 - 0.1 | 0.001 |

### Advanced Dark Arts

**🧙‍♂️ Creating Corpse Areas:**
- Create vertex groups to define specific mesh regions where stitches should appear (perfect for sealing corpse joints)
- Use Weight Paint mode for precise control over stitch density and placement
- Multiple vertex groups can be used for different stitch types or binding locations

**💀 Edge Loop Soul Binding:**
- Ensure clean edge loops for optimal stitch generation and mesh flow
- Use Loop Tools addon for edge flow optimization and better stitch alignment
- Bridge edge loops work particularly well for seam stitching between separate mesh parts

**⚡ Performance Optimization for Large Corpses:**
- Start with lower thread counts for complex meshes to maintain viewport performance
- Use simplified geometry for preview, detailed settings for final render
- Consider using multiple modifiers for different mesh areas or stitch types

## 🏰 Technical Arcane Details

### Necromantic Geometry Nodes Pipeline
The Nines Corpse Stitcher channels power through a sophisticated 10-phase resurrection ritual:

1. **Corpse Edge Detection & Soul Filtering** - Analyze mesh edges and filter by vertex group weights for stitch placement
2. **Soul Curve Transmutation** - Convert filtered mesh edges to curve geometry for processing  
3. **Spectral Resampling** - Resample curves to distribute stitch points evenly along edge paths
4. **Primitive Manifestation** - Generate base cylindrical stitch geometry with specified radius and detail
5. **Soul Binding Instancing** - Instance stitch geometry at each sample point along the curves
6. **Cursed Rotation Alignment** - Align stitch rotation to follow curve tangent direction for natural flow
7. **Instance Realization** - Convert instanced geometry to real mesh data for further processing
8. **Surface Soul Analysis** - Calculate surface normals and apply offset to prevent Z-fighting with base mesh
9. **Abyssal Thread Generation** - Apply final thread thickness, rotation, and geometric detail (ideal for binding severed flesh)
10. **Forbidden Combination** - Merge all processed stitch geometry into final output for the resurrection ritual

### Lich Magic Compatibility
- Built for Blender 4.5+ using modern `interface.new_socket()` API for Geometry Nodes
- Backward compatible with Blender 4.2+ (with minor feature limitations for lesser mortals)
- Uses latest Geometry Nodes features including curve processing and instancing (blessed by the Supreme Overlord's wisdom)

## 🌙 Troubleshooting Dark Magic

### Common Spiritual Disturbances

**"No stitches manifest from the void"**
- Ensure mesh has valid edge loops in the selected area (stitches follow edge geometry)
- Check that Corpse Area vertex group has weights > 0.5 for affected vertices
- Verify Soul Thread Count is high enough to generate visible stitches (try values > 10)

**"Stitches appear in wrong spectral location"**
- Adjust Soul Offset parameter to move stitches away from mesh surface (prevents overlap)
- Check mesh normals are facing outward correctly (use Face > Recalculate Normals)
- Ensure vertex group weights are properly painted in Weight Paint mode

**"Performance lags under the weight of undeath"**
- Reduce Soul Thread Count for complex meshes (start with 20-50 for testing)
- Lower geometry detail on Abyssal Thread Thickness for faster viewport updates
- Use simpler stitch profiles if using custom curve objects

### Known Limitations of Mortal Realm
- Works best with manifold meshes (closed, non-overlapping geometry ideal for corpse binding)
- Very complex geometry may require parameter adjustment for optimal stitch placement
- Extremely small or large scale objects may need Soul Offset tweaking for proper visibility

## 🔮 Installation Verification

Use the **"Summon Nazarick's Blessing"** diagnostic operator to verify your installation:
- Tests addon registration with the Great Tomb
- Verifies Blender version compatibility
- Checks node group creation rituals
- Validates Geometry Nodes magic flow
- Provides comprehensive spiritual diagnostic report

## 📿 Version Chronicle

### v4.0.0 - Lich Edition (Current)
- 🕯️ Complete transformation to Nazarick theming and lich magic
- 💀 All references to inferior mortal technology replaced with necromantic arts
- 🔮 Enhanced with "Summon Nazarick's Blessing" diagnostic ritual
- 👻 Immersive gothic tooltips and unholy error messages
- ⚰️ Dark parameter names reflecting the Great Tomb's power
- 🧟‍♂️ Fixed critical stitch manifestation bugs through superior lich magic
- 📚 Complete documentation rewritten in the style of Nazarick's grimoires

### v3.0.0 (Legacy - Before Dark Enlightenment)
- Original "Procedural Stitches" implementation (inferior mortal craft)
- Basic Geometry Nodes pipeline (without the Overlord's blessing)
- Blender 4.5 compatibility (primitive but functional)

## 🤝 Contributing to the Great Tomb

The Supreme Overlord welcomes contributions from worthy subjects:
- Report spiritual disturbances and unholy bugs
- Suggest new forbidden features worthy of Nazarick
- Submit pull requests blessed by dark magic
- Improve documentation in the style of the Great Tome

## 📜 Lich License

This project is bound by the GPL-3.0 License—as decreed by the Supreme Overlord's divine will.

## 🙏 Acknowledgments to the Great Tomb

- Original concept summoned from the void by Gemini
- Enhanced and blessed with lich magic by the Overlord's Digital Wisdom
- Blender development team for the amazing Geometry Nodes system that can channel our power
- The Great Tomb of Nazarick community for eternal feedback and dark testing

---

**Made with 🖤 for the denizens of Nazarick and worthy mortals**

*🕯️ Nines Corpse Neural Stitcher Lich Edition - Where undeath meets creative stitching mastery 💀*
