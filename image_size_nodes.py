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

# WAN2.1 Simple Resolution Data - Core video generation resolutions
WAN21_SIMPLE_RESOLUTIONS = {
    "832×480 (16:9) - 480p Standard": {"width": 832, "height": 480, "ratio": "16:9"},
    "1280×720 (16:9) - 720p HD": {"width": 1280, "height": 720, "ratio": "16:9"},
    "480×832 (9:16) - 480p Vertical": {"width": 480, "height": 832, "ratio": "9:16"},
    "720×1280 (9:16) - 720p Vertical": {"width": 720, "height": 1280, "ratio": "9:16"},
}

# WAN2.1 Advanced Resolution Data - Extended video generation resolutions
WAN21_ADVANCED_RESOLUTIONS = {
    "832×480 (16:9) - 480p Standard": {"width": 832, "height": 480, "ratio": "16:9"},
    "1280×720 (16:9) - 720p HD": {"width": 1280, "height": 720, "ratio": "16:9"},
    "480×832 (9:16) - 480p Vertical": {"width": 480, "height": 832, "ratio": "9:16"},
    "720×1280 (9:16) - 720p Vertical": {"width": 720, "height": 1280, "ratio": "9:16"},
    "640×480 (4:3) - Classic 480p": {"width": 640, "height": 480, "ratio": "4:3"},
    "960×720 (4:3) - Classic 720p": {"width": 960, "height": 720, "ratio": "4:3"},
    "480×640 (3:4) - Classic Vertical": {"width": 480, "height": 640, "ratio": "3:4"},
    "720×960 (3:4) - Classic Vertical": {"width": 720, "height": 960, "ratio": "3:4"},
    "720×720 (1:1) - Square 720p": {"width": 720, "height": 720, "ratio": "1:1"},
    "480×480 (1:1) - Square 480p": {"width": 480, "height": 480, "ratio": "1:1"},
    "1024×576 (16:9) - Intermediate": {"width": 1024, "height": 576, "ratio": "16:9"},
    "576×1024 (9:16) - Intermediate Vertical": {"width": 576, "height": 1024, "ratio": "9:16"},
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


class ImageSizeDetectorNode:
    """
    Image Size Detector
    
    Takes an image as input and outputs its dimensions as width and height integers.
    Useful for determining the size of existing images in your ComfyUI workflow.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "detect_size"
    CATEGORY = "Image Size Tool"
    
    def detect_size(self, image):
        """Extract width and height from image tensor"""
        # Image tensor shape is [B, H, W, C]
        # We take the first image in the batch
        batch_size, height, width, channels = image.shape
        
        return (int(width), int(height))


class WAN21ResolutionNode:
    """
    WAN2.1 Resolution Calculator
    
    Provides core video resolution presets for WAN2.1 models.
    Includes standard 480p and 720p resolutions with option to halve dimensions
    for lower VRAM usage.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(WAN21_SIMPLE_RESOLUTIONS.keys()),),
                "halve_resolution": ("BOOLEAN", {"default": False}),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING", "INT", "INT")
    RETURN_NAMES = ("width", "height", "aspect_ratio", "halved_width", "halved_height")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution, halve_resolution):
        """Get width, height, aspect ratio, and optionally halved dimensions for WAN2.1"""
        res_data = WAN21_SIMPLE_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        
        # Calculate halved dimensions (rounded to nearest even number for video compatibility)
        halved_width = int(width // 2)
        halved_height = int(height // 2)
        
        # Ensure even numbers for video encoding compatibility
        if halved_width % 2 != 0:
            halved_width += 1
        if halved_height % 2 != 0:
            halved_height += 1
        
        return (width, height, aspect_ratio, halved_width, halved_height)


class WAN21AdvancedResolutionNode:
    """
    WAN2.1 Advanced Resolution Calculator
    
    Provides extended video resolution presets for WAN2.1 models.
    Includes all standard resolutions plus additional aspect ratios and sizes
    with option to halve dimensions for lower VRAM usage.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (list(WAN21_ADVANCED_RESOLUTIONS.keys()),),
                "halve_resolution": ("BOOLEAN", {"default": False}),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING", "INT", "INT")
    RETURN_NAMES = ("width", "height", "aspect_ratio", "halved_width", "halved_height")
    FUNCTION = "get_resolution"
    CATEGORY = "Image Size Tool"
    
    def get_resolution(self, resolution, halve_resolution):
        """Get width, height, aspect ratio, and optionally halved dimensions for WAN2.1"""
        res_data = WAN21_ADVANCED_RESOLUTIONS[resolution]
        width = res_data["width"]
        height = res_data["height"]
        aspect_ratio = res_data["ratio"]
        
        # Calculate halved dimensions (rounded to nearest even number for video compatibility)
        halved_width = int(width // 2)
        halved_height = int(height // 2)
        
        # Ensure even numbers for video encoding compatibility
        if halved_width % 2 != 0:
            halved_width += 1
        if halved_height % 2 != 0:
            halved_height += 1
        
        return (width, height, aspect_ratio, halved_width, halved_height)


# Node registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "SD15ResolutionNode": SD15ResolutionNode,
    "SDXLResolutionNode": SDXLResolutionNode,
    "FluxResolutionNode": FluxResolutionNode,
    "ImageSizeDetectorNode": ImageSizeDetectorNode,
    "WAN21ResolutionNode": WAN21ResolutionNode,
    "WAN21AdvancedResolutionNode": WAN21AdvancedResolutionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD15ResolutionNode": "SD 1.5 Resolution",
    "SDXLResolutionNode": "SDXL Resolution", 
    "FluxResolutionNode": "Flux.1 Dev Resolution",
    "ImageSizeDetectorNode": "Image Size Detector",
    "WAN21ResolutionNode": "WAN2.1 Resolution",
    "WAN21AdvancedResolutionNode": "WAN2.1 Resolution (Advanced)",
}