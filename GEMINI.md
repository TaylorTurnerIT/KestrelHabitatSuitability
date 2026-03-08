# Repository Structure Guide

This document outlines the purpose of each directory to keep the workspace organized.

- **`arcgis/`**: ArcGIS Pro project files, toolboxes, and geodatabases.
- **`data/`**: Raw and processed datasets (e.g., NLCD data, shapefiles, rasters).
- **`docs/`**: Project documentation, references, and meeting notes.
- **`models/`**: Saved models, suitability indices, and related model outputs.
- **`notebooks/`**: Jupyter notebooks for data exploration, analysis, and prototyping.
- **`results/`**: Final outputs, generated figures, summary tables, and maps.
- **`scripts/`**: All Python scripts and source code for data processing, analysis, and automation.

## Environment Guidance

We manage the Python environment using [uv](https://github.com/astral-sh/uv). The workspace is configured with a `.python-version` file that points directly to the built-in ArcGIS Pro Python environment. This ensures all scripts have access to `arcpy` for our geoprocessing workflows.

### Running Scripts

To run scripts using this environment, use `uv run`:

```bash
uv run scripts/your_script.py
```

**Running from WSL (Linux):**
Because ArcGIS Pro and `arcpy` require a strictly Windows environment, the underlying `.python-version` configuration uses a Windows physical path (`C:\Program Files\...`). If you are working from a WSL terminal, the Linux `uv` binary cannot resolve this path. You must explicitly use the Windows binary (`uv.exe`) and forward slashes for script paths:

```bash
uv.exe run scripts/your_script.py
```

Alternatively, you can open the "Python Command Prompt" from the ArcGIS folder in your Start Menu and run your scripts from there.
