# Modules
MODULES = [
	"kde-extra-cmake-modules",
	"kde-solid",
	"vibe",
	"widget-styles",
	"icon-themes",
	"wallpapers",
	"loginmanager",
	"greenisland",
	"swordfish",
	"system-preferences",
	"archiver",
	"eyesight",
	"terminal",
	"widget-factory",
]

# Dependencies
DEPENDENCIES = {
	"kde-extra-cmake-modules": "",
	"kde-solid": "",
	"vibe": "kde-solid",
	"widget-styles": "vibe",
	"icon-themes": "",
	"wallpapers": "",
	"loginmanager": "",
	"greenisland": "vibe,wallpapers",
	"swordfish": "vibe",
	"system-preferences": "vibe",
	"archiver": "vibe",
	"eyesight": "vibe",
	"terminal": "vibe",
	"widget-factory": "widget-styles",
}
