class Comment:
    def __init__(self, username, content, likes=0):
        username = username
        content = content
        likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
