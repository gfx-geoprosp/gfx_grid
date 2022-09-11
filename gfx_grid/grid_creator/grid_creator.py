from ..grid_const import grid_x_min, grid_x_max, grid_y_min, grid_y_max,\
    bin_size_list as size_list
from ..geometry_creator import create_geometry


# iterator for grid geometries
# @params: bbox[minx, miny, maxx, maxy]
#   bounding box in crs 3857
def next_grid_geometry(
        bbox=[-20026400, -20500000, 20026400, 20500000],
):
    # id 1 bbox [-19840000.0, -20480000.0, -19776000.0, -20416000.0]
    _count = 0
    for size in size_list:
        dx = dy = size
        for i in range( int(grid_x_min/dx), int(grid_x_max/dx) ):
            for j in range( int(grid_y_min/dy), int(grid_y_max/dy) ):
                xmin = i * dx
                ymin = j * dx
                xmax = xmin + dx
                ymax = ymin + dy
                _count += 1 # id

                if (
                    (xmin < bbox[0] or xmin > bbox[2])
                    and (xmax < bbox[0] or xmax > bbox[2])
                ):
                    continue
                if (
                    (ymin < bbox[1] or ymin > bbox[3])
                    and (ymax < bbox[1] or ymax > bbox[3])
                ):
                    continue

                yield {
                    'gfx_id': _count,
                    'bin_size': size,
                    'geometry': create_geometry(xmin, xmax, ymin, ymax),
                    'bbox': {
                        'xmin': xmin,
                        'xmax': xmax,
                        'ymin': ymin,
                        'ymax': ymax,
                    },
                }
