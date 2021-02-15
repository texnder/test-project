from db import pg


# create users table 
drop_users_table = pg.execute(
    'DROP TABLE users'
)

# create posts table
drop_posts_table = pg.execute(
    'DROP TABLE posts'
)