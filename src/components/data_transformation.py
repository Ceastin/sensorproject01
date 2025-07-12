import sys
import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler,FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    artifact_dir=os.path.join(artifact_folder)
    transformed_train_file_path=os.path.join(artifact_dir,'train.npy')
    transformed_test_file_path=os.path.join(artifact_dir,'test.npy')
    transformed_object_file_path=os.path.join(artifact_dir,'preprocessor.pkl')
    