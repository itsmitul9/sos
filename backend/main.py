"""
SOSReport Extractor and Reader.

This module extracts and reads sosreport tar.xz archives.
"""
import tarfile as tar
import os

FILE_PATH = "../sosreport-localhost-2025-12-18-xhewwvh.tar.xz"
SOSREPORT_NAME = os.path.basename(FILE_PATH).replace('.tar.xz', '')
EXTRACT_DIR = './extracted'
EXPECTED_PATH = os.path.join(EXTRACT_DIR, SOSREPORT_NAME)


def extract_sosreport(tar_path):
    """Extract sosreport from tar.xz archive."""
    if os.path.exists(EXTRACT_DIR):
        print(f"'{SOSREPORT_NAME}' already extracted at '{EXPECTED_PATH}', skipping...")
    else:
        print("Extracting sosreport...")
        try:
            with tar.open(tar_path, "r:xz") as archive:
                print("sosreport found and extracting files...")
                print(archive.getmembers())
                archive.extractall(EXTRACT_DIR, filter='data')
                print("Extraction completed successfully")
        except tar.ReadError:
            print(f"Error reading file. Could not open '{tar_path}' as a tar archive.")
        except FileNotFoundError:
            print(f"Error: The file '{tar_path}' was not found.")
        except PermissionError as err:
            print(f"Permission error: {err}")


def get_sosreport_info(sos_path):
    """Enter the sosreport directory and list its contents."""
    if not os.path.exists(sos_path):
        print(f"Path does not exist: {sos_path}")
        return

    # Save current directory
    current_dir = os.getcwd()

    # Enter the sosreport directory
    os.chdir(sos_path)
    print(f"Entered directory: {os.getcwd()}\n")

    # List contents of current directory
    print("--- Contents ---")
    for item in os.listdir('.'):
        if os.path.isdir(item):
            print(f"  [DIR]  {item}/")
        else:
            print(f"  [FILE] {item}")

    # Go back to original directory
    os.chdir(current_dir)

def get_cpu_info(cpuinfo_path):
    """Read CPU info from sosreport's proc/cpuinfo file."""
    if not os.path.exists(cpuinfo_path):
        print(f"File not found: {cpuinfo_path}")
        return
    with open(cpuinfo_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'model name' in line:
                print(line.strip())

get_sosreport_info(EXPECTED_PATH)

# Build the path to cpuinfo file
cpuinfo_file = os.path.join(EXPECTED_PATH, 'proc', 'cpuinfo')
get_cpu_info(cpuinfo_file)
