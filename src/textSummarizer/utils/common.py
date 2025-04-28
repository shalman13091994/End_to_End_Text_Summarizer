
from pathlib import Path
from box import ConfigBox  # to access dictionary keys like attributes
import yaml
from ensure import ensure_annotations
import os
from textSummarizer.logging import logger

@ensure_annotations # datatype of the declared should not be changed 
def read_yaml(path_to_yaml: Path) -> ConfigBox: 

    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
      
    with open(path_to_yaml) as f:
       config =  yaml.safe_load(f)
       
    # config = read_yaml(Path(r'D:\Datascience\DL\DL Projects\End_to_End_Text_Summarizer\config\config.yaml'))

    return ConfigBox(config)


#create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    
