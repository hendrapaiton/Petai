import flet as ft
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import routes
from src.view.admin.dashboard.index import create_admin_view
from src.view.pos.index import create_pos_view


def main(page: ft.Page):
    page.title = "AI-Powered Point of Sale for Petshop | PETAI"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.START

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        admin_routes = (
            routes.ADMIN,
            routes.ADMIN_DASHBOARD,
            routes.ADMIN_PRODUCT,
            routes.ADMIN_SALES,
            routes.ADMIN_STOCK,
        )

        if e.route in (routes.HOME, routes.POS):
            page.views.append(create_pos_view(page))
        elif e.route in admin_routes:
            page.views.append(create_admin_view(page, e.route))
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
