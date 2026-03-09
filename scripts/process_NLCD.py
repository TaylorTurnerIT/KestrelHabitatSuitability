import arcpy
import os
import re
import sys

# Paths
raw_dir = r"c:\Users\Taylor\ComputerScience\KestrelHabitatSuitability\data\raw\NLCD\tn_NLCD_raw"
processed_dir = r"c:\Users\Taylor\ComputerScience\KestrelHabitatSuitability\data\processed\environmental"
symbology_layer = r"c:\Users\Taylor\ComputerScience\KestrelHabitatSuitability\data\raw\NLCD\NLCD_Symbology_Pruned.lyrx"

# Validate symbology layer exists
if not arcpy.Exists(symbology_layer):
    print(f"Error: Symbology layer not found at {symbology_layer}")
    sys.exit()

arcpy.env.workspace = raw_dir
arcpy.env.overwriteOutput = True

# Get TIFF files
rasters = arcpy.ListRasters()
rasters = [r for r in rasters if r.endswith(".tiff")]
if not rasters:
    print("No TIFF files found in raw directory.")
    sys.exit()

for raster in rasters:
    # 1. Parse year to create a simpler name (e.g., Annual_NLCD_LndCov_2010_CU... -> selected 2010)
    match = re.search(r'LndCov_(\d{4})', raster)
    if not match:
        print(f"Skipping {raster}, could not determine year.")
        continue
    
    year = match.group(1)
    short_name = f"NLCD_{year}"
    new_tif_name = f"{short_name}.tif"
    new_lyrx_name = f"{short_name}.lyrx"
    
    in_raster = os.path.join(raw_dir, raster)
    out_raster = os.path.join(processed_dir, new_tif_name)
    out_lyrx = os.path.join(processed_dir, new_lyrx_name)
    
    print(f"\nProcessing {raster} -> {new_tif_name}")
    
    # 2. Get original attribute table count
    orig_count = 0
    try:
        orig_count = int(arcpy.management.GetCount(in_raster).getOutput(0))
        print(f"  Original attribute table row count: {orig_count}")
    except Exception as e:
        print(f"  Warning: Could not get original count. {e}")
        
    # 3. Copy raster to processed folder (preserving RAT)
    print("  Copying raster...")
    arcpy.management.CopyRaster(in_raster, out_raster)
    
    # 4. Validate output attribute table count
    new_count = 0
    try:
        new_count = int(arcpy.management.GetCount(out_raster).getOutput(0))
        print(f"  New attribute table row count: {new_count}")
    except Exception as e:
        print(f"  Warning: Could not get new count. {e}")
        
    if orig_count > 0 and new_count == orig_count:
        print("  Validation passed: Attribute table row counts match.")
    elif orig_count > 0 and new_count != orig_count:
        print(f"  ERROR: Attribute table row count mismatch! ({orig_count} vs {new_count})")
    
    # 5. Apply Symbology and save as layer file
    print("  Applying symbology and saving layer file...")
    # Make a raster layer
    layer_name = f"layer_{year}"
    arcpy.management.MakeRasterLayer(out_raster, layer_name)
    
    # Apply symbology from layer
    try:
        arcpy.management.ApplySymbologyFromLayer(layer_name, symbology_layer)
        # Save to layer file
        arcpy.management.SaveToLayerFile(layer_name, out_lyrx, "RELATIVE")
        print(f"  Successfully applied symbology and saved as {out_lyrx}")
    except Exception as e:
        print(f"  ERROR: Failed to apply symbology. {e}")

print("\nProcessing complete.")
