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

Always use the built-in ArcGIS Python environment for executing scripts and notebooks in this project. This is the only environment that supports `arcpy`, which is required for our geoprocessing workflows.

To run scripts using this environment, use the full path to the Python executable:
`"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts/your_script.py`

Or, open the "Python Command Prompt" from the ArcGIS folder in your Start Menu and run your scripts from there.
