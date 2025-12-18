# VibeVoice Codespace

**One-click setup for [Microsoft VibeVoice](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) text-to-speech.**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/rickbarraza/hf-vibevoice-codespace?quickstart=1)

## Quick Start

1. Click the badge above (or the green "Code" button → "Codespaces")
2. Wait ~4 minutes for setup
3. Run: `python quickstart.py`

## What's Included

- Pre-configured Python 3.11 environment
- All dependencies auto-installed (torch, transformers, etc.)
- GitHub Copilot extension ready
- Simple quickstart script

## Requirements

⚠️ **Note:** VibeVoice requires GPU for real-time inference. Standard Codespaces use CPU, which will be slow. For best results:
- Use a local machine with GPU (NVIDIA CUDA or Apple Silicon MPS)
- Or request GPU-enabled Codespaces if available

## Run Locally with Copilot

Copy this prompt into VS Code with GitHub Copilot:

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
