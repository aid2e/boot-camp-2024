# EIC installation and geometry

## eic-shell

Please check out [here](https://eic.github.io/tutorial-setting-up-environment/) for the tutorials from EIC ePIC collaboration.

* `mkdir -p $EIC_PROJECT_DIR/eic && cd $EIC_PROJECT_DIR/eic`
* Download the install file -- `wget --output-document install.sh https://get.epic-eic.org`
* install the file -- `bash install.sh`
* Check your installation -- `eic-shell` and should load the container. 
* With HPC systems that have `cvfms` (CernVM File System), the containers with variety of versons are shipped. if needed a different version to be loaded. If not one has to download versions seperately using `singularity pull`

## dd4hep

Please check out [here](https://eic.github.io/tutorial-geometry-development-using-dd4hep//) for the tutorials from EIC ePIC collaboration.

* `source /opt/detector/epic-main/bin/thisepic.sh` -- sources all the necessary environment variables to identify the detector xml files.
* look into a few variables -- `$DETECTOR_PATH`, `$DETECTOR`, `$DETECTOR_CONFIG`
* Look into the xml file -- `vim ${DETECTOR_PATH}/${DETECTOR}.xml`
* Visualize the geometry by -- `dd_web_display /path/to/xml`
* run overlap checks to see if any geometries are overlapping by -- ``

### Exercise

* Visualize the geometry files for `far forward`, `dRICH` and `inner` detectors. 

### Having own version of the geometry

* `cd $EIC_PROJECT_DIR`
* If not in eic-shell then `./eic/eic-shell`
* `git clone https://github.com/eic/epic.git`
* `mkdir $EIC_PROJECT_DIR/epic_install $EIC_PROJECT_DIR/epic_build`
* `cmake -B $EIC_PROJECT_DIR/epic_build -S $EIC_PROJECT_DIR/epic -DCMAKE_INSTALL_PREFIX=$EIC_PROJECT_DIR/epic_install`
* `cmake --build $EIC_PROJECT_DIR/epic_build -j8`
* `cmake --install $EIC_PROJECT_DIR/epic_build`
* `source $EIC_PROJECT_DIR/epic_install/bin/thisepic.sh`

### Exercise

* Repeat the same steps as above
* Try to change the dimensions of say the cylindrical inner tracker. 

### Caveats 

In nodes without a internet connections, the scripts fail due to the fact the calibration files cannot be downloaded. This is the case in JLab's farm nodes as well as some nodes in W&M. To circumvent this, one can in download all necessary calibration files and place them in the `${DETECTOR_PATH}/calibrations` folder

1. Within the `eic-shell` and with all neccessary `epic_install`, run `dd_web_display  ${DETECTOR_PATH}/${DETECTOR_CONFIG}.xml`
2. This should produce `calibrations` and `fieldmaps`. 
3. `cp -r calibrations/* $DETECTOR_PATH/calibrations/`
4. `cp -r fieldmaps $DETECTOR_PATH/calibrations/`

Now, you have neccesary calibration files for the detector configuration you are using.






