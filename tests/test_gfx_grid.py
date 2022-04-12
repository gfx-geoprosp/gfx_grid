#!/usr/bin/env python

"""Tests for `gfx_grid` package."""


from gfx_grid import grid_creator, geometry_creator, grid_const


def test_grid_creator():
    grid = None
    for item in grid_creator.next_grid_geometry():
        grid = item
        break
    assert grid != None
    keys = grid.keys()
    assert 'gfx_id' in keys
    assert grid['gfx_id'] == 1
    assert 'bin_size' in keys
    assert grid['bin_size'] == 64e3
    assert 'geometry' in keys
    assert 'bbox' in keys
    bbox = grid['bbox']
    keys = bbox.keys()
    assert 'xmin' in keys
    assert 'xmax' in keys
    assert 'ymin' in keys
    assert 'ymax' in keys
    geom = geometry_creator.create_geometry(**bbox)
    assert grid['geometry'].wkt == geom.wkt
    geom2 = geometry_creator.gfxid_geometry(1)
    assert geom.wkt == geom2.wkt


def test_geometry_creator():
    idmax = geometry_creator.get_grid_counts()
    assert len(idmax) == len(grid_const.bin_size_list)

    i, j, bin_size = geometry_creator.get_grid_ij(1)
    assert i == -310
    assert j == -320
    assert bin_size == 64e3
    i, j, bin_size = geometry_creator.get_grid_ij(idmax[0])
    assert i == 309
    assert j == 319
    assert bin_size == 64e3

    i, j, bin_size = geometry_creator.get_grid_ij(idmax[0]+1)
    assert i == -620
    assert j == -640
    assert bin_size == 32e3
    i, j, bin_size = geometry_creator.get_grid_ij(idmax[1])
    assert i == 619
    assert j == 639
    assert bin_size == 32e3

    i, j, bin_size = geometry_creator.get_grid_ij(idmax[1]+1)
    assert i == -1240
    assert j == -1280
    assert bin_size == 16e3
    i, j, bin_size = geometry_creator.get_grid_ij(idmax[2])
    assert i == 1239
    assert j == 1279
    assert bin_size == 16e3
