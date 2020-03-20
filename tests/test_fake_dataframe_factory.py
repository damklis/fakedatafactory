import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from fakedatafactory.fakerow import fake_rows
from fakedatafactory.fakerow.fake_row_base import FakeRowBase
from fakedatafactory.fake_data_factory import (
    FakeDataFactory, _FakeRowParser
)


@pytest.fixture()
def example_fake_row():

    class ExampleFakeRow(FakeRowBase):

        def __init__(self):
            self.first_name = "example_first_name"
            self.last_name = "example_last_name"
            self.id = 100
            self.domain = "gmail.com"

    yield ExampleFakeRow


@pytest.fixture()
def example_pandas_df():
    row = {
        "first_name": "example_first_name",
        "last_name": "example_last_name",
        "id": 100,
        "domain": "gmail.com"
    }

    yield pd.DataFrame(
        [row for _ in range(10)]
    )


@pytest.fixture()
def module():
    yield fake_rows


def test_fakerowparser_parse_name(module):

    row = "ExampleFakeRow"
    expected = "example"
    parser = _FakeRowParser(module)

    result = parser.parse_name(row)

    assert result == expected


def test_fakerowparser_turn_to_object(example_fake_row, module):

    object_name = "ExampleFakeRow"
    parser = _FakeRowParser(module)
    fake_rows.ExampleFakeRow = example_fake_row()

    result = parser.turn_to_object(object_name)

    assert isinstance(result, FakeRowBase)
    assert isinstance(result, example_fake_row)


def test_list_available_dataframe_types():

    fake_df_factory = FakeDataFactory()
    result = fake_df_factory.list_available_dataframe_types()

    assert len(result) > 0
    assert isinstance(result, list)


def test_generate_fake_dataframe(example_fake_row, example_pandas_df):

    fake_rows.ExampleFakeRow = example_fake_row()
    fake_df_factory = FakeDataFactory()
    result = fake_df_factory.generate_fake_dataframe(
        "example",
        10
    )

    assert_frame_equal(result, example_pandas_df)


def test_generate_fake_dataframe_with_wrong_type():

    with pytest.raises(ValueError):
        fake_df_factory = FakeDataFactory()
        fake_df_factory.generate_fake_dataframe(
            "wrong_type",
            10
        )
