import flet as ft


def create_product_content():
    return ft.Column(
        controls=[
            ft.Text("Product Overview", size=30),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
