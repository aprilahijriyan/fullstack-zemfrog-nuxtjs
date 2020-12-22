import os

frontend_name = os.getenv("FRONTEND_DIR", "frontend")
backend_name = os.getenv("BACKEND_DIR", "backend")

# clone frontend nuxtjs + tailwindcss
os.system(
    f"git clone https://github.com/aprilahijriyan/zemfrog-nuxtjs-tailwindcss --depth 1 {frontend_name}")

# install dependencies
os.chdir(frontend_name)
os.system("yarn install")
os.chdir("..")
os.system("pipenv install zemfrog\>\=2.0.3")

# create backend
os.system(f"zemfrog create {backend_name}")

# install requirements.txt
os.chdir(backend_name)
os.system("pipenv install -r requirements.txt")
