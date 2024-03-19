import random


class TestData:
    BASE_URL = 'https://initial.bareegaree.com/'
    USER_NAME = 'Raju02',
    PASSWORD = 'rA123!@#',





    def mobile_number(self):
        MOBILE_NUMBER = "017"

        # Generate random digits for the remaining 8 characters
        for _ in range(8):
            MOBILE_NUMBER += str(random.randint(0, 9))

        return MOBILE_NUMBER


