#reverse a singly linked list

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
	def has_next(self):
		return self.next != None

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = None

head = n0
tail = n9


def print_node(node):
	if node == None:
		return None
	elif node.next == None:
		return "[value=" + str(node.value) + ", next=" + "None]"
	else:
		return "[value=" + str(node.value) + ", next=" + str(node.next.value) + "]"

def print_list(head):
	while True:
		print(print_node(head))
		if head.next:
			head = head.next
		else:
			break

print_list(head)

#reverse a linked list
#must have 3 pointers: previous, current, next (in a consistent order, e.g. before reversing, otherise confusing.)
def reverse_nodes(head):
	previous_node = None
	current_node = head
	while True:
		if current_node.next:
			#temporially keep the next 
			next_node = current_node.next
            
            #this is key reverse action
			current_node.next = previous_node    
            
            #move to next node now
			previous_node = current_node
			current_node = next_node
		else:
			#move to the last one
			current_node.next = previous_node
			head = current_node
			#stop and return
			return head

   	   
print_list(reverse_nodes(head))



	