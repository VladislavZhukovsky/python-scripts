class Animal():
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal!')

    def eat(self):
        print('I am eating')

    #example for abstract class
    def speak(self):
        raise NotImplementedError('abstract class')

class Dog(Animal):
    #class object attribute
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #attributes
        Animal.__init__(self)
        self.breed = breed
        self.name = name
        self.spots = spots
        print('Dog created!')

    def who_am_i(self):
        print('I am a dog!')

    #methods
    def speak(self):
        print('WOOF! My name is {0}!'.format(self.bark))


#mydog = Dog('Shih Tzu', 'Jasya', True)
#mydog.who_am_i()
#print(f'My {my_dog.name} is {my_dog.breed}!')
#print(Dog.species)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} - {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('object deleted from memory')

b = Book('Python rocks', 'Vlad', 777)
print(b)
print(len(b))
del b