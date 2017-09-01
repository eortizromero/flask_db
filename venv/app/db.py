from app import db, Users, Posts

# admin = Users(name='admin', email='admin@example.com', password='admin00', phone='7121288260', gender='0')
# manager = Users(name='manager', email='manager@example.com', password='manager00', phone='7121786765', gender='1')

# admin_post = Posts(title='Admin Post', content="Content for admin post")
# manager_post = Posts(title='Manager Post', content='Content for manager post')

# admin.posts().save(admin_post)

# manager_post.users().associate(manager)

if __name__ == '__main__':
	db.cli.run()
