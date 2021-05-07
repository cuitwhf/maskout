import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfeat
from cartopy.mpl.patch import geos_to_path

from matplotlib.path import Path
import matplotlib.pyplot as plt


def maskout(ax, shp_path):
    # Mask out
    shpdata = Reader(shp_path)
    # <cartopy.io.shapereader.BasicReader object at 0x00000212BAC74C40>
    ax.add_geometries(shpdata.geometries(), crs=ccrs.PlateCarree(), edgecolor='k', facecolor='none', lw=0.0)
    # print(shpdata.geometries())  # <generator object BasicReader.geometries at 0x0000022A28523270>

    # Obtain the shapefile path
    records = shpdata.records()
    for record in records:
        path = Path.make_compound_path(*geos_to_path([record.geometry]))
        # print(path)

    for collection in ax.collections:
        collection.set_clip_path(path, transform=ax.transData)