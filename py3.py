import time
from concurrent.futures import ThreadPoolExecutor

def create_file(index):
    filename = f"file_{index}.txt"
    with open(filename, "w") as file:
        file.write(f"Content of file {index}")
    time.sleep(1)
    print(f"File {filename} created.")

start_time = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:  
    executor.map(create_file, range(100))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Multithreaded execution time: {elapsed_time} seconds.")
