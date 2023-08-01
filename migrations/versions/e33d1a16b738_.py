"""empty message

Revision ID: e33d1a16b738
Revises: 
Create Date: 2023-08-02 02:21:49.072333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e33d1a16b738'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('create_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('reply',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('create_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('message_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    op.drop_table('user')
    op.drop_table('message')
    # ### end Alembic commands ###
