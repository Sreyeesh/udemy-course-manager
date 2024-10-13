import os
import shutil

# Define directories
source_videos_dir = r"C:\Users\sgari\Videos"  # Path to user's video folder
udemy_courses_dir = r"C:\Users\sgari\UdemyCourses"  # Path to Udemy courses folder

# Define the courses and the year
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

# Function to move .mp4 files from the source video folder to the course folder
def move_files_to_course_folder(source_dir, course_dir, course_name, file_extension=".mp4"):
    files = [f for f in os.listdir(source_dir) if f.endswith(file_extension)]
    
    for idx, file in enumerate(files, start=1):
        source_file_path = os.path.join(source_dir, file)
        lesson_number = str(idx).zfill(2)
        new_filename = f"{course_name}_Lesson_{lesson_number}{file_extension}"
        destination_file_path = os.path.join(course_dir, new_filename)
        
        # Move the file to the destination directory
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved {file} to {new_filename}")

# Main function to process all courses
def process_courses(source_videos_dir, udemy_courses_dir, courses):
    for course_name, year in courses.items():
        # Create the new course directory name based on the convention
        new_course_dir_name = get_course_directory_name(course_name, year)
        new_course_path = os.path.join(udemy_courses_dir, new_course_dir_name)
        
        # Create the course directory if it doesn't exist
        create_course_directory(new_course_path)
        
        # Move files from user's video folder to the new course directory
        move_files_to_course_folder(source_videos_dir, new_course_path, course_name)

# Run the process for all courses
process_courses(source_videos_dir, udemy_courses_dir, courses)
