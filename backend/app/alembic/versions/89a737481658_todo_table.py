"""Todo table

Revision ID: 89a737481658
Revises: 
Create Date: 2022-11-09 11:52:53.034215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89a737481658'
down_revision = None
branch_labels = None
depends_on = None


def create_todo_table():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("record", sa.String),
        sa.Column("priority", sa.Boolean)
    )


def upgrade() -> None:
    create_todo_table()


def downgrade() -> None:
    op.drop_table("todos")
