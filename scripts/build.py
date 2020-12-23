import os
from glob import glob
from distutils.file_util import copy_file

static_dir = "../{0}/static".format(os.getenv("BACKEND_DIR"))
temp_dir = "../{0}/templates".format(os.getenv("BACKEND_DIR"))
dist_dir = "dist/"
static_files = ("js", "ico", "png", "svg", "jpg", "jpeg")
ignore_files = ("200.html",)


def build():
    os.chdir(os.getenv("FRONTEND_DIR", "frontend"))
    os.system("yarn install")
    os.system("yarn generate")
    print("Copying templates and static files to the {0!r}... ".format(
        os.getenv("BACKEND_DIR")), end="")
    copy_static_file()
    copy_templates()
    print("done")


def copy_static_file():
    files = []
    for e in static_files:
        e = glob(dist_dir + "**/*." + e, recursive=True)
        files.extend(e)

    for filepath in files:
        dirs = os.path.dirname(filepath.replace(
            dist_dir, "", 1)).replace("static", "", 1).lstrip("/")
        dst = os.path.join(
            static_dir, dirs)
        try:
            os.makedirs(dst)
        except FileExistsError:
            pass

        copy_file(filepath, dst)


def copy_templates():
    for filepath in glob(dist_dir + "**/*.html", recursive=True):
        filename = os.path.basename(filepath)
        if filename not in ignore_files:
            dirs = os.path.join(
                temp_dir, os.path.dirname(filepath.replace(dist_dir, "", 1)))
            try:
                os.makedirs(dirs)
            except FileExistsError:
                pass

            copy_file(filepath, dirs)


if __name__ == "__main__":
    build()
