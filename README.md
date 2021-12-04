# Snowfakery Education

Fake data to support educational institutions

## Installation

Install with pip

`pip install faker-edu`

## Faker Use

```python
from faker import Faker
import faker_edu

fake = Faker()
fake.add_provider(faker_edu.Provider)

for _ in range(10):
    print(fake.institution_name())
```

## Snowfakery Use

For now you will need to clone the repository and then follow the example in the [sample recipe](snowfakery_edu_example.recipe.yml).
