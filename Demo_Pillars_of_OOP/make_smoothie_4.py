# Step 4: Polymorphism

class Blender:
    def __init__(self, capacity=5):
        self.capacity = capacity 
        self.__is_plugged_in = False # private; prevent accidental electrocution 
        self.__contents = [] # private; could over-fill if changed directly
    
    def __plug_in(self):
        print("Plugging in blender")
        self.__is_plugged_in = True
    
    def add_ingredient(self, ingredient):
        if len(self.__contents) >= self.capacity:
            print("Blender is already full!")
            return
        print(f"Adding {ingredient} to blender")
        self.__contents.append(ingredient)

    def blend_contents(self):
        print("Blending contents")
        self.__plug_in()
        self.__contents = Smoothie(self.__contents)
        print(f"Blended smoothie: {self.__contents}")


class Smoothie:
    def __init__(self, contents):
        self.contents = contents[:]
    
    def __repr__(self):
        return f"A smoothie made of {', '.join(map(str, self.contents))}"


class Fruit:
    def __init__(self, name):
        self.name = name
        self.is_prepared = False

    def wash(self):
        print(f"Washing {self.name}")
        self.is_prepared = True

    def prepare(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def __repr__(self):
        return self.name


class Banana(Fruit):
    def __init__(self):
        super().__init__("banana")
        self.is_peeled = False

    def peel(self):
        print("Peeling banana")
        self.is_peeled = True

    def prepare(self):
        self.peel()
        self.is_prepared = True


class Strawberry(Fruit):
    def __init__(self):
        super().__init__("strawberry")
        self.is_deleafed = False

    def deleaf(self):
        print("De-leafing strawberry")
        self.is_deleafed = True

    def prepare(self):
        self.wash()
        self.deleaf()
        self.is_prepared = True


if __name__ == "__main__":
    blender = Blender()

    ingredients = [Banana(), Strawberry(), Strawberry()]
    for ingredient in ingredients:
        ingredient.prepare()
        blender.add_ingredient(ingredient)

    blender.blend_contents()