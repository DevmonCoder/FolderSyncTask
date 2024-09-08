FolderSyncTask

Overview

FolderSyncTask is a Python-based project designed to synchronize the contents of two directories, source and replica, by comparing files and subdirectories. The program ensures that any new files, modified files, or deleted files in the source folder are accurately reflected in the replica folder, maintaining consistency between both directories.

The program performs the following operations:

Copies new files and subdirectories from the source folder to the replica folder.
Updates modified files by replacing them in the replica folder.
Deletes files and subdirectories from the replica folder that no longer exist in the source.
Logs all the actions performed, including file creation, modification, and deletion, to both the console and a log file.

Key Features

File Synchronization: Ensures the replica folder mirrors the source folder's structure and content.
Hash Comparison: Files are compared using MD5 hashes to detect modifications.
Logging: Detailed logs of all synchronization actions (creations, deletions, and updates) are maintained in a log file.
Customizable Sync Intervals: The user can define the interval at which the synchronization occurs.
Command Line Interface (CLI): The program is fully configurable through the command line, allowing users to specify the source folder, replica folder, log file, and sync interval.

Requirements

Python 3.12 or higher
VS Code 1.93.0 or higher (recommended)

Installation

1- Clone this repository to your local machine:
git clone https://github.com/DevmonCoder/FolderSyncTask.git

2- Navigate to the project directory:
cd FolderSyncTask

3- Install any dependencies if necessary. Although no external libraries are required in this version, you can create a virtual environment for better management:
python -m venv venv
source venv/bin/activate  # For Windows, use: venv\Scripts\activate

Usage

Run the program from the command line by specifying the source folder, replica folder, log file path, and synchronization interval.
python main.py --source <source_folder_path> --replica <replica_folder_path> --log <log_file_path> --interval <sync_interval_in_seconds>

For example:
python main.py --source C:/Users/Example/source --replica C:/Users/Example/replica --log C:/Users/Example/sync_log.txt --interval 60

This command will synchronize the source and replica folders every 60 seconds, logging all actions to sync_log.txt.

Command Line Arguments
--source: The path to the source directory containing the files to synchronize.
--replica: The path to the replica directory where files will be copied.
--log: The path to the log file where synchronization events will be recorded.
--interval: The time interval (in seconds) between synchronization operations.
Error Handling
The program uses try-except blocks to manage errors during file operations. If an error occurs (e.g., a file cannot be deleted or copied), the program logs the error and continues without stopping the entire synchronization process.

Future Enhancements
Multithreading: Add multithreading to improve performance for large directories with many files.
Real-Time Monitoring: Implement real-time synchronization using a file system watcher instead of periodic intervals.
Compression: Optionally compress files before copying to save storage and improve speed.
Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

License
This project is licensed under the MIT License. See the LICENSE file for details.
