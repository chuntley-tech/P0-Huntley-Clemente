import importlib.util
import json
from pathlib import Path

SRC_FILE = Path(__file__).resolve().parent.parent / "src" / "system_info.py"

spec = importlib.util.spec_from_file_location("system_info", SRC_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_collect_system_info_keys():
    info = mod.collect_system_info()
    expected = {
        "sistema_operativo",
        "arquitectura",
        "version_python",
        "modelo_procesador",
        "nucleos_fisicos",
        "procesadores_logicos",
        "memoria_ram_total_bytes",
        "memoria_ram_total_gb",
    }
    assert set(info) == expected


def test_collect_system_info_values():
    info = mod.collect_system_info()
    assert info["nucleos_fisicos"] >= 1
    assert info["procesadores_logicos"] >= info["nucleos_fisicos"]
    assert info["memoria_ram_total_bytes"] > 0


def test_main_creates_json(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "DATA_DIR", tmp_path)
    monkeypatch.setattr(mod, "OUTPUT_FILE", tmp_path / "system_info.json")
    assert mod.main() == 0
    output = tmp_path / "system_info.json"
    assert output.exists()
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["version_python"] == mod.collect_system_info()["version_python"]
