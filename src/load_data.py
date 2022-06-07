import argparse
from io import BytesIO
from zipfile import ZipFile

import pandas as pd
import requests
import yaml


def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def load_data(model_var):
    """
    load data set from SKLearn
    input: model_var
    output:pandas dataframe
    """
    config = read_params(config_path)
    url = config["data_source"]["url"]
    with ZipFile(BytesIO(requests.get(url).content), "r") as myzip:

        with myzip.open("column_3C.dat", "r") as f_in:
            df = pd.read_csv(f_in, sep=" ", header=None)
            df.columns = model_var
    return df


def load_raw_data(config_path):
    """
    load data from external location(data/external) to the raw folder(data/raw) with train and testing dataset
    input: config_path
    output: save train file in data/raw folder
    """
    config = read_params(config_path)
    raw_data_path = config["raw_data_config"]["raw_data_csv"]
    model_var = config["raw_data_config"]["model_var"]

    df = load_data(model_var)
    df.to_csv(raw_data_path, index=False)


if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--config", default="../params.yaml")
    parsed_args = args.parse_args()
    config_path = parsed_args.config
    load_raw_data(config_path)
