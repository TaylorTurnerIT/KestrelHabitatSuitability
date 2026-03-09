# NLCD Processing Script (`process_NLCD.py`)

## Overview

The `process_NLCD.py` script automates the processing of raw National Land Cover Database (NLCD) raster data for the American Kestrel Habitat Suitability project. It takes awkwardly named raw NLCD `.tiff` files, renames them simply (e.g., `NLCD_2010.tif`), moves them to the processed directory, validates no data is lost during the move, and applies a standardized ArcGIS layer symbology.

## Requirements

- Designed to be run in the **ArcGIS Pro Python environment** using `uv`.
- Since the `arcpy` module is required, this script can only be run on Windows.

## Execution

Run the script from the root workspace directory using:

```bash
uv run scripts/process_NLCD.py
```

*(If running from WSL, ensure you use `uv.exe` and forward slashes as defined in `GEMINI.md`)*.

## Inputs

- **Raw Rasters**: `data/raw/NLCD/tn_NLCD_raw/*.tiff` (e.g., `Annual_NLCD_LndCov_2010_...tiff`)
- **Symbology Template**: `data/raw/NLCD/NLCD_Symbology.lyrx`. *Note: Ensure this file is fetched via Git LFS (`git lfs pull`) or it will cause an `ERROR 000229`.*

## Outputs

Outputs are saved to `data/processed/environmental/`:

- **Processed Rasters**: Cleanly named `.tif` files (`NLCD_{year}.tif`)
- **Layer Files**: Applied symbology layers (`NLCD_{year}.lyrx`)

## Workflow Steps

1. **Find TIFF Files**: Searches the raw directory for valid NLCD `.tiff` files.
2. **Determine Year & Set Names**: Extracts the 4-digit year dynamically via regex and generates a succinct `.tif` and `.lyrx` name.
3. **Copy Raster**: Uses `arcpy.management.CopyRaster` to move the image.
4. **Validate Rows**: Queries `arcpy.management.GetCount` on both the input and output attribute tables to ensure data continuity. If a mismatch is detected, an attribute table row count error is printed.
5. **Apply Symbology**: Creates an ephemeral raster layer and uses `arcpy.management.ApplySymbologyFromLayer` using `NLCD_Symbology.lyrx`, then saves the new layer configuration to disk.
