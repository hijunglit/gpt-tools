class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"hello my name is {self.name}. and I play for {self.team}")

class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
    
    def show_players(self):
        for player in self.players:
            player.introduce()
    def remove_players(self, name):
        for target_player in self.players:
            if target_player.name == name:
                self.players.remove(target_player)
            else:
                print("This value does not exist")
    def total_xp(self):
        for player in self.players:
            xp = 0
            xp + player.xp
            print(f"The {self.team_name} total xp is {xp}")

team_red = Team("Team red")

team_red.add_player("Haein")
team_red.add_player("John doe")
team_red.add_player("chris")
team_red.add_player("harry")

team_red.show_players()

team_red.remove_players("Haein")
team_red.show_players()
team_red.total_xp()

# 챌린지: 팀 클래스에서 플레이어 삭제 메소드 만들기. => remove 메소드 활용
# 챌린지: 팀 클래스에서 경험치의 총 합을 보여주는 메소드 만들기. 