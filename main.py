"""
Application entry point.

Initializes the Universal Unit Converter,
loads the configured startup page and
starts the desktop application.
"""

from src.ui.desktop.app import UniversalUnitConverterApp

# Create the main application window.
app = UniversalUnitConverterApp()

# Open the user's configured startup page.
startup_page = (
    app.settings_manager
    .load_settings()
    .get("startup_page", "Converter")
)

app.show_page(
    app.pages[startup_page]
)

# Start the Tkinter event loop.
app.mainloop()