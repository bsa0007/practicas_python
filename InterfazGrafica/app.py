# -*- coding: utf-8 -*-
import sys
from PyQt6.QtWidgets import ( # pyright: ignore[reportMissingImports]
    QApplication, QWidget, QLabel, QComboBox, QSlider,
    QHBoxLayout, QVBoxLayout, QPushButton
)
from PyQt6.QtGui import QPixmap, QFont, QPainter, QColor, QMovie # pyright: ignore[reportMissingImports]
from PyQt6.QtCore import Qt # pyright: ignore[reportMissingImports]


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Educativa - Juegos de Estrategia")
        self.setFixedSize(1300, 750)

        # ---------------- Fondo madera ----------------
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("assets/madera.png").scaled(self.width(), self.height()))
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.lower()

        # Layout raíz
        root = QHBoxLayout(self)
        root.setContentsMargins(20, 20, 20, 20)

        # ---------------- Panel Izquierdo ----------------
        left_panel = QVBoxLayout()
        left_panel.setSpacing(20)

        # Selector de juego
        lbl_sel = QLabel("🎮 Selecciona Juego:")
        lbl_sel.setFont(QFont("Comic Sans MS", 16, QFont.Weight.Bold))
        self.cmb_juego = QComboBox()
        self.cmb_juego.setFont(QFont("Comic Sans MS", 14))
        self.cmb_juego.addItems(["Siete y Media", "Uno", "Póker"])
        self.cmb_juego.currentTextChanged.connect(self.mostrar_preview)
        left_panel.addWidget(lbl_sel)
        left_panel.addWidget(self.cmb_juego)

        # Botón de área de juego
        self.btn_area = QPushButton("🌍 Seleccionar Área de Juego")
        self.btn_area.setFont(QFont("Comic Sans MS", 14))
        left_panel.addWidget(self.btn_area)

        # Previsualización dentro de la tablet
        lbl_prev = QLabel("📺 Previsualización:")
        lbl_prev.setFont(QFont("Comic Sans MS", 16, QFont.Weight.Bold))
        left_panel.addWidget(lbl_prev)

        # Tablet
        self.lbl_tablet = QLabel()
        self.lbl_tablet.setPixmap(QPixmap("assets/tablet.png").scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio))
        self.lbl_tablet.setFixedSize(400, 300)
        self.lbl_tablet.setStyleSheet("background: transparent;")
        left_panel.addWidget(self.lbl_tablet, alignment=Qt.AlignmentFlag.AlignCenter)

        # Pantalla de la tablet
        self.lbl_preview = QLabel(self.lbl_tablet)
        self.lbl_preview.setGeometry(40, 40, 320, 220)
        self.lbl_preview.setStyleSheet("background: black;")
        self.lbl_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Crupier animado (gif)
        self.lbl_crupier = QLabel()
        movie = QMovie("assets/crupier.gif")
        self.lbl_crupier.setMovie(movie)
        movie.start()
        left_panel.addWidget(self.lbl_crupier, alignment=Qt.AlignmentFlag.AlignCenter)

        # Bocadillo del crupier
        self.lbl_dialogo = QLabel("👋 ¡Bienvenido! Elige un juego para empezar.")
        self.lbl_dialogo.setFont(QFont("Comic Sans MS", 13))
        self.lbl_dialogo.setWordWrap(True)
        self.lbl_dialogo.setStyleSheet(
            "background: #FFF8DC; border: 2px solid black; border-radius: 10px; padding: 8px;"
        )
        left_panel.addWidget(self.lbl_dialogo, alignment=Qt.AlignmentFlag.AlignCenter)

        root.addLayout(left_panel, 1)

        # ---------------- Panel Derecho (Pergamino) ----------------
        right_panel = QVBoxLayout()
        right_panel.setSpacing(20)

        self.lbl_perg = QLabel()
        self.perg_pix = QPixmap("assets/pergamino.png").scaled(
            750, 650, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        self.lbl_perg.setPixmap(self.perg_pix)
        self.lbl_perg.setFixedSize(self.perg_pix.size())
        right_panel.addWidget(self.lbl_perg, alignment=Qt.AlignmentFlag.AlignCenter)

        # Sliders de perfil
        self.sliders = {
            "Tight / Loose": QSlider(Qt.Orientation.Horizontal, self.lbl_perg),
            "Passive / Aggressive": QSlider(Qt.Orientation.Horizontal, self.lbl_perg),
        }
        y = 220
        for slider in self.sliders.values():
            slider.setRange(0, 100)
            slider.setValue(50)
            slider.valueChanged.connect(self.update_pergamino)
            slider.setGeometry(250, y, 250, 20)
            y += 70

        root.addLayout(right_panel, 2)

        # Config inicial
        self.mostrar_preview()
        self.update_pergamino()

    # ---------------- PREVISUALIZACIÓN ----------------
    def mostrar_preview(self):
        juego = self.cmb_juego.currentText()
        if juego == "Siete y Media":
            base = QPixmap("assets/siete_media.png")
            self.lbl_dialogo.setText("😃 ¡Siete y Media! Calcula bien y no te pases.")
        elif juego == "Uno":
            base = QPixmap("assets/uno.png")
            self.lbl_dialogo.setText("🎨 ¡UNO! Usa bien tus cartas especiales.")
        else:
            base = QPixmap("assets/poker.png")
            self.lbl_dialogo.setText("🃏 ¡Póker! Calma y buenas decisiones.")

        base = base.scaled(
            self.lbl_preview.width(), self.lbl_preview.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.lbl_preview.setPixmap(base)
        self.update_pergamino()

    # ---------------- PERGAMINO ----------------
    def update_pergamino(self):
        tight_val = self.sliders["Tight / Loose"].value()
        aggr_val = self.sliders["Passive / Aggressive"].value()
        juego = self.cmb_juego.currentText()

        # --- Probabilidades y acción dinámicas ---
        if juego == "Siete y Media":
            menos = max(10, 70 - aggr_val)
            exacto = 10
            mas = max(10, aggr_val)
            total = menos + exacto + mas
            self.probabilidades = {
                "Menos de 7.5": int(menos * 100 / total),
                "Exacto 7.5": int(exacto * 100 / total),
                "Más de 7.5": int(mas * 100 / total),
            }
            if aggr_val > 70:
                accion = "✅ Pedir carta"
                just = "📌 Eres arriesgado, puedes ganar más."
            elif tight_val > 70:
                accion = "✅ Plantarse"
                just = "📌 Prefieres no arriesgar, es seguro."
            else:
                accion = "✅ Decidir"
                just = "📌 Buen balance entre riesgo y calma."

        elif juego == "Uno":
            robar = max(10, 70 - aggr_val)
            especial = max(10, aggr_val)
            uno_carta = 30
            total = robar + especial + uno_carta
            self.probabilidades = {
                "Robar carta": int(robar * 100 / total),
                "Carta especial": int(especial * 100 / total),
                "Quedarte con 1": int(uno_carta * 100 / total),
            }
            if aggr_val > 70:
                accion = "✅ Jugar especial"
                just = "📌 Perfecto para un +2 o +4."
            elif tight_val > 70:
                accion = "✅ Robar carta"
                just = "📌 Prefieres esperar algo mejor."
            else:
                accion = "✅ Descartar normal"
                just = "📌 Balance entre ataque y defensa."

        else:  # Póker
            mejorar = max(10, 70 - tight_val)
            ganar = max(10, aggr_val)
            rival = max(10, tight_val)
            total = mejorar + ganar + rival
            self.probabilidades = {
                "Mejorar mano": int(mejorar * 100 / total),
                "Ganar": int(ganar * 100 / total),
                "Rival fuerte": int(rival * 100 / total),
            }
            if aggr_val > 70:
                accion = "✅ Subir apuesta"
                just = "📌 Tu agresividad presiona al rival."
            elif tight_val > 70:
                accion = "✅ Retirarse"
                just = "📌 Mejor esperar una buena mano."
            else:
                accion = "✅ Ver apuesta"
                just = "📌 Mantienes calma y presión."

        # --- Dibujar pergamino ---
        img = self.perg_pix.copy()
        p = QPainter(img)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Título
        p.setPen(QColor("black"))
        p.setFont(QFont("Comic Sans MS", 18, QFont.Weight.Bold))
        p.drawText(img.width()//2 - 120, 140, "📊 Perfil del jugador")

        # Sliders centrados
        p.setFont(QFont("Comic Sans MS", 14))
        y = 200
        for text, slider in self.sliders.items():
            val = slider.value()
            x = img.width()//2 - 150
            p.drawText(x, y - 10, f"{text}: {val}%")
            p.setPen(QColor("#8B5A2B"))
            p.drawRect(x, y, 300, 20)
            p.fillRect(x, y, int(3.0 * val), 20, QColor("#4FC3F7"))
            slider.setGeometry(x, y, 300, 20)
            y += 70

        # Probabilidades centradas
        p.setFont(QFont("Comic Sans MS", 14, QFont.Weight.Bold))
        p.drawText(img.width()//2 - 100, y + 20, "📈 Probabilidades")
        p.setFont(QFont("Comic Sans MS", 12))
        colors = [QColor("#FFB74D"), QColor("#81C784"), QColor("#64B5F6")]
        y += 60
        for i, (nombre, valor) in enumerate(self.probabilidades.items()):
            x = img.width()//2 - 150
            p.setPen(QColor("black"))
            p.drawText(x, y, f"{nombre}: {valor}%")
            barra_x = img.width()//2 + 50
            p.setPen(QColor("#8B5A2B"))
            p.drawRect(barra_x, y - 15, 200, 20)
            p.fillRect(barra_x, y - 15, int(2.0 * valor), 20, colors[i % len(colors)])
            y += 40

        # Acción y justificación debajo de probabilidades
        p.setFont(QFont("Comic Sans MS", 14, QFont.Weight.Bold))
        p.setPen(QColor("darkblue"))
        p.drawText(img.width()//2 - 100, y + 40, accion)

        p.setFont(QFont("Comic Sans MS", 12))
        p.setPen(QColor("black"))
        p.drawText(img.width()//2 - 100, y + 70, just)

        p.end()
        self.lbl_perg.setPixmap(img)

        # --- Diálogo corto del crupier ---
        if juego == "Siete y Media":
            if aggr_val > 70:
                self.lbl_dialogo.setText("😁 Arriesgas mucho, cuidado.")
            elif tight_val > 70:
                self.lbl_dialogo.setText("😎 Muy prudente, seguro.")
            else:
                self.lbl_dialogo.setText("🤔 Buen equilibrio.")
        elif juego == "Uno":
            if aggr_val > 70:
                self.lbl_dialogo.setText("🔥 Usa un +4 ahora.")
            elif tight_val > 70:
                self.lbl_dialogo.setText("😅 Robas demasiado.")
            else:
                self.lbl_dialogo.setText("🎨 Juego variado, ¡bien!")
        elif juego == "Póker":
            if aggr_val > 70:
                self.lbl_dialogo.setText("⚠️ No vayas all-in rápido.")
            elif tight_val > 70:
                self.lbl_dialogo.setText("🧘 Paciente, buena lectura.")
            else:
                self.lbl_dialogo.setText("🃏 Estilo mixto, confundes.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec())
