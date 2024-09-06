import shutil
import os

# This class manage file operations such as copy and delete
class FileOperations:

    def __init__(self,
                 dirs_source, dirs_replica,
                 hashes_source, hashes_replica,
                 files_source, files_replica,
                 from_path, to_path):
        self.dirs_source = dirs_source
        self.dirs_replica = dirs_replica
        self.hashes_source = hashes_source
        self.hashes_replica = hashes_replica
        self.files_source = files_source
        self.files_replica = files_replica
        self.from_path = from_path
        self.to_path = to_path

    # Compare two files and/or two subfolders to verify if they are identical
    def compare_info(self):
        oper_exec = "No Issues..."
        for folder_name in self.dirs_source:
            if folder_name not in self.dirs_replica:
                from_path = os.path.join(self.from_path, folder_name) # Build the full subfolder path in the 'source' folder
                to_path = os.path.join(self.to_path, folder_name) # Build the full subfolder path in the 'replica' folder
                oper_exec = self._copy_info(from_path, to_path, "copy_folder")
        for i, file_hash in enumerate(self.hashes_source):
            if file_hash not in self.hashes_replica:
                file_name = self.files_source[i]
                from_file_path = os.path.join(self.from_path, file_name) # Build the full file path in the 'source' folder
                to_file_path = os.path.join(self.to_path, file_name) # Build the full file path in the 'replica' folder
                oper_exec = self._copy_info(from_file_path, to_file_path, "copy_file")
        for folder_name in self.dirs_replica:
            if folder_name not in self.dirs_source:
                in_path = os.path.join(self.to_path, folder_name) # Build the full subfolder path in the 'replica' folder
                oper_exec = self._delete_info(in_path, "delete_folder")
        for i, file_hash in enumerate(self.hashes_replica):
            if file_hash not in self.hashes_source:
                file_name = self.files_replica[i]
                to_file_path = os.path.join(self.to_path, file_name) # Build the full file path in the 'replica' folder
                oper_exec = self._delete_info(to_file_path, "delete_file")
        return oper_exec

    # Copy a file or subfolder from the 'source' folder to the 'replica' folder
    def _copy_info(self, from_path, to_path, flag_copy):
        if flag_copy == "copy_folder":
            shutil.copytree(from_path, to_path)
            return f"\nFolder copied from:\n\t {from_path} \nto:\n\t {to_path}"
        else:
            try:
                shutil.copy2(from_path, to_path)
                return f"\nFile copied from:\n\t {from_path} \nto:\n\t {to_path}"
            except Exception as e:
                return f"\nError copying the file:\n\t {e}"

    # Delete a file or subfolder in the 'replica' folder
    def _delete_info(self, path_info, flag_delete):
        if flag_delete == "delete_file":
            try:
                os.remove(path_info)
                return f"\nFile:\n\t {path_info} \ndeleted successfully!"
            except Exception as e:
                return f"\nError deleting file\n\t {path_info}:\n\t {e}"
        else:
            try:
                shutil.rmtree(path_info)
                return f"\nFolder:\n\t {path_info} \ndeleted successfully!"
            except Exception as e:
                return f"\nError deleting folder\n\t {path_info}:\n\t {e}"