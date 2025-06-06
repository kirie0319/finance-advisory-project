"""add user table

Revision ID: 33f9bdc5b576
Revises: eab8c934a6be
Create Date: 2025-04-21 12:10:08.253064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f9bdc5b576'
down_revision = 'eab8c934a6be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_prompts_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_email_key', type_='unique')
        batch_op.drop_constraint('users_username_key', type_='unique')
        batch_op.drop_index('ix_users_email')
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.drop_index('ix_users_username')
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.create_index('ix_users_username', ['username'], unique=False)
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.create_index('ix_users_email', ['email'], unique=False)
        batch_op.create_unique_constraint('users_username_key', ['username'])
        batch_op.create_unique_constraint('users_email_key', ['email'])

    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(length=36), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_prompts_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
