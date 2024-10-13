import os

# Define the path to your Udemy course directory
course_directory = r"C:\Users\sgari\UdemyCourses\GitHubDesktopCourse"

# Define a temporary naming convention for "dud" names
temp_naming_convention = "TempFile_{:02d}.mp4"

# Define the final naming convention with the lesson name
final_naming_convention = "GitHubDesktop_Lesson_{:02d}.mp4"

# Get a list of all files in the directory
files = os.listdir(course_directory)

# Filter only .mp4 files and get their full paths
mp4_files = [f for f in files if f.lower().endswith('.mp4')]

# Sort files by last modified time (ascending)
mp4_files.sort(key=lambda f: os.path.getmtime(os.path.join(course_directory, f)))

# Step 1: Rename all files to a temporary name (TempFile)
for idx, filename in enumerate(mp4_files):
    temp_filename = temp_naming_convention.format(idx + 1)
    old_file = os.path.join(course_directory, filename)
    temp_file = os.path.join(course_directory, temp_filename)
    
    # Rename the file to the temporary name
    os.rename(old_file, temp_file)
    print(f"Temporarily renamed: {filename} -> {temp_filename}")

# Step 2: Rename all files to the correct lesson name based on modification time
# Get the list of temp files
temp_files = os.listdir(course_directory)
temp_files = [f for f in temp_files if f.startswith('TempFile')]

# Sort the temp files again by modification time, just in case
temp_files.sort(key=lambda f: os.path.getmtime(os.path.join(course_directory, f)))

# Loop through the temp files and rename them back based on modification time
for idx, temp_filename in enumerate(temp_files):
    final_filename = final_naming_convention.format(idx + 1)
    temp_file = os.path.join(course_directory, temp_filename)
    final_file = os.path.join(course_directory, final_filename)
    
    # Rename the temp file to the final lesson name
    os.rename(temp_file, final_file)
    print(f"Renamed: {temp_filename} -> {final_filename}")

print("All files renamed based on modification time.")
