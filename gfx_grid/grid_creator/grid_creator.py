from ..grid_const import grid_x_min, grid_x_max, grid_y_min, grid_y_max,\
    bin_size_list as size_list
from ..geometry_creator import create_geometry


# iterator for grid geometries
def next_grid_geometry():
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
