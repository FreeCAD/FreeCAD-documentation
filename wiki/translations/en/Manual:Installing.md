# Manual:Installing/en
{{Manual:TOC}}

FreeCAD uses the [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) license; you may download, install, redistribute and use FreeCAD the way you want, regardless of the type of work you\'ll do with it (commercial or non-commercial). You are not bound to any clause or restriction, and the files you produce with it are fully yours. The only thing that the license prohibits, really, is to claim that you programmed FreeCAD yourself!

FreeCAD behaves the same on Windows, Mac OS and Linux. However, the way to install it differs slightly depending on your platform. On Windows and Mac, the FreeCAD community provides precompiled packages (installers) ready to download; while on Linux, the source code is made available to Linux distributions maintainers who are then responsible for packaging FreeCAD for their specific distribution. As a result, on Linux, you can usually install FreeCAD right from the software manager application.

The official FreeCAD download page for Windows and Mac OS is <https://github.com/FreeCAD/FreeCAD/releases>

**FreeCAD versions**

The official releases of FreeCAD, that you can find on the page referenced above and in your distribution\'s software manager, are stable versions. However, the development of FreeCAD is fast! New features and bug fixes are added almost every single day. Since it is often a long time between stable releases, you might be interested in trying a more bleeding-edge version of FreeCAD. These development versions, or pre-releases, are uploaded from time to time to the [download page](https://github.com/FreeCAD/FreeCAD/releases) mentioned above, or, if you are using Ubuntu or Fedora, the FreeCAD community also maintains [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) and [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'daily builds\' which are regularly updated with the most recent changes.

If you are installing FreeCAD in a virtual machine, please be aware that the performance might be poor (in some cases unusable) due to the limits of [OpenGL](https://en.wikipedia.org/wiki/OpenGL) support on most virtual machines.

### Installing on Windows 

1.  Download an installer (.exe) package corresponding to your version of Windows (32bit or 64bit) from the [download page](https://github.com/FreeCAD/FreeCAD/releases). The FreeCAD installers should work on any windows version starting from Windows 7.
2.  Double-click the downloaded installer.
3.  Accept the terms of the LGPL license, this will be one of the few cases where you can really, safely click the \"accept\" button without reading the text. No hidden clauses: ![](images/Freecad-windows-install-01.jpg )
4.  You can leave the default path here, or change if you wish: ![](images/Freecad-windows-install-02.jpg )
5.  No need to set the PYTHONPATH variable, unless you plan to do some advanced python programming, in which case you probably already know what this is for: ![](images/Freecad-windows-install-03.jpg )
6.  During the installation, a couple of additional components, which are bundled inside the installer, will be installed too: ![](images/Freecad-windows-install-04.jpg )
7.  That\'s it, FreeCAD is installed. You will find it in your start menu. ![](images/Freecad-windows-install-05.jpg )

**Installing a development version**

Packaging FreeCAD and creating an installer takes some time and dedication, so usually development (also called pre-release) versions are provided as .zip (or .7z) archives. These don\'t need to be installed; just unpack them and launch FreeCAD by double-clicking the FreeCAD.exe file that you will find inside. This also allows you to keep both the stable and \"unstable\" versions together on the same computer.

### Installing on Linux 

On most modern Linux distributions (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, etc), FreeCAD can be installed with the click of a button, directly from the software management application provided by your distribution (the aspect of it can differ from the images below, each distribution uses its own tool).

1.  Open the software manager and search for \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Click the \"install\" button and that\'s it, FreeCAD gets installed. Don\'t forget to rate it afterwards!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Alternative ways**

One of the big joys of using Linux is the multitude of possibilities to tailor your software, so don\'t restrain yourself. On Ubuntu and derivatives, FreeCAD can also be installed from a [PPA](https://launchpad.net/~freecad-maintainers) maintained by the FreeCAD community (it contains both stable and development versions). On Fedora, recent development versions of FreeCAD can be installed from [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), and because this is open source software, you can also easily [compile FreeCAD yourself](Compiling.md).

### Installing on Mac OS 

Installing FreeCAD on Mac OSX is nowadays as easy as on other platforms. However, since there are fewer people in the community who own a Mac, the available packages sometimes lag a few versions behind the other platforms.

1.  Download a zipped package corresponding to your version from the [download page](https://github.com/FreeCAD/FreeCAD/releases).
2.  Open the Downloads folder, and expand the downloaded zip file: ![](images/Freecad-mac-01.jpg )
3.  Drag the FreeCAD application from inside the zip to the Applications folder: ![](images/Freecad-mac-02.jpg )
4.  That\'s it, FreeCAD is installed! ![](images/Freecad-mac-03.jpg )

5\. If the system prevents FreeCAD from launching due to restricted permissions for applications not coming from the App store, you will need to enable it in the system settings: ![](images/Freecad-mac-04.jpg )

### Uninstalling

Hopefully you won\'t want to uninstall FreeCAD, but it is good to know how. On Windows and Linux, uninstalling FreeCAD is very straightforward. On Windows, use the standard \"remove software\" option found in the control panel; on Linux, remove it with the same software manager you used to install it. On Mac OS, simply remove it from the Applications folder.

### Setting basic preferences 

Once FreeCAD is installed, you might want to open it and change some preferences. Preference settings in FreeCAD are located under menu **Edit → Preferences**. Listed below are some basic settings you may wish to change; you can browse through the preference pages to see if there is anything else you want to change.

1.  **Language**: (*General* category, *General* tab) FreeCAD will automatically pick the language of your operating system, but you might want to change that. FreeCAD is almost fully translated into five or six languages; others are currently only partially translated. You can easily [help translating FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Auto-load module**: (*General* category, *General* tab) Normally, FreeCAD will start by showing you the start page. You can skip this and begin a FreeCAD session directly in the workbench of your choice, listed under *Startup*, *Auto load module after startup*. [Workbenches](Workbenches.md) will be explained in detail in the [next chapter](Manual:The_FreeCAD_Interface.md).
3.  **Create new document at startup**: (*General* category, *Document* tab) Combined with the *Auto-load module* option above, if checked this starts FreeCAD ready for work. ![](images/Freecad-basic-options02.jpg )
4.  **Storage options**: (*General* category, *Document* tab) As with any complex application, FreeCAD likely contains bugs causing it to crash occasionally. Here you can configure options to help you to recover your work in case of a crash.
5.  **Authoring and license**: (*General* category, *Document* tab) Here you set the values to be used for new files you create. Consider making your files shareable right from the start, by using a friendlier, [copyleft](https://en.wikipedia.org/wiki/Copyleft) license like [Creative Commons](https://creativecommons.org/).
6.  **Redirect internal python messages**: (*General* category, *Output window* tab) These two options are always good to check, as they will cause messages from the internal python interpreter to show up in the [Report View](Manual:The_FreeCAD_Interface#Report_view.md) when there\'s a problem running a python script. ![](images/Freecad-basic-options03.jpg )
7.  **Units**: (*General* category, *Units* tab) Here you can set the default units system you wish to use. ![](images/Freecad-basic-options04.jpg )
8.  **Zoom at cursor**: (*Display* category, *3D* tab) If set, zoom operations will be focused at the mouse pointer. If unset, the center of the current view is the zoom focus.
9.  **Invert zoom**: (*Display* category, *3D* tab) Inverts the direction of zooming relative to mouse movement. ![](images/FreeCAD-v0-18-Preferences-Display.png )

### Installing additional content 

As the FreeCAD project and its community grows quickly, and also because it is easy to extend, external contributions and side-projects made by community members and other enthusiasts begin to appear everywhere on the internet. Most of these external projects are workbenches or macros, and can be easily installed right from within FreeCAD via the [Addons Manager](AddonManager.md) located under menu **Tools**. The addons manager will allow you to install many interesting components, for example:

1.  A [Parts library](https://github.com/FreeCAD/FreeCAD-library), which contains all kinds of useful models, or pieces of models, created by FreeCAD users that can be freely used in your projects. The library can be used and accessed right from inside your FreeCAD installation.
2.  [Additional workbenches](https://github.com/FreeCAD/FreeCAD-addons), that extend the functionality of FreeCAD for certain tasks, for example animate parts of your models, or areas, such as sheet metal folding or BIM. Further explanations of each workbench and what tools it contains is given on each addon page, that you can visit by clicking the corresponding link on the addon manager.
3.  A [collection of macros](https://github.com/FreeCAD/FreeCAD-macros), which are also available [on the FreeCAD wiki](Macros_recipes.md) along with documentation about how to use them.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

If you are using the Ubuntu operating system, some of the addons above are also available as packages on the [FreeCAD addons PPA](https://launchpad.net/freecad-extras)

**Read more**

-   [More download options](Download.md)
-   [FreeCAD PPA for Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD addons PPA for Ubuntu](https://launchpad.net/freecad-extras)
-   [Compile FreeCAD yourself](Compiling.md)
-   [FreeCAD translations](https://crowdin.com/project/freecad)
-   [FreeCAD github page](https://github.com/FreeCAD)
-   [The FreeCAD addons manager](Std_AddonMgr.md)




[Category:Poweruser Documentation](Category:Poweruser_Documentation.md) [Category:Tutorials](Category:Tutorials.md)

---
[documentation index](../README.md) > [Poweruser Documentation](Category:Poweruser Documentation.md) > Manual:Installing/en
