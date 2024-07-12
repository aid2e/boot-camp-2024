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






