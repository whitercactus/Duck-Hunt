import json

class Highscore:
    def get_score(self,s):
        self.s = s
        self.data1 = {}
        self.data1["old_score"] = self.s
        self.data1["high_score"] = 0
        with open("score.txt", 'w') as self.file:
            json.dump(self.data1, self.file)

    def get_high_score(self):
        with open('data.txt') as self.json_file:
            self.data2 = json.load(self.json_file)
            if self.s < self.data2:
                self.data1["high_score"] = self.data2
            else:
                self.data1["high_score"] = self.s


