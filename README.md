# GFX Grid
GFX Grid Generator

# Features
- grid geometry iterator with `grid_creator`
    ```python
    from gfx_grid import grid_creator

    for grid in grid_creator.next_grid_geometry():
        # do something with geometry, bin_size, gfx_id, and bbox
        if grid.gfx_id < 1000:
            continue
        elif grid.bin_size < 8e3:
            continue
    ```

- generate single geometry with `geometry_creator`
    ```python
    from gfx_grid import geometry_creator

    geom = geometry_creator.create_geometry(xmin=1, xmax=2, ymin=3, ymax=4)
    geom2 = geometry_creator.gfxid_geometry(1)
    ```

# Credits
This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.
- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)
