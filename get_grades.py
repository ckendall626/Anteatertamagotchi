import requests

# Set up API URL, token, and course ID
canvas_url = input("Canvas API URL")
access_token = input("Access Token")

# Headers for the request
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Example: Get student grades for a specific course
def get_courses():
    response = requests.get(f'{canvas_url}courses', headers=headers)
    
    if response.status_code == 200:
        courses = response.json()
        print(courses)
        for course in courses:
            print(course['name'])
    else:
        print(f"Failed to fetch courses: {response.status_code}")

get_courses()