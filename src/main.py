import flet as ft


def main(page: ft.Page):
    page.title = "Aplikasi Kasir (POS)"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    products = [
        {"name": "Kopi Susu", "price": 18000, "icon": ft.Icons.COFFEE},
        {"name": "Teh Manis", "price": 8000, "icon": ft.Icons.EMOJI_FOOD_BEVERAGE},
        {"name": "Roti Bakar", "price": 15000, "icon": ft.Icons.BAKERY_DINING},
        {"name": "Nasi Goreng", "price": 25000, "icon": ft.Icons.RICE_BOWL},
        {"name": "Mie Ayam", "price": 22000, "icon": ft.Icons.RAMEN_DINING},
        {"name": "Jus Jeruk", "price": 12000, "icon": ft.Icons.LOCAL_BAR},
    ]

    cart_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
    total_price = ft.Text("Rp 0", size=20, weight=ft.FontWeight.BOLD)

    def update_total():
        total = 0
        for item_row in cart_items.controls:
            total += item_row.data["price"] * item_row.data["quantity"]
        total_price.value = f"Rp {total:,}"

    def add_to_cart(e):
        product_data = e.control.data

        existing_item = None
        for item_row in cart_items.controls:
            if item_row.data["name"] == product_data["name"]:
                existing_item = item_row
                break

        if existing_item:
            existing_item.data["quantity"] += 1
            quantity_text = existing_item.data["quantity_control"]
            quantity_text.value = f"Jumlah: {existing_item.data['quantity']}"
        else:
            quantity_text_control = ft.Text(f"Jumlah: 1")
            new_item_row = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                data={
                    "name": product_data["name"],
                    "price": product_data["price"],
                    "quantity": 1,
                    "quantity_control": quantity_text_control},
                controls=[
                    ft.Column([
                        ft.Text(product_data["name"],
                                weight=ft.FontWeight.BOLD),
                        quantity_text_control,
                    ]),
                    ft.Text(f"Rp {product_data['price']:,}",
                            text_align=ft.TextAlign.RIGHT),
                ]
            )
            cart_items.controls.append(new_item_row)

        update_total()
        page.update()

    products_grid = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=200,
        child_aspect_ratio=0.8,
        spacing=10,
        run_spacing=10,
    )

    for product in products:
        products_grid.controls.append(
            ft.Container(
                padding=10,
                border=ft.border.all(1, ft.Colors.OUTLINE),
                border_radius=ft.border_radius.all(5),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(name=product["icon"],
                                size=40, color=ft.Colors.PRIMARY),
                        ft.Text(
                            product["name"], size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Text(f"Rp {product['price']:,}", size=14),
                        ft.ElevatedButton(
                            "Tambah",
                            icon=ft.Icons.ADD_SHOPPING_CART,
                            on_click=add_to_cart,
                            data=product,
                            width=150,
                            bgcolor=ft.Colors.BLUE_200,
                            color=ft.Colors.BLACK
                        )
                    ]
                )
            )
        )

    header_etalase = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Etalase Produk", size=24, weight=ft.FontWeight.BOLD),
            ft.Container(width=40),
            ft.TextField(
                hint_text="Cari produk...",
                prefix_icon=ft.Icons.SEARCH,
                expand=True,
                height=35,
                border_radius=20,
            ),
            ft.ElevatedButton(
                content="Admin",
                icon=ft.Icons.ADMIN_PANEL_SETTINGS,
                on_click=lambda e: print("Go to Admin Page"),
            ),
        ]
    )

    left_panel = ft.Container(
        content=ft.Column(
            controls=[header_etalase, ft.Divider(), products_grid], spacing=10),
        expand=2, padding=10)

    right_panel = ft.Container(
        expand=1,
        padding=20,
        bgcolor=ft.Colors.SURFACE,
        border=ft.border.all(1, ft.Colors.OUTLINE),
        border_radius=ft.border_radius.all(10),
        content=ft.Column(controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.Text("Keranjang".upper(), size=20, weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.END),
                ]
            ),
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Text("Total:".upper(), size=18,
                        weight=ft.FontWeight.NORMAL), total_price,
            ]),
            ft.Divider(),
            ft.Container(content=cart_items, expand=True),
            ft.Row(
                spacing=10,
                controls=[
                    ft.ElevatedButton(
                        "Cash",
                        icon=ft.Icons.MONEY_ROUNDED,
                        expand=True,
                        bgcolor=ft.Colors.GREEN_ACCENT_700,
                        color=ft.Colors.WHITE
                    ),
                    ft.ElevatedButton(
                        "QRIS",
                        icon=ft.Icons.QR_CODE_2,
                        expand=True,
                        bgcolor=ft.Colors.BLUE_GREY_700,
                        color=ft.Colors.WHITE
                    )
                ]
            )
        ])
    )

    page.add(ft.Row(controls=[left_panel, right_panel],
             vertical_alignment=ft.CrossAxisAlignment.STRETCH, expand=True))
    page.update()
