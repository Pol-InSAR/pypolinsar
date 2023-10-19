# from talking and visual inspection , identify flight FL refered to the region, define the PS aquistion numbers from tracks plot baselines
#inspect GEO QL and az-rg QL
# decide if server processing or windows
# for windows copy the scenes (only slc+master, kz, offnadir, slantdem, inc_angle. GTC-folder of master) comment: maybe write a copy script

#!!this is the function that is better to be done from server, no rat file copying except for geo folder
#!!poyyibly save also rp pol files on server and do everything up to georegister on server

##check init_param["file_path_afrisar"], can be D:, C:, server//
fsar_lib.make_npy_all_scenes(inputs,pol_list=["hh","vv","hv","vh"])

fsar_lib.do_calc_pol_covar(inputs,all_baselines_flag=1,pol_list=["hh","vv","hv"],pauli_flag="") #pol_list=["hh","vv","hv","vh"],pauli_flag="pauli"

##think about 3 or 4 polarizations
fsar_lib.data_resample(inputs)

#saving coordinates, note that it reads max, min and resampling factor
georeg.save_band_lat_lon(inputs)

## note that P_Band_set=1 means it will coregister to P band
georeg.coregister_L_P_band(inputs,inputs.common_path_fsar,P_Band_set=1)

##selection of maps to be registered
name_list=["kz_all_hh","offnadir_","inc_a_","slant_dem_",  "rp_pol"]#,  "rp_polpauli"
georeg.georeg_fsar_to_common(inputs,name_list)     

#register lidar
preprocessing.register_lidar_to_common(inputs,common_path)

preprocessing.plot_fsar_phase_coherences_alpha_all_pol(inputs)


if inputs.region=="mabounie": mas_list, sl_list = [0, 0, 0], [2, 3, 5]
if inputs.region=="mondah": mas_list, sl_list = [0, 0, 0], [4, 3, 2]


if inputs.calc_decomp: general_lib.do_calc_decomp(load_path) 
if inputs.psf_calc:  general_lib.do_calc_tomo(inputs,calc_tomo_flag=[1,1,1,1,1])
if inputs.flag_make_pi_matrix: l2_study_class.make_pi_matrix(0,3)
if inputs.ground_calc:    l2_study_class.do_calc_ground()
if inputs.flag_profile_norm:    l2_study_class.do_calc_norm_profile(load_path,calc_tomo_flag=[0,0,1,0,0,0])
if inputs.flag_calc_eigenvec:    l2_study_class.do_calc_eigenvec(),l2_study_class.do_calc_LUTs(profile_switch="norm_hv",bas2_flag=""),l2_study_class.lambda_coefficients()


###tests
#add PSF calculation
reload(tests.test1)
###
tests.test1.test_ramp(inputs)
tests.test1.general_test_resolution_dependent(inputs)
tests.test1.general_test(inputs)
tests.test1.plot_eigen_lambdas(inputs)
tests.test1.test_coh_dif_resolution(inputs)
tests.test1.test_height_tomo(inputs)
###






