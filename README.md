# VibeVoice Codespace

**One-click setup for [Microsoft VibeVoice](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) text-to-speech.**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/rickbarraza/hf-vibevoice-codespace?quickstart=1)

## Quick Start

1. Click the badge above (or the green "Code" button → "Codespaces")
2. Wait ~4 minutes for setup
3. Run: `python quickstart.py`

## What Happens When It Works

When `quickstart.py` runs successfully, it:

1. **Downloads the model** (~2GB on first run)
2. **Generates speech** from a sample text
3. **Saves `output.wav`** in the current directory

### How to Listen

**In Codespaces:**
- Find `output.wav` in the file explorer (left sidebar)
- Right-click → **Download**
- Play locally on your machine

**Running Locally:**
- The file appears in your terminal's current directory
- Play with any audio app, or: `afplay output.wav` (Mac) / `aplay output.wav` (Linux)

## ⚠️ GPU Required

VibeVoice needs GPU for real-time inference. Here's what to expect:

| Environment | Result |
|-------------|--------|
| **Standard Codespaces (CPU)** | Model loads, but generation fails or takes forever |
| **GPU Codespaces** | Works! But requires special access |
| **Local Mac (Apple Silicon)** | Works with `--device mps` |
| **Local NVIDIA GPU** | Works with `--device cuda` |

**The Codespace proves the workflow works** — click, wait, code runs. The GPU limitation is an infrastructure gap, not a code problem.

## What's Included

- Pre-configured Python 3.11 environment
- All dependencies auto-installed (torch, transformers, etc.)
- GitHub Copilot extension ready
- Simple quickstart script

## Run Locally with Copilot

If Codespaces hits the GPU wall, copy this prompt into VS Code with GitHub Copilot:

```
Set up Microsoft VibeVoice text-to-speech on my machine.

Steps:
1. Clone https://github.com/microsoft/VibeVoice
2. Set up Python environment with uv or conda
3. Install with: pip install -e .
4. Run the demo with speaker Carter

Device: Use --device mps on Mac, --device cuda on NVIDIA.
Available voices: Carter, Davis, Emma, Frank, Grace, Mike
```

## Links

- [VibeVoice on HuggingFace](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)
- [Official VibeVoice Repo](https://github.com/microsoft/VibeVoice)
- [Model Paper](https://arxiv.org/abs/2508.19205)
