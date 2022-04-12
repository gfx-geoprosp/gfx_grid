# bin size in meters
# bin_size=1e3 means grid size are 1km x 1km
bin_size_list = [64e3, 32e3, 16e3, 8e3, 4e3, 2e3, 1e3]


# bounding box area for grid
# origin point are 0, 0 in SRID 3857
grid_x_min = -19840000.0 # 64e3 * -310
grid_x_max =  19840000.0 # 64e3 *  310
grid_y_min = -20480000.0 # 64e3 * -320
grid_y_max =  20480000.0 # 64e3 *  320


base_counts = int((
    (grid_x_max - grid_x_min) *
    (grid_y_max - grid_y_min)
) / (bin_size_list[0]**2))
