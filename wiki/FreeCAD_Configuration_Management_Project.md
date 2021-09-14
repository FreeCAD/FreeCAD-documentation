# FreeCAD Configuration Management Project

This page is describes a potential 2018 Google Summer of Code project regarding configuration management for the FreeCAD CAE application.

## Outline

FreeCAD relies on a large number of software packages and is available on most major platforms (Linux, OSX, Windows), each Distro/OS have several distribution methods available (package managers, Libpacks, pip, Conda, AppImages, installers, etc). This makes for a particularly challenging configuration management environment.

## Details

1.  A clear picture of FreeCAD\'s dependencies as well as their dependencies is required. This is envisioned as a visual depiction (perhaps a directed graph) and an analysis of conflicting versions.
2.  A plan for the partitioning of the FreeCAD functionality into manageable chunks along with smaller sets of dependencies is also required. It\'s desirable to identify interdependencies and not re-install them.

## Expected Outcome 

1.  A concrete/documented view of FreeCD\'s dependencies (and perhaps the trusted addons)
2.  A reduction in manual effort when releasing new versions of FreeCAD

## Future Possibilities 

This work will provide experience in the packaging and distribution of multi-platform, cross-dependency software.

## Project Properties 

### Skills

-   Familiarity with
    -   package managers (Launchpad, pbuilder, gitbuilder, conda, NSIS-installer)
    -   build managers (cMake, make, VS, MSBuild, Nmake)
    -   graph theory (Dependency graph)

### Difficulty

Medium

### Additional Information 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)
