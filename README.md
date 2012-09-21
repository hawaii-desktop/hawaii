Hawaii Continuous Integration
=============================

Master module for the Hawaii desktop environment.
It contains git submodules for the whole desktop environment, something
very useful for continuous integration that also make building from git
easier.

Dependencies
------------

In order to build the submodules you need CMake 2.8.9 or better and Qt 5.
Wayland and QtWayland are needed only for the greenisland submodule.

If you are building under Maui there's no problem because it satisfies
Hawaii requirements, but you might not be so lucky with other distributions.

### Building dependencies from sources

Build CMake from sources, look at here:

http://www.cmake.org/cmake/resources/software.html

Read the following pages to build Qt 5 and Wayland from sources:

http://wayland.freedesktop.org/building.html
http://qt-project.org/wiki/Building_Qt_5_from_Git

Some guidance can be found here:

http://www.maui-project.org/en/get-involved/coding/

### Install dependencies on Ubuntu

CMake 2.8.9 was backported from Quantal to Precise by Pier Luigi Fiorini.
Add the PPA and install the package by typing:

```sh
sudo add-apt-repository ppa:plfiorini/cmake
sudo apt-get update
sudo apt-get install cmake
```

There's also a PPA for Qt 5 maintained by Canonical:

https://launchpad.net/~canonical-qt5-edgers/+archive/qt5-daily

How to use it
-------------

### Fetch submodules

The first time you use this module you have to fetch all the submodules.
Type the following command in order to fetch the submodules:

```sh
./init-repository fetch
```

To see more information about fetch arguments:

```sh
./init-repository fetch -h
```

### Update submodules

Every time you want to update the submodules do:

```sh
./init-repository forward
```

To see more information about forward arguments:

```sh
./init-repository forward -h
```

The following command builds the software with default parameters, this means
that the build type is RelWithDebInfo (release mode with debugging information)
and everything gets installed under the Maui file hierarchy.

```sh
./compile
```

Remember to properly configure your environment:

```sh
[ "$(uname -m)" = "x86_64" ] && libext=64 || libext=
export PATH=/system/bin:$PATH
export QT_PLUGIN_PATH=/system/plugins:$QT_PLUGIN_PATH
export QML_IMPORT_PATH=/system/imports:$QML_IMPORT_PATH
export XDG_DATA_DIRS=$XDG_DATA_DIRS:/system/data/
export LD_LIBRARY_PATH=/system/lib${libext}:$LD_LIBRARY_PATH
```

What if you are not building under Maui?
----------------------------------------

Maui has a different file hierarchy. If you are building for another
Linux distribution you have to pass appropriate arguments:

```sh
./compile --prefix=/usr/local --appsdir=share/applications --progsdir=bin \
  --serversdir=bin --sysconfdir=/etc --localstatedir=/var --includedir=include \
  --pkgconfig=lib/pkgconfig --cmakedir=lib/cmake --datarootdir=share
```

Or you can just run compile like this:

```sh
./compile --prefix=/usr/local --linux-fhs
```

Just like with a build for Maui, you need to properly set your environment:

```sh
[ "$(uname -m)" = "x86_64" ] && libext=64 || libext=
export PATH=/usr/local/bin:$PATH
export QT_PLUGIN_PATH=/usr/local/plugins:$QT_PLUGIN_PATH
export QML_IMPORT_PATH=/usr/local/imports:$QML_IMPORT_PATH
export XDG_DATA_DIRS=$XDG_DATA_DIRS:/usr/local/share/
export LD_LIBRARY_PATH=/usr/local/lib${libext}:$LD_LIBRARY_PATH
```

Blacklist and whitelist
-----------------------

The compile script also lets you specify a blacklist and a whitelist
of submodules.

In the following example we assume that compile ignores icon-themes by
default. We put kde-solid and vibe into the blacklist and override the
default blacklist by placing icon-themes on the whitelist:

```sh
./compile --blacklist kde-solid vibe --whitelist icon-themes
```

If both --blacklist and --whitelist are passed, the latter takes
precedence.

*Beware*, if you blacklist a submodule that is a dependency of another
submodule the build might break.  There's no control, you have to be clever.

Notes
-----

Building a module is a four step process:

 1. Run cmake to configure the submodule.
 2. Run make to compile the software.
 3. Run sudo make install to install the software.
 4. Create a cookie that indicates the submodule was already built.

If you see a password prompt it's probably the installation step that
is asking the password.  This might happen multiple times during the
build process if the build time is greater than sudo timeout.
