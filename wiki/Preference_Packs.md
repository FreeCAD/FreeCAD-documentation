# Preference Packs
**This page documents a new feature in the 0.20 development branch. It is not available in previous releases. This documentation is a work-in-progress, please help us by improving it!
**

A **Preference Pack** is a distributable collection of user preferences that can be installed as an add-on and applied as a single set. Any user parameter that can be set in the user.cfg file can be included in a Preference Pack. Applying a preference pack sets all of the variables in the supplied CFG file without modifying any other user settings. For example, these packs can be used to create \"Themes\" by bundling together a custom stylesheet along with a set of user preferences that sets the various colors and styles of items in FreeCAD that aren\'t controlled by stylesheet.

### Applying an installed pack 

To apply a Preference Pack, click the \"Apply\" button next to its name on the General tab in the User Preferences dialog.

### Creating a new pack 

Packs can be created by hand, or jump-started by using the \"Save\" feature on the General tab in the User Preferences dialog.

### Distributing a pack 

Eventually packs will be distributed identically to Addon Workbenches, through the Addon Manager. This feature is still under development. To install a pack manually, use git to clone the package repository into your FreeCAD data directory (the directory where your user.cfg file is located), in a subdirectory called \"Preference Packs\".

---
[documentation index](../README.md) > Preference Packs
