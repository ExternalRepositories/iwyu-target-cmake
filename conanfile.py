from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.6"


class IWYUCTargetCmakeConan(ConanFile):
    name = "iwyu-target-cmake"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    requires = ("cmake-include-guard/master@smspillaz/cmake-include-guard",
                "tooling-find-pkg-util/master@smspillaz/tooling-find-pkg-util",
                "tooling-cmake-util/master@smspillaz/tooling-cmake-util")
    url = "http://github.com/polysquare/iwyu-target-cmake"
    license = "MIT"
    options = {
        "dev": [True, False]
    }
    default_options = "dev=False"

    def requirements(self):
        if self.options.dev:
            self.requires("cmake-module-common/master@smspillaz/cmake-module-common")

    def source(self):
        zip_name = "iwyu-target-cmake.zip"
        download("https://github.com/polysquare/"
                 "iwyu-target-cmake/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="Find*.cmake",
                  dst="",
                  src="iwyu-target-cmake-" + VERSION,
                  keep_path=True)
        self.copy(pattern="*.cmake",
                  dst="cmake/iwyu-target-cmake",
                  src="iwyu-target-cmake-" + VERSION,
                  keep_path=True)
