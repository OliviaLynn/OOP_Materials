# Step 3: Inheritance 

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
        self.is_peeled = False
        self.is_washed = False
        self.is_deleafed = False

    def wash(self):
        print(f"Washing {self.name}")
        self.is_washed = True
    
    def __repr__(self):
        return self.name


class Banana(Fruit):
    def __init__(self, name="banana"):
        super().__init__(name)

    def peel(self):
        print("Peeling banana")
        self.is_peeled = True

    def prepare(self):
        self.peel()


class Strawberry(Fruit):
    def __init__(self, name="strawberry"):
        super().__init__(name)

    def deleaf(self):
        print("De-leafing strawberry")
        self.is_deleafed = True

    def prepare(self):
        super().wash()
        self.deleaf()


if __name__ == "__main__":
    blender = Blender()

    banana = Banana()
    banana.peel()
    blender.add_ingredient(banana)

    strawberry = Strawberry()
    strawberry.prepare()
    blender.add_ingredient(strawberry)

    blender.blend_contents()