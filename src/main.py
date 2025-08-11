import flet as ft

from . import routes
from .view.admin.index import create_admin_view
from .view.pos.index import create_pos_view


def main(page: ft.Page):
    page.title = "PETSHOP DENGAN ARTIFICIAL INTELIGENCE | PETAI"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    print(page.route)

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        if e.route in (routes.HOME, routes.POS):
            page.views.append(create_pos_view(page))
        elif e.route == routes.ADMIN:
            page.views.append(create_admin_view(page))
        else:
            page.views.append(
                ft.View(
                    route=routes.NOT_FOUND,
                    controls=[
                        ft.Text("404: Halaman tidak ditemukan", size=30),
                        ft.ElevatedButton(
                            "Kembali ke Beranda",
                            on_click=lambda _: page.go(routes.HOME)
                        ),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route or "/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route if page.route is not None else "/")
