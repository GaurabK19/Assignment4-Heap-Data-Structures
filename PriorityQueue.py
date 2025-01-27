import heapq

class Task:
    """
    A class to represent a Task with attributes like ID, priority, arrival time, and deadline.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        """
        Custom comparison based on priority for a min-heap.
        """
        return self.priority < other.priority

    def __repr__(self):
        """
        String representation of a Task.
        """
        return f"Task(ID={self.task_id}, Priority={self.priority}, Arrival={self.arrival_time}, Deadline={self.deadline})"


class PriorityQueue:
    """
    A Priority Queue implemented using a binary heap (min-heap) for efficient task management.
    """
    def __init__(self):
        """
        Initializes an empty heap to store tasks.
        """
        self.heap = []

    def insert(self, task):
        """
        Inserts a new task into the heap while maintaining the heap property.
        Time Complexity: O(log n).
        """
        heapq.heappush(self.heap, task)
        print(f"Inserted: {task}")

    def extract_min(self):
        """
        Removes and returns the task with the lowest priority.
        Time Complexity: O(log n).
        """
        if not self.is_empty():
            task = heapq.heappop(self.heap)
            print(f"Extracted: {task}")
            return task
        else:
            print("Priority Queue is empty.")
            return None

    def decrease_key(self, task_id, new_priority):
        """
        Updates the priority of a task and adjusts the heap.
        Time Complexity: O(n) for locating the task, O(log n) for adjusting the heap.
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    self.heap[i].priority = new_priority
                    heapq.heapify(self.heap)  # Reorganize the heap to maintain the heap property
                    print(f"Decreased priority of Task(ID={task_id}) to {new_priority}")
                else:
                    print(f"New priority {new_priority} is not less than current priority {task.priority}")
                return
        print(f"Task(ID={task_id}) not found.")

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        Time Complexity: O(1).
        """
        return len(self.heap) == 0


def scheduler_simulation(tasks):
    """
    Simulates scheduling using a Priority Queue.
    """
    pq = PriorityQueue()
    
    print("\n--- Scheduler Simulation ---")
    for task in tasks:
        pq.insert(task)  # Insert tasks into the priority queue

    print("\n--- Task Execution Order ---")
    while not pq.is_empty():
        # Extract tasks based on priority (lowest priority first in this min-heap)
        pq.extract_min()


# Example Task List
if __name__ == "__main__":
    tasks = [
        Task(task_id=1, priority=5, arrival_time=0, deadline=10),
        Task(task_id=2, priority=3, arrival_time=1, deadline=8),
        Task(task_id=3, priority=8, arrival_time=2, deadline=12),
        Task(task_id=4, priority=1, arrival_time=3, deadline=6)
    ]

    # Run the Scheduler Simulation
    scheduler_simulation(tasks)