import os
import subprocess

def push_mini_maps():
    # Read output folder from file written by extraction script
    try:
        with open("last_output_folder.txt", "r") as f:
            output_folder = f.read().strip()
    except FileNotFoundError:
        print("Error: last_output_folder.txt not found. Run extraction script first.")
        return

    if not os.path.exists(output_folder):
        print(f"Error: Output folder '{output_folder}' does not exist.")
        return

    print(f"Pushing contents of folder: {output_folder}")

    os.chdir(output_folder)

    # Run git commands
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update mini maps"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    push_mini_maps()
