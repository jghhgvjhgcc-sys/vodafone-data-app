# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock
import threading

KV = r"""
#:import dp kivy.metrics.dp
BoxLayout:
    orientation: "vertical"
    canvas.before:
        Color:
            rgba: (0.055, 0.055, 0.075, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        size_hint_y: None
        height: dp(76)
        padding: dp(18), dp(10)
        canvas.before:
            Color:
                rgba: (0.72, 0.04, 0.10, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: "vertical"
        Label:
            text: "بيانات فودافون"
            bold: True
            font_size: "24sp"
            color: (1,1,1,1)
        Label:
            text: "واجهة أندرويد"
            font_size: "12sp"
            color: (1,0.85,0.87,1)

    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: dp(20)
            spacing: dp(14)

            Label:
                text: "أدخل بياناتك"
                size_hint_y: None
                height: dp(36)
                font_size: "20sp"
                bold: True
                color: (1,1,1,1)
                halign: "right"
                text_size: self.size

            Label:
                text: "استخدم حسابك الشخصي فقط. لا تشارك كلمة المرور أو رموز الدخول مع أي شخص."
                size_hint_y: None
                height: self.texture_size[1] + dp(18)
                text_size: self.width, None
                halign: "right"
                color: (0.85,0.82,0.83,1)

            TextInput:
                id: phone
                hint_text: "رقم الهاتف"
                multiline: False
                input_filter: "int"
                size_hint_y: None
                height: dp(52)
                padding: dp(12)
                background_color: (0.14,0.14,0.17,1)
                foreground_color: (1,1,1,1)
                hint_text_color: (0.65,0.65,0.68,1)
                cursor_color: (1,0.2,0.25,1)

            TextInput:
                id: password
                hint_text: "كلمة المرور"
                password: True
                multiline: False
                size_hint_y: None
                height: dp(52)
                padding: dp(12)
                background_color: (0.14,0.14,0.17,1)
                foreground_color: (1,1,1,1)
                hint_text_color: (0.65,0.65,0.68,1)
                cursor_color: (1,0.2,0.25,1)

            Button:
                text: "بدء"
                size_hint_y: None
                height: dp(54)
                background_normal: ""
                background_color: (0.78,0.04,0.12,1)
                color: (1,1,1,1)
                bold: True
                font_size: "18sp"
                on_release: app.start_request()

            Label:
                id: status
                text: "جاهز"
                size_hint_y: None
                height: dp(32)
                color: (1,0.35,0.4,1)
                halign: "right"
                text_size: self.size

            Label:
                text: "النتائج"
                size_hint_y: None
                height: dp(34)
                font_size: "18sp"
                bold: True
                color: (1,1,1,1)
                halign: "right"
                text_size: self.size

            TextInput:
                id: results
                text: "ستظهر النتائج هنا بعد ربط التطبيق بواجهة رسمية ومصرّح بها."
                readonly: True
                size_hint_y: None
                height: dp(230)
                padding: dp(12)
                background_color: (0.10,0.10,0.13,1)
                foreground_color: (0.92,0.92,0.94,1)
                hint_text_color: (0.65,0.65,0.68,1)

            Label:
                text: "تنبيه: هذه نسخة واجهة أولية؛ لم يتم تفعيل تسجيل الدخول أو استدعاء واجهات فودافون."
                size_hint_y: None
                height: self.texture_size[1] + dp(18)
                text_size: self.width, None
                color: (0.75,0.72,0.73,1)
                halign: "right"
"""

class VodafoneApp(App):
    def build(self):
        self.title = "بيانات فودافون"
        if platform != "android":
            Window.size = (390, 780)
        return Builder.load_string(KV)

    def start_request(self):
        phone = self.root.ids.phone.text.strip()
        password = self.root.ids.password.text
        if not phone:
            self.root.ids.status.text = "اكتب رقم الهاتف أولاً."
            return
        if not password:
            self.root.ids.status.text = "اكتب كلمة المرور."
            return

        # Intentionally no credentials are sent or stored in this starter UI.
        self.root.ids.status.text = "الواجهة جاهزة، لكن الربط بالخدمة الرسمية غير مفعّل."
        self.root.ids.results.text = (
            "لم يتم إرسال بيانات الدخول أو حفظها.\\n"
            "لإكمال الوظائف، اربط التطبيق بواجهة رسمية ومصرّح بها، "
            "مع تجنّب تخزين كلمة المرور أو رموز الدخول."
        )
        self.root.ids.password.text = ""

if __name__ == "__main__":
    VodafoneApp().run()
