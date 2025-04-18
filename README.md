# 📦 airkoreapy

`airkoreapy` is an unofficial Python client for downloading air quality data from the [Air Korea](http://www.airkorea.or.kr) website. It helps researchers and developers easily fetch and process open air pollutant datasets provided by the Korea Environment Corporation (KECO).

---

## ✨ Features

- Download fixed monitoring station data (`download_fixed_data`)
- Support for multiple years and regions
- Clean interface for research and analysis

---

## 🚀 Installation

```bash
pip install airkoreapy
```

---

## 🧪 Example Usage
```python
from airkoreapy import AirKoreaPy

akp = AirKoreaPy()
akp.download_fixed_data(year=2021)
```

---

## 📊 Data Source
This package accesses publicly available air quality data from the Air Korea platform, operated by the Korea Environment Corporation.

If you use this data in a scientific publication, please include the following citation in the Data Availability section (e.g., for Springer journals):
```latex
\section*{Declarations}

\subsection*{Data Availability}
The air pollutant data were obtained from the Air Korea website (http://www.airkorea.or.kr, Open data) produced by the Institute of Health and Environment in Seoul City and managed by Korea Environment Corporation.
```
If you would like to mention the data acquisition process, you may optionally include the following:
> For the air quality measurement, an equipment produced by KIMOTO was mainly used, and the data acquired through each equipment was filtered to have accurate measurement values.
> For reference, see: https://doi.org/10.1007/s12145-024-01676-x

## ⚠️ Disclaimer
This package is not affiliated with or endorsed by Air Korea or Korea Environment Corporation. It is provided as an unofficial utility for research and educational purposes.

---
