import random

from rich.console import Console
from rich.table import Table

def ssq():
    console = Console()
    # n = int(input('生成几注号码：'))
    n = 1
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]

    #创建表头
    table = Table(show_header=True)
    for col_name in ('序号', '红球', '篮球'):
        table.add_column(col_name, justify="center")
    for i in range(n):
        selected_red_balls = random.sample(red_balls, 6)
        selected_red_balls.sort()
        blue_ball = random.choice(blue_balls)
        #向表格中添加行

        table.add_row(
            str(i + 1),
            f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_red_balls])}[/red]',
            f'[blue]{blue_ball:0>2d}[/blue]'
        )
    console.print(table)

if '__main__' == __name__:
    ssq()