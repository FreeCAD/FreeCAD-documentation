# CfdOF Install
## Platforms supported 

### Linux

Any system on which FreeCAD and the prerequisites listed below can be installed.

### Windows

Windows 7-11; 64-bit version is required.

### macOS

Not widely tested, but success has been reported. See [the following forum post](https://forum.freecadweb.org/viewtopic.php?f=37&t=63782&p=547611#p547578) for instructions.

## Prerequisites

The CfdOF workbench depends on the following external software, some of which can be automatically installed (see below for instructions).

1.  [Latest release version of FreeCAD (at least version 0.20.0 / git commit 29177)](https://www.freecadweb.org/downloads.php) or [latest development version (prerelease).](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)
2.  OpenFOAM Foundation [versions 9-10](http://openfoam.org/download/) or ESI-OpenCFD [versions 2006-2306.](http://openfoam.com/download)
3.  [Paraview.](http://www.paraview.org/)
4.  [cfMesh (customised version updated to compile with latest OpenFOAM versions).](https://sourceforge.net/projects/cfmesh-cfdof/)
5.  [HiSA (High Speed Aerodynamic Solver).](https://hisa.gitlab.io/)
6.  [Gmsh (version 2.13 or later)](http://gmsh.info/) - optional, for generating tetrahedral meshes.

## Setting up the CfdOF workbench 

### Windows 

The latest [release](https://www.freecadweb.org/downloads.php) or [development](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) FreeCAD build can be obtained (64 bit version) and installed by respectively running the installer or extracting the .7z archive to a directory . In the latter case, FreeCAD can be run in place (\\bin\\FreeCAD.exe).

CfdOF itself is installed into FreeCAD using the Addon manager:

-   Run FreeCAD
-   Select Tools \| Addon manager \...
-   Select CfdOF in the list of workbenches, and click \"Install/update\"
-   Restart FreeCAD
-   For installation of dependencies, see below

Note: The CfdOF workbench can be updated at any time through the Addon manager.

#### Dependency installation 

Dependencies can be checked and installed conveniently from the CfdOF Preferences panel in FreeCAD. In the FreeCAD window, select Edit \| Preferences \... and choose \"CfdOF\". The dependencies can be installed as individual components or as part of a docker container (refer to the [Docker container install](CfdOF_Install#Docker_container_install.md) section below).

The OpenFOAM installation is via the [OpenCFD MinGW package](https://www.openfoam.com/download/install-binary-windows-mingw.php), and the [BlueCFD Core](https://bluecfd.github.io/Core/) port of OpenFOAM is also supported.

OpenFOAM can be installed manually using the above links, or by clicking the relevant button in the Preferences panel described above. If you experience problems running OpenFOAM in CfdOF, please make sure you have a working installation by following instructions on the relevant websites.

To interface correctly with the OpenFOAM installation, CfdOF needs to be able to write to its install location. Some users experience problems using a location inside C:\\Program Files due to restrictions imposed by Windows User Account Control. It is therefore suggested to install to an alternative location, preferably in your home directory.

If OpenFOAM is installed with administrator privileges using the above packages, then Microsoft MPI will also optionally be installed. If not, then it will be necessary to download and install it manually from the [Microsoft MPI download page](https://learn.microsoft.com/en-us/message-passing-interface/microsoft-mpi#ms-mpi-downloads). MPI is needed in order to run in parallel.

Set the OpenFOAM install directory in the preferences panel to the install directory ending in the \'vXXXX\' subfolder (where XXXX is the version number installed) for the MinGW package, or the BlueCFD install directory. It will be automatically detected in the default install locations.

Any version of [ParaView](https://www.paraview.org/download/) can be installed, by following the above link or clicking the relevant button in the Preferences panel. Set the ParaView install path in the preferences panel to the \'paraview.exe\' file in the \'bin\' subfolder of the ParaView installation. Common defaults will be detected if it is left blank.

Likewise, cfMesh and HiSA can be installed from the Preferences panel. Do not close it until the \'Install completed\' message is received. Note that the OpenFOAM installation must be in a writable location for cfMesh and HiSA to be installed successfully.

Choosing the \"Check dependencies\" option will verify that all prerequisites have been successfully installed.

### Linux 

AppImages of the latest [release](https://www.freecadweb.org/downloads.php) or [development](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) versions of FreeCAD can be downloaded and run directly without installation. Note that you will have to enable execution permission on the downloaded file to run it. Otherwise, FreeCAD can be built from the source code on the [FreeCAD GitHub page](https://github.com/FreeCAD/FreeCAD).

Note:

-   Installations of FreeCAD via Linux package managers make use of your local Python installation. Therefore you might need to install additional Python packages to get full functionality. The dependency checker (see below) can help to diagnose this.
-   Note that the \'Snap\' container installed through some distributions\' package managers can be problematic as it does not allow access to system directories, and therefore OpenFOAM has to be installed in the user\'s home directory to be runnable from FreeCAD.

For the reasons above we recommend the AppImage as the most robust installation option on Linux.

CfdOF itself is installed into FreeCAD using the Addon manager:

-   Run FreeCAD
-   Select Tools \| Addon manager \...
-   Select CfdOF in the list of workbenches, and click \"Install/update\"
-   Restart FreeCAD
-   For installation of dependencies, see below

Note: The CfdOF workbench can be updated at any time through the Addon manager.

#### Dependency installation 

Dependencies can be checked and some of them installed conveniently from the CFD Preferences panel in FreeCAD. In the FreeCAD window, select Edit \| Preferences \... and choose \"CfdOF\".

The dependencies can be installed manually, or as part of a docker container (refer to [Docker container install](http://CfdOF_Install#Docker_container_install)_below). Manual installation may be undertaken for OpenFOAM ([OpenCFD](https://openfoam.com/download) or [Foundation](https://openfoam.org/download/) versions), [ParaView](http://www.paraview.org/) and [Gmsh](http://gmsh.info/) (optional) by using the links above or your distribution\'s package manager. Note, however, that the OpenFOAM packages bundled in some Linux distributions may be out of date or incomplete; for example, the standard Debian and Ubuntu packages do not include the build command \'wmake\' and therefore cannot be used with the optional components \'HiSA\' and \'cfMesh\'. We therefore recommend installation of the packages supplied through the official websites above. Please make sure the install the \'development\' package where available (usually named with the suffix \'-devel\' or \'-dev\') to be sure that the optional components \'HiSA\' and \'cfMesh\' can be compiled with \'wmake\'.

Set the OpenFOAM install directory in the preferences panel - examples of typical install locations are /usr/lib/openfoam/openfoam2306, /opt/openfoam10 or /home/user/OpenFOAM/OpenFOAM-10.x (it will be automatically detected in common default install locations). Note that if you have loaded the desired OpenFOAM environment already before starting FreeCAD, the install directory should be left blank.

cfMesh and HiSA can be installed using the Preferences panel described above, and can be downloaded and built from their source code inside your OpenFOAM installation if you have not already done so yourself. Note that this is a lengthy process.

Choosing the \"Check dependencies\" option will verify that all prerequisites have been successfully installed.

### Docker container install 

Docker containers offer a convenient way of providing pre-compiled program packages for both windows and linux. macOS can also be supported but assistance will be required to setup a container. Please leave a message on the [forum](https://forum.freecadweb.org/viewforum.php?f=37).

#### Docker on Windows 

The preferred docker run-time for Windows is via [podman](https://podman.io/) as currently this provides fast filesystem integration. [Docker Desktop](https://www.docker.com/products/docker-desktop/) may also be used.

1.  Install [podman](https://github.com/containers/podman/releases/download/v4.2.1/podman-v4.2.1.msi) (or [docker desktop](https://www.docker.com/products/docker-desktop/)).
2.  If using podman, open a cmd window and issue the following commands:
    -   podman machine init
    -   podman machine start
    -   podman machine set --rootful
3.  Edit → Preferences → CfdOF: Press the Install Paraview button.
4.  Edit → Preferences → CfdOF: Select Use docker.
5.  Press the Install Docker Container button. There is no need to install gmsh, cfmesh and HISA as they are included in the docker image.
    -   If using podman, fast WSL file system integration can be enabled:
    -   Create a new subdirectory (for example cfdof) in the following directory created by podman: \\wsl$\podman-machine-default\home\user
    -   In the cfdof preference page, set the default output directory as above: \\wsl$\podman-machine-default\home\user\cfdof
6.  Press the Run dependency checker button.

#### Docker on Linux 

1.  Install docker using these [instructions](https://www.linuxtechi.com/install-docker-engine-on-debian/) (or similar).
2.  Install paraview as per the package installation instructions for your distribution (for example sudo apt-get install paraview on debian).
3.  Edit → Preferences → CfdOF: Select Use docker.
4.  Press the Install Docker Container button. There is no need to install gmsh, cfmesh and HISA as they are included in the docker image.
5.  Press the Run dependency checker button.



---
⏵ [documentation index](../README.md) > CfdOF Install
