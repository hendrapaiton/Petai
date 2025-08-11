import flet as ft

from src import routes


def create_pos_view(page: ft.Page):
    return ft.View(
        route=routes.POS,
        controls=[
            ft.Text("Etalase Produk", size=30),
            ft.ElevatedButton(
                "Kunjungi Admin",
                on_click=lambda _: page.go(routes.ADMIN)
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
