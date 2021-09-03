---
- GuiCommand:/pt-br
   Name:Addon manager
   Name/pt-br:Addon manager
   Icon:AddonManager.svg
   MenuLocation:Tools → Addon manager
   Workbenches:''None''
   SeeAlso:[Macros](Macros/pt-br.md), [[External workbenches/pt-br]]
   Version:0.17
---


</div>

## Description

The **Std AddonMgr** command opens the Addon manager. With the Addon manager you can install and manage [external workbenches](external_workbenches.md) and [macros](macros.md) provided by the FreeCAD community. The available workbenches and macros are taken from two repositories, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), and from the [Macros recipes](Macros_recipes.md) page.

Addons that are marked as {{emphasis|Python 2 Only}} will not work in FreeCAD version 0.19 or higher.

Due to changes to the GitHub platform in the year 2020 the Addon manager no longer works if you use FreeCAD version 0.17 or earlier. You need to upgrade to version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) or a recent [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre) version. Alternatively you can install addons manually, see [Notes](#Notes.md) below.

![](images/Std_AddonMgr_dialog.png ) *The Addon manager dialog box*

## Usage

1.  Select the {{MenuCommand|Tools → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager}} option from the menu.
2.  If you are using the Addon manager for the first time, a dialog box will open warning you that the addons in the Addon manager are not officially part of FreeCAD. Press the **OK** button to confirm and continue.
3.  The Addon manager dialog box opens. For more information see [Options](#Options.md).
4.  The **<img src="images/Button_valid.svg" width=16px> Update all** button does not work at this time.
5.  Press the **<img src="images/Process-stop.svg" width=16px> Close** button to close the dialog box.
6.  If you have installed or updated a workbench a new dialog box will open informing you that you have to restart FreeCAD for the changes to take effect.

## Options

The Addon manager dialog box has two tabs on the left, one listing the available workbenches and the other listing the available macros. The information panel on the right will display the homepage of the selected addon.

### Uninstall

1.  Select an installed addon on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
2.  Press the **<img src="images/Delete.svg" width=16px> Uninstall selected** button.

### Install/update

1.  Select an addon on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
2.  Press the **<img src="images/Edit_OK.svg" width=16px> Install/update selected** button.
3.  If you want to add a macro to a custom toolbar then don\'t forget to manually download the icon image file, if available, by clicking on the link on the homepage in the information panel. See [Interface Customization](Interface_Customization#Toolbars.md).
4.  To change the position of an addon workbench in the [Workbench selector](Std_Workbench.md) list see [Interface Customization](Interface_Customization#Workbenches.md).

### Configuration

1.  Press the **<img src="images/Preferences-general.svg" width=16px> Configure...** button.
2.  The Addon manager options dialog box opens.
3.  Optionally check the {{CheckBox|TRUE|Automatically check for updates at start (requires GitPython)}} checkbox.
4.  Optionally add repositories to the **Custom repositories** list. Addons from these repositories will be added on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
5.  Optionally choose proxy settings.
6.  Press the **OK** button or the **Cancel** button to close the dialog box.

## Notes

-   The use of addons is not restricted to the FreeCAD version they were installed from. You will also be able to use them in any other FreeCAD version, supported by the addon, that you may have on your system.
-   The addons available in the Addon manager are not part of the official FreeCAD program and are not supported by the core FreeCAD development team. You should read the provided information carefully to make sure you know what you are installing.
-   Bug reports and feature requests should be made directly to the creator of the addon by visiting the indicated website. Many addon developers are regular users of the [FreeCAD forum](https://forum.freecadweb.org), and can also be contacted there.
-   If the [GitPython](https://github.com/gitpython-developers/GitPython) package is installed on your computer the Addon manager will make use of it, making downloads faster.
-   You can also install addons manually. See [How to install additional workbenches](How_to_install_additional_workbenches.md) and [How to install macros](How_to_install_macros.md).

## Information for developers {#information_for_developers}

If you have developed a workbench or macro, and want to see it included in the Addon manager, read how to do so on the repository pages: ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python workbenches {#python_workbenches}

For python workbenches, you don\'t need any specific approval to have your workbench added to the Addon manager and, being outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it.

### C++ workbenches {#c_workbenches}

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https://forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.





{{Std Base navi

}}  
