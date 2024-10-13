import os
import shutil

# Define the base directory where all your courses are stored
courses_base_dir = r"C:\Users\sgari\UdemyCourses"

# Define the naming convention structure
file_extension = ".mp4"
# Define a dictionary for course-specific names and years
courses = {
    "Docker": 2024,
    "GitHubDesktop": 2024,
    "Python": 2024
}

# Function to create a course directory name based on the naming convention
def get_course_directory_name(course_name, year):
    return f"{course_name}_{year}"

# Function to create a course directory if it doesn't exist
def create_course_directory(course_dir):
    if not os.path.exists(course_dir):
        os.makedirs(course_dir)
        print(f"Created course directory: {course_dir}")
    else:
        print(f"Directory already exists: {course_dir}")

# Function to move files from old directories to new directories
def move_files_to_new_directory(old_dir, new_dir, file_extension):
    for file in os.listdir(old_dir):
        if file.endswith(file_extension):
            source = os.path.join(old_dir, file)
            destination = os.path.join(new_dir, file)
            shutil.move(source, destination)
            print(f"Moved {file} from {old_dir} to {new_dir}")

# Function to check if all files have been moved and delete the old folder if it's empty
def remove_old_folder_if_empty(old_dir):
    if not os.listdir(old_dir):
        os.rmdir(old_dir)
        print(f"Removed empty old folder: {old_dir}")
    else:
        print(f"Old folder is not empty: {old_dir}")

# Main function to process all courses
def process_courses(courses_base_dir, courses, file_extension):
    for course_name, year in courses.items():
        # Get the new course directory name based on the convention
        new_course_dir_name = get_course_directory_name(course_name, year)
        new_course_path = os.path.join(courses_base_dir, new_course_dir_name)

        # Create the new course directory if it doesn't exist
        create_course_directory(new_course_path)

        # Define the old course directory paths (assuming old folder names are different)
        old_course_dir_name = f"{course_name}Course" if course_name != "Docker" else "Docker_2024"  # Adjust if needed
        old_course_path = os.path.join(courses_base_dir, old_course_dir_name)

        # Move files from the old directory to the new one
        if os.path.exists(old_course_path):
            move_files_to_new_directory(old_course_path, new_course_path, file_extension)

            # Check if all files were moved and remove the old directory if it's empty
            remove_old_folder_if_empty(old_course_path)
        else:
            print(f"Old course folder not found: {old_course_path}")

# Run the process for all courses
process_courses(courses_base_dir, courses, file_extension)
