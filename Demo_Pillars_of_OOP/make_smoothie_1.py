# Step 1: Encapsulation 

class Blender:
    def __init__(self, capacity=5):
        self.capacity = capacity 
        self.__is_plugged_in = False # private; prevent accidental electrocution 
        self.__contents = [] # private; could over-fill if changed directly

    def plug_in(self):
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
        self.__contents = Smoothie(self.__contents)
        print(f"Blended smoothie: {self.__contents}")


class Smoothie:
    def __init__(self, contents):
        self.contents = contents[:]
    
    def __repr__(self):
        return f"A smoothie made of {', '.join(map(str, self.contents))}"


class Banana:
    def __init__(self, name="banana"):
        self.name = name
        self.is_peeled = False

    def peel(self):
        print("Peeling banana")
        self.is_peeled = True

    def __repr__(self):
        return self.name


class Strawberry:
    def __init__(self, name="strawberry"):
        self.name = name
        self.is_washed = False
        self.is_deleafed = False

    def wash(self):
        print("Washing strawberry")
        self.is_washed = True

    def deleaf(self):
        print("De-leafing strawberry")
        self.is_deleafed = True

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    blender = Blender()
    banana = Banana()
    strawberry = Strawberry()

    banana.peel()
    blender.add_ingredient(banana)

    strawberry.wash()
    strawberry.deleaf()
    blender.add_ingredient(strawberry)

    # Can even add another strawberry

    blender.plug_in()
    blender.blend_contents()