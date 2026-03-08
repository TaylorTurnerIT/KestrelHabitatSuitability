# Kestrel Habitat Suitability Analysis

This repository contains data, scripts, and workspaces for the American Kestrel Habitat Suitability Analysis project.

## Repository Structure

For a detailed breakdown of the directory structure and what belongs where, please refer to [GEMINI.md](GEMINI.md).

## Environment Setup

This project requires the `arcpy` module, meaning all scripts must run within the built-in ArcGIS Pro Python environment. We use [uv](https://github.com/astral-sh/uv) to automatically manage this. A `.python-version` file at the root of the repository points `uv` directly to the correct ArcGIS Python executable.

### Running Scripts

To execute any Python script within the correct ArcGIS environment, use `uv run`:

```bash
uv run scripts/process_NLCD.py
```

**Important Note for WSL/Linux Users:**
Because ArcGIS Pro is a Windows application, our configured Python environment path (`C:\Program Files\...`) is a Windows path. If you execute commands from inside a WSL terminal, the Linux `uv` binary will fail. You MUST explicitly call the Windows binary (`uv.exe`) and use forward slashes for the script path:

```bash
uv.exe run scripts/process_NLCD.py
```
