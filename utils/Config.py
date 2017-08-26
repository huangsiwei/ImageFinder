import os


class Configuration:
    MAC_CONFIG = dict(
        ass_file_dir="/Users/huangsiwei/PycharmProjects/ImageFinder/assfile/",
        raw_image_dir="/Users/huangsiwei/PycharmProjects/ImageFinder/raw_img/",
        image_dir="/Users/huangsiwei/PycharmProjects/ImageFinder/image/",
        mov_dir="/Users/huangsiwei/PycharmProjects/ImageFinder/mov/"
    )

    WINDOWS_CONFIG = {

    }

    def current_config(self):
        if os.name == "posix":
            return self.MAC_CONFIG
        elif os.name == "nt":
            return self.WINDOWS_CONFIG

    def ass_file_dir(self):
        if os.name == "posix":
            return self.MAC_CONFIG["ass_file_dir"]
        elif os.name == "nt":
            return self.WINDOWS_CONFIG