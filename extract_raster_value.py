import numpy
import rasterio

def extract_raster_value(input_raster_path: str, pixel_values: list[float], output_raster_path: str | None, color: tuple = (0, 0, 0, 255)):
  """
  Extracts all pixels of the specified value or values and returns it as a single band.
  
  If `output_raster_path` is defined, a new raster file will be created based on the output.
  
  `color` should be an rgba tuple (e.g., `(255, 0, 0, 255)`for red) ,
  """
  # open the raster and lock it in the filesystem while working on it
  raster = rasterio.open(input_raster_path)
    
  # create new array where all values in the band of 2 becomes 1 and everything else becomes 0
  # in order to create an array that shows where developed land is located
  band1 = raster.read(1)
  recalc: numpy.ndarray[float] = numpy.where(numpy.isin(band1, pixel_values), 1, 0)

  # export the extracted band pixel values
  # with the extracted band as black pixels and the rest as transparent white pixels
  out_profile = raster.profile.copy()
  out_profile.update(nodata=0)
  with rasterio.open(output_raster_path, "w", **out_profile) as dest:
    dest.write(recalc, 1)
    dest.write_colormap(1, { 1: color })

  # remove the lock on the raster
  raster.close()
  
  return recalc
  
  