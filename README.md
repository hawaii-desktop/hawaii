Hawaii Continuous Integration
=============================

Master module for the Hawaii desktop environment.
It contains git submodules for the whole desktop environment, something
very useful for continuous integration that also make building from git
easier.

How to use it
-------------

The first time you use this module you have to fetch all the submodules.
Type the following command in order to fetch the submodules:

```sh
./init_repository fetch
```

Every time you want to update the submodules do:

```sh
./init_repository forward
```

The following command builds the software with default parameters, this means
that the build type is RelWithDebInfo (release mode with debugging information)
and everything gets installed under the Maui file hierarchy.

```sh
./compile
```

Remember to properly configure your environment:

```sh
export PATH=/system/bin:$PATH
export QT_PLUGIN_PATH=/system/plugins:$QT_PLUGIN_PATH
export QML_IMPORT_PATH=/system/imports:$QML_IMPORT_PATH
export XDG_DATA_DIRS=$XDG_DATA_DIRS:/system/data/
export LD_LIBRARY_PATH=/system/lib:$LD_LIBRARY_PATH
```

However you might want to build with a different configuration, for example if
you are going to build under another Linux distribution you should type:

```sh
./compile --prefix=/usr/local --datadir=share
```

Just like with a build for Maui, you need to properly set your environment:

```sh
export PATH=/usr/local/bin:$PATH
export QT_PLUGIN_PATH=/usr/local/plugins:$QT_PLUGIN_PATH
export QML_IMPORT_PATH=/usr/local/imports:$QML_IMPORT_PATH
export XDG_DATA_DIRS=$XDG_DATA_DIRS:/usr/local/data/
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```
