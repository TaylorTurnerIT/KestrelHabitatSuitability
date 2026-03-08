# American Kestrel Habitat Suitability Analysis

The purpose of this project is to predict the habitat suitability of American Kestrels in Tennessee using machine learning algorithms to evaluate the overall habitat suitability trends over time.

**Target Species:** *American Kestrel*
**Target Region:** *Tennessee*
**Time Range:** *2010 - 2024*
**Authors:** *Nora Marchese, Taylor Turner*

## Tooling

ArcGIS Pro
Python (Arcpy)
MaxEnt

## Available Data

- National Land Cover Database (NLCD) 2010-2024
- Cornell University eBird Dataset 2010-2024

## Citizen Science Bias

The eBird dataset is a citizen science dataset, which means that it is collected by volunteers. These volunteers may not be experts in bird identification, and may not be able to identify all species of birds. This can lead to bias in the dataset, as certain species may be overrepresented or underrepresented. Further, the data is highly localized near cities, which may not be representative of the entire region.

We acknowledge the citizen science bias in our dataset and we do not plan to correct for it to prevent biasing the results.

## MaxEnt

MaxEnt is a machine learning algorithm that is used to predict the distribution of species based on environmental variables. It is a species distribution modeling (SDM) algorithm that is based on the idea that species are more likely to be found in areas where the environmental variables are similar to those where the species has been observed.

## Project Milestones

- Determine the overall distribution of each land cover type in Tennessee
- Estimate the overall distribution of American Kestrels in Tennessee by using observational data
- Merge similar land cover types into a smaller number of categories
  - Allows for simpler calculations and faster processing
  - The American Kestrel is not likely to prefer a specific type of forest or similar land cover types over others
- Trim the land cover dataset to Tennessee
- Remove eBird observations from months outside of breeding season (March - August)
  - Doing so removes the migratory observations that are far from normal habitat locations from the dataset.
- (Possibly) Use spatial thinning to reduce the number of data points.
- Buffer the eBird data points by 1km (or similar distance) to create a buffer zone around the points.
- Copy and clip the land cover data to the buffer zone around the eBird data points.
- Standardize all environmental layers (extent, resolution, and projection) to prepare for MaxEnt input.
- Split occurrence data into training and validation datasets.
- Run the MaxEnt model to estimate habitat suitability.
- Evaluate model validity using metrics such as the Area Under the Curve (AUC).
- Generate a predictive habitat suitability map for the state of Tennessee for each year.
- Apply linear regression to the habitat suitability data to determine the trend in habitat suitability over time.
  - A negative trend in total habitat would indicate a decrease in habitat suitability over time, while a positive trend would indicate an increase in habitat suitability over time.
