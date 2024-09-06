import os
from FolderSynchronizer import FolderSynchronizer
from CLIHandle import CLIHandler

if __name__ == "__main__":

    cli_handler = CLIHandler()

    source_path, replica_path, log_path, interval = cli_handler.parse_arguments()

    sync = FolderSynchronizer(source_path, replica_path, log_path, interval)

    sync.run()