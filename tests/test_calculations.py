import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_dcf_independent_math_and_workbook(tmp_path):
    dcf = load("dcf", "dcf-modeling/scripts/dcf.py")
    model = json.loads((ROOT / "dcf-modeling/examples/model.json").read_text())
    model["scenarios"] = {
        s: {"ufcf": [100], "wacc": 0.10, "terminal_growth": 0}
        for s in ("base", "bull", "bear")
    }
    assert dcf.calculate(model)["results"]["base"]["value_per_share"] == pytest.approx(
        9
    )
    p = tmp_path / "DCF.xlsx"
    dcf.workbook(model, p)
    from openpyxl import load_workbook

    wb = load_workbook(p)
    assert wb.active["B7"].value.startswith("=")
    assert wb.active["B8"].value == pytest.approx(9)
    model["scenarios"]["base"]["terminal_growth"] = 0.10
    with pytest.raises(ValueError):
        dcf.calculate(model)


def test_technical_known_linear_and_flat():
    technical = load("technical", "technical-analysis/scripts/technical.py")
    df = pd.DataFrame(
        {
            "date": pd.bdate_range("2024-01-01", periods=300),
            "adjusted_close": np.arange(100, 400),
            "volume": 1000,
        }
    )
    out = technical.analyze(df)
    assert (
        out["rsi14"] == 100
        and out["sma50"] == pytest.approx(374.5)
        and out["sma200"] == pytest.approx(299.5)
    )
    df["adjusted_close"] = 100
    assert technical.analyze(df)["rsi14"] == 50
    with pytest.raises(ValueError):
        technical.analyze(df.head(200))
