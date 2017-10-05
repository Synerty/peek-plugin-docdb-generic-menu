"""Added Setting Table

Peek Plugin Database Migration Script

Revision ID: 450e040742f8
Revises: 0b12f40fadba
Create Date: 2017-03-21 02:13:25.190281

"""

# revision identifiers, used by Alembic.
revision = '450e040742f8'
down_revision = '0b12f40fadba'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pl_generic_diagram_menu'
    )
    op.create_table('SettingProperty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('settingId', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=16), nullable=True),
    sa.Column('int_value', sa.Integer(), nullable=True),
    sa.Column('char_value', sa.String(), nullable=True),
    sa.Column('boolean_value', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['settingId'], ['pl_generic_diagram_menu.Setting.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pl_generic_diagram_menu'
    )
    op.create_index('idx_SettingProperty_settingId', 'SettingProperty', ['settingId'], unique=False, schema='pl_generic_diagram_menu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_SettingProperty_settingId', table_name='SettingProperty', schema='pl_generic_diagram_menu')
    op.drop_table('SettingProperty', schema='pl_generic_diagram_menu')
    op.drop_table('Setting', schema='pl_generic_diagram_menu')
    # ### end Alembic commands ###