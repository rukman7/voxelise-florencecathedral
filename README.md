# Voxelizing the Florence Cathedral Dome  
Convert any STL model into equal-sized cubes (voxels) — inspired by Leonardo da Vinci’s geometric methods in Codex Forster I.

## 1. Clone the repository

```bash
git clone https://github.com/rukman7/voxelise_florencecathedral.git
cd voxelise_florencecathedral
```

Your folder should look like:

```
.
├── florence_dome.stl
├── voxelise_dome.py
└── README.md
```

## 2. Install Python 3.10

Open3D does not support Python 3.12+ yet, so install Python 3.10.

### macOS (Homebrew)

```bash
brew install python@3.10
```

### Windows

Download and install from:  
https://www.python.org/downloads/release/python-3100/

Check installation:

```bash
python3.10 --version
```

## 3. Create and activate a virtual environment

### macOS / Linux

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### Windows PowerShell

```powershell
python3.10 -m venv venv
.\venv\Scripts\Activate.ps1
```

You should now see `(venv)` in your terminal prompt.

## 4. Upgrade pip inside the venv

```bash
pip install --upgrade pip
```

## 5. Install all prerequisites

Install Open3D:

```bash
pip install open3d
```

(Optional) ensure numpy is installed:

```bash
pip install numpy
```

Verify installation:

```bash
python -c "import open3d, numpy; print('OK')"
```

You should see:

```
OK
```

## 6. Run the voxelization script

Make sure `florence_dome.stl` is in the same folder as the script.

Run:

```bash
python voxelise_dome.py
```

Expected terminal output:

```
Voxel size: 1 ft
Number of cubes: XXXXX
Approx dome volume: XXXXX ft³
Rendering voxelized (cube) dome...
```

A 3D window will open showing the cathedral converted into cubes.

## 7. Adjusting cube size (optional)

Edit inside `voxelise_dome.py`:

```python
VOXEL_SIZE_FEET = 1.0
```

For faster rendering or a more blocky look:

```python
VOXEL_SIZE_FEET = 5
```

## 8. Deactivate the virtual environment

After you're done:

```bash
deactivate
```

## That’s it!

You now have a voxelized (cube-based) version of the Florence Cathedral Dome — a modern computational geometry version of Leonardo da Vinci’s shape reduction technique from Codex Forster I.
