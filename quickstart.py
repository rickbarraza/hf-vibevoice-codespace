#!/usr/bin/env python3
"""
VibeVoice Quickstart - From zero to audio in 2 minutes.

Run this in GitHub Codespaces or locally:
  python quickstart.py

That's it. Audio comes out.
"""

import os
import sys
from pathlib import Path

# Detect environment
def get_device():
    """Auto-detect the best available device."""
    import torch
    if torch.cuda.is_available():
        return "cuda"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"  # Apple Silicon
    else:
        return "cpu"

def main():
    print("🎤 VibeVoice Quickstart")
    print("=" * 40)
    
    # Check for required packages
    try:
        import torch
        import torchaudio
        from transformers import AutoModel, AutoTokenizer
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("   Run: pip install torch torchaudio transformers accelerate soundfile")
        sys.exit(1)
    
    device = get_device()
    print(f"📱 Device: {device}")
    
    # The text we'll synthesize
    text = """
    Hello! This is VibeVoice, a real-time text-to-speech model from Microsoft.
    You're hearing this because you clicked a button and it just worked.
    That's the goal: from HuggingFace to hearing audio in under two minutes.
    """
    
    print(f"📝 Text: {text[:60]}...")
    print("⏳ Loading model (first run downloads ~2GB)...")
    
    try:
        # Load model
        model_name = "microsoft/VibeVoice-Realtime-0.5B"
        
        # Note: VibeVoice has a custom architecture, so we need to trust remote code
        model = AutoModel.from_pretrained(
            model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16 if device != "cpu" else torch.float32
        )
        model = model.to(device)
        model.eval()
        
        print("✅ Model loaded!")
        print("🎵 Generating audio...")
        
        # Generate audio
        with torch.no_grad():
            # VibeVoice uses a specific generation method
            # This is simplified - real usage would use the full demo script
            output = model.generate(
                text=text,
                speaker_name="Carter",  # Default speaker
            )
        
        # Save audio
        output_path = Path("output.wav")
        if hasattr(output, "save"):
            output.save(str(output_path))
        else:
            import soundfile as sf
            sf.write(str(output_path), output.cpu().numpy(), 24000)
        
        print(f"✅ Audio saved to: {output_path.absolute()}")
        print()
        print("🎉 Success! You just generated speech with VibeVoice.")
        print()
        print("Next steps:")
        print("  • Play output.wav to hear the result")
        print("  • Edit the 'text' variable and run again")
        print("  • Try different speakers: Carter, Nova, Aria, etc.")
        print()
        print("📚 Full docs: https://github.com/microsoft/VibeVoice")
        
    except Exception as e:
        print(f"⚠️  Generation failed: {e}")
        print()
        print("This quickstart uses simplified code.")
        print("For the full experience, clone the VibeVoice repo:")
        print("  git clone https://github.com/microsoft/VibeVoice")
        print("  cd VibeVoice && pip install -e .")
        print("  python demo/realtime_model_inference_from_file.py --speaker_name Carter")
        sys.exit(1)

if __name__ == "__main__":
    main()
