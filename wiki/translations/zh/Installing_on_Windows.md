# Installing on Windows/zh
<div class="mw-translate-fuzzy">

在Windows上安装FreeCAD的最简单方法是下载下面的一个安装程序。


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

下载.msi（Microsoft Installer）文件后，双击它启动安装过程。


</div>


<div class="mw-translate-fuzzy">

以下是有关技术选项的更多信息。如果它看起来令人生畏，不要担心！大多数Windows用户不需要上述.msi以外的任何东西来完成安装并**[入门](Getting_started.md)**FreeCAD！


</div>

### 简单的Microsoft Installer安装 

在Windows上安装FreeCAD的最简单方法是使用上面的可下载安装程序包。本页介绍了Microsoft Installer的用法和功能，以获取更多安装选项。

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

如果要下载开发版本（程序运行可能不稳定），请参阅[下载页面](Download.md)。

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

### 命令行安装

使用msiexec.exe命令行实用程序，可以使用其他功能，例如非交互式安装和管理安装。见下面的例子。

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

### 非交互式安装

使用命令行进行非交互式安装

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

安装可以通过编程方式启动。例如，可以在命令行的末尾传递附加参数。


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### 有限的用户界面

可以使用/q选项控制安装程序允许呈现的用户控制界面：

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - 没有界面
-   /qb - 基本界面 - 仅显示带取消按钮的进度对话框
-   /qb - 和/qb一样，但隐藏取消按钮
-   /qr - 简化界面 - 显示所有不需要用户交互的对话框（跳过所有模态对话框）
-   /qn+ -和/qn一样，但最后显示"已完成"对话框
-   /qb+ -和/qb一样，但最后显示"已完成"对话框


</div>

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

#### 功能选择

FreeCAD 安装器提供了安装，重装，卸载选项：

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - 安装适当的软件，再加上核心库。
-   Documentation - 安装文档。
-   Source code - 安装源码
-   \... ToDo

此外，ALL 指定的所有功能。所有的特性依赖于默认功能 DefaultFeature，所以安装任何功能都会安装 DefaultFeature，下面的参数为指定重装或者卸载

-   ADDLOCAL - 指定需要安装的功能
-   REMOVE - 指定需要卸载的功能
-   ADDDEFAULT - list of features added in their default configuration (which is local for all FreeCAD features)
-   REINSTALL - 指定需要重装／修复的功能
-   ADVERTISE - 指定需要广告方式安装的功能

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


<div class="mw-translate-fuzzy">


{{docnav/zh|Feature list/zh|Install on Unix/zh}}


</div>

---
[documentation index](../README.md) > Installing on Windows/zh
