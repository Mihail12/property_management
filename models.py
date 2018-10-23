
class House(models.Model):
    number = models.Charfield(max_lenght=255)
    street = models.Charfield(max_lenght=255)
    ...


class Person(models.Model):
    last_name = models.Charfield(max_lenght=255)
    first_name = models.Charfield(max_lenght=255)
    phone = models.Charfield(max_lenght=255)
    house = models.ForeignKey('House', on_delete=models.SET_NULL)
    ...


class Service1(models.Model):
    last_name = models.Charfield(max_lenght=255)
    first_name = models.Charfield(max_lenght=255)
    phone = models.Charfield(max_lenght=255)
    number = models.Charfield(max_lenght=255)
    street = models.Charfield(max_lenght=255)
    Person = models.ForeignKey('Person', on_delete=models.SET_NULL)


class Service2(models.Model):
    last_name = models.Charfield(max_lenght=255)
    first_name = models.Charfield(max_lenght=255)
    csv_file = models.FielField()
    phone = models.Charfield(max_lenght=255)
    number = models.Charfield(max_lenght=255)
    street = models.Charfield(max_lenght=255)
    Person = models.ForeignKey('Person', on_delete=models.SET_NULL)