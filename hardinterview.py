from heapq import merge

class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            # last item in linked list
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

def merge_k_linked_lists(linked_lists):
    all_lists = []
    for links in linked_lists:
        one_llist = []
        while links:
            print(links.val)
            one_llist.append(links.val)
            links = links.next
        all_lists.append(one_llist)
    print(all_lists)
    new_list = []
    print(len(all_lists))
    while len(all_lists) > 1:
        new_list.append(min(all_lists, key=lambda x: x[0]))
        all_lists.remove(min(all_lists, key=lambda x: x[0]))
    new_list.append(*all_lists)
    print(new_list)
    


def merge_k_linked_lists_one(linked_list):
    values = []
    # creating list of all elements in the given linked lists
    for link in linked_list:
        while link:
            values.append(link.val)
            link = link.next
    # sorting those elements
    sorted_val = sorted(values)
    '''
    I know the next section is supposed to start creating
    a linked list by iterating through the sorted values
    but am unclear how.
    '''
    # I know this is initialisng the final linked list
    result = Link(0)
    # what is happening here? I think this is the key point I'm struggling with
    # we're only updating pointer in the for loop, but that's changing result
    # How?
    pointer = result
    for val in sorted_val:
        print(f'result is {result}, pointer is {pointer}')
        pointer.next = Link(val)
        pointer = pointer.next
    # I understand the .next removes the first "0" that we added when creating the linked list
    return result.next



if __name__ == "__main__":
    print(merge_k_linked_lists([
        Link(7, Link(9)),
        Link(3, Link(4)),
        Link(4, Link(6))
    ]))