import pandas as pd
from fakedatafactory import fake_rows


class FakeDataFactory:

    module = fake_rows

    def __init__(self):
        self.parser = _FakeRowParser(module=self.module)
        self.fake_rows = self._get_fake_rows()

    def _get_fake_rows(self):
        """Retrieves class definitions from
        module specified as a class attribute
        """
        return {
            self.parser.parse_name(row): self.parser.turn_to_object(row)
            for row
            in dir(self.module) if row.endswith("FakeRow")
        }

    def generate_fake_dataframe(self, dataframe_type, num_of_rows):
        """Generates pandas fake DataFrame with number of rows
        specified in `num_of_rows` argument
        """
        if dataframe_type not in self.fake_rows.keys():
            raise ValueError(f"Allowed types: {list(self.fake_rows.keys())}")
        else:
            return pd.DataFrame(
                [
                    self.fake_rows[dataframe_type].get_new_row().to_dict()
                    for _ in range(num_of_rows)
                ]
            )

    def list_available_dataframe_types(self):
        """Returns list of fake dataframe types you can use
        in `generate_fake_dataframe` method
        """
        return [
            row_name for row_name in self.fake_rows.keys()
        ]


class _FakeRowParser:

    def __init__(self, module):
        self.module = module

    @staticmethod
    def parse_name(row):
        """Formates provided row name
        """
        return row.replace("FakeRow", "").lower()

    def turn_to_object(self, object_name):
        """Converts string with object name
        to a subclass of FakeRowBase class
        """
        return getattr(self.module, object_name)