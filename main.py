class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def sleep(self):
        print("zzzzz")

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
    def rrrr(self):
        print("Stay away!")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
    def woof_woof(self):
        print("woof woof!")

ruffus = Puppy("ruffus", "yoksher")
bibi = GuardDog("bibi", "terria")
ruffus.sleep()
bibi.sleep()

# 챌린지: 팀 클래스에서 플레이어 삭제 메소드 만들기. => remove 메소드 활용
# 챌린지: 팀 클래스에서 경험치의 총 합을 보여주는 메소드 만들기. 