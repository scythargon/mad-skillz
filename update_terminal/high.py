class Highlight:
  def __init__(self,color): self.color=color
  def __enter__(self):
    print(self.color, end="")
  def __exit__(self,type,value,traceback):
    print(Fore.RESET, end="")

with Highlight(Fore.GREEN):
  print("this is highlighted")
print("this is not")
