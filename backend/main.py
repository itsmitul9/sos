#-x : Extract/get/unzip files from an archive.
#-f archive.tar.xz : Use this archive file or device archive for extracting files
import tarfile as tar
import shutil
import os
import stat

file_path = "../sosreport-localhost-2025-12-18-xhewwvh.tar.xz"
sosreport_name = os.path.basename(file_path).replace('.tar.xz', '')
extract_dir = './extracted'
expected_path = os.path.join(extract_dir, sosreport_name)

def extract_sosreport(file_path):
    if os.path.exists(extract_dir):
        print(f"'{sosreport_name}' already extracted at '{expected_path}', skipping...")
    else:
        print(f"sosreport name and expected path are not the same")
        try:
            file = tar.open(file_path, "r:xz")
            print("sosreport found and extracting files...")
            print(file.getmembers())
            file.extractall(extract_dir, filter='data')  # 'data' filter ignores permissions
            file.close()
            print("Extraction completed successfully")
        except tar.ReadError as e:
            print(f"Error reading file. Could not open '{file_path}' as a tar archive.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
