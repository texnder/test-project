from db import pg

# create users table 
create_users_table = pg.execute(
    'CREATE TABLE users( \
        id SERIAL PRIMARY KEY \
        username VARCHAR(32) UNIQUE  NOT NULL \
        password VARCHAR(256) NOT NULL \
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP \
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP \
    )'
)

# create posts table
create_posts_table = pg.execute(
    'CREATE TABLE posts( \
        id SERIAL PRIMARY KEY \
        title VARCHAR(400)  NOT NULL \
        caption VARCHAR(400) \
        body TEXT NOT NULL \
        user_id REFRENCE users(id) \
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP \
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP \
        deleted_at TIMESTAMP WITH TIME ZONE DEFAULT NULL \
    )'
)