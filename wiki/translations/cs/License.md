# License/cs
## Licenses used in FreeCAD 

FreeCAD uses two different licenses, one for the application itself, and one for the documentation:

**[Lesser General Public License, version 2 or superior (LGPL2+)](wikipedia_LGPL.md)** For all of the FreeCAD source code found in the [official Git repository](https://github.com/FreeCAD/FreeCAD). The + means you can also, at your option, use FreeCAD under the terms of a later version of the license, such as LGPL3

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** For the [documentation](https://wiki.freecad.org) and the [website](https://www.freecad.org).

See FreeCAD\'s [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) for more details about the licenses used by the different open-source components used in FreeCAD

## Impact of the licenses 

Below is a friendlier explanation of what the LGPL license means for you:

#### All users 

Anybody can **download, use and redistribute FreeCAD free of charge**, without any restriction. Your copy of FreeCAD is truly yours, as are the files you produce with FreeCAD. You will not be forced to update FreeCAD after a certain time, nor change your usage of FreeCAD. Using FreeCAD doesn\'t bind you to any kind of contract or obligation. The FreeCAD source code is public and can be inspected, so it is possible to verify that it doesn\'t do things without your knowledge such as sending your private data somewhere.

#### Professional users 

FreeCAD can be **used freely for any kind of purpose**, being private, commercial or institutional. Any version of FreeCAD can be deployed and installed anywhere, any number of times. You can also modify and adapt FreeCAD for your own purposes without any restriction. However, you cannot make the FreeCAD developers liable for possible damage or business loss that could occur from using FreeCAD.

#### Open-source software developers 

You can use FreeCAD as a base to develop your own application, or simply extend it by creating new modules for it. If FreeCAD is embedded into your own application, you can choose either the GPL or the LGPL license, or any other license that is compatible with LGPL, to allow the use of your work in proprietary software or not. If you are developing a module to be used as an extension, and don\'t include any of the FreeCAD code in it, then you can choose any license you want. However, if you wish to see your module integrated into FreeCAD one day, it is a good idea to use the same LGPL license as FreeCAD itself, as FreeCAD will only accept code with LGPL, MIT or BSD licenses.

#### Closed-source software developers 

The LGPL license allows you to use FreeCAD as a component for your own application, and you are not forced to make your application open source. You will get support from the FreeCAD developers as long as it is not a \'one way street\'. The license states however two important conditions:

1\) You must clearly **inform your users that your application is using FreeCAD** and that FreeCAD is LGPL.

2\) The LGPL license also stipulate your users must be able to swap your modified FreeCAD component with the original FreeCAD equivalent. That is would be done by dynamically linking to the FreeCAD components, so users are allowed to change it. However, this is often hard to achieve by today\'s requirements. At FreeCAD, we understand that the important point here is to not restrict the freedom given to FreeCAD users by the LGPL license. So an equivalent to dynamic linking is to offer the choice to your users, by **making your users aware of the possibility to use FreeCAD for free**. This can be done in a number of ways.

If any of the two conditions above are unacceptable to you or cannot be implemented, then you must make your FreeCAD component LGPL too and release the source code with all the modifications you made to it.

There is a special case called **derivatives**, which is when you publish basically a \"rebranded\" version of FreeCAD. Derivatives which are not open-source are prohibited by the LGPL license. The FreeCAD community is active and efficient in finding rebranded versions, reporting them to the platforms where they were found and exposing them until they are taken down.

#### Files

The models and other files produced with FreeCAD are not subject to any license stated above, nor bound to any kind of restriction or ownership. Your files are truly yours. You can set the owner of the file and specify your own license terms for the files you produce inside FreeCAD, via menu File → Project Information.

## Logo

The FreeCAD logo is a [trademark owned by the FPA (FreeCAD project association)](https://fpa.freecad.org/documents/Trademark.pdf). This means the [FPA](https://fpa.freecad.org) is the sole body authorized to say who has the right to use the FreeCAD logo or not. The logo files, which are part of the FreeCAD source code or available elsewhere, for example on this wiki, are still all under the same licenses as the rest of FreeCAD (LGPL for the source code and Creative Commons for this wiki). You are still free to use the FreeCAD logo anywhere, on the same terms as the rest of FreeCAD, which means, basically, that you must use it to reference FreeCAD, and not use it, for example, for your own product, or any other way that is not referencing FreeCAD.

## Statement of the main developer 

I know that the discussion on the *\"right\"* license for open source occupied a significant portion of internet bandwidth and so is here the reason why, in my opinion, FreeCAD should have this one.

I chose the [LGPL](http://en.wikipedia.org/wiki/LGPL) for the project and I know the pro and cons about the LGPL and will give you some reasons for that decision.

FreeCAD is a mixture of a library and an application, so the GPL would be a little bit strong for that. It would prevent writing commercial modules for FreeCAD because it would prevent linking with the FreeCAD base libs. You may ask why commercial modules at all? Therefore Linux is good example. Would Linux be so successful when the GNU C Library would be GPL and therefore prevent linking against non-GPL applications? And although I love the freedom of Linux, I also want to be able to use the very good NVIDIA 3D graphic driver. I understand and accept the reason NVIDIA does not wish to give away driver code. We all work for companies and need payment or at least food. So for me, a coexistence of open source and closed source software is not a bad thing, when it obeys the rules of the LGPL. I would like to see someone writing a Catia import/export processor for FreeCAD and distribute it for free or for some money. I don\'t like to force him to give away more than he wants to. That wouldn\'t be good neither for him nor for FreeCAD.

Nevertheless this decision is made only for the core system of FreeCAD. Every writer of an application module may make his own decision.


{{Quote|Jürgen Riegel|15 October 2006}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > License/cs
