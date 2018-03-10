from models import *
member1=Member("Aymen",20)
member2=Member("Fisher",21)
post1=Post("help me","what is python?")
post2=Post("Python quizz","write python code that calculates days between dates")
post3=Post("diffirence?","whats the diffirence between python 2 & python 3")

member_store=MemberStore()
post_store=PostStore()

member_store.add(member2)
member_store.add(member1)
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
member_store.get_all()
post_store.get_all()
print member_store.get_by_id(1)
print post_store.get_by_id(2)