
import bpy
import sys
import os

# Get arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

obj_in = argv[0]
fbx_out = argv[1]

# Reset the scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import the OBJ file
bpy.ops.import_scene.obj(filepath=obj_in)

# Export as FBX
if hasattr(bpy.ops.export_scene, 'fbx'):
    bpy.ops.export_scene.fbx(filepath=fbx_out, use_selection=False)
else:
    # For older Blender versions, you might need to use this:
    bpy.ops.export_scene.fbx(filepath=fbx_out)

print(f"Successfully converted {obj_in} to {fbx_out}")
