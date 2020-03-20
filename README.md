# Fake Data Factory

My helper module that allows you to create fake Pandas DataFrames.

For example, you can create a fake dataset with bank accounts data,
marketing campaign data, customer and transaction data, etc.

Recommended library to generate fake data:
* [Faker](https://github.com/joke2k/faker) is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

# Usage
1.List all currently available DataFrames.
```python
from fakedatafactory import FakeDataFactory

fake_data_factory = FakeDataFactory()

fake_data_factory.list_available_dataframe_types()
```

Returns:
```python
["bankaccount", "campaignevent", "customer", "cardtransactions"]
```

2.Create fake pandas DataFrame.
```python
from fakedatafactory import FakeDataFactory

fake_data_factory = FakeDataFactory()

fake_data_factory.generate_fake_dataframe(
    dataframe_type="customer",
    num_of_rows=5
)
```

Returns:

| l | date | first_name | surname | state | email | company |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | 2019-07-25| Megan | Fischer | Connecticut | meganfischer@hotmail.com | Miller-Castro |
| 1 | 2019-06-23| James | Moore | Hawaii | jamesmoore@hotmail.com | Holloway and Sons |
| 2 | 2019-12-27| Kathleen | Collins | Utah | kathleencollins@gmail.com | Lane, Bennett and Gray |
| 3 | 2019-02-23| Nathan | Jordan | Delaware | nathanjordan@hotmail.com | Griffin-Bradley |
| 4 | 2018-08-15| Michael | Jones | Indiana | michaeljones@yahoo.com | Gonzalez, Johnson and Wu |



# Contribution

You can easily create a new DataFrame type adding subclass of FakeRowBase to file `fake_rows.py`.
Requirement:
* Your class name needs to end with `FakeRow` phrase. (example: `FootballGameFakeRow`)
