from dataclasses import dataclass
from pathlib import Path

from loguru import logger
import pandas as pd
from prefect import flow, task
import yaml


@dataclass
class CompletedSubflow:
    continue_run: bool
    df: pd.DataFrame | None = None
    message: str | None = None


def parse_config(config: str | Path):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


class Extraction:
    def __init__(self, config: Path | str):
        self.config = parse_config(config)

    @task
    def do_some_fetching(self):
        # fetch some stuff
        pass

    @flow(name="Extraction")
    def run(self) -> CompletedSubflow:
        # Main logic

        return CompletedSubflow(continue_run=True, df=pd.DataFrame())


class Transform(Extraction):
    def __init__(self, config: Path | str, df: pd.DataFrame):
        self.config = parse_config(config)

        # save df
        self.df = df

    @task
    def do_some_transformations(self):
        # transform some stuff
        pass

    @flow(name="Transformation")
    def run(self) -> CompletedSubflow:
        # Main logic

        return CompletedSubflow(continue_run=True, df=pd.DataFrame())


class Loading(Extraction):
    def __init__(self, config: Path | str, df: pd.DataFrame):
        self.config = parse_config(config)

        # save df
        self.df = df

    @task
    def load_some_stuff(self) -> None:
        # do some loading
        pass

    @flow(name="Loading")
    def run(self) -> CompletedSubflow:
        # Main logic

        return CompletedSubflow(continue_run=True)
