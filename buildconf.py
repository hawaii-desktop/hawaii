# File whose presence means the submodule was already configured
COOKIENAME_CONFIGURE = ".hawaii-ci-configure-cookie"

# File whose presence means the submodule was already built
COOKIENAME_BUILD = ".hawaii-ci-build-cookie"

# Modules
MODULES = [
    "kde-extra-cmake-modules",
    "kde-solid",
    "polkit-qt-1",
    "vibe",
    "widget-styles",
    "icon-themes",
    "wallpapers",
    "fluid",
    "fluid-themes",
    "login-manager",
    "greenisland",
    "swordfish",
    "system-preferences",
    "archiver",
    "eyesight",
    "terminal",
    "widget-factory",
]

# Ignore modules
IGNORED_MODULES = [
]

# Dependencies
DEPENDENCIES = {
    "kde-extra-cmake-modules": "",
    "kde-solid": "kde-extra-cmake-modules",
    "polkit-qt-1": "kde-extra-cmake-modules",
    "vibe": "kde-solid",
    "fluid": "vibe,fluid-themes",
    "fluid-themes": "vibe",
    "widget-styles": "vibe,fluid",
    "icon-themes": "vibe",
    "wallpapers": "vibe",
    "login-manager": "fluid",
    "greenisland": "vibe,fluid,wallpapers,polkit-qt-1",
    "swordfish": "vibe",
    "system-preferences": "vibe",
    "archiver": "vibe",
    "eyesight": "vibe",
    "terminal": "vibe",
    "widget-factory": "widget-styles",
}

# Protocols for GitHub repositories
PROTOCOLS = ["http", "ssh"]

# Base URLs for GitHub repositories
BASE_URLS = {
    "http": "https://github.com/",
    "ssh": "git@github.com:",
}

# vim:set ts=4 sw=4 et:
