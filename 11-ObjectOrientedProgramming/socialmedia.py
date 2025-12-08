class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(f"{self.username} posts:")
        for i in range(len(self.posts)):
            print(f"{i + 1}. {self.posts[i]}")


def main() -> None:
    johndoe = SocialMediaProfile("John Doe")
    johndoe.add_post("Hello, world!")
    johndoe.add_post("Had a greate day at the park!")
    johndoe.add_post("What's up, Natalie? How are you?")

    johndoe.display_timeline()


if __name__ == "__main__":
    main()

