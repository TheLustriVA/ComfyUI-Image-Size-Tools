import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.resolution_data import SDXL_RESOLUTIONS, validate_resolution, get_aspect_ratio_text

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
        
        # Validate the resolution (should always pass for our presets)
        is_valid, message = validate_resolution(width, height, "SDXL")
        if not is_valid:
            print(f"Warning: Invalid resolution {width}×{height}: {message}")
        
        return (width, height, aspect_ratio, total_pixels)

# Node registration will be handled in __init__.py
NODE_CLASS_MAPPINGS = {
    "SDXLResolutionNode": SDXLResolutionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLResolutionNode": "SDXL Resolution"
}