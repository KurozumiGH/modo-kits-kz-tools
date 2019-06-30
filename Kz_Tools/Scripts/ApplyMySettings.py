#python
# -*- coding: utf-8 -*-

import lx


#================================================================
# Defaults
#================================================================

#Application
lx.eval("pref.value application.indexStyle uscore")

# Image & Painting
lx.eval("pref.value application.imageAA false")
lx.eval("pref.value application.imageThumbnails true")

#UI
lx.eval("pref.value remapping.baseProficiency advanced")
lx.eval("pref.value uiimages.uiimageMax 400")
lx.eval("pref.value uiimages.uiimageCacheSize 1073741824")
lx.eval("pref.value uiimages.uiimageThumbSize 256")
lx.eval("pref.value remapping.toolPropsType inline")


#================================================================
# Display
#================================================================

#3D Information Overlays
lx.eval("pref.value overlays.toolSnap true")
lx.eval("pref.value overlays.UVCoverage true")

#RayGL
lx.eval("pref.value preview.rglSync synchronous")

#Tool Handles
lx.eval("pref.value handles.lineDraw 1.5")
lx.eval("pref.value handles.lineHit 2.0")
lx.eval("pref.value handles.toolHandleSel advanced")
lx.eval("pref.value handles.toolHandleUnsel advanced")



#================================================================
# File I/O
#================================================================

#FBX I/O
lx.eval("user.value sceneio.fbx.save.format FBX2018")
lx.eval("user.value sceneio.fbx.save.smoothingGroups true")

#Image I/O
lx.eval("pref.value application.imageFormatName PNG16")
lx.eval("user.value ImageIO.JPEG.subsampling.index sample444")
lx.eval("user.value ImageIO.JPEG.quality 100")
lx.eval("user.value ImageIO.JPEG.subsampling.index sample444")



#================================================================
# Input
#================================================================

#3D Mouse
lx.eval("pref.value remapping.spaceballSpeedGlobal 0.3")
lx.eval("pref.value remapping.spaceballSwapYAndZ true")
lx.eval("pref.value remapping.spaceballInvertPosY true")
lx.eval("pref.value remapping.spaceballInvertRotY true")
lx.eval("pref.value remapping.spaceballPosThresholdX 0.1")
lx.eval("pref.value remapping.spaceballPosThresholdY 0.1")
lx.eval("pref.value remapping.spaceballPosThresholdZ 0.1")
lx.eval("pref.value remapping.spaceballRotThresholdX 0.1")
lx.eval("pref.value remapping.spaceballRotThresholdY 0.1")
lx.eval("pref.value remapping.spaceballRotThresholdZ 0.1")

#Units
#lx.eval("pref.value units.default millimeters")
lx.eval("pref.value units.system metric")
lx.eval("pref.value units.default centimeters")

#Work Plane
lx.eval("pref.value workplane.gridType fixed")
lx.eval("pref.value workplane.gridSize 0.001")



#================================================================
# Rendering
#================================================================

#Final Rendering
lx.eval("pref.value render.useNetwork true")
lx.eval("pref.value render.netJobSize 3.0")

#V-Ray Renderer
lx.eval("user.value vray.packageAutoAdd.physCamera true")

