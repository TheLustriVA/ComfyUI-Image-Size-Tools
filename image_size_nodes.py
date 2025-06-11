"""
ComfyUI Image Size Tool

Resolution calculator nodes for AI image generation models.
Zero dependencies, embedded data, bulletproof imports.
"""

# SD 1.5 Resolution Data - All dimensions divisible by 8, native 512x512
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

# SDXL Resolution Data - Dimensions divisible by 64, targeting ~1 megapixel
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

# Flux.1 Dev Resolution Data - No strict divisibility requirements, flexible
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


class SD15ResolutionNode:
    """
    SD 1.5 Resolution Calculator
    
    Provides optimal resolution presets for Stable Diffusion 1.5 models.
    All resolutions are validated to be divisible by 8 (VAE constraint).
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(SD15_RESOLUTIONS.keys()),),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "aspect_ratio")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution):
        """Get width, height, and aspect ratio for selected SD 1.5 resolution"""
        res_data = SD15_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        
        return (width, height, aspect_ratio)


class SDXLResolutionNode:
    """
    SDXL Resolution Calculator
    
    Provides bucket-trained resolution presets for SDXL models.
    All resolutions target ~1 megapixel and are divisible by 64.
    Based on the 43-bucket training system for optimal quality.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(SDXL_RESOLUTIONS.keys()),),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING", "INT")
    RETURN_NAMES = ("width", "height", "aspect_ratio", "total_pixels")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution):
        """Get width, height, aspect ratio, and pixel count for selected SDXL resolution"""
        res_data = SDXL_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        total_pixels = res_data["pixels"]
        
        return (width, height, aspect_ratio, total_pixels)


class FluxResolutionNode:
    """
    Flux.1 Dev Resolution Calculator
    
    Provides practical resolution presets for Flux.1 Dev models.
    No strict divisibility requirements, focused on hardware compatibility
    and common use cases from 1024x1024 to 2560x1440.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(FLUX_RESOLUTIONS.keys()),),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "aspect_ratio")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution):
        """Get width, height, and aspect ratio for selected Flux.1 Dev resolution"""
        res_data = FLUX_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        
        return (width, height, aspect_ratio)


# Node registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "SD15ResolutionNode": SD15ResolutionNode,
    "SDXLResolutionNode": SDXLResolutionNode,
    "FluxResolutionNode": FluxResolutionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD15ResolutionNode": "SD 1.5 Resolution",
    "SDXLResolutionNode": "SDXL Resolution", 
    "FluxResolutionNode": "Flux.1 Dev Resolution",
}