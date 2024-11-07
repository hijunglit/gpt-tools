class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"Puppy named {self.name} and breed is {self.breed}"

ruffus = Puppy(
    name="wangja",
    breed="jindo"
)
bibi = Puppy(
    name="gongju",
    breed="jindo"
)

print(
    ruffus,
    bibi
)