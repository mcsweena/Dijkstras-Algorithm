
import itertools
from heapq import heapify, heappush, heappop

# A priority queue implementation based on standard library heapq
# module. Taken from https://docs.python.org/2/library/heapq.html, but
# encapsulated in a class. Also iterable, printable, and len-able.

# TODO some extra capabilities that would be nice: check for empty, peek.


class PriorityQueue:

    REMOVED = '<removed-task>' # placeholder for a removed task

    def __init__(self, tasks_prios=None):
        self.pq = []
        self.entry_finder = {} # mapping of tasks to entries
        self.counter = itertools.count() # unique sequence count -- tie-breaker when prios equal
        if tasks_prios:
            for task, prio in tasks_prios:
                self.add_task(task, prio) # would be nice to use heapify here instead

    def __iter__(self):
        return ((task, prio) for (prio, count, task) in self.pq if task is not self.REMOVED)

    def __len__(self):
        return len(list(self.__iter__()))

    def __str__(self):
        return str(list(self.__iter__()))

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority # NB a change from the original: we return prio as well
        raise KeyError('pop from an empty priority queue')

if __name__ == "__main__":
    pq = PriorityQueue((('a', 30), ('b', 31), ('d', 10)))
    pq.add_task('a', 17)
    pq.add_task('b', 19)
    pq.add_task('c', 5)
    pq.add_task('b', 3)
    print(pq.pop_task())
    pq.remove_task('c')
    print(pq.pop_task())
