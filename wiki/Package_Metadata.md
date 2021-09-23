# Package Metadata

**This page documents a feature currently under development.
**

## Introduction


{{TOCright}}

External add-ons (workbenches, macros, and preference packs) may be distributed with a metadata file describing the contents of the package. If the file \"package.xml\" is present it is read by FreeCAD and its contents used in various parts of the user interface. It is currently optional for workbenches and macros, and required for preference packs. This page documents the format of that metadata file. The format (and the contents of this Wiki page) are based on [REP 149](https://ros.org/reps/rep-0149.html).

## Overall file format 

This document currently describes file format version 1.

The metadata file must be a valid, well-formed XML 1.0 document. It must be called \"package.xml\", and must exist in the base directory of the software package. All understood XML tags are in lowercase, but unrecognized tags are **not** an error. Most tags are optional, and some only apply to certain types of package contents (for example, only Workbenches currently provide a \"classname\" element). Unneeded or unrecognized elements are ignored.

## Content elements 

### 

The only top-level element allowed is . Immediately subordinate to that are several required or optional elements, defined here. No other tags are permitted directly under the  element.

    <package format="1">

The  tag is the unique top-level tag in a package.xml file. All other tags are nested under it.

#### Attributes

-   format=\"NUMBER\": Specifying the package.xml format being used. For this interface, you must specify format=\"1\".

#### Required child tags 

The top-level  element must contain at least the following tags:

-   [](#.3Cname.3E.md)
-   [](#.3Cversion.3E.md)
-   [](#.3Cdescription.3E.md)
-   [](#.3Cmaintainer.3E.md) (multiple, but at least one)
-   [](#.3Clicense.3E.md) (multiple, but at least one)
-   [](#.3Ccontent.3E.md) (container element for package content items)
    -   [](#.3Cicon.3E.md)
    -   [](#.3Cclassname.3E.md)
    -   [](#.3Cfile.3E.md) (multiple)
    -   [](#.3Ctype.3E.md)

#### Optional child tags 

-   [](#.3Curl.3E.md) (multiple)
-   [](#.3Cauthor.3E.md) (multiple)
-   [](#.3Cdepend.3E.md) (multiple)
-   [](#.3Cconflict.3E.md) (multiple)
-   [](#.3Creplace.3E.md) (multiple)
-   [](#.3Ctag.3E.md) (multiple)
-   [](#.3Cfreecadmin.3E.md)
-   [](#.3Cfreecadmax.3E.md)

###  

REQUIRED

The name of this package. Must only contain characters that are valid for filenames (disallowed characters are /\\?%\*:\|\"\<\> ).

###  

REQUIRED

A version number that follows the [semantic versioning 2.0 standard](https://semver.org) (e.g. 1.0.2-beta).

###  

REQUIRED

A concise (up to several sentences) text-only description of this package. No markup is supported.

###  

AT LEAST ONE REQUIRED (multiple allowed)

The name of the person maintaining the package. All packages require a maintainer. For orphaned packages see below.

#### Attributes 

-   email=\"name\@domain.tld\" (required): Email address of the maintainer.

An orphaned package is one with no current maintainer. Orphaned packages should use the following maintainer information:

    <maintainer email="no-one@freecadweb.org">No current maintainer</maintainer>

###  

AT LEAST ONE REQUIRED (multiple allowed)

Name of license for this package, e.g. BSD, GPL, LGPL. In order to assist machine readability, only include the license name in this tag. For multiple licenses multiple separate tags must be used. A package will have multiple licenses if different source files have different licenses. Every license occurring in the source files should have a corresponding  tag. For any explanatory text about licensing caveats, please use the  tag.

Most common open-source licenses are described on the [OSI website](https://opensource.org/licenses/alphabetical).

Commonly-used license strings:

-   Apache-2.0
-   BSD
-   Boost Software License
-   GPLv2
-   GPLv3
-   LGPLv2.1
-   LGPLv3
-   MIT
-   Mozilla Public License Version 1.1

#### Attributes 

-   file=\"FILE\" (optional): A path relative to the package.xml file containing the full license text. Many licenses require including the license text when redistributing the software. E.g. the Apache License, Version 2.0 states in paragraph 4.1: \"You must give any other recipients of the Work or Derivative Works a copy of this License\"

###  

REQUIRED

The  tag describes the actual contents of the package. It has no attributes, and contains any number of children. Those children can have arbitrary tag names, only some of which may be recognized by FreeCAD. During this preliminary development phase of the metadata standard, only \"\" children are recognized. In the future, support for \"\" and \"\" is planned. Each child is then defined recursively by this standard, containing any or all of the elements allowed for the root  node. For example:

    <content>
      <preferencepack>
        <name>Unicorn Sparkles Theme</name>
        <version>1.0.0</version>
        <url type="readme">https://github.com/chennes/FreeCAD-themes/Unicorn%20Sparkles%20Theme/Readme.md</url>
        <icon>sparkles.svg</icon>
        <type>appearance</type>
      </preferencepack>
    </content>

The existence of  items implies a set of subfolders, one for each content item, named exactly as the given name of the item. So for the example above, the package\'s folder structure is:

    Package Directory/
      package.xml
      Unicorn Sparkles Theme/
        Unicorn Sparkles Theme.cfg
        sparkles.svg
        (the theme's other files)

In addition to the other elements of , content items can optionally provide information in , , , and  tags (technically these can be provided to the root  tag as well, but they are generally unused there).

####  

REQUIRED for Workbenches

The path to an icon file. If it is an icon for the top-level package this path is relative to the package.xml file itself. If the icon is an element of a  item, then the path is relative to the content\'s folder, which must be named the same as the  element for the content item.

####  

REQUIRED for Workbenches

For workbenches, the name of the Python main entry class.

####  

Optional

Provided for convenience to other tools, any number of other files may be listed here. Their use depends on the type of content.

####  

REQUIRED for Preference Packs, not supported for other content elements

Either \"appearance\", \"behavior\", or \"combination\" describing to end users what type of changes they can expect this preference pack to change.

###  

Multiple allowed

A Uniform Resource Locator for the package\'s website, bug tracker, source repository, readme file, or documentation.

It is a good idea to include  tags pointing users to these resources. The website is commonly a wiki page on wiki.freecadweeb.org where users can find and update information about the package.

#### Attributes 

-   type=\"TYPE\" (required): The type should be one of the following identifiers \-- \"website\", \"bugtracker\", \"repository\", \"readme\", or \"documentation\".

###  

Multiple allowed

The name of a person who is an author of the package, as acknowledgement of their work and for questions.

#### Attributes 

-   email=\"name\@domain.tld\" (optional): Email address of author.

###  

Multiple allowed

Declares another FreeCAD package that is required in order to use this package. That package itself must provide a package.xml file in order for the dependency system to identify it.

#### Attributes 

All dependencies and relationships may restrict their applicability to particular versions. For each comparison operator an attribute can be used. Two of these attributes can be used together to describe a version range.

-   version\_lt=\"VERSION\" (optional): The dependency to the package is restricted to versions less than the stated version number.
-   version\_lte=\"VERSION\" (optional): The dependency to the package is restricted to versions less or equal than the stated version number.
-   version\_eq=\"VERSION\" (optional): The dependency to the package is restricted to a version equal than the stated version number.
-   version\_gte=\"VERSION\" (optional): The dependency to the package is restricted to versions greater or equal than the stated version number.
-   version\_gt=\"VERSION\" (optional): The dependency to the package is restricted to versions greater than the stated version number.
-   condition=\"CONDITION\_EXPRESSION\": Every dependency can be conditional on a condition expression. If the condition expression evaluates to \"true\" the dependency is used and considered as if it doesn\'t have a condition attribute. If the condition expression evaluates to \"false\" the dependency is ignored and considered as if it doesn\'t exist. The expression must be a valid FreeCAD Expression (i.e. Python syntax), and may refer to the variables \"\$BuildVersionMajor\", \"\$BuildVersionMinor\", and \"\$BuildRevision\" representing the version of FreeCAD currently running.

###  

Multiple allowed

Declares a package name with which this package conflicts. This package and the conflicting package should not be installed at the same time.

#### Attributes 

See .

###  

Multiple allowed

Declares a package name that this package is intended to replace.

#### Attributes 

See .

###  

A simple text tag used for categorization when using a package manager. Multiple  elements may be specified.

###  

The minimum version of FreeCAD required to use this package/element, as a semantic version 2.0 string in the format MAJOR.MINOR.BUILD

###  

The maximum version of FreeCAD required to use package/element, as a semantic version 2.0 string in the format MAJOR.MINOR.BUILD

## Example

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1">
      <name>Built-In Preference Packs</name>
      <description>Preference Packs included with the FreeCAD distribution</description>
      <version>1.0.0</version>
      <maintainer email="email@freecadweb.org">No Maintainer</maintainer>
      <license file="../../LICENSE">LGPL2</license>
      <url type="repository">https://github.com/FreeCAD/FreeCAD</url>

      <content>
        <preferencepack>
          <name>FreeCAD Classic Colors</name>
          <description>FreeCAD default colors for core app and included Mods.</description>
          <version>1.0.0</version>
          <type>appearance</type>
        </preferencepack>
      </content>

    </package>
