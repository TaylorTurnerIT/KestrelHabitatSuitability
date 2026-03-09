import arcpy
import json
import os
import glob
import sys

# Paths
raw_dir = r"c:\Users\Taylor\ComputerScience\KestrelHabitatSuitability\data\raw\NLCD"
raw_tiffs_dir = os.path.join(raw_dir, "tn_NLCD_raw")
symbology_layer = os.path.join(raw_dir, "NLCD_Symbology.lyrx")
pruned_lyrx = os.path.join(raw_dir, "NLCD_Symbology_Pruned.lyrx")

# 1. Generate base template from raw data
raw_tiffs = glob.glob(os.path.join(raw_tiffs_dir, "*.tiff"))
if not raw_tiffs:
    print(f"Error: No raw TIFFs found in {raw_tiffs_dir}")
    sys.exit(1)

sample_tiff = raw_tiffs[0]
print(f"Extracting base symbology template from {os.path.basename(sample_tiff)}...")
arcpy.env.overwriteOutput = True
arcpy.management.MakeRasterLayer(sample_tiff, "temp_nlcd_layer")
arcpy.management.SaveToLayerFile("temp_nlcd_layer", symbology_layer, "RELATIVE")
print(f"Saved base template to: {symbology_layer}")

# Documentation mapping
nlcd_labels = {
    "11": "11 - Open Water", "Open Water": "11 - Open Water",
    "12": "12 - Perennial Ice/Snow", "Perennial Ice/Snow": "12 - Perennial Ice/Snow",
    "21": "21 - Developed, Open Space", "Developed, Open Space": "21 - Developed, Open Space",
    "22": "22 - Developed, Low Intensity", "Developed, Low Intensity": "22 - Developed, Low Intensity",
    "23": "23 - Developed, Medium Intensity", "Developed, Medium Intensity": "23 - Developed, Medium Intensity",
    "24": "24 - Developed High Intensity", "Developed, High Intensity": "24 - Developed High Intensity",
    "31": "31 - Barren Land (Rock/Sand/Clay)", "Barren Land": "31 - Barren Land (Rock/Sand/Clay)",
    "41": "41 - Deciduous Forest", "Deciduous Forest": "41 - Deciduous Forest",
    "42": "42 - Evergreen Forest", "Evergreen Forest": "42 - Evergreen Forest",
    "43": "43 - Mixed Forest", "Mixed Forest": "43 - Mixed Forest",
    "51": "51 - Dwarf Scrub", "Dwarf Scrub": "51 - Dwarf Scrub",
    "52": "52 - Shrub/Scrub", "Shrub/Scrub": "52 - Shrub/Scrub",
    "71": "71 - Grassland/Herbaceous", "Grassland/Herbaceous": "71 - Grassland/Herbaceous",
    "72": "72 - Sedge/Herbaceous", "Sedge/Herbaceous": "72 - Sedge/Herbaceous",
    "73": "73 - Lichens", "Lichens": "73 - Lichens",
    "74": "74 - Moss", "Moss": "74 - Moss",
    "81": "81 - Pasture/Hay", "Pasture/Hay": "81 - Pasture/Hay",
    "82": "82 - Cultivated Crops", "Cultivated Crops": "82 - Cultivated Crops",
    "90": "90 - Woody Wetlands", "Woody Wetlands": "90 - Woody Wetlands",
    "95": "95 - Emergent Herbaceous Wetlands", "Emergent Herbaceous Wetlands": "95 - Emergent Herbaceous Wetlands"
}

with open(symbology_layer, 'r') as f:
    data = json.load(f)

colorizer = data['layerDefinitions'][0]['colorizer']

if colorizer['type'] == 'CIMRasterColorMapColorizer':
    colors = colorizer['colors']
    values = colorizer['values']

    new_colors = []
    new_values = []
    new_labels = []

    for i, val in enumerate(values):
        val_str = str(val)
        if val_str in nlcd_labels:
            new_colors.append(colors[i])
            new_values.append(val)
            new_labels.append(nlcd_labels[val_str])

    print(f"Pruned colormap from {len(values)} to {len(new_values)} classes.")

    colorizer['colors'] = new_colors
    colorizer['values'] = new_values
    colorizer['labels'] = new_labels

elif colorizer['type'] == 'CIMRasterUniqueValueColorizer':
    updated_count = 0
    total_classes = 0
    if 'groups' in colorizer:
        for grp in colorizer['groups']:
            if 'classes' in grp:
                for cls in grp['classes']:
                    total_classes += 1
                    val_str = str(cls['values'][0])
                    if val_str in nlcd_labels:
                        cls['label'] = nlcd_labels[val_str]
                        updated_count += 1
                        
    print(f"Updated labels for {updated_count} out of {total_classes} Unique Value classes.")

data['layerDefinitions'][0]['colorizer'] = colorizer

# Save new template
with open(pruned_lyrx, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Saved refined template to: {pruned_lyrx}")
