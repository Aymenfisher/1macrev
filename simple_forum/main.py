from models import *
member1=Member("Aymen",20)
member2=Member("Fisher",21)
post1=Post("help me","what is python?")
post2=Post("Python quizz","write python code that calculates days between dates")
post3=Post("diffirence?","whats the diffirence between python 2 & python 3")

member_store=MemberStore()
post_store=PostStore()

member_store.add(member2.name)
member_store.add(member1.name)
post_store.add(post1.title)
post_store.add(post2.title)
post_store.add(post3.title)
member_store.get_all()
post_store.get_all()