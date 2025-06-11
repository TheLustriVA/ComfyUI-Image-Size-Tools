import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.resolution_data import SD15_RESOLUTIONS, validate_resolution, get_aspect_ratio_text

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
        
        # Validate the resolution (should always pass for our presets)
        is_valid, message = validate_resolution(width, height, "SD15")
        if not is_valid:
            print(f"Warning: Invalid resolution {width}×{height}: {message}")
        
        return (width, height, aspect_ratio)

# Node registration will be handled in __init__.py
NODE_CLASS_MAPPINGS = {
    "SD15ResolutionNode": SD15ResolutionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD15ResolutionNode": "SD 1.5 Resolution"
}