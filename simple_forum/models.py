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
	last_id=0
	def add(self,member):
		member.id=MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id+=1
	def get_all(self):
		return MemberStore.members	
	def get_by_id(self,id):
		all_members=self.get_all()
		for n in all_members:
			if n.id==id:
				result=n
		return n	
	def entity_exists(self,member):
		if member in MemberStore.members:
			return True
		else:
			return False
	def delete(self,id):
		all_members=MemberStore.members
		for n in all_members:
			print n.id
			if n.id==id:
				MemberStore.members.remove(n)
			


		

class PostStore(object):
	posts=[]
	last_id=0
	def add(self,post):
		post.id=PostStore.last_id
		PostStore.posts.append(post)
		PostStore.last_id+=1
	def get_by_id(self,id):
		all_posts=PostStore.posts
		for i in all_posts:
			if i.id==id:
				result=i
		return result		
		
	def get_all(self):
		return PostStore.posts
	def entity_exists(self,member):
		if member in PostStore.posts:
			return True
		else:
			return False
	def delete(self,id):
		all_posts=PostStore.posts
		for n in all_posts:
			print n.id
			if n.id==id:
				PostStore.posts.remove(n)