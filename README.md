https://orcid.org/my-orcid?orcid=0009-0004-1872-1153
https://doi.org/10.5281/zenodo.20567157
-----------------
# GRA-ASI-Metric-Space / Пространство метрик GRA для ASI

[English](#english) | [Русский](#русский)

<a name="english"></a>
## English

### Overview
This repository implements the formal metric space for **GRA (Geometric Recursive Analytics) ASI** — a self-improving AI agent that maintains its integrity by minimizing **foam** `Φ` across hierarchical levels. The metrics are **impossible to specify explicitly** yet **executable** via the nullification operator. This repository provides a working implementation of foam computation, hierarchical stability rank `N`, swarm coherence, and a frontend demo.

### Key Concepts
- **Foam** `Φ` – measure of chaos, inconsistency, or instability.
- **Nullification operator** `𝒩` – reduces foam when moving up the hierarchy.
- **Stability conditions**: `Φ=0`, `dΦ/dh=0`, `d²Φ/dh²>0`.
- **Rank N** – minimal order where second difference becomes positive.
- **Swarm foam** – coherence among multiple agents; leader selection formula.

### Installation
```bash
git clone https://github.com/yourname/GRA-ASI-Metric-Space.git
cd GRA-ASI-Metric-Space
pip install -r requirements.txt
```

### Usage
Run demo:

```bash
python examples/demo.py
```

Run tests:

```bash
python -m pytest tests/
```

Start frontend:

```bash
cd frontend && python -m http.server 8000
# then open http://localhost:8000
```

### Paper
The theoretical foundations are in `paper/paper.tex` (compile with pdflatex).

### License
MIT

<a name="русский"></a>

## Русский

### Обзор
Репозиторий реализует формальное пространство метрик для GRA-ASI — самоулучшающегося ИИ-агента, сохраняющего целостность за счёт минимизации пены Φ на иерархических уровнях. Метрики невозможно задать явно, но можно выполнить через оператор обнуления. Репозиторий содержит работающую реализацию вычисления пены, иерархического ранга стабильности N, роевой когерентности и фронтенд-демонстрацию.

### Ключевые понятия
- **Пена** Φ – мера хаоса, противоречий, нестабильности.
- **Оператор обнуления** 𝒩 – уменьшает пену при подъёме по иерархии.
- **Условия стабильности**: Φ=0, dΦ/dh=0, d²Φ/dh²>0.
- **Ранг N** – минимальный порядок, на котором вторая разность становится положительной.
- **Роевая пена** – когерентность множества агентов; формула выбора лидера.

### Установка
```bash
git clone https://github.com/yourname/GRA-ASI-Metric-Space.git
cd GRA-ASI-Metric-Space
pip install -r requirements.txt
```

### Использование
Запуск демо:

```bash
python examples/demo.py
```

Тесты:

```bash
python -m pytest tests/
```

Фронтенд:

```bash
cd frontend && python -m http.server 8000
# затем http://localhost:8000
```

### Статья
Теоретические основы в `paper/paper.tex` (компиляция pdflatex).

### Лицензия
MIT
