class Member(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
class Post(object):
	def __init__(self,title,content):
		self.title=title
		self.content=content
class MemberStore(object):
	members=[]
	def add(self,member):
		MemberStore.members.append(member)
	def get_all(self):
		print MemberStore.members
class PostStore(object):
	posts=[]
	def add(self,post):
		PostStore.posts.append(post)
	def get_all(self):
		print PostStore.posts
		

		
