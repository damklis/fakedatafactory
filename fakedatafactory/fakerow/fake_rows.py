import uuid
import random
from fakedatafactory.fakerow.fake_row_base import FakeRowBase


class CardTransactionFakeRow(FakeRowBase):

    def __init__(self):
        self.transaction_date = str(self.fake.date_between(
            start_date="-2y",
            end_date="today")
        )
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.iban = self.fake.iban()
        self.price = random.randint(1, 10000)
        self.credit_card_number = self.fake.credit_card_number()
        self.currency_code = "USD"
        self.state = self.fake.state()
        self.email = self.generate_email(
            self.first_name,
            self.last_name,
            self.fake.free_email_domain()
        )
        self.company = self.fake.company()


class BankAccountFakeRow(FakeRowBase):

    def __init__(self):
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.generate_email(
            self.first_name,
            self.last_name,
            self.fake.free_email_domain()
        )
        self.company = self.fake.company()
        self.state = self.fake.state_abbr(include_territories=True)
        self.zipcode = self.fake.zipcode_in_state(state_abbr=self.state)
        self.birth_date = str(self.fake.date_between(
            start_date="-55y",
            end_date="-18y")
        )


class CampaignEventFakeRow(FakeRowBase):

    events = [
        "open", "close", "subscribe", "unsubscribe",
    ]

    def __init__(self):
        self.user_id = self._generate_uuid()
        self.event_name = self._generate_event_name()
        self.net_explorer = self.fake.internet_explorer()
        self.ip = self.fake.ipv4_public()
        self.username = self.fake.user_name()
        self.url_source = self.fake.url()

    def _generate_event_name(self):
        """Gets random item form sequence of events
        """
        return random.choice(
            self.events
        )

    def _generate_uuid(self):
        """Provides unique user ID
        """
        return uuid.uuid4()


class CustomerFakeRow(FakeRowBase):

    user_id = 1

    def __init__(self):
        self.id = self.user_id
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.generate_email(
            self.first_name,
            self.last_name,
            self.fake.free_email_domain()
        )
        self.company = self.fake.company()
        self.birth_date = str(self.fake.date_between(
            start_date="-55y",
            end_date="-18y")
        )

        CustomerFakeRow.user_id += 1
