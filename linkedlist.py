class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def __str__(self):
		out = ""
		cur = self.head

		while cur:
			out += str(cur.item) + '|'
			cur = cur.next
		return out



	def insert(self, item):
		newNode = Node(item)
		cur = self.head

		if self.head is None:
			self.head = newNode  #1
		else:
			while cur.next is not None:
				cur = cur.next
			cur.next = newNode


if __name__ == '__main__':
	ll = LinkedList()

	for i in range(1,4):
		ll.insert(i)

	print(ll)




