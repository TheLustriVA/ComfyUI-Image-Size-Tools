# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a ComfyUI node for setting image sizes based on AI model specifications. The project aims to create a resolution calculator that understands the technical constraints and optimal resolutions for different AI image generation models (SD 1.5, SDXL, Flux.1, HiDream, Wan2.1, Illustrious XL, SD3).

## Key Technical Concepts

### Model-Specific Resolution Constraints
- **SD 1.5**: Dimensions must be divisible by 8, native 512×512
- **SDXL**: Dimensions must be divisible by 64, uses bucket system targeting ~1 megapixel
- **Flux.1 Dev**: No strict divisibility requirements, native 1024×1024
- **SD3**: Dimensions must be divisible by 64, optimal around 1 megapixel
- **Illustrious XL**: Native 1536×1536, follows SDXL constraints

### Architecture Understanding
The tool needs to implement resolution validation and suggestion algorithms that:
1. Validate against model-specific divisibility factors
2. Suggest closest trained bucket resolutions for optimal quality
3. Calculate VRAM requirements based on resolution and model size
4. Handle aspect ratio preservation with proper rounding

## Development Commands

```bash
# Run the main application
python main.py

# Install dependencies (when they exist)
pip install -e .
```

## Critical Implementation Notes

- Resolution calculations must account for VAE downsampling factors
- SDXL uses a sophisticated 43-bucket resolution system - don't calculate arbitrary resolutions
- Always validate divisibility constraints before suggesting resolutions
- Consider VRAM scaling (roughly quadratic with resolution increase)
- Bucket systems solve the cropping problem by training on natural aspect ratios

## Reference Documentation

The `res_reference.md` file contains comprehensive technical specifications for all supported models, including mathematical formulas, bucket algorithms, and hardware requirements. This is the authoritative source for resolution constraints and optimal settings.