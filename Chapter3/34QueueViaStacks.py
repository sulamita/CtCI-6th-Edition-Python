import unittest
from Queue import LifoQueue
from Queue import Queue
from random import randint

class MyQueue():

	def __init__(self):
		self.stackNewest = LifoQueue()
		self.stackOldest = LifoQueue()
		
	def shiftStacks(self):
		if self.stackOldest.empty():
			while not self.stackNewest.empty():
				self.stackOldest.put(self.stackNewest.get())

	def put(self, item):
		self.stackNewest.put(item)


	def get(self):
		self.shiftStacks()
		return self.stackOldest.get()

class Test(unittest.TestCase):
	'''Tests MyQueue against a real Queue'''
	test_q = Queue()
	my_q = MyQueue()

	def test_myQ(self):
		for i in range(100):
			choice = randint(0,10)
			if choice <= 5: # enqueue
				element = randint(1,10)
				self.my_q.put(element)
				self.test_q.put(element)
				print("Enqueued {}", element)
			elif not self.test_q.empty(): 
				top1 = self.test_q.get()
				top2 = self.my_q.get()
				self.assertEqual(top1, top2)


if __name__ == "__main__":
    unittest.main()
