import sys
import os
from PyQt6 .QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence

class AferitanBrowser(QMainWindow):
    def __init__(self):
        super(AferitanBrowser, self).__init__()

        self.setWindowTitle("Aferitan Pro")
        
        # --- ИКОНКА ВЕЗДЕ ---
        self.icon_path = os.path.join(os.path.dirname(__file__), "logo.ico")
        if os.path.exists(self.icon_path):
            self.setWindowIcon(QIcon(self.icon_path))
        
        self.showMaximized()

        # Темная тема
        self.setStyleSheet("""
            QMainWindow { background-color: #1a1a1a; }
            QToolBar { background-color: #2d2d2d; border: none; padding: 5px; spacing: 8px; }
            QLineEdit { background-color: #3d3d3d; color: white; border-radius: 10px; padding: 5px; }
            QPushButton { background-color: #444; color: white; border-radius: 5px; padding: 5px 12px; }
            QPushButton:hover { background-color: #555; }
            QComboBox { background-color: #444; color: white; border-radius: 5px; padding: 3px; }
        """)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        navbar = QToolBar()
        self.addToolBar(navbar)

        # Навигация
        for text, slot in [("←", self.browser.back), ("→", self.browser.forward), ("↻", self.browser.reload)]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            navbar.addWidget(btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # --- ЗАКЛАДКИ ---
        self.bookmarks = QComboBox()
        self.bookmarks.addItem("Bookmarks ⭐")
        self.bookmarks.addItems(["YouTube", "GitHub", "Yandex", "Xtechsport it", "vk", "tiktok", "minecraft", "steam"])
        self.bookmarks.currentIndexChanged.connect(self.open_bookmark)
        navbar.addWidget(self.bookmarks)

        # Зум
        self.zoom_btn = QPushButton("100%")
        self.zoom_btn.clicked.connect(lambda: self.browser.setZoomFactor(1.0))
        navbar.addWidget(self.zoom_btn)

        self.browser.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))

        # Горячие клавиши
        QShortcut(QKeySequence("F11"), self).activated.connect(self.toggle_fs)

    def navigate_to_url(self):
        q = self.url_bar.text()
        if "." not in q: url = "https://www.google.com/search?q=" + q
        elif not q.startswith('http'): url = 'http://' + q
        else: url = q
        self.browser.setUrl(QUrl(url))

    def open_bookmark(self):
        site = self.bookmarks.currentText()
        urls = {
            "YouTube": "https://www.youtube.com",
            "GitHub": "https://github.com",
            "Yandex": "https://yandex.ru",
            "Xtechsport it": "https://xtechsport.it",
            "vk": "https://vk.ru",
            "tiktok": "tiktok.com",
            "minecraft": "https://www.minecraft.net/ru-ru",
            "steam": "https://store.steampowered.com/"  
        }
        if site in urls:
            self.browser.setUrl(QUrl(urls[site]))

    def toggle_fs(self):
        if self.isFullScreen(): self.showMaximized()
        else: self.showFullScreen()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("logo.ico")) # Дублируем иконку для панели задач
window = AferitanBrowser()
window.show()
sys.exit(app.exec())
