#!/usr/bin/env python3
import sys
import os
Ortho4XP_dir='..' if getattr(sys,'frozen',False) else '.'
sys.path.append(os.path.join(Ortho4XP_dir,'src'))

import O4_File_Names as FNAMES
sys.path.append(FNAMES.Provider_dir)
import O4_Imagery_Utils as IMG
import O4_Vector_Map as VMAP
import O4_Mesh_Utils as MESH
import O4_Mask_Utils as MASK
import O4_Tile_Utils as TILE
import O4_Config_Utils as CFG  # CFG imported last because it can modify other modules variables


cmd_line="USAGE: Ortho4XP_v130.py lat lon imagery zl (won't read a tile config)\n   OR:  Ortho4XP_v130.py lat lon (with existing tile config file)"

if __name__ == '__main__':
    if not os.path.isdir(FNAMES.Utils_dir):
        print("Missing ",FNAMES.Utils_dir,"directory, check your install. Exiting.")
        sys.exit()   
    for directory in (FNAMES.Preview_dir, FNAMES.Provider_dir, FNAMES.Extent_dir, FNAMES.Filter_dir, FNAMES.OSM_dir,
                      FNAMES.Mask_dir,FNAMES.Imagery_dir,FNAMES.Elevation_dir,FNAMES.Geotiff_dir,FNAMES.Patch_dir,
                      FNAMES.Tile_dir,FNAMES.Tmp_dir):
        if not os.path.isdir(directory):
            try: 
                os.makedirs(directory)
                print("Creating missing directory",directory)
            except: 
                print("Could not create required directory",directory,". Exit.")
                sys.exit()
    IMG.initialize_extents_dict()
    IMG.initialize_color_filters_dict()
    IMG.initialize_providers_dict()
    IMG.initialize_combined_providers_dict()
    
    #if len(sys.argv)==1:
    lat=int(os.environ['O_LAT'])
    lon=int(os.environ['O_LON'])
    apt_dep=os.environ['O_APT_DEP']
    apt_arr=os.environ['O_APT_ARR']
    #else:
    #lat=int(sys.argv[1])
    #    lon=int(sys.argv[2])
    #    apt_dep=sys.argv[3]
    #    apt_arr=sys.argv[4]

    tile=CFG.Tile(lat,lon,'')

    tile.apt_dep=apt_dep
    tile.apt_arr=apt_arr

    try:
        VMAP.build_poly_file(tile)
        sys.stdout.flush()
        MESH.build_mesh(tile)
        sys.stdout.flush()
        MASK.build_masks(tile)
        sys.stdout.flush()
        TILE.build_tile(tile)
        sys.stdout.flush()
        print("Bon vol!")
    except:
        print("Crash!")
 
        
