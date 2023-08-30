import requests

def get_github_profile_info(username):
    try:
        print(f"Fetching GitHub profile for user '{username}'...\n\n")
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()
            print(f"GitHub Username: {user_data['login']}")
            print(f"Name: {user_data['name']}")
            print(f"Bio: {user_data['bio']}")
            print(f"Followers: {user_data['followers']}")
            print(f"Following: {user_data['following']}")
            print(f"Public Repositories: {user_data['public_repos']}")
            print(f"GitHub Profile Url: {user_data['html_url']}")
            return True
        elif response.status_code == 404:
            print(f"User '{username}' not found on GitHub.")
        else:
            print(f"Error: Unable to fetch data for user '{username}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return False

if __name__ == "__main__":
    while True:
        username = input("Enter a GitHub username: ")
        if get_github_profile_info(username):
            break
