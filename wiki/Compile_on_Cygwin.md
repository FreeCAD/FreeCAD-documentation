# Compile on Cygwin
**(2019) The contents of this page are obsolete. Please help us to keep it updated!<br/> Meanwhile, try other [compilation options](Compiling.md).**

## How to build and run FreeCAD under Cygwin 

### Prerequisites

To compile FreeCAD, you will need, besides functioning Cygwin environment and programming tools (like compiler), the following libraries:

-   Python ( <http://www.python.org> ), \>= 2.5.x
-   Qt ( <http://www.trolltech.no> ), \>= 4.1.x
-   Coin3D ( <http://www.coin3d.org> ), \>= 2.4.x
-   SoQt ( <http://www.coin3d.org> ), \>= 1.2.x
-   Xerces-c ( <http://xml.apache.org/dist/xerces-c/> )
-   zlib ( <http://www.zlib.net/> )

As far as I know, except of Coin3D and SoQt all libraries are available as prebuilt binary packages from one of the Cygwin mirrors. To install them, first download the latest version of setup.exe from www.cygwin.com and run it with administrator rights. Then follow the instructions of the wizard until the list of all available packages appears. Select the devel files of all the required libraries and install them.

Then download the source tarballs of Coin3D and SoQt and unpack them into a directory of your choice. The Coin library can be built with ./configure \--disable-msvc;make; make install.

Building SoQt is a bit tricky and I haven\'t managed yet to build it in a proper way. There are various problems with X11 functions and Windows API functions which I don\'t know how to solve.

And for the Mesh module of FreeCAD the additional libraries

-   GTS Library ( <http://gts.sourceforge.net> )
-   Wild Magic ( <http://www.geometrictools.com> )
-   OpenCASCADE ( <http://www.opencascade.org> ), you need \>=5.2 here

are required. OpenCASCADE is also needed by the Part and Raytracing modules.

#### Note 1 

As OpenCASCADE that is also required by the Mesh, Part and Raytracing modules is not available for Cygwin it is not possible to build them for this platform. It is planned for the future to move all OpenCASCADE dependencies of the Mesh module into a separate module so that at least this module can be built under Cygwin.

#### Note 2 

All libraries listed above must be built as shared library. Refer to their documentation to see how to do.

#### Note 3 

If possible you should enable thread support for the libraries. At least for Qt thread support is strongly recommended, otherwise you will run into linker errors at build time of FreeCAD.

#### Note 4 

zlib might be already on your system, as this is a library that is used from a lot of other libraries.

#### Note 5 

There seems to be various problems with Qt\'s uic tool of the Cygwin port.

Due to these problems it is not possible to run the GUI under Cygwin at the moment. It is only possible to run the commandline version.

### Configuration

For the build process of FreeCAD we make use of configure scripts. To have an overview of all options type in ./configure \--help, first.

If you have installed all libraries above into standard paths you need not any of the \'\--with\' options at all. Unless you have installed any library into a non-standard path, then make use of the \--with-XXX-includes or \--with-XXX-libs options. (XXX represents the corresponding library.)

#### Note 1 

Due to some limitations of the Windows platform it is not possible to build libraries with unresolved symbols at link time. Thus it is strongly recommended to run ./configure with the option LDFLAGS=-no-undefined, otherwise the creation of shared libraries fails. For more details see section 11.2.1 Creating Libtool Libraries with Automake of the libtool documentation.

#### Note 2 

To specify FreeCAD\'s root directory it is recommended to use only the \'\--prefix\' option from the configure script but not the \--bindir, \--libdir, \... options, because at startup FreeCAD makes assumptions where its lib-, doc-, .. directories reside. The default root directory is located in \~/FreeCAD.

If you know how to work with GNU autoconf, feel free to contribute improvements to our configuration scripts \-\-- that would be great.

### Installation

Once you have built the sources successfully using \'make\' with \'make install\' you can install FreeCAD onto your machine whereever you want. Go to the directory FreeCAD/bin and just type in ./FreeCADCmd. FreeCAD\'s default root directory resides under \~/FreeCAD, so you don\'t need root privileges therefore.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Cygwin
