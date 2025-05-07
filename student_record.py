import os

# Create output directory if it doesn't exist
output_dir = "feedback_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# This function creates general comment based on understanding level dependent on score
def general_comments_text(understanding_level: int, first_name: str) -> str:
    if understanding_level >= 8:
        return (
            f"{first_name} has an excellent grasp of the material. "
            f"{first_name} regularly understands new ideas quickly and applies them well in class. "
            f"This strong understanding helps {first_name} make steady and confident progress."
        )
    elif understanding_level >= 5:
        return (
            f"{first_name} has a basic understanding of the subject. "
            f"There are times when extra support is needed to fully grasp key ideas, "
            f"but with some more practice and focus, {first_name} can improve steadily."
        )
    else:
        return (
            f"{first_name} is finding many parts of the material quite difficult. "
            f"Regular help and extra time reviewing core topics will be important for progress. "
            f"With support and encouragement, {first_name} can start to build confidence in the subject."
        )

# This function  creates comment about punctuality and engagement dependent on score
def punctuality_engagement_text(contribution_level: int, first_name: str) -> str:
    if contribution_level >= 8:
        return f"{first_name} is highly punctual and regularly contributes with enthusiasm during lessons."
    elif contribution_level >= 5:
        return f"{first_name} participates occasionally and usually meets punctuality expectations."
    else:
        return f"{first_name} is often late and shows minimal engagement in class activities."

# This function creates comment for further learning based on score
def further_learning_text(understanding_level: int, contribution_level: int, first_name: str) -> str:
    if understanding_level >= 8 and contribution_level >= 8:
        return "Continue to challenge yourself with advanced material and maintain active participation."
    elif understanding_level < 5 or contribution_level < 5:
        return f"{first_name} should consider attending extra help sessions and actively engaging with homework and class discussions."
    else:
        return "Review past topics regularly and aim to contribute more consistently in class."

# Loop to get student information and scores needed to generate feedback reports
while True:
    # Get and validate the student's first name, checks first name is not empty
    while True:
        first_name = input("Enter student's first name (or type 'Exit' to finish): ").strip().title()
        if first_name.lower() == 'exit':
            exit()
        if first_name:
            break
        print("First name cannot be empty. Please enter a valid name.")

    # Validates student's last name, checks last name is not empty
    while True:
        last_name = input("Enter student's last name: ").strip().title()
        if last_name:
            break
        print("Last name cannot be empty. Please enter a valid name.")

    full_name = f"{first_name} {last_name}"

    # This section gets and validate the student's understanding level between 0-10
    while True:
        try:
            understanding_level = int(input(f"Enter understanding level for {full_name} (0-10): "))
            if 0 <= understanding_level <= 10:
                break
            else:
                print("Please enter a score between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # This sectio gets and validate the student's contribution level (0-10)
    while True:
        try:
            contribution_level = int(input(f"Enter contribution level for {full_name} (0-10): "))
            if 0 <= contribution_level <= 10:
                break
            else:
                print("Please enter a score between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # This section saves the feedback comments to variables
    general_comment = general_comments_text(understanding_level, first_name)
    engagement_comment = punctuality_engagement_text(contribution_level, first_name)
    learning_comment = further_learning_text(understanding_level, contribution_level, first_name)

    # Create the filename based on firstname and last name and full file path for the student's feedback folder
    filename = f"{first_name}_{last_name}_report.txt"
    file_path = os.path.join(output_dir, filename)

    # Error handles the write to feedback_file folder
    try:
        with open(file_path, "w") as file:
            file.write("General comments\n")
            file.write("*****************\n\n")
            file.write(general_comment + "\n\n")
            file.write("Punctuality and engagement\n")
            file.write("**************************\n\n")
            file.write(engagement_comment + "\n\n")
            file.write("Further learning\n")
            file.write("****************\n\n")
            file.write(learning_comment + "\n")

        print(f"Feedback for {full_name} saved in {filename}")

    # Handles a file writing errors
    except OSError as e:
        print(f"Error: Could not write file for {full_name}. Reason: {e}")
print("Student feedbacks have all been processed.")