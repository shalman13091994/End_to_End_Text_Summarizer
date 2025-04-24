import os
from pathlib import Path

project_name ='cnn_classifier'

list_of_files =[
 "github/workflows/.gitkeep",
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/init.py",
  f"src/{project_name}/utils/__init__.py",
   f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    print('filepath-->', filepath)
    filedir,filename=os.path.split(filepath)

    print('filedir,filename-->', filedir,filename)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")
