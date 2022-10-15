from user import User
from post import Post

user_info_one = User("nana@gmail.com", "nana", "nana@123", "Devops Architect")
user_info_one.get_user_info()

user_info_2 = User("megha@gmail.com", "Megha Saraf", "megha@123", "Devops Engineer")
user_info_2.get_user_info()

new_post = Post("On a secret mission today",user_info_2.name)
new_post.get_post_info()