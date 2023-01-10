from faker import Faker


# fake = Faker()
fake = Faker(['pt_br', 'pt-br', 'pt_BR', 'pt-BR'])

name = fake.name()
address = fake.address()
text = fake.text()

print('name =', name)
print('address =', address)
print('text =', text)
