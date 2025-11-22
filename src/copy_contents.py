import os
import shutil


def copy_contents(source_dir, target_dir):
    if os.path.exists(target_dir):
        print("Removing existing directory:\n\t", target_dir)
        shutil.rmtree(target_dir)

    print("Creating directory:\n\t", target_dir)
    os.makedirs(target_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        if os.path.isfile(source_path):
            print("Copying file:\n\t", source_path, "\n\t", target_path)
            shutil.copy(source_path, target_path)
        else:
            copy_contents(source_path, target_path)