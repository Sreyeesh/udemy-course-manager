import os
import shutil

# Define the base directory where all your courses are stored
courses_base_dir = r"C:\Users\sgari\UdemyCourses"

# Define the naming convention structure
file_extension = ".mp4"
# Define a dictionary for course-specific names
course_names = {
    "GitHubDesktopCourse": "GitHubDesktop",
    "Docker_2024": "Docker"
}

# Function to move all .mp4 files from subdirectories to the root
def move_files_to_root(course_dir, file_extension):
    for root, dirs, files in os.walk(course_dir):
        for file in files:
            if file.endswith(file_extension):
                # Define source (current location) and destination (root directory)
                source = os.path.join(root, file)
                destination = os.path.join(course_dir, file)
                
                # Move file to root if it's not already there
                if source != destination:
                    shutil.move(source, destination)
                    print(f"Moved {file} to {course_dir}")

# Function to rename files in the root directory of each course
def rename_files_in_directory(course_dir, course_name, file_extension):
    # List all files in the root directory
    files = [f for f in os.listdir(course_dir) if f.endswith(file_extension)]
    
    # Sort files if needed, for example, alphabetically
    files.sort()

    for idx, filename in enumerate(files, start=1):
        # Pad the lesson number to two digits
        lesson_number = str(idx).zfill(2)

        # Create the new filename with the proper format
        new_filename = f"{course_name}_Lesson_{lesson_number}{file_extension}"
        
        # Define the full file paths
        old_file_path = os.path.join(course_dir, filename)
        new_file_path = os.path.join(course_dir, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

# Function to remove empty subdirectories after files have been moved
def remove_empty_subdirs(course_dir):
    for root, dirs, _ in os.walk(course_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            # Check if the directory is empty
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty directory: {dir_path}")

# Main function to process all courses
def process_courses(courses_base_dir, course_names, file_extension):
    for course_folder in os.listdir(courses_base_dir):
        course_path = os.path.join(courses_base_dir, course_folder)
        
        # If the folder is a course directory, process it
        if course_folder in course_names:
            course_name = course_names[course_folder]
            print(f"Processing course: {course_name}")
            
            # Move all .mp4 files from subdirectories to the root directory
            move_files_to_root(course_path, file_extension)
            
            # Rename files in the root directory
            rename_files_in_directory(course_path, course_name, file_extension)
            
            # Remove any empty subdirectories
            remove_empty_subdirs(course_path)

# Run the process for all courses
process_courses(courses_base_dir, course_names, file_extension)
