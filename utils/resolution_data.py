# Resolution data extracted from technical specifications
# Based on model training constraints and optimal quality buckets

# SD 1.5 - All dimensions must be divisible by 8, native 512x512
SD15_RESOLUTIONS = {
    "512×512 (1:1) - Native": {"width": 512, "height": 512, "ratio": "1:1"},
    "768×512 (3:2) - Landscape": {"width": 768, "height": 512, "ratio": "3:2"},
    "512×768 (2:3) - Portrait": {"width": 512, "height": 768, "ratio": "2:3"},
    "768×576 (4:3) - Standard": {"width": 768, "height": 576, "ratio": "4:3"},
    "576×768 (3:4) - Standard Portrait": {"width": 576, "height": 768, "ratio": "3:4"},
    "912×512 (16:9) - Widescreen": {"width": 912, "height": 512, "ratio": "16:9"},
    "512×912 (9:16) - Mobile": {"width": 512, "height": 912, "ratio": "9:16"},
    "768×768 (1:1) - Large Square": {"width": 768, "height": 768, "ratio": "1:1"},
}

# SDXL - Dimensions must be divisible by 64, targeting ~1 megapixel
# Using most commonly used bucket resolutions from the 43-bucket system
SDXL_RESOLUTIONS = {
    "1024×1024 (1:1) - Native": {"width": 1024, "height": 1024, "ratio": "1:1", "pixels": 1048576},
    "1152×896 (9:7) - Landscape": {"width": 1152, "height": 896, "ratio": "9:7", "pixels": 1032192},
    "896×1152 (7:9) - Portrait": {"width": 896, "height": 1152, "ratio": "7:9", "pixels": 1032192},
    "1344×768 (7:4) - Wide": {"width": 1344, "height": 768, "ratio": "7:4", "pixels": 1032192},
    "768×1344 (4:7) - Tall": {"width": 768, "height": 1344, "ratio": "4:7", "pixels": 1032192},
    "1216×832 (19:13) - Cinema": {"width": 1216, "height": 832, "ratio": "19:13", "pixels": 1011712},
    "832×1216 (13:19) - Tall Cinema": {"width": 832, "height": 1216, "ratio": "13:19", "pixels": 1011712},
    "1280×768 (5:3) - Ultrawide": {"width": 1280, "height": 768, "ratio": "5:3", "pixels": 983040},
    "768×1280 (3:5) - Ultra Portrait": {"width": 768, "height": 1280, "ratio": "3:5", "pixels": 983040},
    "1536×640 (12:5) - Banner": {"width": 1536, "height": 640, "ratio": "12:5", "pixels": 983040},
    "640×1536 (5:12) - Skyscraper": {"width": 640, "height": 1536, "ratio": "5:12", "pixels": 983040},
    "1600×640 (5:2) - Extreme Wide": {"width": 1600, "height": 640, "ratio": "5:2", "pixels": 1024000},
    "640×1600 (2:5) - Extreme Tall": {"width": 640, "height": 1600, "ratio": "2:5", "pixels": 1024000},
}

# Flux.1 Dev - No strict divisibility requirements, more flexible
# Focus on practical resolutions with good hardware compatibility
FLUX_RESOLUTIONS = {
    "1024×1024 (1:1) - Native": {"width": 1024, "height": 1024, "ratio": "1:1"},
    "1920×1080 (16:9) - Full HD": {"width": 1920, "height": 1080, "ratio": "16:9"},
    "1080×1920 (9:16) - Vertical HD": {"width": 1080, "height": 1920, "ratio": "9:16"},
    "1536×640 (12:5) - Ultrawide": {"width": 1536, "height": 640, "ratio": "12:5"},
    "640×1536 (5:12) - Ultra Portrait": {"width": 640, "height": 1536, "ratio": "5:12"},
    "1600×1600 (1:1) - High Detail": {"width": 1600, "height": 1600, "ratio": "1:1"},
    "1280×720 (16:9) - HD": {"width": 1280, "height": 720, "ratio": "16:9"},
    "720×1280 (9:16) - Vertical HD": {"width": 720, "height": 1280, "ratio": "9:16"},
    "1366×768 (16:9) - Laptop": {"width": 1366, "height": 768, "ratio": "16:9"},
    "768×1366 (9:16) - Vertical Laptop": {"width": 768, "height": 1366, "ratio": "9:16"},
    "2560×1440 (16:9) - 2K": {"width": 2560, "height": 1440, "ratio": "16:9"},
}

# Model-specific validation constraints
MODEL_CONSTRAINTS = {
    "SD15": {
        "divisible_by": 8,
        "native_resolution": (512, 512),
        "recommended_max": 1024,
    },
    "SDXL": {
        "divisible_by": 64,
        "native_resolution": (1024, 1024),
        "target_pixels": 1048576,  # ~1 megapixel
    },
    "FLUX": {
        "divisible_by": None,  # No strict requirement
        "native_resolution": (1024, 1024),
        "recommended_range": (512, 2560),
    },
}

def validate_resolution(width, height, model_type):
    """Validate resolution against model-specific constraints"""
    constraints = MODEL_CONSTRAINTS.get(model_type)
    if not constraints:
        return True, "Unknown model type"
    
    if constraints["divisible_by"]:
        factor = constraints["divisible_by"]
        if width % factor != 0 or height % factor != 0:
            return False, f"Dimensions must be divisible by {factor}"
    
    return True, "Valid resolution"

def get_aspect_ratio_text(width, height):
    """Calculate and return human-readable aspect ratio"""
    from math import gcd
    common_divisor = gcd(width, height)
    ratio_w = width // common_divisor
    ratio_h = height // common_divisor
    return f"{ratio_w}:{ratio_h}"