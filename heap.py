from dataclasses import dataclass, field
from typing import Optional, List
import time

@dataclass(order=True)
class Job:
    """Represents an individual unit of work with priority and metadata."""
    priority: int
    arrival_order: int = field(compare=True)
    name: str = field(compare=False)

    def __str__(self) -> str:
        return f"Job(Name: '{self.name}', Priority: {self.priority})"


class MaxHeapScheduler:
    """A high-performance priority queue scheduler powered by a Max Heap."""
    
    def __init__(self) -> None:
        self._heap: List[Job] = []
        self._sequence_counter: int = 0

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def schedule_job(self, name: str, priority: int) -> Job:
        """Inserts a new job into the scheduler queue."""
        self._sequence_counter += 1
        # Negate arrival order so older jobs win ties under max-heap logic
        job = Job(priority=priority, arrival_order=-self._sequence_counter, name=name)
        self._heap.append(job)
        self._percolate_up(len(self._heap) - 1)
        return job

    def peek_next_job(self) -> Optional[Job]:
        """Returns the highest priority job without removing it."""
        return self._heap[0] if not self.is_empty() else None

    def process_next_job(self) -> Optional[Job]:
        """Removes and returns the highest priority job from the queue."""
        if self.is_empty():
            return None
        
        highest_job = self._heap[0]
        last_job = self._heap.pop()
        
        if not self.is_empty():
            self._heap[0] = last_job
            self._percolate_down(0)
            
        return highest_job

    def get_sorted_queue(self) -> List[Job]:
        """Returns all jobs ordered by priority (descending) without disrupting state."""
        if self.is_empty():
            return []
        
        backup_heap = list(self._heap)
        sorted_jobs = []
        
        while not self.is_empty():
            sorted_jobs.append(self.process_next_job())
            
        self._heap = backup_heap
        return sorted_jobs

    def _percolate_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self._heap[parent] < self._heap[index]:
            self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _percolate_down(self, index: int) -> None:
        length = len(self._heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < length and self._heap[left] > self._heap[largest]:
                largest = left

            if right < length and self._heap[right] > self._heap[largest]:
                largest = right

            if largest != index:
                self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
                index = largest
            else:
                break


def run_cli() -> None:
    scheduler = MaxHeapScheduler()
    
    print("=" * 50)
    print("      ENTERPRISE PRIORITY JOB SCHEDULER")
    print("=" * 50)
    print("Commands:")
    print("  submit <name> <priority>  - Queue a new job")
    print("  next                      - View highest priority job")
    print("  process                   - Execute/remove highest priority job")
    print("  list                      - Display all jobs in queue order")
    print("  exit                      - Terminate application\n")

    while True:
        try:
            command_line = input("scheduler> ").strip()
            if not command_line:
                continue
                
            parts = command_line.split()
            action = parts[0].lower()

            if action in ('exit', 'quit'):
                print("Shutting down scheduler. Goodbye.")
                break

            elif action == 'next':
                job = scheduler.peek_next_job()
                print(f"[Result] Next Job -> {job}" if job else "[Result] Queue is empty.")

            elif action == 'process':
                job = scheduler.process_next_job()
                print(f"[Result] Processed -> {job}" if job else "[Result] No jobs to process.")

            elif action == 'list':
                jobs = scheduler.get_sorted_queue()
                if not jobs:
                    print("[Result] Queue is empty.")
                else:
                    print(f"[Result] Active Queue ({len(jobs)} jobs, ordered by priority):")
                    for idx, j in enumerate(jobs, 1):
                        print(f"  {idx}. [Priority: {j.priority}] {j.name}")

            elif action == 'submit':
                if len(parts) < 3:
                    print("[Error] Usage: submit <name> <priority>")
                    continue
                name = parts[1]
                priority = int(parts[2])
                job = scheduler.schedule_job(name, priority)
                print(f"[Success] Scheduled -> {job}")

            else:
                print(f"[Error] Unknown command '{action}'. Type 'exit' to quit.")

        except (ValueError, IndexError):
            print("[Error] Invalid argument format. Ensure priority is an integer.")
        except KeyboardInterrupt:
            print("\nShutting down scheduler. Goodbye.")
            break


if __name__ == "__main__":
    run_cli()
