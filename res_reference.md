# Technical Specifications for AI Image/Video Generation Models: Resolution and Aspect Ratio Guide

## Stable Diffusion 1.5

### Training specifications and constraints
- **Native Training Resolution**: 512×512 pixels
- **VAE Downsampling Factor**: 8x (reduces images to latent space of H/8 × W/8)
- **Resolution Constraint**: All dimensions must be divisible by 8
- **Mathematical Formula**: `(width % 8 == 0) and (height % 8 == 0)`

### Recommended resolutions for optimal quality
| Aspect Ratio | Resolution | Use Case |
|--------------|------------|----------|
| 1:1 | 512×512, 768×768 | Square images |
| 2:3 | 512×768 | Portrait |
| 3:2 | 768×512 | Landscape |
| 4:3 | 768×576 | Standard format |
| 16:9 | 912×512 | Widescreen |
| 9:16 | 512×912 | Mobile/tall |

### Technical constraints
- Model performs best at native 512×512 resolution
- Quality significantly degrades when deviating from training resolution
- 1.3 billion parameters with CLIP ViT-L/14 text encoder
- Minimum VRAM: 4GB (limited), Recommended: 8GB

## SDXL (Stable Diffusion XL)

### Advanced bucket resolution system
SDXL uses a sophisticated multi-aspect ratio training approach with 43 official bucket resolutions ranging from 512×2048 to 2048×512, all targeting approximately 1 megapixel (1,048,576 pixels).

### Key technical specifications
- **Native Resolution**: 1024×1024 pixels
- **Resolution Constraint**: Dimensions must be divisible by 64
- **Mathematical Formula**: `(width % 64 == 0) and (height % 64 == 0)`
- **Pixel Target**: Total pixels ≈ 1,048,576
- **Aspect Ratio Range**: 0.25 ≤ aspect_ratio ≤ 4.0

### Resolution calculation algorithm

```python
def calculate_sdxl_resolution(aspect_ratio):
    target_pixels = 1048576  # ~1 megapixel
    center_point = 1024
    
    width = int(center_point * (aspect_ratio**0.5))
    height = int(target_pixels / width)
    width = width - (width % 64)  # Round to nearest 64
    height = height - (height % 64)
    return width, height
```

### Most commonly used resolutions

| Aspect Ratio | Resolution | Pixels |
|--------------|------------|--------|
| 1:1 | 1024×1024 | 1,048,576 |
| 7:9 | 896×1152 | 1,032,192 |
| 9:7 | 1152×896 | 1,032,192 |
| 7:4 | 1344×768 | 1,032,192 |
| 4:7 | 768×1344 | 1,032,192 |

### Performance specifications

- 3.5 billion parameters (3x larger than SD 1.5)
- Dual text encoders: OpenCLIP-ViT/G + CLIP-ViT/L
- Minimum VRAM: 4GB (extremely limited), Recommended: 12GB+
- Novel conditioning: size, crop, and aesthetic parameters

## Flux.1 Dev

### Flexible architecture specifications

- **Native Resolution**: 1024×1024 pixels
- **Training Range**: 0.2 to 2 megapixels
- **Architecture**: 12 billion parameter rectified flow transformer
- **Key Feature**: No specific divisibility requirements (more flexible than SD models)

### Recommended resolutions

- 1024×1024 (standard, 20-second render)
- 1920×1080 (Full HD, optimal balance)
- 1536×640 (ultrawide/banner format)
- 1600×1600 (high detail, 35-40 second render)

### Technical considerations

- Effective resolution range: 512×512 to 2560×1440 (hardware dependent)
- RTX 3090: Best at 1920×1080 or lower
- RTX 4090: Can handle up to 2560×1440
- 4× slower than SDXL for equivalent resolutions
- Uses rotary positional embeddings for hardware efficiency

## HiDream-I1

### Model specifications

- **Native Resolution**: 1024×1024 pixels
- **Architecture**: 17 billion parameter Mixture of Experts (MoE) with Sparse Diffusion Transformer
- **Standard Output**: 1024×1024 pixels
- **Resolution Flexibility**: Follows SDXL-style constraints

### Hardware requirements

- Requires NVIDIA Ampere or newer (RTX 3090+, A100, H100)
- Full model: ~60GB VRAM
- Dev model: ~24GB VRAM
- Quantized versions available (FP16, FP8, NF4)
- Multiple text encoders: OpenCLIP ViT-bigG, CLIP ViT-L, T5-XXL, Llama-3.1-8B

## Wan2.1

### Video generation specifications

- **Model Variants**: 1.3B and 14B parameters
- **Architecture**: Flow Matching framework with Diffusion Transformers
- **Primary Resolutions**:
  - 480P: 832×480 pixels
  - 720P: 1280×720 pixels
- **VAE Capability**: Can encode/decode 1080P videos

### Technical parameters

- Video output: 5-second clips at 16 FPS
- Flow_shift parameter: 5.0 for 720P, 3.0 for 480P
- 1.3B model: Only 8.19GB VRAM required
- 14B model: 24GB+ VRAM recommended
- Supports both Chinese and English text in videos

## Illustrious XL

### Enhanced SDXL variant specifications

- **Base Architecture**: SDXL without modifications
- **Native Resolution**: 1536×1536 pixels (v1.0+)
- **Resolution Range**: 512×512 to 1536×1536 pixels
- **Future Support**: v2.0 targeting 2048×2048 and 20MP+ generation

### Technical requirements

- Minimum resolution: 512×512 (lower causes errors)
- ClipSkip: Must be set to 2
- CFG Scale: 3-7 recommended (4.5-5 optimal)
- Sampling Steps: 20-28 steps
- Euler a sampler recommended
- Can extend to 3744×3744 experimentally

## SD3 (Stable Diffusion 3)

### Multi-resolution architecture

- **Native Resolution**: 1024×1024 pixels (optimal)
- **Architecture**: MMDiT-X (Multimodal Diffusion Transformer)
- **Resolution Constraint**: Dimensions must be divisible by 64
- **Training Range**: 0.25 to 2 megapixels
- **VAE**: 16-channel (improved from 4-channel)

### Recommended resolutions
Same divisibility-by-64 constraint as SDXL, with optimal performance around 1 megapixel:

- Square: 1024×1024, 1152×1152
- Landscape: 1344×768, 1280×768, 1216×832
- Portrait: 768×1344, 832×1216, 896×1152

### Technical limitations

- T5 token limit: Artifacts may occur when exceeding 256 tokens
- Poor upscaling performance beyond native resolution
- SD3 Medium: 9.9GB VRAM (excluding text encoders)
- SD3 Large: 24GB VRAM requirement

## Mathematical Formulas for Resolution Calculation

### General validation formula

```python
def validate_resolution(width, height, vae_factor, min_size=256, max_size=2048):
    # Divisibility check
    if width % vae_factor != 0 or height % vae_factor != 0:
        return False
    
    # Size bounds check
    if min(width, height) < min_size or max(width, height) > max_size:
        return False
    
    return True
```

### Aspect ratio preservation formula

```python
def preserve_aspect_ratio(original_width, original_height, target_pixels, factor):
    aspect_ratio = original_width / original_height
    
    # Calculate dimensions based on target pixel count
    optimal_height = int((target_pixels / aspect_ratio) ** 0.5)
    optimal_width = int(optimal_height * aspect_ratio)
    
    # Round to valid dimensions
    valid_width = (optimal_width // factor) * factor
    valid_height = (optimal_height // factor) * factor
    
    return valid_width, valid_height
```

### VRAM requirements formula

```python
def calculate_vram_gb(width, height, model_size_gb, batch_size=1):
    # Activation memory approximation
    pixels = width * height * batch_size
    activation_memory_gb = pixels * 8 / 1e9
    
    # Total VRAM = model + activations
    total_vram = model_size_gb + activation_memory_gb
    return total_vram
```

## Implementation Guide for Resolution Calculator

### Model-specific divisibility factors

- **SD 1.5**: 8
- **SDXL**: 64
- **Flux.1 Dev**: No strict requirement (recommend 8 for compatibility)
- **HiDream**: 64 (follows SDXL)
- **Wan2.1**: Model-specific for 480P/720P
- **Illustrious**: 64 (SDXL-based)
- **SD3**: 64

### Performance scaling considerations

1. **Memory scaling**: Roughly quadratic with resolution increase
2. **Time scaling**: Non-linear due to attention mechanisms (~O(n^1.2) where n is pixel count)
3. **Quality considerations**: Each model has an optimal resolution range where training data density is highest

### Key implementation notes

1. Always validate resolutions against model-specific constraints before generation
2. Consider using bucket systems for models trained with multi-aspect ratios
3. Implement safety margins for VRAM calculations (use 80% of available VRAM)
4. Cache commonly used resolutions to avoid recalculation
5. For video models (Wan2.1), consider temporal dimension in memory calculations

The bucket system is a crucial training technique that solves a fundamental problem in AI image generation. Let me break it down:

## The Core Problem

Traditional diffusion models like early Stable Diffusion were trained only on square images (512×512). When you trained these models on non-square images, you had two bad options:

1. **Center crop** everything to squares → cuts off heads, feet, important parts
2. **Pad** images to squares → wastes computation on empty space

This is why early AI models generated images with "unnatural crops" - people without heads or feet, swords that were just straight lines extending beyond the frame.

## What Bucket Systems Solve

Aspect ratio bucketing allows the creation of batches where every item in the batch has the same size, but the image size of batches may differ. This means the model can learn from images in their natural aspect ratios without destructive cropping.

## How Bucketing Works Technically

### 1. **Bucket Generation Algorithm** (NovelAI's approach):

```python
# Simplified version of the algorithm
buckets = []
width = 256
max_dimension = 1024
max_pixels = 512 * 768  # Memory constraint

while width <= max_dimension:
    max_height = min(max_dimension, max_pixels // width)
    buckets.append((width, max_height))
    width += 64

# Repeat with width/height swapped
# Remove duplicates, add 512×512
```

This generates buckets like:

- 256×1024 (aspect ratio 0.25)
- 320×1024 (aspect ratio 0.3125)  
- 384×1024 (aspect ratio 0.375)
- 512×768 (aspect ratio 0.67)
- 512×512 (aspect ratio 1.0)
- 768×512 (aspect ratio 1.5)
- 1024×384 (aspect ratio 2.67)

### 2. **Image Assignment**:

For each image in the dataset, we retrieve its resolution and calculate the aspect ratio. The image aspect ratio is subtracted from the array of bucket aspect ratios, allowing us to efficiently select the closest bucket according to the absolute value of the difference between aspect ratios

### 3. **Batch Creation**:

- All images in a single batch must be the same resolution
- Different batches can have different resolutions
- When a batch is requested, we randomly draw a bucket from a weighted distribution. The bucket weights are set as the size of the bucket divided by the size of all remaining buckets

### 4. **Image Processing**:

The image is scaled, while preserving its aspect ratio, in such a way that it either fits the bucket resolution exactly if the aspect ratio happens to match or it extends past the bucket resolution on one dimension while fitting it exactly on the other. In the latter case, a random crop is applied

## Why This Matters for Your Tool

**For SDXL**: Uses 43 different bucket resolutions, all targeting ~1 megapixel. Your tool should validate that user-requested resolutions match these trained buckets for optimal quality.

**For SD 1.5**: Doesn't use sophisticated bucketing, so stick to divisible-by-8 constraints near 512×512.

**For Implementation**: When someone requests an arbitrary aspect ratio, your tool should:

1. Find the closest trained bucket resolution for that model
2. Suggest that resolution instead of arbitrary calculations
3. Warn if the requested ratio is far from any trained bucket

The bucket system is why SDXL can generate clean 896×1152 portraits or 1344×768 landscapes without cropping artifacts, while SD 1.5 struggles with anything far from square.

