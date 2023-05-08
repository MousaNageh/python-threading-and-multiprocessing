import multiprocessing

def child_process(conn):
    # Receive a message from the parent process
    message = conn.recv()
    print(f"Child process received message: {message}")
    # Send a response to the parent process
    response = "Hello from the child process!"
    conn.send(response)
    # Close the connection
    conn.close()

# Create a pipe for communication between the parent and child processes
parent_conn, child_conn = multiprocessing.Pipe()
# Spawn a child process to run the child_process function
p = multiprocessing.Process(target=child_process, args=(child_conn,))
p.start()
# Send a message to the child process
message = "Hello from the parent process!"
parent_conn.send(message)
# Receive a response from the child process
response = parent_conn.recv()
print(f"Parent process received response: {response}")