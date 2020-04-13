from task import Task
class List:
  def __init__(self, user):
    self.user = user
    self.tasks = []
  
  def createTask(self, description, dueDate):
    t = Task(description, dueDate)
    self.tasks.append(t)
  
  def printList(self):
    for t, num in zip(self.tasks, range(1,len(self.tasks)+1)):
      print('{}) {}'.format(num,t.description, t.dueDate))
  
  def deleteTask(self,num):
    print(self.tasks.pop(num-1), 'Deleted')