import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')

Project_name = "Delhi_House_Price_Prediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/logs/__init__.py",
    f"src/{Project_name}/logs/logger.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/utils/utils.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/components/data_ingetion.py",
    f"src/{Project_name}/components/data_transformation.py",
    f"src/{Project_name}/components/model_training.py",
    f"src/{Project_name}/pipelines/__init__.py",
    f"src/{Project_name}/pipelines/train_pipeline.py",
    f"src/{Project_name}/pipelines/prediction_pipeline.py",
    f"src/{Project_name}/exceptions.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file {filepath}")

    else:
        logging.info(f"file {filename} already exists.")
