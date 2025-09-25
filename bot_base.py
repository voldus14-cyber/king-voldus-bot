class BaseBot:
  def __init__(self, token):
      self.token = token

  def start(self):
      print("Bot started with token:", self.token)
