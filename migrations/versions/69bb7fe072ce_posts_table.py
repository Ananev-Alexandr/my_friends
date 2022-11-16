"""posts table

Revision ID: 69bb7fe072ce
Revises: a156caa33301
Create Date: 2022-11-15 19:36:04.957112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69bb7fe072ce'
down_revision = 'a156caa33301'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('login', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('name', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('surname', sa.String(length=20), nullable=True))
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(batch_op.f('ix_user_login'), ['login'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_surname'), ['surname'], unique=False)
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_surname'))
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.drop_index(batch_op.f('ix_user_login'))
        batch_op.create_index('ix_user_username', ['username'], unique=False)
        batch_op.drop_column('surname')
        batch_op.drop_column('name')
        batch_op.drop_column('login')

    # ### end Alembic commands ###
