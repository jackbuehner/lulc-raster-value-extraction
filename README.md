# Raster pixel value extractor tool

This repsository contains a script to extract all pixels from a raster
that match any value in a provided list.

For example, the USGS used their FORE-SCE model
to produce the [Conterminous United States Land Cover Projections](https://www.sciencebase.gov/catalog/item/5b96c2f9e4b0702d0e826f6d), which contains 18 different land use and
land cover classes (pixel values 1-18). This script can be used to extract
only the water and developed land classes with the function `extract_raster_value`
in `extract_raster_value.py`.

To extract the matching pixels from a raster and save the result to a new raster:
```python
extract_raster_value(
  "input_raster.tiff" # path to the input raster
  [1, 2], # pixel values that should be extracted
  "matching_pixels_output_raster.tiff", # where the output raster should be saved
  (255, 0, 0, 255) # set the color of the extracted pixels to red (rgba format)
)
```

The `extract_developed_land` function in `extract_developed_land.py`
loops through a directory, processes all found `tif` or `tiff` files
to find all developed land pixels, and saves the developed land rasters
to a specified output directory.
It can be adapted to work for other pixel values.