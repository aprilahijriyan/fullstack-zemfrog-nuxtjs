import os
from distutils.dir_util import remove_tree

os.system("pipenv --rm")
dirs = (os.getenv("FRONTEND_DIR", "frontend"),
        os.getenv("BACKEND_DIR", "backend"))
for d in dirs:
    try:
        remove_tree(d)
    except FileNotFoundError:
        pass
