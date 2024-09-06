import argparse
import os

# This class handle the input and validation of command-line arguments
class CLIHandler:

    def __init__(self):
        # Create an arguments parser
        self.parser = argparse.ArgumentParser(
            description = "Folder Synchronizer: Synchronizes a source folder with a replica folder periodically")

    def parse_arguments(self):
        self.parser.add_argument(
            '--source', required = True, help = "Path to the source folder"
        )
        self.parser.add_argument(
            '--replica', required = True, help = "Path to the replica folder"
        )
        self.parser.add_argument(
            '--log', required = True, help = "Path to the log file"
        )
        self.parser.add_argument(
            '--interval', type = float, required = True, help = "Synchronization interval in seconds"
        )

        args = self.parser.parse_args() # Parsea the arguments

        # Verify if the folders exist
        if not os.path.isdir(args.source):
            self.parser.error(f"The source folder '{args.source}' doesn't exist or is not a folder")
        if not os.path.isdir(args.replica):
            self.parser.error(f"The source folder '{args.replica}' doesn't exist or is not a folder")
        
        # Verify if the log file is accessible
        log_dir = os.path.dirname(args.log)
        if log_dir and not os.path.exists(log_dir):
            self.parser.error(f"The folder for the log file '{log_dir}' doesn't exist")
        
        # If all is valid
        return args.source, args.replica, args.log, args.interval