class Puppy:

    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"{self.breed} puppy named {self.name}"


wangja = Puppy("Wangja", "Jindo")
gongju = Puppy("Gongju", "jindo")

print(wangja, gongju)
