from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

#Example 1
"""
with onto:
    class Person(Thing):
        pass

   
    class has_name(DataProperty):
        range = [str]

me = Person()
me.has_name.append("Ali")

# Ontolojiyi kaydet
onto.save(file="onto.owl")
"""
#Example 2
"""
with onto:
    # Person sınıfı
    class Person(Thing):
        pass
    class Car(Thing):
        pass
    
    class has_name(DataProperty):
        range = [str]
    
    class has_age(DataProperty):
        range = [int]

    class has_model(DataProperty):
        range = [str]
    
    class has_year(DataProperty):
        range = [int]
    
    # Nesne özelliği (Object Property)
    class owns(ObjectProperty):
        domain = [Person]
        range = [Car]

person1 = Person()
person1.has_name = ["Metin"]
person1.has_age = [23]

car1 = Car()
car1.has_model = ["Toyota"]
car1.has_year = [2020]

# Person arabaya sahip 
person1.owns.append(car1)

onto.save(file="onto_with_car.owl")
"""
#Example 3
"""
with onto:
    class Animal(Thing):
        pass
    
    class Mammal(Animal):
        pass
    
    class Bird(Animal):
        pass
    
    class has_fur(DataProperty):
        range = [bool]
    
    class can_fly(DataProperty):
        range = [bool]
    
    class has_species_name(DataProperty):
        range = [str]
    
    
    class feeds_on(ObjectProperty):
        domain = [Animal]
        range = [Animal]


tiger = Mammal()
tiger.has_species_name = ["Panthera tigris"]
tiger.has_fur = [True]

eagle = Bird()
eagle.has_species_name = ["Aquila chrysaetos"]
eagle.can_fly = [True]

# Kaplanın kartalla beslenenir.
tiger.feeds_on.append(eagle)

onto.save(file="animal_ontology.owl")
"""
#Example 4
"""
with onto:
    class Animal(Thing):
        pass

    class Cat(Animal):
        pass

    class Bird(Animal):
        pass

    class Habitat(Thing):
        pass

    class Forest(Habitat):
        pass

    class Lake(Habitat):
        pass

    class feeds_on(ObjectProperty):
        domain = [Animal]
        range = [Animal]

    class lives_in(ObjectProperty):
        domain = [Animal]
        range = [Habitat]


cat = Cat("whiskers")
bird = Bird("sparrow")
forest = Forest("amazon_forest")
lake = Lake("great_lake")


cat.feeds_on.append(bird)    # Kedi kuşu yer
cat.lives_in.append(forest)   # Kedi ormanda yaşar
bird.lives_in.append(lake)    # Kuş gölde yaşar

# Ontolojiyi kaydet
onto.save(file="animal_habitats.owl")
"""