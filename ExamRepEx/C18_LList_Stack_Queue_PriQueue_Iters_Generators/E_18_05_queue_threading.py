import threading
import queue

def main():
    threading.Thread(target=dequeuer, daemon=True).start()

    for i in range(50):
        message = f"Message {i+1} "  # Create a message
        q.put(message)  # Add the message to the queue
        print(f"Queued: {message}")  # Print the message

    print('All messages queued\n', end='')
    q.join()  # Wait for all tasks to be processed
    print('All work completed')

def dequeuer():
    while True:
        message = q.get()  # Read a message from the queue
        print(f"Dequeued: {message}")  # Print the message
        q.task_done()  # Inform the queue that the task is done

q = queue.Queue()
main()
