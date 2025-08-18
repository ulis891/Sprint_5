import faker

def get_new_user():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password