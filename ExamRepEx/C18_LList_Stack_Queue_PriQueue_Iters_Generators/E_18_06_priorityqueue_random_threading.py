import threading
import queue
import random

def main():
    threading.Thread(target=dequeuer, daemon=True).start()

    for i in range(50):
        message = f"Message {i+1}"  # Create a message
        priority = "High" if random.random() < 0.5 else "Low"  # Randomly assign priority
        q.put((priority, message))  # Add (priority, message) tuple to the queue
        print(f"Queued: {priority} priority - {message}")  # Print the message

    print('All messages queued\n', end='')
    q.join()  # Wait for all tasks to be processed
    print('All work completed')

def dequeuer():
    while True:
        priority, message = q.get()  # Read a message from the queue
        print(f"Dequeued: {priority} priority - {message}")  # Print the message
        q.task_done()  # Inform the queue that the task is done

q = queue.PriorityQueue()
main()
