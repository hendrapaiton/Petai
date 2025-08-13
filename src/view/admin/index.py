import flet as ft

from src import routes
from src.view.admin.dashboard.index import create_dashboard_content
from src.view.admin.product.index import create_product_content


def create_admin_view(page: ft.Page, route: str):
    menu_items_data = [
        {"title": "Dasbor", "icon": ft.Icons.SHOPPING_CART, "data": "overview"},
        {"title": "Produk", "icon": ft.Icons.INVENTORY, "data": "product"},
    ]

    content_mapping = {
        "overview": create_dashboard_content(),
        "product": create_product_content(),
    }

    route_to_data_key = {
        routes.ADMIN: "overview",
        routes.ADMIN_DASHBOARD: "overview",
        routes.ADMIN_PRODUCT: "product",
    }

    def handle_menu_click(e):
        for control in sidebar.controls:
            if isinstance(control, ft.ListTile):
                control.bgcolor = None

        e.control.bgcolor = ft.Colors.PRIMARY_CONTAINER
        sidebar.update()

        content_area.controls.clear()
        menu_clicked = e.control.data

        new_content = content_mapping.get(
            menu_clicked, ft.Text("Konten tidak ditemukan.", size=20)
        )
        content_area.controls.append(new_content)

        content_area.update()

    sidebar_items = [
        ft.Text("Petshop Management".upper(),
                size=18, weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER),
        ft.Divider(height=10, color="transparent"),
    ]

    sidebar_items.append(
        ft.Container(
            content=ft.ElevatedButton(
                "Kembali ke Beranda", on_click=lambda _: page.go(routes.HOME)),
            alignment=ft.Alignment.CENTER)
    )

    sidebar_items.append(ft.Divider(height=10, color="transparent"))

    for item in menu_items_data:
        sidebar_items.append(
            ft.ListTile(
                title=ft.Text(item["title"]),
                leading=ft.Icon(item["icon"]),
                on_click=handle_menu_click,
                data=item["data"],
            )
        )

    sidebar = ft.Column(
        controls=sidebar_items,
        width=250,
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    initial_data_key = route_to_data_key.get(route, "overview")
    content_area = ft.Column(
        [
            content_mapping[initial_data_key],
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    initial_menu_item = next(
        (c for c in sidebar.controls if isinstance(
            c, ft.ListTile) and c.data == initial_data_key), None
    )
    if initial_menu_item:
        initial_menu_item.bgcolor = ft.Colors.PRIMARY_CONTAINER

    main_layout = ft.Row(
        [sidebar, ft.VerticalDivider(
            width=2, color=ft.Colors.GREY_300), content_area],
        expand=True,
    )

    return ft.View(
        route=route,
        controls=[main_layout],
        padding=ft.padding.all(10),
        bgcolor=ft.Colors.SURFACE
    )
