class Band:
  def init(self, name):
  self.name = name
  self.musicians = []
  def add(self, musician):
    self.musicians.append(musician)

  def play(self):
    playing = ""
    for musician in self.musicians:
        if musician.guitars:
            playing += f"{musician.name} is playing: {musician.guitars[0]}\n"
        else:
            playing += f"{musician.name} needs an instrument!\n"
    return playing

  def __str__(self):
    return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"