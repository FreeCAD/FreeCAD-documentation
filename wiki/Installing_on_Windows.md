# Installing on Windows
You can install FreeCAD on Windows by downloading one of the installers below:


{{DownloadWindowsStable}}

After downloading the .exe (NSIS Installer) file, double-click on it to start the installation process.

Below is more information about some technical options. Nevertheless, most users don\'t need more than the above .exe files. Head to [Get started](Getting_started.md) after installation is complete.

## Simple NSIS Installer Installation 

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

If you would like to download a development version (which may be unstable), see the [Download](Download.md) page.

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:

 
```python
choco install freecad
```

every once in a while you can update your software with

 
```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

## Command line installation 

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

### Non-interactive installation 

With the command line

 
```python
msiexec /i FreeCAD<version>.msi
```

installation can be initiated programmatically. Additional parameters can be passed at the end of the command line, for example

 
```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Limited user interface 

The amount of user control permitted by the installer can be controlled with /q options:

-   /qn - No interface
-   /qb - Basic interface - display only a progress dialog with Cancel button
-   /qb! - Like /qb, but hide the Cancel button
-   /qr - Reduced interface - display all dialogs that do not require user interaction (skip all modal dialogs)
-   /qn+ - Like /qn, but display \"Completed\" dialog at the end

### Target directory 

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with

 
```python
TARGETDIR=R:\FreeCAD25
```

The default TARGETDIR is \[WindowsVolume\\Programm Files\\\]FreeCAD.

### Installation for All Users 

Adding

 
```python
ALLUSERS=1
```

causes an installation usable by all users. By default, a non-interactive (/i) installation makes the package usable by the current user (the one performing the installation) only; an interactive installation presents a dialog which defaults to \"all users\" if the user performing the installation is sufficiently privileged.

### Feature Selection 

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - install the software proper, plus the core libraries
-   Documentation - install the documentation
-   Source code - install the sources
-   \... ToDo

In addition, ALL specifies all features. All features depend on DefaultFeature, so installing any feature automatically installs the default feature as well. The following properties control features to be installed or removed

-   ADDLOCAL - list of features to be installed on the local machine
-   REMOVE - list of features to be removed from the local machine
-   ADDDEFAULT - list of features added in their default configuration (which is local for all FreeCAD features)
-   REINSTALL - list of features to be reinstalled/repaired
-   ADVERTISE - list of features for which to perform an advertise installation

There are a few additional properties available; see the MSDN documentation for details.

With these options, adding

 
```python
ADDLOCAL=Extensions
```

installs the interpreter itself and registers the extensions, but does not install anything else.

## Uninstallation

With

 
```python
msiexec /x FreeCAD<version>.msi
```

FreeCAD can be uninstalled. It is not necessary to have the MSI file available for uninstallation; alternatively, the package or product code can also be specified. You can find the product code by looking at the properties of the Uninstall shortcut that FreeCAD installs in the start menu.

## Administrative installation 

With

 
```python
msiexec /a FreeCAD<version>.msi
```

an \"administrative\" (network) installation can be initiated. The files get unpacked into the target directory (which should be a network directory), but no other modification is made to the local system. In addition, another (smaller) msi file is generated in the target directory, which clients can then use to perform a local installation (future versions may also offer to keep some features on the network drive altogether).

Currently, there is no user interface for administrative installations, so the target directory must be passed on the command line.

There is no specific uninstall procedure for an administrative install - simply delete the target directory if no client uses it anymore.

## Advertisement

With

 
```python
msiexec /jm FreeCAD<version>.msi
```

it would be possible, in principle, to \"advertise\" FreeCAD to a machine (with /ju to a user). This would cause the icons to appear in the start menu and the extensions to become registered, without the software actually being installed. The first usage of a feature would cause that feature to be installed.

The FreeCAD installer currently only supports advertisement of start menu entries, but no advertisement of shortcuts.

## Automatic installation on a group of machines 

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Group policy propagation typically takes some time - to reliably deploy the package, all machines should be rebooted.

## Installation on Linux using Crossover Office 

You can install the windows version of FreeCAD on a Linux system using *CXOffice 5.0.1*. Run *msiexec* from the CXOffice command line. Assuming the install package is in the \"software\" directory on drive \"Y:\":

 
```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under _ i.e. Google _.

---
[documentation index](../README.md) > Installing on Windows
