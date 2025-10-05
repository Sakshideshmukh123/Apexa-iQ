import requests
import sys

# Redirect output to file
sys.stdout = open("output.txt", "w", encoding="utf-8")

# Base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# 1️ Get all posts
def get_all_posts():
    print("\nGetting all posts...")
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        print(f"Total posts fetched: {len(posts)}")
        # show only first 3 posts for short output
        for post in posts[:3]:
            print(f"ID: {post['id']} | Title: {post['title']}")
    else:
        print("Error while fetching posts!")

# 2️ Get a single post
def get_single_post(post_id):
    print(f"\nGetting post with ID {post_id}...")
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        post = response.json()
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    else:
        print("Post not found!")

# 3️ Create a new post
def create_post(title, body, user_id):
    print("\nCreating a new post...")
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:  # 201 means 'Created'
        new_post = response.json()
        print("New post created successfully!")
        print(f"ID: {new_post['id']}")
        return new_post
    else:
        print("Error while creating post!")

# 4️ Delete a post
def delete_post(post_id):
    print(f"\nDeleting post with ID {post_id}...")
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print("Post deleted successfully (simulated).")
    else:
        print("Error while deleting post!")

# Main program
if __name__ == "__main__":
    # 1. Get all posts
    get_all_posts()

    # 2. Get one post
    get_single_post(3)

    # 3. Create a post
    new_post = create_post("My New Post", "This is my post body", 1)

    # 4. Delete a post (the one we created)
    if new_post:
        delete_post(new_post["id"])

    print("\n Program completed successfully.")

# Close redirection
sys.stdout.close()
