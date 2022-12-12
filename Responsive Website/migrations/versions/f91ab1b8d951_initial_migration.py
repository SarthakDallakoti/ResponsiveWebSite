"""Initial Migration

Revision ID: f91ab1b8d951
Revises: 
Create Date: 2022-12-08 01:08:57.359804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f91ab1b8d951'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserAccount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('User', sa.String(length=500), nullable=True),
    sa.Column('Email', sa.String(length=500), nullable=True),
    sa.Column('Password', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_UserAccount_Email'), 'UserAccount', ['Email'], unique=False)
    op.create_index(op.f('ix_UserAccount_Password'), 'UserAccount', ['Password'], unique=False)
    op.create_index(op.f('ix_UserAccount_User'), 'UserAccount', ['User'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_UserAccount_User'), table_name='UserAccount')
    op.drop_index(op.f('ix_UserAccount_Password'), table_name='UserAccount')
    op.drop_index(op.f('ix_UserAccount_Email'), table_name='UserAccount')
    op.drop_table('UserAccount')
    # ### end Alembic commands ###