# Let's start by making a smoothie using procedural coding (extra spaghetti-like)


if __name__ == "__main__":
    contents_of_blender = []
    is_blender_plugged_in = False
    blender_capacity = 5

    # add banana to blender, but only after it's peeled
    def peel_banana():
        print("Peeling banana")
    
    peel_banana()
    contents_of_blender.append("banana")

    # add strawberry to blender, but only after washing and de-leafing
    def wash_strawberry():
        print("Washing strawberry")

    def deleaf_strawberry():
        print("De-leafing strawberry")
    
    wash_strawberry()
    deleaf_strawberry()
    contents_of_blender.append("strawberry")

    # check if blender is full - we've already added 2 whole things!
    if len(contents_of_blender) >= blender_capacity:
        print("Blender is full!")

    # add another strawberry to blender
    wash_strawberry()
    deleaf_strawberry()
    contents_of_blender.append("strawberry")

    # let's say, we're ready to blend

    # check if blender is plugged in - if not, plug it in
    def plug_blender_in():
        print("Plugging blender in")
        return True
    
    if not is_blender_plugged_in:
        is_blender_plugged_in = plug_blender_in()

    # if blender is too full, we can't close the lid
    if len(contents_of_blender) > blender_capacity:
        print("Blender is too full to blend!")

    # blend contents
    print("Blending contents")
    print(f"Made smoothie out of: {contents_of_blender}")
    

