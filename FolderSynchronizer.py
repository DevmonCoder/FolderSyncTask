import os
import hashlib
from FileOperations import FileOperations
from datetime import datetime
import time

# This Class manages the synchronization between 'source' and 'replica' folders
class FolderSynchronizer:

    def __init__(self, source_path, replica_path, log_path, interval):
        self.source_path = source_path
        self.replica_path = replica_path
        self.log_path = log_path
        self.interval = interval
        self.log_path = log_path

    # Traverse the folder and generate MD5 hashes and folders name
    def _traverse_folder(self, folder_path):
        list_dirs = []
        list_hashes = []
        list_files = []
        for root, dirs, files in os.walk(folder_path):
            for dir_name in dirs:
                # Store relative paths to keep folder structure
                rel_dir_path = os.path.relpath(os.path.join(root, dir_name), folder_path)
                list_dirs.append(rel_dir_path)  # Add relative folder path
            for file_name in files:
                file_path = os.path.join(root, file_name) # Create the full path to the file
                list_files.append(os.path.relpath(file_path, folder_path))  # Store relative file path
                with open(file_path, 'rb') as file: # Open each file individually
                    data = file.read() # Read the file data
                    md5 = hashlib.md5(data).hexdigest() # Generate the MD5 hash
                    list_hashes.append(md5) # CREATE THE LIST WITH THE FILES HASH
        return list_dirs, list_hashes, list_files

    # Perform the synchronization between the folders
    def synchronize(self):

        list_dirs_source, list_hashes_source, list_files_source = self._traverse_folder(self.source_path) # Get lists for 'source' folder
        list_dirs_replica, list_hashes_replica, list_files_replica = self._traverse_folder(self.replica_path) # Get lists for 'replica' folder

        self.file_operations = FileOperations(
                                        list_dirs_source,
                                        list_dirs_replica,
                                        list_hashes_source,
                                        list_hashes_replica,
                                        list_files_source,
                                        list_files_replica,
                                        self.source_path,
                                        self.replica_path)

        res_oper = self.file_operations.compare_info()

        self.log_operation(res_oper)

    # Log the operations performed (creation, copy, deletion) in the log file and the console
    def log_operation(self, operation):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get the current timestamp
        log_message = f"{timestamp} - OPERATION:\n\n\t {operation}" # Format the log message
        print(log_message.strip()) # Write the log to the console
        with open(self.log_path, 'a') as log_file:
            log_file.write(log_message) # Write the log to the file
    
    # Excute the periodic synchronization
    def run(self):
        print(f"Starting synchronization every {self.interval} seconds...")
        while True:
            try:
                self.synchronize()
                time.sleep(self.interval)
            except KeyboardInterrupt:
                print("\nSynchronization stopped by user...")
                return