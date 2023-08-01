# Compile on Docker
## Overview

Among the options for building and installing FreeCAD, there is the option of using Docker. This method is primarily useful for FreeCAD developers, using Linux or Mac OS computers.

### Benefits

All of FreeCAD\'s dependencies are already installed, compatible with each other, and configured appropriately, allowing you to get started developing very quickly.

-   The dependencies are contained within the docker container, preventing any unwanted packages contaminating your workstation, and preventing any clashing versions.
-   The source code and build directories are outside the docker container. This allows you to use your preferred editors, versioning systems, dev tools etc, without having to set them up in the docker container. You can just use them as normal, right from your workstation. (Also, it means you don\'t have to rebuild the docker container each time you want to build FreeCAD.)
-   For those using obscure \*nix distros and [instructions are not available](Compile_on_Linux#Getting_the_dependencies.md) for fetching dependencies, all you need to install on your workstation is docker, which is quite commonly available across many distributions.
-   It provides a static, immutable development environment. I personally find this useful when developing to reduce the number of potential variables that could be causing an issue. You know you\'ve not altered something esoteric in the environment between builds. For developers collaborating, and both using the same docker container, you can be sure you\'re both working from the same environment, which reduces communication errors caused by differences in environment.

## Docker Repository 

-   Original: <https://gitlab.com/daviddaish/freecad_docker_env>
-   Official: <https://GitHub.com/FreeCAD/Docker>

## Prerequisites

-   10GB of free storage
-   Docker

## Installation

### Download the source 

The best way to get FreeCAD\'s source code is to clone the [Git repository](https://github.com/FreeCAD/FreeCAD). For this you need the `git` program which can be easily installed in most Linux and Mac OS distributions, and it can also be obtained from the [official website](http://git-scm.com/).

This will place a copy of the latest version of the FreeCAD source code in a new directory called `freecad_source`.

 {{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
}}

For more information on using Git, and contributing code to the project, see [Source code management](Source_code_management.md).

#### Source archive 

Alternatively you can download the source as an [archive](https://github.com/FreeCAD/FreeCAD/releases/latest), a `.zip` or `.tar.gz` file, and unpack it in the desired directory.

### Create build directory 

Create a directory to hold your compiled FreeCAD source.

 {{Code|lang=bash|code=
mkdir ~/my_code/freecad_build
}}

### Pull Docker image 

Pull the Docker image. (Official image coming soon.)

 {{Code|lang=bash|code=
docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}

### Allow access to your window manager 

In order for FreeCAD to launch it\'s GUI from within the Docker container, you need to give Docker access permissions to your window manager. In most Linux distributions, this is the X window system. You can use the below command to allow blanket access to X, until you reboot or logoff your computer.

 {{Code|lang=bash|code=
xhost +
}}

If you\'re connected to any untrusted systems, such as via `ssh`, this will make you vulnerable to malicious code. Either close any `ssh` connections, or look into more secure xhost permissions, which is outside the scope of this tutorial.

#### Mac OS users 

For those using Mac OS, the X window system may not be installed. The XQuartz project is a long running open source project that will allow you to add it to your computer. [You can find it here](https://www.xquartz.org/).

### Launch the docker image 

Assign environment variables so the Docker container will mount FreeCAD\'s source code, and build directory. In addition, you can mount an extra directory to contain any files you\'d like to use for testing purposes. In the below snippet, we\'ve left it as your home directory as a simple default.

 {{Code|lang=bash|code=
fc_source=~/my_code/freecad_source
fc_build=~/my_code/freecad_build
other_files=~/
}}

Launch the Docker image.

 {{Code|lang=bash|code=
docker run -it --rm \
-v $fc_source:/mnt/source \
-v $fc_build:/mnt/build \
-v $other_files:/mnt/files \
-e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}

### Build FreeCAD 

You can build FreeCAD using the installed build script, or using your preferred method.

 {{Code|lang=bash|code=
/root/build_script.sh
}}

### Run FreeCAD 

Once FreeCAD has been built, it can be run as normal.

 {{Code|lang=bash|code=
/mnt/build/bin/FreeCAD
}}

You can find the attached directories in the `/mnt` directory.

## Discussion

-   [Docker env build container](https://forum.freecadweb.org/viewtopic.php?f=4&t=42954)
-   [VSCode setup with Docker (1)](https://forum.freecadweb.org/viewtopic.php?f=10&t=48266)
-   [VSCode setup with Docker (2)](https://forum.freecadweb.org/viewtopic.php?p=427812#p427812)

## Related

-   [AppImage](AppImage.md)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > Compile on Docker
