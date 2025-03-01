import samgeo
from osgeo import gdal
import os
import torch
from samgeo import SamGeo, tms_to_geotiff

bbox = [-95.3704, 29.6762, -95.368, 29.6775]
image = r'images/download/test.tif'
# tms_to_geotiff(output=image, bbox=bbox, zoom=20, source='Satellite')

out_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
# checkpoint = os.path.join(out_dir, 'src\sam_vit_b_01ec64.pth')
checkpoint = r'asset\sam_vit_b_01ec64.pth'

device = 'cuda' if torch.cuda.is_available() else 'cpu'
sam = SamGeo(
    checkpoint=checkpoint,
    model_type='vit_b',
    device=device,
    # erosion_kernel=(3, 3),
    # mask_multiplier=255,
    sam_kwargs=None,
)

mask = r'images/segmentation/test.tif'
sam.generate(image, mask)

vector = r'images/segmentation/test.shp'
sam.tiff_to_shp(mask, vector, simplify_tolerance=None)
print("pilllll!:")
print('a')

a = 1
if a==1:
    print("111")
else: 
    print("222")

print("AAaa")

print('小香猪')

print("小骆")