import os
from distutils.dir_util import remove_tree

static_dir = "{0}/static".format(os.getenv("BACKEND_DIR"))
temp_dir = "{0}/templates".format(os.getenv("BACKEND_DIR"))


def clean():
    print("Clean templates and static files... ", end="")
    clean_static_file()
    clean_templates()
    print("done")


def clean_static_file():
    files = os.listdir(static_dir)
    for f in files:
        f = os.path.join(static_dir, f)
        if os.path.isdir(f):
            remove_tree(f)
        elif os.path.isfile(f):
            os.remove(f)


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
    clean()
