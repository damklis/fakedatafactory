import pytest
from fakedatafactory.fakerow.fake_row_base import FakeRowBase


@pytest.fixture()
def example_fake_row():

    class ExampleFakeRow(FakeRowBase):

        def __init__(self):
            self.first_name = "example_first_name"
            self.last_name = "example_last_name"
            self.id = 100
            self.domain = "gmail.com"

    yield ExampleFakeRow


def test_object_initialization_of_fake_row_base():

    with pytest.raises(TypeError):
        FakeRowBase()


def test_generate_email(example_fake_row):

    email = "example_first_nameexample_last_name@gmail.com"
    example_fake_row = example_fake_row()

    result = example_fake_row.generate_email(
        example_fake_row.first_name,
        example_fake_row.last_name,
        example_fake_row.domain
    )

    assert result == email


def test_to_dict(example_fake_row):

    dict_attr = {
        "first_name": "example_first_name",
        "last_name": "example_last_name",
        "id": 100,
        "domain": "gmail.com"
    }

    example_fake_row = example_fake_row()
    result = example_fake_row.to_dict()

    assert result == dict_attr


def test_get_new_row(example_fake_row):

    example_fake_row = example_fake_row()
    fake_row = example_fake_row.get_new_row()

    assert isinstance(fake_row, FakeRowBase)
