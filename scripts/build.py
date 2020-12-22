import os
from distutils.dir_util import remove_tree, copy_tree
from distutils.file_util import copy_file

static_dir = "../{0}/static".format(os.getenv("BACKEND_DIR"))
temp_dir = "../{0}/templates".format(os.getenv("BACKEND_DIR"))
dist_dir = "dist/"
static_files = ("_nuxt", "favicon.ico")
ignore_files = ("200.html", ".nojekyll", "README.md")


def build():
    os.chdir(os.getenv("FRONTEND_DIR", "frontend"))
    os.system("yarn install")
    os.system("yarn generate")
    copy_static_file()
    copy_templates()


def copy_static_file():
    clean_static_file()
    for f in static_files:
        dst = static_dir
        target = dist_dir + f
        if os.path.isfile(target):
            func = copy_file
        else:
            func = copy_tree
            dst += os.sep + f

        func(target, dst)


def copy_templates():
    clean_templates()
    for root, _, files in os.walk(dist_dir):
        for f in files:
            if f.endswith(".html") and f not in ignore_files:
                f = os.path.join(root, f)
                dirs = os.path.join(
                    temp_dir, os.path.dirname(f.replace(dist_dir, "")))
                try:
                    os.makedirs(dirs)
                except FileExistsError:
                    pass

                copy_file(f, dirs)


def clean_static_file():
    for f in static_files:
        target = static_dir + "/" + f
        if os.path.isfile(target):
            os.remove(target)
        elif os.path.isdir(target):
            remove_tree(target)


def clean_templates():
    templates = os.listdir(temp_dir)
    try:
        templates.remove("emails")
    except ValueError:
        pass

    for t in templates:
        t = os.path.join(temp_dir, t)
        if os.path.isdir(t):
            remove_tree(t)
        elif os.path.isfile(t):
            os.remove(t)


if __name__ == "__main__":
    build()
