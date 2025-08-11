import flet as ft

from src import routes


def create_admin_view(page: ft.Page):
    return ft.View(
        route=routes.ADMIN_STOCK,
        controls=[
            ft.Text("Stock Overview", size=30),
            ft.ElevatedButton(
                "Kembali ke Beranda",
                on_click=lambda _: page.go(routes.HOME)
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
