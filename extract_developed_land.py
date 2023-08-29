import os
from extract_raster_value import extract_raster_value 

def extract_developed_land(input_directory: str, output_directory: str, output_file_prefix: str, color: tuple | None):
  os.makedirs(output_directory, exist_ok=True)
  
  for file in sorted(os.listdir(input_directory)):
    filename = os.fsdecode(file)
    
    if filename.endswith(".tif") or filename.endswith(".tiff"):
      print('Processing file "' + os.path.join(input_directory, filename) + '"…')
      extract_raster_value(os.path.join(input_directory, filename), [2], os.path.join(output_directory, output_file_prefix + filename), color)
