import csv
import os
import resend

# Set the API key for the resend module
resend.api_key = os.environ["RESEND_API_KEY"]

# Function to read HTML content from file


def read_html_file(html_file_path):
    with open(html_file_path, "r") as file:
        html_content = file.read()
    return html_content

# Function to read emails from CSV and send them


def send_emails_from_csv(csv_file, html_file):
    # Read HTML content from file
    html_content = read_html_file(html_file)
    count=0
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            # name = row[1]  # Assuming name is in the second column
            email = row[0]  # Assuming email is in the first column
            count+=1
            email_params = {
                "from": "Shreyas@email.maneuverventures.com",
                "to": email,
                "subject": "Unlock Your Investment Potential with Maneuver Ventures",
                "html": html_content,
                "reply_to": "connect@maneuverventures.com",
            }
            email = resend.Emails.send(email_params)
            # print(email)
            if(count%100==0):
                print(count)


# Call the function and pass the path to your CSV file and HTML file
send_emails_from_csv('a.csv', 'RF.html')
