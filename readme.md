# Earth Engine Mosaic and Animation - World Temperature
This project utilizes Google Earth Engine and Python to create a mosaic of MODIS MOD11A2.061 Land Surface Temperature (LST) images for Kazakhstan and generates seasonal animations. Additionally, it includes code for creating smooth transitions between yearly mosaics.

## Requirements
- Earth Engine Python API
- geemap
- imageio
- Pillow

  
## Earth Engine Initialization
Make sure to authenticate and initialize the Earth Engine Python API using:

```python
import ee
import geemap

# Authentication and Earth Engine initialization
ee.Initialize()
```

## Generating Yearly Mosaics
Load Kazakhstan boundaries:
```python
kazakhstan = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017') \
    .filter(ee.Filter.eq('country_na', 'Kazakhstan'))
```

Define functions for obtaining image IDs and generating mosaics:
```python
def get_image_ids(collection):
    image_ids = collection.aggregate_array('system:index')
    return image_ids

def generate_mosaic(year):
    # ... (see code for more details)
```
Create mosaics for each year:
```python
# Iterating over years and generating mosaics
for year in range(2000, 2021):
    generate_mosaic(year)
```
## Creating Seasonal Animations
1.Uncomment the relevant section for either winter or summer.  

2.Modify the font path, size, and text position.  

3.Choose the appropriate images (winter or summer).  

4.Run the script to create animations.    

5.Save the animations in MP4 format.  

## Data Source
The images are based on MODIS MOD11A2.061 LST data.

## Additional Information
The script prints MODIS image IDs for each year.
Mosaic images are displayed on an interactive map using geemap.
Animations are saved with a smooth transition effect and labeled with the corresponding year.

## Credits
Original code by [TyuninaA]

MODIS MOD11A2.061 data source: [[Google EE ] (https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A2)https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A2]
