class Node:
  """
  Class implementing node of the LinkedList
  Attributes:
    -> data - data held by the node
    -> next - link to the next node
  """
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  """
  Class implementing Queue as a LinkedList
  """
  def __init__(self):
    """
    Initialises Queue object with pointers head and tail set to None
    """
    self.head = None
    self.tail = None

  def enqueue(self, data) -> None:
    """
    Adds node containing data passed to the rear of the queue
    """
    new = Node(data)
    if not self.tail is None:
      self.tail.next = new
    if self.head is None:
      self.head = new
    self.tail = new

  def dequeue(self) -> None:
    """
    Removes node from the rear of the queue
    """
    if not self.head is None:
      self.head = self.head.next
      if self.head is None:
        self.tail = None

  def status(self) -> None:
    """
    It prints all the elements of Queue.
    """
    elements = ""
    curr = self.head
    while not curr is None:
      elements += str(curr.data) + "=>"
      curr = curr.next
    print(elements + "None")


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
