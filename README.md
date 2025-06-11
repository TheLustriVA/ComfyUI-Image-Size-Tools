# ComfyUI Image Size Tool

A professional resolution calculator node pack for ComfyUI that provides model-specific, constraint-aware image dimensions for optimal AI generation quality.

## Why This Tool Exists

Most existing resolution tools either:
- Force you to manually enter width/height (error-prone)
- Ignore model-specific training constraints 
- Provide arbitrary resolutions that hurt generation quality
- Break your ComfyUI installation with complex dependencies

This tool solves the **resolution calculation problem** by providing curated, model-optimized presets based on actual training specifications and bucket systems.

## Features

✅ **Zero Dependencies** - No external libraries, no conflicts, no breakage  
✅ **Model-Aware** - Respects VAE constraints (div by 8/64) and training buckets  
✅ **Quality Focused** - Uses actual SDXL bucket resolutions, not arbitrary calculations  
✅ **Plug & Play** - Simple dropdowns, clean outputs, works immediately  
✅ **Professional** - Semantic versioning, proper documentation, stable API  

## Included Nodes

### SD 1.5 Resolution
- **8 optimized presets** from 512×512 to 912×512
- **Divisible by 8** constraint validation (VAE requirement)
- **Outputs:** `width`, `height`, `aspect_ratio`

### SDXL Resolution  
- **13 bucket-trained presets** targeting ~1 megapixel
- **Divisible by 64** constraint validation
- **Based on the 43-bucket training system** for optimal quality
- **Outputs:** `width`, `height`, `aspect_ratio`, `total_pixels`

### Flux.1 Dev Resolution
- **11 practical presets** from 1024×1024 to 2560×1440
- **No strict constraints** - more flexible than SD models
- **Hardware-optimized** for common use cases
- **Outputs:** `width`, `height`, `aspect_ratio`

## Installation

### Method 1: Git Clone (Recommended)
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/TheLustriVA/ComfyUI-Image-Size-Tool.git
```

### Method 2: ComfyUI Manager
1. Open ComfyUI Manager
2. Install from Git URL: `https://github.com/TheLustriVA/ComfyUI-Image-Size-Tool`

No additional dependencies to install - just restart ComfyUI.

## Usage

1. **Add Node**: Search for "Image Size Tool" in the node menu
2. **Select Resolution**: Choose from the dropdown (e.g., "1920×1080 (16:9) - Full HD")
3. **Connect Outputs**: Wire `width` and `height` to your Empty Latent Image node
4. **Generate**: Enjoy optimal quality with proper model constraints

### Example Workflow
```
[Flux.1 Dev Resolution] → [Empty Latent Image] → [KSampler] → [VAE Decode] → [Save Image]
     ↓ width=1920
     ↓ height=1080
```

## Why Model-Specific Resolutions Matter

### SD 1.5
- **Trained at 512×512** - quality degrades significantly when deviating
- **VAE constraint** - dimensions must be divisible by 8 or generation fails

### SDXL  
- **Bucket training system** - uses 43 specific resolutions targeting 1MP
- **Quality buckets** - arbitrary resolutions produce inferior results
- **VAE constraint** - dimensions must be divisible by 64

### Flux.1 Dev
- **Flexible architecture** - handles 0.2 to 2 megapixels effectively  
- **Hardware optimized** - common resolutions for practical generation

## Troubleshooting

### Nodes Don't Appear
```bash
cd ComfyUI/custom_nodes/ComfyUI-Image-Size-Tool
git pull
find . -name "__pycache__" -exec rm -rf {} +
```
Then restart ComfyUI.

### Import Errors (If Any)
This tool uses zero external dependencies and a single-file architecture specifically to avoid import issues. If you encounter problems, please open an issue.

## Technical Details

- **Architecture**: Single-file design with embedded constants
- **Dependencies**: None (Python stdlib only)
- **Compatibility**: ComfyUI (all recent versions)
- **Performance**: Instant loading, zero overhead

## Contributing

Issues and pull requests welcome! This tool aims to be the definitive resolution calculator for ComfyUI.

## License

MIT License - see LICENSE file for details.

---

**Generated with professional AI development practices**  
*No more resolution guesswork - just optimal image generation*