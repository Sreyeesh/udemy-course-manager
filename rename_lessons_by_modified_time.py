import os

# Function to rename files in the specified course directory based on modification time
def rename_files_as_lessons(course_dir, course_name, max_lessons=37, final_lesson=37, file_extension=".mp4"):
    # Get a list of all files with the specified extension in the directory
    files = [f for f in os.listdir(course_dir) if f.endswith(file_extension)]

    # Sort the files by last modified time to maintain correct lesson order
    files.sort(key=lambda x: os.path.getmtime(os.path.join(course_dir, x)))

    lesson_number = 0  # Start lesson numbering at 0

    # Rename each file according to the modification time and format
    for idx, filename in enumerate(files):
        if lesson_number >= max_lessons:
            print(f"Maximum lesson limit reached. Stopping at Lesson {max_lessons}. No more files will be renamed.")
            break

        lesson_number += 1

        # If the lesson number exceeds the final lesson specified, stop renaming
        if lesson_number > final_lesson:
            print(f"Reached final lesson: Lesson {final_lesson}. No more files will be renamed.")
            break

        # Format lesson number with leading zeros
        lesson_number_str = str(lesson_number).zfill(2)

        # Create the new filename with the correct Lesson format
        new_filename = f"{course_name}_Lesson_{lesson_number_str}{file_extension}"
        
        old_file_path = os.path.join(course_dir, filename)
        new_file_path = os.path.join(course_dir, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

# Main function to rename files for any specified course
def rename_course_files():
    print("Renaming files for a course...")
    
    # Input course name and year
    course_name = input("Enter the course name: ")
    course_year = input("Enter the course year: ")
    
    # Define the course directory
    course_dir_name = f"{course_name}_{course_year}"  # e.g., Docker_2024
    course_dir_path = os.path.join(r"C:\Users\sgari\UdemyCourses", course_dir_name)  # Adjust base path as needed
    
    if os.path.exists(course_dir_path):
        rename_files_as_lessons(course_dir_path, course_name)
    else:
        print(f"Course folder not found: {course_dir_path}")

# Example usage
if __name__ == "__main__":
    rename_course_files()
