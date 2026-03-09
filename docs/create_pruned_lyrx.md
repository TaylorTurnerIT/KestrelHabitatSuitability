# NLCD Colormap Pruning Utility (`create_pruned_lyrx.py`)

## Overview
The `create_pruned_lyrx.py` utility is used to dynamically construct a clean, concise symbology template (`NLCD_Symbology_Pruned.lyrx`) from raw National Land Cover Database (NLCD) raster files. 

## The Core Problem
Raw NLCD `.tiff` datasets inherently store an embedded colormap containing 255 discrete values. However, only 16 of these values are actual, active land cover classifications (e.g., `11` for Open Water, `41` for Deciduous Forest).

When you use the standard `arcpy.management.ApplySymbologyFromLayer` tool in ArcGIS Pro relying on a `.lyrx` template generated from the raw data, ArcGIS pulls across the **entire 255-element colormap**. This generates a massive, predominantly empty legend filled with blank colors spanning values from `0` to `255`, heavily cluttering map layouts and the table of contents.

## What This Script Does
To fix this without resorting to highly complex and brittle `arcpy.cim` Custom Unique Value Object construction, this script intelligently intercepts the layer template JSON:

1. **Extraction**: It automatically identifies a raw NLCD `.tiff` file located in `data/raw/NLCD/tn_NLCD_raw`. It creates an ephemeral ArcGIS raster layer and natively extracts its embedded colormap, saving it to disk as a base template (`NLCD_Symbology.lyrx`).
2. **Pruning**: It parses the generated layer JSON and filters the 255-element array down strictly to the 16 documented NLCD classes (discarding black default/padding classes).
3. **Label Enrichment**: As it filters, it updates the visual labels from simple numerical indices (e.g., "11") to rich, human-readable text derived from `docs/NLCDclasses.md` (e.g., "11 - Open Water").
4. **Finalization**: It saves the newly pruned, enriched colormap as `NLCD_Symbology_Pruned.lyrx`.

Because the downstream script (`process_NLCD.py`) utilizes this *pruned* layer template, ArcGIS natively imports only those 16 classes, rendering a clean, perfectly structured legend.

## Prerequisites
- Requires the **ArcGIS Pro Python environment** (`uv run`).
- Requires raw `.tiff` data to exist in `data/raw/NLCD/tn_NLCD_raw` prior to execution.

## Execution
Run the utility from the root workspace directory before the primary NLCD processing script:
```bash
uv run scripts/create_pruned_lyrx.py
```
