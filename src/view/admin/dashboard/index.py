import flet as ft

from src import routes


def create_admin_view(page: ft.Page):
    def handle_menu_click(e):
        for control in sidebar.controls:
            if isinstance(control, ft.ListTile):
                control.bgcolor = None

        e.control.bgcolor = ft.Colors.PRIMARY_CONTAINER
        sidebar.update()

        content_area.controls.clear()
        menu_clicked = e.control.data

        if menu_clicked == "menu_1":
            content_area.controls.append(
                ft.Text("Ini adalah halaman untuk Menu 1", size=20))
        elif menu_clicked == "menu_2":
            content_area.controls.append(
                ft.Text("Ini adalah halaman untuk Menu 2", size=20))
        elif menu_clicked == "menu_3":
            content_area.controls.append(
                ft.Text("Ini adalah halaman untuk Menu 3", size=20))

        content_area.controls.append(
            ft.ElevatedButton(
                "Kembali ke Beranda", on_click=lambda _: page.go(routes.HOME)
            )
        )

        content_area.update()

    sidebar_items = [
        ft.Text("Petshop Management".upper(),
                size=18, weight=ft.FontWeight.BOLD),
        ft.Divider(height=10, color="transparent"),
        ft.ListTile(
            title=ft.Text("Menu 1"),
            leading=ft.Icon(ft.Icons.DASHBOARD),
            on_click=handle_menu_click,
            data="menu_1",
        ),
        ft.ListTile(
            title=ft.Text("Menu 2"),
            leading=ft.Icon(ft.Icons.PEOPLE),
            on_click=handle_menu_click,
            data="menu_2",
        ),
        ft.ListTile(
            title=ft.Text("Menu 3"),
            leading=ft.Icon(ft.Icons.SETTINGS),
            on_click=handle_menu_click,
            data="menu_3",
        ),
    ]

    sidebar = ft.Column(
        controls=sidebar_items,
        width=250,
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    content_area = ft.Column(
        [
            ft.Text("Ini adalah halaman untuk Menu 1", size=20),
            ft.ElevatedButton(
                "Kembali ke Beranda", on_click=lambda _: page.go(routes.HOME)
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    first_menu_item = next(
        (c for c in sidebar.controls if isinstance(c, ft.ListTile)), None)
    if first_menu_item:
        first_menu_item.bgcolor = ft.Colors.PRIMARY_CONTAINER

    main_layout = ft.Row(
        [sidebar, ft.VerticalDivider(
            width=2, color=ft.Colors.GREY_300), content_area],
        expand=True,
    )

    return ft.View(
        route=routes.ADMIN_DASHBOARD, 
        controls=[main_layout], 
        padding=ft.padding.all(10), 
        bgcolor=ft.Colors.SURFACE
    )
