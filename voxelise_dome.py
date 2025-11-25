import open3d as o3d
import numpy as np

# ====================================================
# CONFIGURATION
# ====================================================

MESH_PATH = "florence_dome.stl"

# 1 foot in meters
FEET_TO_METERS = 0.3048
VOXEL_SIZE_FEET = 1.0       # try 5 or 10 first if it's too heavy
VOXEL_SIZE = VOXEL_SIZE_FEET * FEET_TO_METERS

VOXEL_COLOR = (0.9, 0.5, 0.1)  # orange-ish

# ====================================================
# LOAD MESH
# ====================================================

mesh = o3d.io.read_triangle_mesh(MESH_PATH)
if mesh.is_empty():
    raise RuntimeError("Error: Could not load STL mesh. Check file name/path.")

mesh.compute_vertex_normals()
print("Loaded mesh:")
print(mesh)

# ====================================================
# ALIGN MESH SO BASE LIES ON z = 0
# ====================================================

bbox = mesh.get_axis_aligned_bounding_box()
min_bound = bbox.min_bound
mesh.translate([0, 0, -min_bound[2]])

# ====================================================
# VOXELIZATION
# ====================================================

voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(
    mesh,
    voxel_size=VOXEL_SIZE
)

voxels = voxel_grid.get_voxels()
num_cubes = len(voxels)
volume_ft3 = num_cubes * (VOXEL_SIZE_FEET ** 3)

print("=============================================")
print(f"Voxel size: {VOXEL_SIZE_FEET} ft")
print(f"Number of cubes: {num_cubes}")
print(f"Approx dome volume: {volume_ft3:.2f} ft³")
print("=============================================")

# ====================================================
# CONVERT VOXEL GRID TO A TRIANGLE MESH OF CUBES
# ====================================================

def voxelgrid_to_mesh(vg, color=(0.9, 0.5, 0.1)):
    vs = vg.voxel_size
    origin = vg.origin
    boxes = []

    for v in vg.get_voxels():
        # Create a unit cube of size vs
        box = o3d.geometry.TriangleMesh.create_box(width=vs, height=vs, depth=vs)
        box.paint_uniform_color(color)

        # Compute voxel center in world coordinates
        idx = np.array(v.grid_index, dtype=float)
        center = origin + vs * (idx + 0.5)

        # Move cube so its center is at that position
        box.translate(center - box.get_center())

        boxes.append(box)

    if not boxes:
        return o3d.geometry.TriangleMesh()

    mesh_out = boxes[0]
    for b in boxes[1:]:
        mesh_out += b

    mesh_out.compute_vertex_normals()
    return mesh_out

print("Building cube mesh from voxels (this may take a bit)...")
cube_mesh = voxelgrid_to_mesh(voxel_grid, VOXEL_COLOR)

# ====================================================
# VISUALIZE RESULT
# ====================================================

print("Rendering voxelized (cube) dome...")
o3d.visualization.draw_geometries([cube_mesh])

