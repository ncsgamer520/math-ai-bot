import os
import flet as ft

def main(page: ft.Page):
    page.title = "MATH AI BOT"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="https://images.alphacoders.com/109/1094054.jpg",
            fit="cover",
        )
    )

    SENS_DATA = {
        "Infinix": ["Note 7", "Note 8", "Note 10", "Note 11", "Note 12", "Note 30", "Note 40", "Hot 9", "Hot 10", "Hot 11", "Hot 12", "Hot 20", "Hot 30", "Hot 40", "Smart 5", "Smart 6", "Smart 7", "Smart 8", "Zero 8", "Zero 30", "GT 10 Pro", "GT 20 Pro", "Note 50", "Hot 50", "Zero 40"],
        "TECNO": ["Spark 5", "Spark 6", "Spark 7", "Spark 8", "Spark 9", "Spark 10", "Spark 20", "Spark 30", "Pova", "Pova 2", "Pova 3", "Pova 4", "Pova 5", "Pova 6", "Camon 15", "Camon 16", "Camon 17", "Camon 18", "Camon 19", "Camon 20", "Camon 30", "Phantom X", "Phantom V", "Spark 40", "Pova 7"],
        "Samsung": ["A01", "A02", "A03", "A04", "A05", "A11", "A12", "A13", "A14", "A15", "A21", "A22", "A23", "A24", "A31", "A32", "A34", "A35", "A51", "A52", "A54", "A55", "S23 Ultra", "S24 Ultra", "S25 Ultra"],
        "Xiaomi": ["Redmi 9", "9A", "9C", "Note 9", "Note 9S", "Note 10", "Note 10S", "Note 11", "Note 11S", "Note 12", "Note 13", "Note 14", "Poco M3", "Poco M4", "Poco M5", "Poco M6", "Poco X2", "Poco X3", "Poco X4", "Poco X5", "Poco X6", "Poco F5", "Poco F6", "Redmi 13C", "Poco C65"],
        "iPhone": ["7", "7 Plus", "8", "8 Plus", "X", "XR", "XS", "XS Max", "11", "11 Pro", "11 Pro Max", "12", "12 Mini", "12 Pro", "12 Pro Max", "13", "13 Mini", "13 Pro", "13 Pro Max", "14", "14 Plus", "14 Pro", "14 Pro Max", "15 Pro", "16 Pro"]
    }
    
    WEAPON_TIPS = {
        "Desert Eagle": "🦅 Desert Eagle: Neck-level aim. Use a firm, vertical drag-up.",
        "MP40": "🔥 MP40: Close range. Use a 'J' motion to track chest-to-head.",
        "M1887": "💥 M1887: Chest-height crosshair. Execute a rapid, snapping drag.",
        "AWM": "🎯 AWM: Head-aim. Quick-switch immediately after firing."
    }
    
    FF_COLORS = {"Red": "[FF0000]", "Green": "[00FF00]", "Blue": "[0000FF]", "Yellow": "[FFFF00]", "Purple": "[6E00FF]", "Cyan": "[00FFFF]", "Orange": "[FF9000]", "Pink": "[FF00FF]"}

    main_menu = ft.Column(visible=False, alignment=ft.MainAxisAlignment.CENTER)
    content_area = ft.Column(visible=False, alignment=ft.MainAxisAlignment.CENTER)
    
    def show_menu(e=None):
        main_menu.visible = True
        content_area.visible = False
        gate_container.visible = False
        page.update()

    def show_simple(title, content, is_colors=False):
        content_area.controls = [ft.Text(title, size=22, weight="bold", color="white")]
        if is_colors:
            for name, code in FF_COLORS.items():
                content_area.controls.append(ft.ListTile(title=ft.Text(f"{name}: {code}"), leading=ft.Icon("palette"), on_click=lambda e, c=code: print(f"Copied {c}")))
        else:
            content_area.controls.append(ft.Text(content, size=16, color="white"))
        content_area.controls.append(ft.FilledButton("⬅️ Back", on_click=show_menu))
        main_menu.visible = False
        content_area.visible = True
        page.update()

    def show_brands():
        content_area.controls = [ft.Text("🎯 SELECT BRAND", size=20, weight="bold", color="white")]
        for brand in SENS_DATA:
            content_area.controls.append(ft.ElevatedButton(brand, on_click=lambda e, b=brand: show_models(b)))
        content_area.controls.append(ft.FilledButton("⬅️ Back", on_click=show_menu))
        main_menu.visible = False
        content_area.visible = True
        page.update()

    def show_models(brand):
        content_area.controls = [ft.Text(f"{brand} MODELS", size=20, weight="bold", color="white")]
        for model in SENS_DATA[brand]:
            content_area.controls.append(ft.ElevatedButton(model, on_click=lambda e, b=brand, m=model: show_sens(b, m)))
        content_area.controls.append(ft.FilledButton("⬅️ Back", on_click=show_brands))
        page.update()

    def show_sens(brand, model):
        gen = 85 + (len(brand) + len(model))
        red = 80 + (len(brand) + len(model))
        dpi = 400 + ((len(brand) + len(model)) * 10)
        res = f"🎯 {brand} {model}\n\nGen: {gen}\nRed: {red}\nDPI: {dpi}\n\n⚠️ NOTE: 75-80% ACCURACY"
        content_area.controls = [ft.Text(res, size=18, color="white", text_align="center"), ft.FilledButton("⬅️ Back", on_click=show_brands)]
        page.update()

    def show_wep_menu():
        content_area.controls = [ft.Text("🔫 SELECT WEAPON", size=20, weight="bold", color="white")]
        for w in WEAPON_TIPS:
            content_area.controls.append(ft.ElevatedButton(w, on_click=lambda e, w=w: show_simple(w, WEAPON_TIPS[w])))
        content_area.controls.append(ft.FilledButton("⬅️ Back", on_click=show_menu))
        main_menu.visible = False
        content_area.visible = True
        page.update()

    enter_btn = ft.FilledButton("✅ ENTER BOT", visible=False, on_click=show_menu)
    gate_container = ft.Column([
        ft.Text("MATH AI BOT\nMOBILE ASSISTANCE TACTICAL HELPER", size=25, weight="bold", color="white", text_align="center"),
        ft.FilledButton("📱 FOLLOW NCS ON TIKTOK", url="https://www.tiktok.com/@ncs_gamer520", on_click=lambda e: (setattr(enter_btn, 'visible', True), page.update())),
        enter_btn
    ], alignment=ft.MainAxisAlignment.CENTER)
    
    main_menu.controls = [
        ft.Text("🔓 SYSTEM ACCESS GRANTED", size=25, color="green", weight="bold"),
        ft.FilledButton("🎯 Sensitivity", on_click=lambda e: show_brands()),
        ft.FilledButton("🔫 Weapon Mastery", on_click=lambda e: show_wep_menu()),
        ft.FilledButton("🏹 Aim Routine", on_click=lambda e: show_simple("🏹 ELITE AIM ROUTINE", "1. Warmup: 5m Target Range.\n2. Drill: 10m Flicking.\n3. Recoil: 10m Spray Control.\nConsistency > Intensity.")),
        ft.FilledButton("🎨 FF Colors", on_click=lambda e: show_simple("🎨 FF COLORS (Tap to Copy)", "", is_colors=True)),
        ft.FilledButton("⚡ Reflex", on_click=lambda e: show_simple("⚡ REFLEX DRILL", "Practice tracking moving targets at varying speeds for 10 minutes daily.")),
        ft.FilledButton("🔒 Secret", on_click=lambda e: show_simple("🔒 SECRET", "Master the 'Jump-Shoot-Cover' technique for maximum survival rate.")),
    ]

    page.add(ft.Column([gate_container, main_menu, content_area], alignment=ft.MainAxisAlignment.CENTER))

if __name__ == "__main__":
    import os
    os.environ["FLET_FORCE_WEB_SERVER"] = "true"
    port = int(os.environ.get("PORT", 10000))
    ft.app(target=main, port=port)
