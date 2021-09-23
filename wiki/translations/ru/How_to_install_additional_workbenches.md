# How to install additional workbenches/ru
<div class="mw-translate-fuzzy">


{{TutorialInfo/ru
|Topic=Programming
|Level=Medium programmer
|Time=15 minutes
|FCVersion=All
|Author=[r-frank](User:R-Frank.md)
}}


</div>

## Description

Power users have extended FreeCAD with various custom [external workbenches](external_workbenches.md) that are not integrated into the core source code but are easy to install on an existing FreeCAD distribution. Here we will cover the installation methods for the different operating systems.


**Note:**

starting from version 0.17, FreeCAD features an <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) in the **Tools → Addon Manager** menu, that allows installing both macros and workbenches. The instructions below are only required if you wish to manually install a workbench. This may be necessary if for some reason the Addon Manager doesn\'t work but you have access to the workbench downloaded as a {{FileName|.zip}} package.


<div class="mw-collapsible mw-collapsed toccolours">

## Installing on Windows 

How to install additional workbenches and addons on Windows


<div class="mw-collapsible-content">

### Obsolete


**Note:**

using the \"addons-installer\" is not recommended any more. Using the [Addon Manager](Addon_Manager.md) in all systems is the recommended way.

Use the [addons-installer from Github](https://github.com/FreeCAD/FreeCAD-addons).

During Google Summer of Code 2016 student Mandeep Singh started work on an improved version ([available here](https://github.com/mandeeps708/PluginManager)) but that version needs further work before it can be fully integrated in FreeCAD.

### Manual Install 


**Note:**

This method is possible but not necessary with the introduction of the [Addon Manager](Addon_Manager.md). Nevertheless, the information here may still be useful to some.

-   Download the workbench from github by clicking on the button **Clone** or **Download** on the github page (upper right corner) and choosing \"Download ZIP\"
-   Unpack the downloaded archive on your local hard disk
-   Within FreeCAD, locate the macro path by choosing **Edit → Preferences → General → Macro** and look for the "Macro path"
-   Supposed your Windows-Login is "*username*" the default macro path is {{FileName|%APPDATA%\FreeCAD\}} which is usually {{FileName|C:\Users\''username''\Appdata\Roaming\FreeCAD}}
-   Within the macro-directory create (if not already present) a folder called "{{FileName|Mod}}"
-   Within the Mod folder, create a folder with the name of the workbench, for example "Curves"
-   Now move the unpacked files and sub-folders of the workbench to the just created workbench-folder
-   After restart of FreeCAD you should now have an entry in the [workbench selector](Std_Workbench.md)

**Additional Recommendation for updating workbenches**

On windows, when updating an already installed workbench, Windows keeps the old .py files as .pyc. Since this may lead to trouble, it is recommended to uninstall the workbench, restart FreeCAD and install the new version of the workbench.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installing on Linux 

How to install additional workbenches and addons on Linux


<div class="mw-collapsible-content">

### Using git 

Adding the [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) within the ppa-manager.
Installing the workbenches via synaptic packet manager.


```python
$ sudo apt-get install git python-numpy python-pyside
$ mkdir ~/.FreeCAD/Mod
$ cd ~/.FreeCAD/Mod
$ git clone  https://github.com/tomate44/CurvesWB.git
```

In FreeCAD you will now have a new workbench-entry called \"CurvesWB\". Once installed, use git to upgrade to the latest version:


```python
$ cd ~/.FreeCAD/Mod/CurvesWB
$ git pull
$ rm *.pyc
```

### Manual Installation 


**Note:**

This method is possible but not necessary with the introduction of the [Addon Manager](Addon_Manager.md). Nevertheless, the information here may still be useful to some.

-   Download the workbench from github by clicking on the button **Clone** or **Download** on the github page (upper right corner) and choosing \"Download ZIP\"
-   Unpack the downloaded archive on your local hard disk
-   Within FreeCAD, locate the macro path by choosing **Edit → Preferences → General → Macro** and look for the "Macro path"
-   By default, the macro directory is the (hidden) **./.FreeCAD/** directory in your home-directory
-   Within the macro-directory create (if not already present) a folder called "{{FileName|Mod}}"
-   Within the Mod/ folder, create a folder with the name of the workbench, for example "Curves"
-   Now move the unpacked files and sub-folders of the workbench to the just created workbench-folder
-   After restart of FreeCAD you should now have an entry in the [workbench selector](Std_Workbench.md)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installing on Mac 

How to install additional workbenches and addons on MacOS


<div class="mw-collapsible-content">

### Manual Installation 


**Note:**

This method is possible but not necessary with the introduction of the [Addon Manager](Addon_Manager.md). Nevertheless, the information here may still be useful to some.

For the sake of this example, say you\'ve chosen the [Curves Workbench](Curves_Workbench.md) as the external workbench you want to install:

-   Choose and download the git repository of your chosen external workbench as a ZIP file
-   There are two possible locations for your Addon workbench \'Mods\':

1.  All Users: {{FileName|/Applications/FreeCAD.app/Contents/Resources/Mod}}
2.  Current user only: {{FileName|/Users/myusername/Library/Preferences/FreeCAD/Mod}}

-   If you use Finder to navigate manually to the All Users location in Applications you will need to
    -   go to {{FileName|/Applications}}\" and select FreeCAD.app
    -   right-mouse-click and select \"Show Package Contents\", a new window will appear with a folder named \"Contents\"
    -   single-click on the folder \"Contents\" then on \"Resources\" and double-click to open the folder \"Mod\"
-   Once you are in whichever \"Mod\" folder you want to use, create a New Folder named \"Curves\"
-   Unzip downloaded repository in the folder \"Mod/Curves\"


</div>


</div>

## General troubleshooting 

-   Don\'t use special characters (for example German umlauts) in your windows user name, otherwise FreeCAD will not recognize files and folders in the macro path.
-   If you have already set up a user name with special characters either create a new user name or point the macro path to a directory not using special characters.
-   Go to **Tools → Customize → Workbenches** and make sure the workbench is not set to invisible.
-   With 32-bit systems and FreeCAD 0.16.6706, after attempts to install, the additional Workbenches may not be available. In this case
    -   keep the [report view](report_view.md) open while starting FreeCAD, and read the error,
    -   see this forum thread [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)


 {{Powerdocnavi}}

[Category:External Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)

---
[documentation index](../README.md) > [External Workbenches](Category:External Workbenches.md) > How to install additional workbenches/ru
