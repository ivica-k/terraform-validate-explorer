import json
import pathlib
import re
import sys
from typing import List


try:
    from PySide6.QtWidgets import (
        QMainWindow,
        QApplication,
        QFileDialog,
        QTreeWidgetItem,
        QMessageBox,
        QHeaderView,
        QDialog,
    )
except ImportError:
    sys.exit(
        "Missing PySide6. Install the requirements by running 'pip install -r requirements.txt'"
    )

import parser
from ui.ui import Ui_MainWindow
from ui import resources_rc
from ui.about import Ui_dialog_about

SEARCH_TYPES = ["contains", "does not contain", "regex"]

__version__ = "0.1.0"


class TerraformValidateExplorer(QMainWindow):
    def __init__(self):
        super(TerraformValidateExplorer, self).__init__()
        self.original_items = {
            "errors": [],
            "warnings": [],
        }
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.combo_search_type.insertItems(0, SEARCH_TYPES)

        self.file_path = ""
        self.file_contents = None
        self.ui.treeWidget.header().setSectionResizeMode(
            0, QHeaderView.ResizeToContents
        )

        self._setup_signals()
        self.ui.statusbar.showMessage(
            "Open a file generated with 'terraform validate -json' to continue."
        )

    def _setup_signals(self):
        self.ui.actionOpen.triggered.connect(self.load_initial_data)
        self.ui.line_filter.textChanged.connect(self.filter_items)
        self.ui.combo_search_type.currentIndexChanged.connect(self.filter_items)
        self.ui.actionAbout.triggered.connect(self._show_about)

    def _show_about(self):
        dlg = AboutDialog()
        dlg.exec()

    def get_file_contents(self):
        file_path = self.open_file()

        if file_path:
            with open(file_path, "r") as file:
                self.file_contents = json.load(file)

            if not parser.validation_file_valid(self.file_contents):
                QMessageBox.critical(
                    self, "Error", "This Terraform validate output file is invalid."
                )

            else:
                return True
        else:
            return False

    def filter_items(self):
        errors = []
        warnings = []

        line_text = str(self.ui.line_filter.text())
        search_type = self.ui.combo_search_type.currentText()
        function_name = search_type.replace(" ", "_")

        if search_type == "regex" and len(line_text) > 0:
            try:
                re.compile(line_text)
                errors, warnings = getattr(parser, f"filter_{function_name}")(
                    self.original_items, line_text
                )

            except re.error:
                # ignore invalid regex expressions; they happen while typing in the line edit
                # since each keystroke triggers this function
                pass

        elif len(line_text) > 3:
            errors, warnings = getattr(parser, f"filter_{function_name}")(
                self.original_items, line_text
            )

        self.fill_tree(
            items=TerraformValidateExplorer.contents_to_dict(
                {"errors": errors, "warnings": warnings}
            )
        )
        self.ui.statusbar.showMessage(
            f"Number of errors: {str(len(errors))}. Number of warnings: {str(len(warnings))}"
        )

        if self.file_contents and len(line_text) == 0:
            self.fill_tree(
                items=TerraformValidateExplorer.contents_to_dict(self.original_items)
            )

    @staticmethod
    def contents_to_dict(data: dict) -> List[QTreeWidgetItem]:
        items = []

        for _type in data.keys():
            item = QTreeWidgetItem([_type])

            if len(data[_type]) == 0:
                child = QTreeWidgetItem([f"No {_type}."])
                item.addChild(child)
            else:
                for value in data[_type]:
                    text = value.get("address") or value.get("detail")
                    filename = value.get("range").get("filename")
                    line_number = value.get("range").get("start").get("line")
                    child = QTreeWidgetItem([text, filename, str(line_number)])
                    item.addChild(child)

            items.append(item)

        return items

    def load_initial_data(self):
        if self.get_file_contents():
            self.original_items = parser.get_initial_data(self.file_contents)
            items = TerraformValidateExplorer.contents_to_dict(self.original_items)

            # save for future use to avoid reading the file again
            # self.original_items = data

            self.fill_tree(items)
            num_errors = len(self.original_items.get("errors"))
            num_warnings = len(self.original_items.get("warnings"))

            self.ui.statusbar.showMessage(
                f"Number of errors: {str(num_errors)}. Number of warnings: {str(num_warnings)}"
            )

    def fill_tree(self, items: list = None):
        if not items:
            items = {}

        tree = self.ui.treeWidget
        tree.setHeaderLabels(["Resource address", "Filename", "Line"])
        tree.clear()

        tree.insertTopLevelItems(0, items)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            str(pathlib.Path.home()),
            "JSON (*.json)",
        )

        return file_path


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.about = Ui_dialog_about()
        self.about.setupUi(self)

        self.about.label_title.setText(
            f"<b>Terraform validate explorer v{__version__}</b>"
        )
        self.about.label_text.setText(
            """Easily filter, search and explore the output of 'terraform validate -json'.<br /><br />
            
<a href="https://github.com/ivica-k/terraform-validate-explore">Website</a>
"""
        )

        self.about.btn_ok.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("terraform-validate-explorer")
    app.setApplicationDisplayName("terraform-validate-explorer")
    tfve = TerraformValidateExplorer()
    tfve.show()
    sys.exit(app.exec())
