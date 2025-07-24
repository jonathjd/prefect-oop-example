from pathlib import Path
from unittest.mock import call

from conftest import mock_config
import pandas as pd
import pytest

from subflows import Extraction, Transform, Loading


@pytest.fixture(scope="module")
def extraction_mock_instance():
    return Extraction(mock_config)


@pytest.fixture(scope="module")
def transform_mock_instance():
    return Transform(mock_config, pd.DataFrame())


@pytest.fixture(scope="module")
def load_mock_instance():
    return Loading(mock_config, pd.DataFrame())


class TestExtraction:
    def test_extraction_method(self, extraction_mock_instance):
        # write some tests and assert some stuff
        pass


class TestTransformation:
    def test_transformation_method(self, transform_mock_instance):
        # write some tests and asser some stuff
        pass


class TestLoading:
    def test_loading_method(self, load_mock_instance):
        # write some tests and assert some stuff
        pass
