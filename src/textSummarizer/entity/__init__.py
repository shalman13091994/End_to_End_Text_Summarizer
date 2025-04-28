

# data_ingestion:
#   root_dir: artifacts/data_ingestion
#   source_URL: https://drive.google.com/file/d/16RZa3YHx0rrTSp_JbNfF0Gz3TrqcGwkr/view?usp=drive_link
#   local_data_file: artifacts/data_ingestion/data.csv  # or whatever the file type is
#   unzip_dir: ""  # leave blank or remove if not unzipping


# data_validation:
#   root_dir: artificats/data_validation
#   STATUS_FILE: artificats/data_validation/status.txt
#   ALL_REQUIRED_FILES: ['train', 'test', 'validation']


# data_transformation:
#    root_dir: artificats/data_transformation
#    data_path: artificats/data_ingestion/samsun_dataset
#    tokenizer_name: google/pegasus-cnn_dailymail # to create abstract 


# model_trainer:
#    root_dir: artificats/model_trainer
#    data_path: artificats/data_transformation/samsun_dataset
#    model_ckpt: google/pegasus-cnn_dailymail 


# model_evaluation:
#   root_dir: artificats/model_evaluation
#   data_path: artificats/data_ingestion/samsun_dataset
#   model_path: artificats/model_trainer/pegasus-samsun-model
#   tokenizer_path: artificats/model_trainer/tokenizer
#   metric_file_name: artificats/model_evaluation/metrics.csv



from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
   
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    model_ckpt: str
    data_path: str
    root_dir: str  # <-- Keep as str (safe!)
# training arugument
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size:int
    weight_decay: float
    logging_steps:int
    evaluation_strategy: str
    eval_steps:int
    save_steps:int
    gradient_accumulation_steps:int

# TrainingArguments: # from the params.yaml
#   num_train_epochs: 1 # one full time to allow the entire dataset
#   warmup_steps: 500 #  gradually increase for the first 500 steps
#   per_device_train_batch_size: 1 #because of gpu
#   weight_decay: 0.01 #Helps prevent overfitting.
#   logging_steps: 10 #Logs loss/metrics every 10 steps 
#   evaluation_strategy: "steps" #Evaluate the model every eval_steps
#   eval_steps: 500 #Run evaluation (e.g. compute metrics) every 500 steps.
#   save_steps: 1e6 #1_000_000
#   gradient_accumulation_steps: 16  
