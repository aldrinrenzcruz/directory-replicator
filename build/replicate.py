import os
import shutil
import time

# Define the function to create the folder structure
def create_folder_structure(folder_path, file_name):
    # Convert the file name to uppercase for consistency
    file_name = file_name.upper()

    # Get the total number of main folders
    num_main_folders = len([name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))])

    # Initialize a counter for the main folders
    main_folder_count = 0

    # Loop through all main folders in the shared folder
    for main_folder in os.listdir(folder_path):
        main_folder_path = os.path.join(folder_path, main_folder)

        # Check if the main folder contains subfolders
        if os.path.isdir(main_folder_path):
            # Print a message for the current folder being worked on
            main_folder_count += 1
            print(f'{main_folder_count} of {num_main_folders}: {main_folder}')

            # Create the corresponding main folder in the working directory if it doesn't exist
            if not os.path.exists(main_folder):
                os.makedirs(main_folder, exist_ok=True)

            # Copy the file to the corresponding parent folder, if it exists
            for subfolder in os.listdir(main_folder_path):
                subfolder_path = os.path.join(main_folder_path, subfolder)
                if os.path.isdir(subfolder_path):
                    for filename in os.listdir(subfolder_path):
                        if file_name in filename.upper():
                            old_file = os.path.join(subfolder_path, filename)
                            new_file = os.path.join(main_folder, filename)
                            shutil.copy2(old_file, new_file)

                            # Create the corresponding subfolder in the working directory if it doesn't exist
                            new_subfolder = os.path.join(main_folder, subfolder)
                            if not os.path.exists(new_subfolder):
                                os.makedirs(new_subfolder, exist_ok=True)

    # Display a message when the folder structure has been created
    print('[SUCCESS] All folders and subfolders have been replicated.')

# Prompt the user to enter the network shared folder path
folder_path = input('Enter the network shared folder path: ')

# Prompt the user to enter the file name to copy
file_name = input('Enter the masterfile name you want to copy (FFE2 or FFE3): ').upper()

# Check if the file name is valid
if file_name not in ['FFE2', 'FFE3']:
    print('Invalid file name. Please enter either FFE2 or FFE3.')
else:
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f'The folder path {folder_path} does not exist.')
    else:
        start_time = time.time()
        # Create the folder structure and copy the files
        create_folder_structure(folder_path, file_name)
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        if elapsed_time > 60:
            elapsed_time = round(elapsed_time / 60, 2)
            print(f'The script took {elapsed_time} minutes to complete.')
        else:
            print(f'The script took {elapsed_time} seconds to complete.')
        # Auto-close the console window
        input('Press enter to exit.')