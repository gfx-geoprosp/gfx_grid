import math
import geopandas as gpd
from shapely import geometry
from ..grid_const import grid_x_min, grid_x_max, grid_y_min, grid_y_max,\
    bin_size_list as size_list, base_counts as base


# return array of total grid counts for each grid size included respectfully
def get_grid_counts():
    idmax = []
    count = 0
    for size in size_list:
        le_max = int( base * ( ( max(size_list) / size )**2 ) )
        idmax.append(
            count + le_max
        )
        count += le_max
    return idmax


# convert gfx_id to i, j index
def get_grid_ij(gfx_id):
    idmax = get_grid_counts()
    gfx_bins = [e for e in idmax if e < gfx_id]
    gfx_bin_size = size_list[len(gfx_bins)]
    gfx_id_reducer = gfx_bins[-1] if len(gfx_bins) > 0 else 0
    xidx = [
        int( grid_x_min / gfx_bin_size ),
        int( grid_x_max / gfx_bin_size )
    ]
    yidx = [
        int( grid_y_min / gfx_bin_size ),
        int( grid_y_max / gfx_bin_size )
    ]
    # xn = xidx[1] - xidx[0]
    yn = yidx[1] - yidx[0]

    wipos = math.floor( (gfx_id - gfx_id_reducer - 1) / yn )
    wi = [i for i in range(xidx[0], xidx[1])][wipos]
    wjpos = (gfx_id - gfx_id_reducer - 1) % yn
    wj = [j for j in range(yidx[0], yidx[1])][wjpos]
    return wi, wj, gfx_bin_size


# create geometry
def create_geometry(xmin, xmax, ymin, ymax, **kwargs):
    grid_geom = geometry.Polygon([
        [xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]
    ])

    gdf = gpd.GeoDataFrame(geometry=[grid_geom])
    gdf = gdf.set_crs(epsg=3857)
    gdf = gdf.to_crs(epsg=4326)
    grid_geom = gdf['geometry'][0] # type: ignore
    return grid_geom


# return grid geometry for gfx_id
def gfxid_geometry(gfx_id):
    wi, wj, bsize = get_grid_ij(gfx_id)
    xmin = wi * bsize
    ymin = wj * bsize
    xmax = xmin + bsize
    ymax = ymin + bsize

    return create_geometry(xmin, xmax, ymin, ymax)
