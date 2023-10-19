#register fnf to the same folder
#lidar extent coordinates are predefined maulally based on documentaion and visual insepection
georeg.extract_lidar_image_norm_grid(inputs,inputs.lat_lvis,inputs.lon_lvis,path_lidar_in)
#extract the lidar data: rh100, rh95.., zg and wave forms

#register the lidar to common tdx/lidar/fsar folder

print("register_lidar_to_common")
register_lidar_to_common(inputs,common_path)

georeg.register_fnf2(inputs,common_path)

plot_im_lidar_fnf(inputs,common_path)
#register fnf to the same folder
#plot all lidar plots

#plot all lidar plots
#preprocessing.plot_im_lidar_fnf(inputs,inputs.common_path_fsar,1)
#preprocessing.plot_im_lidar_fnf(inputs,inputs.common_path_fsar)