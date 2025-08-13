import flet as ft


def create_dashboard_content():
    return ft.Column(
        controls=[
            ft.Text("Dashboard Overview", size=30),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
