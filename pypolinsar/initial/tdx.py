
preprocessing.make_scenes_plot(inputs,scenes_dir="scenes")


georeg.min_lat_lon_tdx(inputs)

#search coordniates in Changhuyn folder
#visually assess the baselines and copy the suited ones manually to folder scenes
#make inputs of suitable scenes
search_tdx_scenes_flag=0
if search_tdx_scenes_flag:
    search_tdx_scenes()

#find common extent of tdx scenes and generate lat, lon axes, also it should be smaller than LVIS extent
if min_lat_lon_tdx_flag:     
        georeg.min_lat_lon_tdx(inputs,inputs.tdx_scene_name_list)
    
    # #register to the coordinates
    # if tdx_preprocessing_flags["register_tdx_to_common_tdx_flag"]:
    #     for tdx_scene_name in inputs.tdx_scene_name_list:  
    #         print(tdx_scene_name)
    #         register_tdx_to_common_tdx(inputs,tdx_scene_name)


#tests
#in the common tdx folder make tdx plots to check the values of phase, coherence, alpha with respect to kz_h
for tdx_scene_name in inputs.tdx_scene_name_list:  compensate_absolute_phase(inputs,tdx_scene_name,extent="tdx")
for tdx_scene_name in inputs.tdx_scene_name_list:  check_complex_coh(inputs,tdx_scene_name,extent="tdx",phase_cor=1)
for tdx_scene_name in inputs.tdx_scene_name_list:  check_complex_coh(inputs,tdx_scene_name,extent="tdx")


#check the phase ramp and absolute shift
#save corrected for ramp images in the new folder \phase_corrected
#repeat plots make  of phase, coherence, alpha with respect to kz_h

#register tdx scenes lidar/all tdx/fsar common extent

#pct
#check kz and kz non corrected processin
#make slope analysis-> dependency of inversion



#name explicitly the data you want to register
name_list=["coh_cor","kz_cor","dem","phase","coh","kz","phase_0cor"] #+"_geo_lonlat"
#choose to which coordinates to project
#lat_to,lon_to=np.load(Path(inputs.common_path_tdx,"lat.npy")),np.load(Path(inputs.common_path_tdx,"lon.npy"))   
#or
lat_to,lon_to=np.load(Path(inputs.common_path_fsar,"lat.npy")),np.load(Path(inputs.common_path_fsar,"lon.npy"))   

#below 2nd options for registering to different folder is written. can be improved!

for tdx_scene_name in inputs.tdx_scene_name_list: 
    #load_path=Path(inputs.data_path,inputs.region,"tdx",                "scenes" , tdx_scene_name )
    load_path=Path(inputs.data_path,inputs.region,"tdx","common_extent","scenes" , tdx_scene_name )
    #save_path=Path(inputs.data_path,inputs.region,"tdx","common_extent","scenes" , tdx_scene_name )
    save_path=Path(inputs.data_path,inputs.region,"fsar","common_extent","scenes" , tdx_scene_name )
    #lat_from,lon_from = np.load(Path(load_path, "col_axis_lat_coord.npy")),np.load(Path(load_path,"row_axis_lon_coord.npy"))
    lat_from_path=Path(inputs.data_path,inputs.region,"tdx","common_extent")
    #lat_from,lon_from = np.load(Path(load_path, "col_axis_lat_coord.npy")),np.load(Path(load_path,"row_axis_lon_coord.npy"))
    lat_from,lon_from = np.load(Path(lat_from_path, "lat.npy")),np.load(Path(lat_from_path,"lon.npy"))
    preprocessing.register_different_latlon(inputs,load_path,save_path,name_list,lat_from,lon_from,lat_to,lon_to)
