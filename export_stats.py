import numpy
import rasterio
import json

def get_stats(raster_path: str):
  raster_name = raster_path.split('/')[-1].replace('.tif', '')

  dictionary = { 
                  "name": raster_name,
                  "year": raster_name[-4:],
                  "scenario": raster_name.split('_')[1],
                }

  # open the raster and lock it in the filesystem while working on it
  raster = rasterio.open(raster_path)
  band1 = raster.read(1)

  # count the number of occurances for each pixel value
  value, counts = numpy.unique(band1, return_counts=True)
  pixel_value_counts = dict(zip(value, counts))

  # rename pixel numbers to meaning
  if pixel_value_counts.get(0): pixel_value_counts.pop(0) # exclude 0 since it indicates no value
  if pixel_value_counts.get(1): pixel_value_counts['Water'] = int(pixel_value_counts.pop(1))
  if pixel_value_counts.get(2): pixel_value_counts['Developed'] = int(pixel_value_counts.pop(2))
  if pixel_value_counts.get(3): pixel_value_counts['Mechanically Disturbed National Forests'] = int(pixel_value_counts.pop(3))
  if pixel_value_counts.get(4): pixel_value_counts['Mechanically Disturbed Other Public Lands'] = int(pixel_value_counts.pop(4))
  if pixel_value_counts.get(5): pixel_value_counts['Mechanically Disturbed Private'] = int(pixel_value_counts.pop(5))
  if pixel_value_counts.get(6): pixel_value_counts['Mining'] = int(pixel_value_counts.pop(6))
  if pixel_value_counts.get(7): pixel_value_counts['Barren'] = int(pixel_value_counts.pop(7))
  if pixel_value_counts.get(8): pixel_value_counts['Deciduous Forest'] = int(pixel_value_counts.pop(8))
  if pixel_value_counts.get(9): pixel_value_counts['Evergreen Forest'] = int(pixel_value_counts.pop(9))
  if pixel_value_counts.get(10): pixel_value_counts['Mixed Forest'] = int(pixel_value_counts.pop(10))
  if pixel_value_counts.get(11): pixel_value_counts['Grassland'] = int(pixel_value_counts.pop(11))
  if pixel_value_counts.get(12): pixel_value_counts['Shrubland'] = int(pixel_value_counts.pop(12))
  if pixel_value_counts.get(13): pixel_value_counts['Cropland'] = int(pixel_value_counts.pop(13))
  if pixel_value_counts.get(14): pixel_value_counts['Hay/Pasture Land'] = int(pixel_value_counts.pop(14))
  if pixel_value_counts.get(15): pixel_value_counts['Herbaceous Wetland'] = int(pixel_value_counts.pop(15))
  if pixel_value_counts.get(16): pixel_value_counts['Woody Wetland'] = int(pixel_value_counts.pop(16))
  if pixel_value_counts.get(17): pixel_value_counts['Perennial Ice/Snow'] = int(pixel_value_counts.pop(17))

  dictionary['pixels'] = pixel_value_counts
  dictionary['totalPixels'] = int(sum(counts[1:]))
  
  return dictionary

def export_stats(raster_path: str, export_path: str):
  dictionary = get_stats(raster_path)
  
  with open(export_path, 'w') as file:
    json.dump(dictionary, file, indent=2, separators=(',', ': '))
