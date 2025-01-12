import pandas as pd
from faker import Faker

fake = Faker('en_SG')

data = []
for _ in range(100):
    data.append({
        'Id': fake.uuid4(),
        'Name': fake.name(),
        'Age': fake.random_int(min=18, max=80),
        'Gender': fake.random_element(elements=['Male', 'Female']),
        'Location': fake.city()
    })

df = pd.DataFrame(data)
df.to_csv('synthetic_data.csv', index=False)